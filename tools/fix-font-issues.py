#!/usr/bin/env python3
"""
Автоматическое исправление некоторых проблем шрифта после сборки
"""

import sys
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables import ttProgram
from pathlib import Path
from typing import Tuple
import unicodedata
from fontTools.pens.basePen import DecomposingPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

BASELINE_UNDERLINE_THICKNESS = None  # не нормализуем поперёк веса
# Канонические ширины математических знаков по семейству (считываем из Regular)
CANONICAL_MATH_WIDTHS = {}
DESIRED_WIN_ASCENT = 1600
DESIRED_WIN_DESCENT = 400

def fix_font_issues(font_path):
    """Исправляет основные проблемы в TTF файле"""
    print(f"🔧 Исправляем {font_path}...")
    
    font = TTFont(font_path)
    glyf_table = font.get('glyf')
    
    # Исправляем OS/2 таблицу
    if 'OS/2' in font:
        os2 = font['OS/2']
        
        # Исправляем sTypoLineGap
        if os2.sTypoLineGap != 0:
            print(f"  ✅ Исправляем sTypoLineGap: {os2.sTypoLineGap} → 0")
            os2.sTypoLineGap = 0
        
        # Исправляем fsSelection для USE_TYPO_METRICS
        if not (os2.fsSelection & (1 << 7)):
            print(f"  ✅ Включаем USE_TYPO_METRICS")
            os2.fsSelection |= (1 << 7)
        
        # Исправляем fsType (убираем ограничения)
        if os2.fsType != 0:
            print(f"  ✅ Исправляем fsType: {os2.fsType} → 0")
            os2.fsType = 0

        # Устанавливаем Vendor ID (зарегистрируйте при желании на Microsoft)
        if getattr(os2, 'achVendID', 'NONE') in (None, 'NONE', '    '):
            os2.achVendID = 'UKWN'

        # Нормализуем usWeightClass на основе имени файла (Akt-Weight.ttf)
        try:
            stem = Path(font_path).stem  # e.g., 'Akt-Bold'
            weight_token = stem.split('-', 1)[1] if '-' in stem else None
            weight_to_class = {
                'Thin': 100,
                'ExtraLight': 200,
                'Light': 300,
                'Regular': 400,
                'Medium': 500,
                'SemiBold': 600,
                'Bold': 700,
                'ExtraBold': 800,
                'Black': 900,
            }
            if weight_token in weight_to_class:
                expected_wc = weight_to_class[weight_token]
                if getattr(os2, 'usWeightClass', 0) != expected_wc:
                    print(f"  ✅ Устанавливаем usWeightClass: {getattr(os2, 'usWeightClass', 0)} → {expected_wc} по имени файла")
                    os2.usWeightClass = expected_wc
            # Настройка fsSelection флагов Regular/Bold/Italic для согласованности со стилем
            is_bold = (weight_token == 'Bold')
            is_italic = False  # курсивов нет
            # fsSelection биты: 0=ITALIC, 5=BOLD, 6=REGULAR, 7=USE_TYPO_METRICS
            # Сначала очистим биты 0/5/6
            os2.fsSelection &= ~(1 << 0)  # italic
            os2.fsSelection &= ~(1 << 5)  # bold
            os2.fsSelection &= ~(1 << 6)  # regular
            if is_italic:
                os2.fsSelection |= (1 << 0)
            if is_bold:
                os2.fsSelection |= (1 << 5)
            else:
                os2.fsSelection |= (1 << 6)

            # Гарантируем отсутствие клиппинга и единые Win-метрики:
            # winAscent/Descent ≥ head.yMax/|yMin| и ≥ 1600/400
            try:
                if 'head' in font:
                    head = font['head']
                    yMax = getattr(head, 'yMax', None)
                    yMin = getattr(head, 'yMin', None)
                    target_ascent = max(int(getattr(os2, 'usWinAscent', 0) or 0), int(yMax or 0), DESIRED_WIN_ASCENT)
                    if getattr(os2, 'usWinAscent', 0) != target_ascent:
                        print(f"  ✅ Устанавливаем usWinAscent: {getattr(os2, 'usWinAscent', 0)} → {target_ascent}")
                        os2.usWinAscent = target_ascent
                    if yMin is not None:
                        absMin = int(abs(yMin))
                        target_descent = max(int(getattr(os2, 'usWinDescent', 0) or 0), absMin, DESIRED_WIN_DESCENT)
                        if getattr(os2, 'usWinDescent', 0) != target_descent:
                            print(f"  ✅ Устанавливаем usWinDescent: {getattr(os2, 'usWinDescent', 0)} → {target_descent}")
                            os2.usWinDescent = target_descent
            except Exception:
                pass
        except Exception:
            pass

        # Если шрифт моноширинный (все глифы одной ширины), корректно проставим PANOSE и isFixedPitch
        try:
            widths = set(aw for (aw, _lsb) in font['hmtx'].metrics.values())
        except Exception:
            widths = set()
        is_mono_by_metrics = len(widths) == 1 and len(widths) > 0
        if is_mono_by_metrics:
            # PANOSE proportion = 9 (monospace)
            try:
                if hasattr(os2, 'panose') and getattr(os2.panose, 'bProportion', 0) != 9:
                    print("  ✅ Устанавливаем OS/2.panose.bProportion = 9 (monospace)")
                    os2.panose.bProportion = 9
            except Exception:
                pass
            # post.isFixedPitch = 1
            if 'post' in font and getattr(font['post'], 'isFixedPitch', 0) == 0:
                print("  ✅ Устанавливаем post.isFixedPitch = 1 (monospace)")
                font['post'].isFixedPitch = 1
    
    # Исправляем hhea таблицу
    if 'hhea' in font and 'OS/2' in font:
        hhea = font['hhea']
        os2 = font['OS/2']
        
        # Синхронизируем метрики
        if hhea.ascent != os2.sTypoAscender:
            print(f"  ✅ Синхронизируем ascender: hhea {hhea.ascent} → OS/2 {os2.sTypoAscender}")
            hhea.ascent = os2.sTypoAscender
        
        if hhea.descent != os2.sTypoDescender:
            print(f"  ✅ Синхронизируем descender: hhea {hhea.descent} → OS/2 {os2.sTypoDescender}")
            hhea.descent = os2.sTypoDescender
        
        if hhea.lineGap != 0:
            print(f"  ✅ Исправляем hhea lineGap: {hhea.lineGap} → 0")
            hhea.lineGap = 0

    # Добавляем отсутствующие пробельные глифы U+0020 и U+00A0
    try:
        hmtx = font['hmtx']
        glyf = font['glyf'] if 'glyf' in font else None
        cmap_table = font['cmap']
        # Определим целевую ширину (максимум из имеющихся, для моноширинного будет единственная)
        try:
            target_aw = max(aw for (aw, _lsb) in hmtx.metrics.values())
        except ValueError:
            target_aw = 600

        def ensure_glyph(name: str, uni: int):
            nonlocal glyf, hmtx, cmap_table, target_aw
            glyph_order = font.getGlyphOrder()
            if name not in glyph_order:
                if glyf is None:
                    return
                from fontTools.ttLib.tables._g_l_y_f import Glyph
                new_g = Glyph()
                new_g.numberOfContours = 0
                glyf[name] = new_g
                font.setGlyphOrder(glyph_order + [name])
                hmtx.metrics[name] = (target_aw, 0)
                # Добавим cmap mapping
                for subtable in cmap_table.tables:
                    if subtable.isUnicode():
                        subtable.cmap[uni] = name

        ensure_glyph('space', 0x0020)
        # NBSP часто именуется uni00A0
        ensure_glyph('uni00A0', 0x00A0)
    except Exception as e:
        print(f"  ⚠️ Не удалось гарантировать пробелы: {e}")

    # Добавляем/исправляем 'gasp' таблицу для оптимального рендера
    try:
        gasp = font.get('gasp') or newTable('gasp')
        # Включаем все флаги для всех размеров
        gasp.gaspRange = {0xFFFF: 0x0F}
        font['gasp'] = gasp
    except Exception as e:
        print(f"  ⚠️ Не удалось добавить gasp: {e}")

    # Добавляем/исправляем 'meta' таблицу (dlng/slng) как UTF-8 байтовые строки
    try:
        meta = font.get('meta') or newTable('meta')
        if not hasattr(meta, 'data') or meta.data is None:
            meta.data = {}
        # Таблица 'meta' ожидает строки; обеспечим str
        meta.data['slng'] = 'Latn,Cyrl'
        meta.data['dlng'] = 'Latn,Cyrl'
        font['meta'] = meta
    except Exception as e:
        print(f"  ⚠️ Не удалось добавить meta: {e}")

    # Добавляем минимальный 'prep' с включением smart dropout
    try:
        prog = ttProgram.Program()
        # PUSHW 0x01FF ; SCANCTRL
        # PUSHB 0x04   ; SCANTYPE
        prog.fromBytecode([0xB8, 0x01, 0xFF, 0x85, 0xB0, 0x04, 0x8D])
        prep = newTable('prep')
        prep.program = prog
        font['prep'] = prep
    except Exception as e:
        print(f"  ⚠️ Не удалось добавить prep: {e}")

    # Версионность: НЕ трогаем head.fontRevision, используем как есть и синхронизируем NameID5
    try:
        # Оставляем версию без изменений
        pass
    except Exception:
        pass

    # Добавляем NameID 5/13/14 (Version / License Description / License URL)
    try:
        name = font['name']
        # Канонический текст NameID 13: ровно одно предложение без URL
        ofl_snippet = "This Font Software is licensed under the SIL Open Font License, Version 1.1."
        # setName(text, nameID, platformID, platEncID, langID)
        name.setName(ofl_snippet, 13, 3, 1, 0x409)
        name.setName(ofl_snippet, 13, 1, 0, 0)
        license_url = "https://scripts.sil.org/OFL"
        name.setName(license_url, 14, 3, 1, 0x409)
        name.setName(license_url, 14, 1, 0, 0)

        # NameID 5 должен соответствовать head.fontRevision (без форс‑минимума)
        if 'head' in font:
            head = font['head']
            try:
                # Минимум 1.000 для GF релиза
                if float(head.fontRevision) < 1.0:
                    print(f"  ✅ Повышаем head.fontRevision: {head.fontRevision} → 1.000 (требование GF)")
                    head.fontRevision = 1.0
                version_string = f"Version {float(head.fontRevision):.3f}"
            except Exception:
                version_string = "Version 1.000"
        else:
            version_string = "Version 1.000"
        # Перепишем ВСЕ записи NameID 5 на всех платформах/языках
        # Удалим существующие записи NameID 5 и NameID 16 (Typographic Family) для статиков
        name.names = [nr for nr in name.names if nr.nameID not in (5, 16)]
        name.setName(version_string, 5, 3, 1, 0x409)
        name.setName(version_string, 5, 3, 10, 0x409)  # UCS-4 fallback
        name.setName(version_string, 5, 1, 0, 0)

        # Обновим NameID 3 (Unique font identifier) к ожидаемому GF формату:
        # "Version X.XXX;VEND;PostScriptName"
        try:
            os2 = font['OS/2']
            vend = getattr(os2, 'achVendID', 'UKWN') or 'UKWN'
        except Exception:
            vend = 'UKWN'
        # постскрипт имя возьмём из NameID 6, если есть
        ps = None
        for rec in name.names:
            if rec.nameID == 6 and rec.platformID == 3 and rec.platEncID == 1:
                try:
                    ps = str(rec.string, 'utf-16-be')
                except Exception:
                    ps = rec.toUnicode()
                break
        if not ps:
            # запасной путь: сконструируем из имени файла
            from pathlib import Path
            stem = Path(font_path).stem
            ps = stem.replace(' ', '')
        unique_str = f"{version_string};{vend};{ps}"
        # зачистим прежние nameID 3
        name.names = [nr for nr in name.names if nr.nameID != 3]
        # platform 3,1 и 1,0
        name.setName(unique_str, 3, 3, 1, 0x409)
        name.setName(unique_str, 3, 1, 0, 0)
    except Exception as e:
        print(f"  ⚠️ Не удалось установить NameID 13: {e}")

    # Выравниваем ширины математических знаков внутри стиля и к канону семьи
    try:
        hmtx = font['hmtx']
        cmap = font['cmap']
        # cp → предпочтительный набор знаков
        math_cps = [
            0x002B,  # plus
            0x2212,  # minus
            0x00D7,  # multiply
            0x00F7,  # divide
            0x003D,  # equal
            0x2260,  # not equal
            0x2248,  # almost equal
            0x00B1,  # plusminus
            0x007E,  # tilde
        ]
        # Соберём мэппинг cp→glyphName
        cp_to_glyph = {}
        for st in cmap.tables:
            if st.isUnicode():
                for cp, gname in st.cmap.items():
                    if cp in math_cps and cp not in cp_to_glyph:
                        cp_to_glyph[cp] = gname
        present = [cp for cp in math_cps if cp in cp_to_glyph]
        if present:
            # целевой шириной считаем ширину плюса, если он есть, иначе моду наиболее частой ширины
            def get_aw(gname: str) -> int:
                try:
                    return hmtx.metrics[gname][0]
                except Exception:
                    return None
            target_aw = None
            if 0x002B in cp_to_glyph:
                target_aw = get_aw(cp_to_glyph[0x002B])
            if not target_aw:
                widths = {}
                for cp in present:
                    aw = get_aw(cp_to_glyph[cp])
                    if aw is not None:
                        widths[aw] = widths.get(aw, 0) + 1
                if widths:
                    target_aw = sorted(widths.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
            if target_aw:
                changed = 0
                for cp in present:
                    gname = cp_to_glyph[cp]
                    aw, lsb = hmtx.metrics.get(gname, (None, None))
                    if aw is None:
                        continue
                    # Если есть канон по семейству, используем его
                    fam_aw = CANONICAL_MATH_WIDTHS.get(cp)
                    final_aw = fam_aw if fam_aw else target_aw
                    if aw != final_aw:
                        hmtx.metrics[gname] = (final_aw, lsb)
                        changed += 1
                if changed:
                    print(f"  ✅ Выровнены ширины матзнаков: {changed} шт. (цель: {fam_aw if fam_aw else target_aw})")
    except Exception as e:
        print(f"  ⚠️ Не удалось выровнять матзнаки: {e}")

    # Гарантируем наличие U+002E FULL STOP в cmap (→ 'period')
    try:
        if 'cmap' in font:
            cmap = font['cmap']
            glyph_order = set(font.getGlyphOrder())
            period_name = 'period' if 'period' in glyph_order else None
            if period_name is not None:
                for st in cmap.tables:
                    if st.isUnicode():
                        st.cmap[0x002E] = period_name
    except Exception as e:
        print(f"  ⚠️ Не удалось гарантировать U+002E: {e}")
    
    # Установка head флагов/macStyle (underlineThickness не унифицируем)
    try:
        if 'head' in font:
            head = font['head']
            # Требование integer PPEM для hinted: установить бит 3
            head.flags |= (1 << 3)
            # macStyle: 0=BOLD, 1=ITALIC
            stem = Path(font_path).stem
            weight_token = stem.split('-', 1)[1] if '-' in stem else None
            is_bold = (weight_token == 'Bold')
            is_italic = False
            if is_bold:
                head.macStyle |= (1 << 0)
            else:
                head.macStyle &= ~(1 << 0)
            if is_italic:
                head.macStyle |= (1 << 1)
            else:
                head.macStyle &= ~(1 << 1)
    except Exception:
        pass

    # underlineThickness оставляем как в мастер‑источнике для каждого веса

    # Полная декомпозиция всех композитов в контуры (закрывает nested/transformed)
    try:
        if glyf_table is not None:
            glyph_set = font.getGlyphSet()

            def has_transform(t: Tuple[float, float, float, float, float, float]) -> bool:
                a, b, c, d, e, f = t
                return not (abs(a - 1.0) < 1e-6 and abs(b) < 1e-6 and abs(c) < 1e-6 and abs(d - 1.0) < 1e-6)

            # Соберём кандидатов на декомпозицию
            to_decompose = []
            for gname in font.getGlyphOrder():
                try:
                    g = glyf_table[gname]
                except Exception:
                    continue
                if hasattr(g, 'isComposite') and g.isComposite():
                    # Опционально обнаружим признаки nested/transformed для отчёта
                    nested = False
                    transformed = False
                    for comp in getattr(g, 'components', []) or []:
                        if hasattr(comp, 'transform') and has_transform(comp.transform):
                            transformed = True
                        try:
                            cg = glyf_table[comp.glyphName]
                            if hasattr(cg, 'isComposite') and cg.isComposite():
                                nested = True
                        except Exception:
                            pass
                    to_decompose.append((gname, nested, transformed))

            if to_decompose:
                decomposed_count = 0
                for gname, nested, transformed in to_decompose:
                    try:
                        tt_pen = TTGlyphPen(glyph_set)
                        decomp_pen = DecomposingPen(glyph_set, tt_pen)
                        glyf_table[gname].draw(glyph_set, decomp_pen)
                        simple = tt_pen.glyph()
                        # Если после декомпозиции глиф всё ещё composite (должно быть False), пропустим
                        if hasattr(simple, 'isComposite') and simple.isComposite():
                            continue
                        glyf_table[gname] = simple
                        decomposed_count += 1
                    except Exception:
                        continue
                if decomposed_count:
                    print(f"  ✅ Декомпозировано глифов: {decomposed_count}")
    except Exception:
        pass

    # Создаём недостающие парные мэппинги (upper/lower) только в cmap (без добавления новых глифов)
    try:
        cmap_table = font.get('cmap')
        if cmap_table:
            unicode_to_glyph = {}
            subtables = [st for st in cmap_table.tables if st.isUnicode()]
            for st in subtables:
                unicode_to_glyph.update(st.cmap)

            added = 0
            for cp, gname in list(unicode_to_glyph.items()):
                try:
                    ch = chr(cp)
                except ValueError:
                    continue
                cat = unicodedata.category(ch)
                if cat == 'Lu':
                    lower = ch.lower()
                    if len(lower) == 1:
                        cl = ord(lower)
                        if cl != cp and cl not in unicode_to_glyph:
                            for st in subtables:
                                st.cmap[cl] = gname
                            unicode_to_glyph[cl] = gname
                            added += 1
                elif cat == 'Ll':
                    upper = ch.upper()
                    if len(upper) == 1:
                        cu = ord(upper)
                        if cu != cp and cu not in unicode_to_glyph:
                            for st in subtables:
                                st.cmap[cu] = gname
                            unicode_to_glyph[cu] = gname
                            added += 1
            if added:
                print(f"  ✅ Добавлены парные мэппинги в cmap: {added} шт.")
    except Exception as e:
        print(f"  ⚠️ Не удалось дополнить case-мэппинг (cmap): {e}")

    # Сохраняем изменения
    font.save(font_path)
    print(f"  💾 Сохранено: {font_path}")
    font.close()

def rename_and_fix_names_statics_gf(font_path: Path, base_family: str = "Akt") -> Path:
    """Normalize static TTF naming to Google Fonts statics scheme:
    - For Regular weight:
      * nameID 1 (Family): 'Akt'
      * nameID 2 (Subfamily): 'Regular'
      * nameID 4 (Full): 'Akt Regular'
      * nameID 6 (PostScript): 'Akt-Regular'
      * OMIT nameID 16/17
    - For non-Regular weights (e.g., Bold):
      * nameID 1 (Family): 'Akt Bold' (per-weight legacy family)
      * nameID 2 (Subfamily): 'Regular'
      * nameID 4 (Full): 'Akt Bold'
      * nameID 6 (PostScript): 'Akt-Bold'
      * nameID 16 (Typographic Family): 'Akt'
      * nameID 17 (Typographic Subfamily): 'Bold'
    File renamed to 'Akt-WeightName.ttf'. Returns new path.
    """
    ttf = TTFont(font_path)
    os2 = ttf['OS/2'] if 'OS/2' in ttf else None
    weight_class = getattr(os2, 'usWeightClass', None)
    weight_map = {
        100: 'Thin',
        200: 'ExtraLight',
        300: 'Light',
        400: 'Regular',
        500: 'Medium',
        600: 'SemiBold',
        700: 'Bold',
        800: 'ExtraBold',
        900: 'Black',
    }
    # Prefer filename token AFTER hyphen to infer style; fallback to OS/2 weight
    weight_name = None
    name_token = font_path.stem.split('-', 1)[1] if '-' in font_path.stem else None
    if name_token in weight_map.values():
        weight_name = name_token
    else:
        weight_name = weight_map.get(weight_class or 400, 'Regular')

    name = ttf['name']
    # Drop existing 1/2/4/6/16/17
    name.names = [nr for nr in name.names if nr.nameID not in (1, 2, 4, 6, 16, 17)]

    if weight_name == 'Regular':
        fam = base_family
        subfam = 'Regular'
        full = f"{base_family} Regular"
        ps = f"{base_family}-Regular".replace(' ', '')
        for pid, eid, lid in [(3,1,0x409), (1,0,0)]:
            name.setName(fam, 1, pid, eid, lid)
            name.setName(subfam, 2, pid, eid, lid)
            name.setName(full, 4, pid, eid, lid)
            name.setName(ps, 6, pid, eid, lid)
        canonical = f"{base_family}-Regular.ttf"
    elif weight_name == 'Bold':
        # Bold is a supported style in the main family (RIBBI)
        fam = base_family
        subfam = 'Bold'
        full = f"{base_family} Bold"
        ps = f"{base_family}-Bold".replace(' ', '')
        for pid, eid, lid in [(3,1,0x409), (1,0,0)]:
            name.setName(fam, 1, pid, eid, lid)
            name.setName(subfam, 2, pid, eid, lid)
            name.setName(full, 4, pid, eid, lid)
            name.setName(ps, 6, pid, eid, lid)
        canonical = f"{base_family}-Bold.ttf"
    else:
        fam = f"{base_family} {weight_name}"
        subfam = 'Regular'
        full = fam
        ps = f"{base_family}-{weight_name}".replace(' ', '')
        for pid, eid, lid in [(3,1,0x409), (1,0,0)]:
            name.setName(fam, 1, pid, eid, lid)
            name.setName(subfam, 2, pid, eid, lid)
            name.setName(full, 4, pid, eid, lid)
            name.setName(ps, 6, pid, eid, lid)
            name.setName(base_family, 16, pid, eid, lid)
            name.setName(weight_name, 17, pid, eid, lid)
        canonical = f"{base_family}-{weight_name}.ttf"

    ttf.save(font_path)
    ttf.close()
    new_path = font_path.with_name(canonical)
    if new_path != font_path:
        font_path.rename(new_path)
    return new_path

def main():
    global BASELINE_UNDERLINE_THICKNESS
    # Исправляем все TTF файлы
    ttf_files = list(Path('fonts/ttf').glob('*.ttf'))
    variable_files = list(Path('fonts/variable').glob('*.ttf'))
    
    all_files = ttf_files + variable_files
    
    if not all_files:
        print("❌ Не найдено TTF файлов для исправления")
        return 1
    
    # Определим baseline underlineThickness и канонические мат-ширины из Regular, если доступен
    try:
        regular_path = Path('fonts/ttf/Akt-Regular.ttf')
        if regular_path.exists():
            reg = TTFont(regular_path)
            BASELINE_UNDERLINE_THICKNESS = getattr(reg['post'], 'underlineThickness', None)
            # Считаем канонические ширины матзнаков
            try:
                hmtx = reg['hmtx']
                cmap = reg['cmap']
                math_cps = [0x002B, 0x2212, 0x00D7, 0x00F7, 0x003D, 0x2260, 0x2248, 0x00B1, 0x007E]
                cp_to_glyph = {}
                for st in cmap.tables:
                    if st.isUnicode():
                        for cp, gname in st.cmap.items():
                            if cp in math_cps and cp not in cp_to_glyph:
                                cp_to_glyph[cp] = gname
                for cp, gname in cp_to_glyph.items():
                    try:
                        CANONICAL_MATH_WIDTHS[cp] = hmtx.metrics[gname][0]
                    except Exception:
                        pass
                if CANONICAL_MATH_WIDTHS:
                    print(f"  ℹ️ Канонические мат-ширины взяты из Regular: {len(CANONICAL_MATH_WIDTHS)}")
            except Exception:
                pass
            reg.close()
    except Exception:
        BASELINE_UNDERLINE_THICKNESS = None
    
    import traceback
    renamed_paths = []
    for font_file in all_files:
        try:
            fix_font_issues(font_file)
        except Exception as e:
            print(f"❌ Ошибка при исправлении {font_file}: {e}")
            traceback.print_exc()
            return 1
        # Apply single-family naming to any Akt*.ttf except legacy AktGrotesk
        try:
            if font_file.name.startswith('Akt') and not font_file.name.startswith('AktGrotesk'):
                new_path = rename_and_fix_names_statics_gf(font_file)
                renamed_paths.append((font_file, new_path))
        except Exception as e:
            print(f"  ⚠️ Не удалось нормализовать имена {font_file}: {e}")
    
    print(f"\n✅ Исправлено {len(all_files)} файлов")
    if renamed_paths:
        print("🔤 Переименованы файлы:")
        for old, new in renamed_paths:
            print(f"  {old.name} → {new.name}")
    print("🔄 Теперь запустите: make update-metadata && make qa")
    return 0

if __name__ == '__main__':
    sys.exit(main())
