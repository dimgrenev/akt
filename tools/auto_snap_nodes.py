#!/usr/bin/env python3
"""
Утилита для автоматического снаппинга узлов по базовым линиям шрифта.
Помогает исправить проблемы с выравниванием контуров (outline alignment misses).

Основные линии для снаппинга по умолчанию:

Скрипт предпочитает работать через glyphsLib (точная работа с контурами),
а при её отсутствии использует безопасный текстовый анализ/снап только при явной команде.
"""

import sys
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Set
import argparse

# Попробуем использовать glyphsLib для точечного изменения выбранных глифов
try:
    from glyphsLib import GSFont
    HAS_GLYPHSLIB = True
except Exception:
    HAS_GLYPHSLIB = False

# Пороговые значения для снаппинга (в юнитах)
SNAP_THRESHOLD = 3

# Базовые линии по умолчанию (если не удастся прочитать из мастера)
DEFAULT_BASELINE_METRICS = {
    'baseline': 0,
    'x-height': 500,
    'cap-height': 720,
    'ascender': 960,
    'descender': -240,
}


def _derive_metrics_from_font(font) -> Dict[str, float]:
    """Считывает метрики из первого мастера, при недоступности — возвращает значения по умолчанию."""
    metrics = dict(DEFAULT_BASELINE_METRICS)
    try:
        if hasattr(font, 'masters') and font.masters:
            m = font.masters[0]
            # Имена атрибутов в glyphsLib: ascender, descender, xHeight, capHeight
            if getattr(m, 'ascender', None) is not None:
                metrics['ascender'] = float(m.ascender)
            if getattr(m, 'descender', None) is not None:
                metrics['descender'] = float(m.descender)
            if getattr(m, 'xHeight', None) is not None:
                metrics['x-height'] = float(m.xHeight)
            if getattr(m, 'capHeight', None) is not None:
                metrics['cap-height'] = float(m.capHeight)
            # baseline всегда 0
            metrics['baseline'] = 0.0
    except Exception:
        pass
    return metrics


def _derive_metrics_by_master(font):
    """Возвращает словарь метрик по мастерам: {masterId: metrics_dict}."""
    metrics_by_master: Dict[str, Dict[str, float]] = {}
    try:
        for m in getattr(font, 'masters', []) or []:
            md = dict(DEFAULT_BASELINE_METRICS)
            if getattr(m, 'ascender', None) is not None:
                md['ascender'] = float(m.ascender)
            if getattr(m, 'descender', None) is not None:
                md['descender'] = float(m.descender)
            if getattr(m, 'xHeight', None) is not None:
                md['x-height'] = float(m.xHeight)
            if getattr(m, 'capHeight', None) is not None:
                md['cap-height'] = float(m.capHeight)
            md['baseline'] = 0.0
            mid = getattr(m, 'id', None) or getattr(m, 'name', 'master')
            metrics_by_master[str(mid)] = md
    except Exception:
        pass
    # Если по какой-то причине пусто — добавим дефолт под ключом 'default'
    if not metrics_by_master:
        metrics_by_master['default'] = dict(DEFAULT_BASELINE_METRICS)
    return metrics_by_master


def should_snap_to_baseline(y_coord: float, baseline_value: float, threshold: int = SNAP_THRESHOLD) -> bool:
    """Проверяет, нужно ли привязать координату к базовой линии."""
    return abs(y_coord - baseline_value) <= threshold


def snap_coordinate_value(y_coord: float, metrics: Dict[str, float], threshold: int = SNAP_THRESHOLD) -> Tuple[float, Optional[str]]:
    """Привязывает Y-координату к ближайшей базовой линии при необходимости."""
    for name, value in metrics.items():
        if should_snap_to_baseline(y_coord, value, threshold=threshold):
            return value, name
    return y_coord, None


def _iter_path_nodes(layer):
    """Итератор по on-curve узлам слоя."""
    # В некоторых версиях glyphsLib узлы доступны через layer.shapes (GSPath) -> nodes
    if not hasattr(layer, 'paths'):
        return
    for path in layer.paths:
        if not hasattr(path, 'nodes') or not path.nodes:
            continue
        for node in path.nodes:
            ntype = getattr(node, 'type', None)
            # offcurve — это управляющие точки Безье, их пропускаем
            if ntype == 'offcurve':
                continue
            yield node


def _iter_components(layer):
    """Итератор по компонентам слоя (если есть)."""
    if not hasattr(layer, 'components'):
        return
    for comp in layer.components or []:
        yield comp


def _get_layer_master_id(layer) -> str:
    mid = getattr(layer, 'associatedMasterId', None) or getattr(layer, 'master', None)
    # у некоторых версий layer.master может быть объектом; попробуем взять id
    if hasattr(mid, 'id'):
        return str(getattr(mid, 'id'))
    return str(mid) if mid is not None else 'default'


def _analyze_font_glyphs(
    font,
    targets: Optional[Set[str]] = None,
    include_points: bool = True,
    include_components: bool = True,
    threshold: int = SNAP_THRESHOLD,
) -> Tuple[Dict[str, List[Tuple[str, float]]], Dict[str, float]]:
    metrics_by_master = _derive_metrics_by_master(font)
    # для краткого вывода вернём метрики первого мастера
    any_metrics = next(iter(metrics_by_master.values()))
    issues: Dict[str, List[Tuple[str, float]]] = {k: [] for k in any_metrics.keys()}

    glyph_names = [g.name for g in font.glyphs]
    if targets:
        glyph_names = [n for n in glyph_names if n in targets]

    for gname in glyph_names:
        glyph = font.glyphs[gname]
        for layer in getattr(glyph, 'layers', []) or []:
            if not hasattr(layer, 'paths'):
                continue
            m_id = _get_layer_master_id(layer)
            metrics = metrics_by_master.get(m_id) or any_metrics
            if include_points:
                for node in _iter_path_nodes(layer):
                    try:
                        y = float(node.y)
                    except Exception:
                        continue
                    for line, value in metrics.items():
                        if should_snap_to_baseline(y, value, threshold=threshold):
                            issues[line].append((gname, y))
            if include_components:
                for comp in _iter_components(layer):
                    try:
                        pos = getattr(comp, 'position', None)
                        y = float(pos.y) if pos is not None else None
                    except Exception:
                        y = None
                    if y is None:
                        # попробуем прочитать из transform (если есть dy)
                        tr = getattr(comp, 'transform', None)
                        try:
                            dy = float(tr.dy)
                            y = dy
                        except Exception:
                            y = None
                    if y is None:
                        continue
                    for line, value in metrics.items():
                        if should_snap_to_baseline(y, value, threshold=threshold):
                            issues[line].append((gname + ' [component]', y))
    return issues, any_metrics


def analyze_outline_issues(file_path: Path, target_glyphs: Optional[List[str]] = None):
    """Анализирует потенциальные проблемы с выравниванием контуров.
    При наличии glyphsLib анализ выполняется точно (per-glyph, per-node).
    В противном случае используется упрощённый текстовый анализ файла.
    """
    print(f"Анализ проблем выравнивания в: {file_path}")

    if HAS_GLYPHSLIB:
        font = GSFont(str(file_path))
        targets = set(g.strip() for g in target_glyphs) if target_glyphs else None
        issues, metrics = _analyze_font_glyphs(font, targets)

        total = 0
        print("\nИспользуемые метрики:")
        for k, v in metrics.items():
            print(f"  {k}: {int(v) if float(v).is_integer() else v}")

        print("\nПотенциальные near-miss узлы (счётчики по линиям):")
        for line, items in issues.items():
            if not items:
                continue
            total += len(items)
            uniq_glyphs = sorted(set(g for g, _ in items))
            print(f"  {line} ({int(metrics[line]) if float(metrics[line]).is_integer() else metrics[line]}): {len(items)} узлов в {len(uniq_glyphs)} глифах")
            # Выведем до 40 имён глифов для обзора
            preview = ', '.join(uniq_glyphs[:40])
            if preview:
                print(f"    Глифы: {preview}{' …' if len(uniq_glyphs) > 40 else ''}")
        if total == 0:
            print("\nПроблемы не обнаружены!")
        else:
            print(f"\nВсего потенциальных проблем: {total}")
        return

    # --- Fallback: текстовый анализ на всём файле ---
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    coord_pattern = r'\((-?\d+(?:\.\d+)?), (-?\d+(?:\.\d+)?)\)'
    matches = re.findall(coord_pattern, content)

    potential_issues = {name: [] for name in DEFAULT_BASELINE_METRICS.keys()}

    for _x_str, y_str in matches:
        y_coord = float(y_str)
        for name, baseline_value in DEFAULT_BASELINE_METRICS.items():
            if should_snap_to_baseline(y_coord, baseline_value):
                potential_issues[name].append(y_coord)

    print("\nПотенциальные проблемы выравнивания:")
    total_issues = 0
    for line_name, coords in potential_issues.items():
        if coords:
            unique_coords = sorted(set(coords))
            print(f"  {line_name} ({DEFAULT_BASELINE_METRICS[line_name]}): {len(coords)} узлов")
            print(f"    Уникальные Y-координаты: {unique_coords}")
            total_issues += len(coords)

    if total_issues == 0:
        print("  Проблемы не обнаружены!")
    else:
        print(f"\nВсего потенциальных проблем: {total_issues}")


def _snap_font_nodes(
    font,
    targets: Optional[Set[str]] = None,
    include_points: bool = True,
    include_components: bool = True,
    threshold: int = SNAP_THRESHOLD,
) -> Tuple[int, Dict[str, int], Dict[str, float], Set[str]]:
    metrics_by_master = _derive_metrics_by_master(font)
    any_metrics = next(iter(metrics_by_master.values()))
    snapped_count = 0
    snapped_by_line = {name: 0 for name in any_metrics.keys()}
    affected: Set[str] = set()

    glyph_names = [g.name for g in font.glyphs]
    if targets:
        glyph_names = [n for n in glyph_names if n in targets]

    for gname in glyph_names:
        glyph = font.glyphs[gname]
        glyph_changed = False
        for layer in getattr(glyph, 'layers', []) or []:
            if not hasattr(layer, 'paths'):
                continue
            m_id = _get_layer_master_id(layer)
            metrics = metrics_by_master.get(m_id) or any_metrics
            # точки контуров
            if include_points:
                for node in _iter_path_nodes(layer):
                    try:
                        y = float(node.y)
                    except Exception:
                        continue
                    new_y, line = snap_coordinate_value(y, metrics, threshold=threshold)
                    if new_y != y:
                        node.y = new_y
                        snapped_count += 1
                        glyph_changed = True
                        if line:
                            snapped_by_line[line] += 1
            # компоненты: корректируем только Y-позицию/сдвиг
            if include_components:
                for comp in _iter_components(layer):
                    changed = False
                    # position
                    pos = getattr(comp, 'position', None)
                    if pos is not None:
                        try:
                            y = float(pos.y)
                            new_y, line = snap_coordinate_value(y, metrics, threshold=threshold)
                            if new_y != y:
                                pos.y = new_y
                                setattr(comp, 'position', pos)
                                snapped_count += 1
                                glyph_changed = True
                                changed = True
                                if line:
                                    snapped_by_line[line] += 1
                        except Exception:
                            pass
                    # transform.dy
                    if not changed:
                        tr = getattr(comp, 'transform', None)
                        if tr is not None and hasattr(tr, 'dy'):
                            try:
                                y = float(tr.dy)
                                new_y, line = snap_coordinate_value(y, metrics, threshold=threshold)
                                if new_y != y:
                                    tr.dy = new_y
                                    setattr(comp, 'transform', tr)
                                    snapped_count += 1
                                    glyph_changed = True
                                    if line:
                                        snapped_by_line[line] += 1
                            except Exception:
                                pass
        if glyph_changed:
            affected.add(gname)

    return snapped_count, snapped_by_line, any_metrics, affected


def process_glyphs_file(
    file_path: Path,
    target_glyphs: Optional[List[str]] = None,
    include_points: bool = True,
    include_components: bool = True,
    threshold: int = SNAP_THRESHOLD,
    dry_run: bool = False,
):
    """
    Обрабатывает файл .glyphs и выполняет снаппинг узлов.
    Если glyphsLib доступна — используется точный режим по всем/указанным глифам.
    Иначе доступен только безопасный текстовый режим для ВСЕГО файла (без частичного снапа).
    """
    file_path = Path(file_path)
    print(f"Обработка файла: {file_path}")

    # Если доступна glyphsLib — используем её и для частичного, и для полного снапа
    if HAS_GLYPHSLIB:
        original_content = file_path.read_text(encoding='utf-8')
        font = GSFont(str(file_path))

        targets = {g.strip() for g in target_glyphs} if target_glyphs else None
        snapped_count, snapped_by_line, metrics, affected = _snap_font_nodes(
            font,
            targets,
            include_points=include_points,
            include_components=include_components,
            threshold=threshold,
        )

        if snapped_count > 0 and not dry_run:
            backup_path = file_path.with_suffix('.glyphs.snap_backup')
            backup_path.write_text(original_content, encoding='utf-8')
            font.save(str(file_path))
            print(f"Создана резервная копия: {backup_path}")
            print(f"\nРезультаты снаппинга (glyphsLib):")
            print(f"Всего узлов изменено: {snapped_count}")
            for line_name, count in snapped_by_line.items():
                if count > 0:
                    val = metrics[line_name]
                    print(f"  - {line_name} ({int(val) if float(val).is_integer() else val}): {count} узлов")
            if affected:
                names = sorted(list(affected))
                print(f"\nЗатронутые глифы ({len(names)}): {', '.join(names[:60])}{' …' if len(names) > 60 else ''}")
        else:
            # dry-run summary
            print(f"\nРезультаты снаппинга (glyphsLib){' [dry-run]' if dry_run else ''}:")
            print(f"Всего узлов изменено: {snapped_count}")
            for line_name, count in snapped_by_line.items():
                if count > 0:
                    val = metrics[line_name]
                    print(f"  - {line_name} ({int(val) if float(val).is_integer() else val}): {count} узлов")
            if affected:
                names = sorted(list(affected))
                print(f"\nЗатронутые глифы ({len(names)}): {', '.join(names[:60])}{' …' if len(names) > 60 else ''}")
            if snapped_count == 0 and not dry_run:
                print("Узлы для снаппинга не найдены в выбранном наборе глифов.")
        return

    # --- Fallback: текстовый режим по всему файлу (как было) ---
    content = file_path.read_text(encoding='utf-8')

    # Статистика изменений
    snapped_count = 0
    snapped_by_line = {name: 0 for name in DEFAULT_BASELINE_METRICS.keys()}

    # Регулярное выражение для поиска координат узлов в формате "(<x>, <y>)"
    coord_pattern = r'\((-?\d+(?:\.\d+)?), (-?\d+(?:\.\d+)?)\)'

    def replace_coordinate(match):
        nonlocal snapped_count
        x_str, y_str = match.groups()
        try:
            y = float(y_str)
        except Exception:
            return match.group(0)
        new_y, line = snap_coordinate_value(y, DEFAULT_BASELINE_METRICS, threshold=threshold)
        if new_y != y:
            snapped_count += 1
            if line:
                snapped_by_line[line] += 1
            return f"({x_str}, {int(new_y) if float(new_y).is_integer() else new_y})"
        return match.group(0)

    if target_glyphs:
        print("[ВНИМАНИЕ] glyphsLib недоступна, пропускаю точечный режим. Обработка всего файла отключена для безопасности.")
        return

    new_content = re.sub(coord_pattern, replace_coordinate, content)

    if snapped_count > 0 and not dry_run:
        backup_path = file_path.with_suffix('.glyphs.snap_backup')
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Создана резервная копия: {backup_path}")

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"\nРезультаты снаппинга:")
        print(f"Всего узлов обработано: {snapped_count}")
        for line_name, count in snapped_by_line.items():
            if count > 0:
                print(f"  - {line_name} ({DEFAULT_BASELINE_METRICS[line_name]}): {count} узлов")
    else:
        print(f"\nРезультаты снаппинга{' [dry-run]' if dry_run else ''}:")
        print(f"Всего узлов обработано: {snapped_count}")
        for line_name, count in snapped_by_line.items():
            if count > 0:
                print(f"  - {line_name} ({DEFAULT_BASELINE_METRICS[line_name]}): {count} узлов")


def main():
    parser = argparse.ArgumentParser(
        description="Анализ и снаппинг узлов/компонентов по базовым линиям для .glyphs"
    )
    parser.add_argument("file", help="Путь к файлу .glyphs")
    parser.add_argument("command", nargs="?", default="snap", choices=["analyze", "snap"], help="Команда: analyze или snap (по умолчанию: snap)")
    parser.add_argument("glyphs", nargs="*", help="Опциональный белый список глифов для точечной обработки")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--components-only", action="store_true", help="Обрабатывать только компоненты")
    group.add_argument("--points-only", action="store_true", help="Обрабатывать только точки контуров")
    parser.add_argument("--threshold", type=int, default=SNAP_THRESHOLD, help=f"Порог привязки, юнитов (по умолчанию: {SNAP_THRESHOLD})")
    parser.add_argument("--dry-run", action="store_true", help="Не записывать изменения, только отчёт")

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Ошибка: файл {file_path} не найден")
        raise SystemExit(1)

    include_points = True
    include_components = True
    if args.components_only:
        include_points = False
        include_components = True
    elif args.points_only:
        include_points = True
        include_components = False

    targets = args.glyphs if len(args.glyphs) > 0 else None

    if args.command == "analyze":
        if HAS_GLYPHSLIB:
            # точный анализ с флагами
            issues, metrics = _analyze_font_glyphs(
                GSFont(str(file_path)),
                targets=set(targets) if targets else None,
                include_points=include_points,
                include_components=include_components,
                threshold=args.threshold,
            )
            print("\nПотенциальные проблемы выравнивания:")
            total = 0
            for line_name, coords in issues.items():
                if coords:
                    val = metrics[line_name]
                    print(f"  {line_name} ({int(val) if float(val).is_integer() else val}): {len(coords)} узлов")
                    uniq_glyphs = []
                    seen = set()
                    for gname, _y in coords:
                        if gname not in seen:
                            uniq_glyphs.append(gname)
                            seen.add(gname)
                    preview = ', '.join(uniq_glyphs[:40])
                    if preview:
                        print(f"    Глифы: {preview}{' …' if len(uniq_glyphs) > 40 else ''}")
                    total += len(coords)
            if total == 0:
                print("\nПроблемы не обнаружены!")
            else:
                print(f"\nВсего потенциальных проблем: {total}")
        else:
            # Fallback: прежний текстовый анализ по всему файлу
            analyze_outline_issues(file_path, targets)
    else:  # snap
        process_glyphs_file(
            file_path,
            target_glyphs=targets,
            include_points=include_points,
            include_components=include_components,
            threshold=args.threshold,
            dry_run=args.dry_run,
        )

if __name__ == "__main__":
    main()