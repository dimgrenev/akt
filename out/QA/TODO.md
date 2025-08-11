# Akt – TODO для устранения оставшихся FAIL в FontBakery

Источник: `sources/Akt.glyphs`
Актуальный отчёт: `out/fontbakery/report-akt-full.html` и `out/fontbakery/report-akt-full.md`

## Обязательные ручные правки в источнике

1) Dotted Circle (uni25CC)
- Добавить якоря `top` и `bottom` на всех мастерах.
- Убедиться, что `uni25CC` в GDEF Base (не Mark).
- Проверить привязку следующих mark-глифов (см. отчёт):
  - acutecomb, dotbelowcomb, gravecomb, tildecomb,
    uni0302, uni0304, uni0306, uni0307, uni0308, uni030A, uni030B, uni030C,
    uni0312, uni0326, uni0327, uni0328, uni0335.

2) Case mapping (соответствие регистров)
- Обеспечить парные буквы противоположного регистра (из отчёта):
  - U+039E GREEK CAPITAL LETTER XI ↔ U+03BE GREEK SMALL LETTER XI
  - U+03B1 GREEK SMALL LETTER ALPHA ↔ U+0391 GREEK CAPITAL LETTER ALPHA
  - U+1E03 LATIN SMALL LETTER B WITH DOT ABOVE ↔ U+1E02 LATIN CAPITAL LETTER B WITH DOT ABOVE
  - U+1E28 LATIN CAPITAL LETTER H WITH CEDILLA ↔ U+1E29 LATIN SMALL LETTER H WITH CEDILLA

3) Nested components (вложенные компоненты)
- Развернуть/упростить компоненты в глифах (начало списка; полный в отчёте):
  - uni01CD, Adieresis, uni1EA0, Agrave, Ccaron, Dcaron, Dcroat, Ecaron, Edieresis,
    uni1EB8, Egrave, uni01EE, Gcaron, uni01CF, Idieresis, uni1ECA, Igrave, uni01E8,
    uni01E8.ss02, uni013B.loclMAH, uni013B.loclMAH.ss02, Ldot, Ldot.ss02, Ncaron,
    uni0145.loclMAH, Odieresis, uni1ECC, Ograve, Ohungarumlaut, Rcaron, Scaron,
    Tcaron, Udieresis, uni1EE4, Ugrave, Uhungarumlaut, Wdieresis, Wgrave,
    Ydieresis, Ygrave, Zcaron, uni01CE, uni01CE.cv01, uni01CE.ss01,
    uni01CE.ss01.cv01, uni01CE.ss02, uni01CE.ss02.cv01, adieresis …

4) Transformed components (масштаб/поворот/инверсия)
- Убрать трансформации компонентов или перевести их в контуры для глифов:
  - uni018E (component E), uni0281 (component uni044F), a.small (component a), b.small (component b),
    c.small (component c), d (component b), d.small (component d), dcroat (component uni0335),
    e.small (component e), uni01DD (component e), uni0259 (component e), uni0259.small (component uni0259),
    f.small (component f), g.small (component g), h.small (component h), i.small (component i),
    j.small (component j), k.small (component k), l.small (component l), ldot (component uni0307),
    ldot.ss01 (component uni0307), m.small (component m), n.small (component n), o.small (component o),
    p (component b), p.small (component p), q (component b), q.small (component q), r.small (component r),
    s.small (component s), longs (component uni0237), t.small (component t), u (component n), u.small (component u),
    v.small (component v), w.small (component w), x.small (component x), y.small (component y), z.small (component z),
    uni0413 (component L), uni0413.ss02 (component L.ss02), uni0418 (component N), uni041B.loclBGR (component V),
    uni042C (component P), uni0404 (component uni042D), uni040B (component uni0427), uni042F (component R),
    uni04BA (component uni0427), uni0510 (component uni0417), uni043B.loclBGR (component v),
    uni0448.loclBGR (component uni0442.loclBGR), uni044D (component uni0454), uni04D9 (component e),
    uni0511 (component uni0437), nine (component six), zero.small (component zero)

5) Полу-вертикальные/полу-горизонтальные сегменты (advisory)
- Выровнять до строго вертик./гориз., если это не сознательный дизайн:
  - pi (две вертикали), uni0414, uni0426, uni044E, uni044E.loclBGR, uni04B4.

6) Очень короткие сегменты (advisory)
- Основные повторяющиеся группы (править в мастерах, затем пересобрать):
  - Латиница A-серии: A, Aacute, Abreve, uni01CD, Acircumflex, Adieresis, uni0226, uni1EA0, Agrave,
    Amacron, Aogonek, Aring, Aringacute, Atilde.
  - Альтернативы «a»: a.ss01 и все производные (aacute.ss01, abreve.ss01, …, aringacute.ss01, …).
  - Кириллица: uni0410, uni04D0, uni04D2, (часто) uni041B, uni0409, uni0512, некоторые локали/стили.
  - Прочее: Z, Zacute, Zcaron, Zdotaccent, f_f_j, f_f_l, f_j, germandbls, ampersand, uni2120, пары uni01B7/01EE,
    uni0292/01EF, и т.д. — см. развёрнутые списки в отчёте.

## Проверка после правок
- Пересохранить `sources/Akt.glyphs`.
- Запустить: `make build` → `python3 fix-font-issues.py` → `make qa`.
- Проверить, что разделы FAIL в отчёте исчезли или сократились.

Примечание: автоматом исправлены метрики/флаги/версия/имена/period/meta. Оставшиеся FAIL касаются именно контуров и компоновки глифов и должны решаться в источнике.
