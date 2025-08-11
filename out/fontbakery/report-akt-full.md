## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[27] Akt-Black.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;198.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;198.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;472.0,720.0&gt;--&lt;622.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni040B (U+040B): L&lt;&lt;344.0,0.0&gt;--&lt;194.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;628.0,0.0&gt;--&lt;478.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;325.0,500.0&gt;--&lt;467.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;360.0,500.0&gt;--&lt;500.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;56.0,500.0&gt;--&lt;196.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;56.0,500.0&gt;--&lt;196.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;362.0,500.0&gt;--&lt;504.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;642.0,500.0&gt;--&lt;784.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;56.0,500.0&gt;--&lt;192.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;244.0,0.0&gt;--&lt;104.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;498.0,0.0&gt;--&lt;356.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;426.0,240.0&gt;--&lt;410.0,487.0&gt;&gt; -&gt; L&lt;&lt;410.0,487.0&gt;--&lt;410.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;550.0,720.0&gt;--&lt;550.0,487.0&gt;&gt; -&gt; L&lt;&lt;550.0,487.0&gt;--&lt;534.0,240.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;106.0,261.0&gt;--&lt;90.0,14.0&gt;&gt; -&gt; L&lt;&lt;90.0,14.0&gt;--&lt;90.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;230.0,-219.0&gt;--&lt;230.0,14.0&gt;&gt; -&gt; L&lt;&lt;230.0,14.0&gt;--&lt;214.0,261.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;642.0,72.0&gt;--&lt;642.0,249.0&gt;&gt; -&gt; L&lt;&lt;642.0,249.0&gt;--&lt;642.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;626.0,240.0&gt;--&lt;610.0,487.0&gt;&gt; -&gt; L&lt;&lt;610.0,487.0&gt;--&lt;610.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;750.0,720.0&gt;--&lt;750.0,487.0&gt;&gt; -&gt; L&lt;&lt;750.0,487.0&gt;--&lt;734.0,240.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;205.0,720.0&gt;--&lt;205.0,580.0&gt;&gt; -&gt; L&lt;&lt;205.0,580.0&gt;--&lt;189.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;71.0,240.0&gt;--&lt;55.0,580.0&gt;&gt; -&gt; L&lt;&lt;55.0,580.0&gt;--&lt;55.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;178.0,720.0&gt;--&lt;178.0,620.0&gt;&gt; -&gt; L&lt;&lt;178.0,620.0&gt;--&lt;166.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;48.0,380.0&gt;--&lt;36.0,620.0&gt;&gt; -&gt; L&lt;&lt;36.0,620.0&gt;--&lt;36.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* pi (U+03C0): L&lt;&lt;244.0,380.0&gt;--&lt;246.0,0.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;413.0,0.0&gt;--&lt;415.0,380.0&gt;&gt;

* uni0414 (U+0414): L&lt;&lt;136.0,474.0&gt;--&lt;138.0,720.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;582.0,-160.0&gt;--&lt;581.0,0.0&gt;&gt;

* uni044E (U+044E): L&lt;&lt;304.0,316.0&gt;--&lt;305.0,196.0&gt;&gt;

* uni044E.loclBGR: L&lt;&lt;304.0,316.0&gt;--&lt;305.0,196.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;722.0,-160.0&gt;--&lt;721.0,0.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni01B7 (U+01B7) contains a short segment L&lt;&lt;341.0,436.0&gt;--&lt;346.0,436.0&gt;&gt;

* uni01EE (U+01EE) contains a short segment L&lt;&lt;341.0,436.0&gt;--&lt;346.0,436.0&gt;&gt;

* a.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* a.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aacute.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aacute.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* abreve.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* abreve.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni01CE.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni01CE.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* acircumflex.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* acircumflex.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* adieresis.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* adieresis.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni0227.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0227.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni1EA1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni1EA1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* agrave.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* agrave.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* amacron.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* amacron.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aogonek.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aogonek.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aring.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aring.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aringacute.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aringacute.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* atilde.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* atilde.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;290.0,220.0&gt;--&lt;292.0,220.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;290.0,220.0&gt;--&lt;292.0,220.0&gt;&gt;

* germandbls (U+00DF) contains a short segment B&lt;&lt;440.5,111.0&gt;-&lt;450.0,116.0&gt;-&lt;456.0,127.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;701.0,-86.0&gt;--&lt;730.0,-86.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni049A.ss01 contains a short segment L&lt;&lt;542.0,0.0&gt;--&lt;540.0,0.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni04E0 (U+04E0) contains a short segment L&lt;&lt;341.0,436.0&gt;--&lt;346.0,436.0&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;10.0,120.0&gt;--&lt;15.0,120.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;10.0,120.0&gt;--&lt;15.0,120.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;340.0,310.0&gt;--&lt;346.0,310.0&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;290.0,220.0&gt;--&lt;292.0,220.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;10.0,120.0&gt;--&lt;15.0,120.0&gt;&gt;

* ampersand (U+0026) contains a short segment B&lt;&lt;226.0,545.0&gt;-&lt;226.0,529.0&gt;-&lt;232.5,514.5&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;140.0,462.0&gt;--&lt;140.0,456.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;206.0,618.0&gt;--&lt;206.0,624.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[27] Akt-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;275.0,-20.0&gt;--&lt;275.0,94.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;198.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;198.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;472.0,720.0&gt;--&lt;622.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni040B (U+040B): L&lt;&lt;344.0,0.0&gt;--&lt;194.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;628.0,0.0&gt;--&lt;478.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;325.0,500.0&gt;--&lt;467.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;360.0,500.0&gt;--&lt;500.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;56.0,500.0&gt;--&lt;196.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;56.0,500.0&gt;--&lt;196.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;362.0,500.0&gt;--&lt;504.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;642.0,500.0&gt;--&lt;784.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;56.0,500.0&gt;--&lt;192.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;244.0,0.0&gt;--&lt;104.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;498.0,0.0&gt;--&lt;356.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;426.0,240.0&gt;--&lt;410.0,487.0&gt;&gt; -&gt; L&lt;&lt;410.0,487.0&gt;--&lt;410.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;550.0,720.0&gt;--&lt;550.0,487.0&gt;&gt; -&gt; L&lt;&lt;550.0,487.0&gt;--&lt;534.0,240.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;106.0,261.0&gt;--&lt;90.0,14.0&gt;&gt; -&gt; L&lt;&lt;90.0,14.0&gt;--&lt;90.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;230.0,-219.0&gt;--&lt;230.0,14.0&gt;&gt; -&gt; L&lt;&lt;230.0,14.0&gt;--&lt;214.0,261.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;642.0,72.0&gt;--&lt;642.0,249.0&gt;&gt; -&gt; L&lt;&lt;642.0,249.0&gt;--&lt;642.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt; -&gt; L&lt;&lt;182.0,280.0&gt;--&lt;459.0,280.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;626.0,240.0&gt;--&lt;610.0,487.0&gt;&gt; -&gt; L&lt;&lt;610.0,487.0&gt;--&lt;610.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;750.0,720.0&gt;--&lt;750.0,487.0&gt;&gt; -&gt; L&lt;&lt;750.0,487.0&gt;--&lt;734.0,240.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;205.0,720.0&gt;--&lt;205.0,580.0&gt;&gt; -&gt; L&lt;&lt;205.0,580.0&gt;--&lt;189.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;71.0,240.0&gt;--&lt;55.0,580.0&gt;&gt; -&gt; L&lt;&lt;55.0,580.0&gt;--&lt;55.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;178.0,720.0&gt;--&lt;178.0,620.0&gt;&gt; -&gt; L&lt;&lt;178.0,620.0&gt;--&lt;166.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;48.0,380.0&gt;--&lt;36.0,620.0&gt;&gt; -&gt; L&lt;&lt;36.0,620.0&gt;--&lt;36.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* pi (U+03C0): L&lt;&lt;244.0,380.0&gt;--&lt;246.0,0.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;413.0,0.0&gt;--&lt;415.0,380.0&gt;&gt;

* uni0414 (U+0414): L&lt;&lt;136.0,474.0&gt;--&lt;138.0,720.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;582.0,-160.0&gt;--&lt;581.0,0.0&gt;&gt;

* uni044E (U+044E): L&lt;&lt;304.0,316.0&gt;--&lt;305.0,196.0&gt;&gt;

* uni044E.loclBGR: L&lt;&lt;304.0,316.0&gt;--&lt;305.0,196.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;722.0,-160.0&gt;--&lt;721.0,0.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni01B7 (U+01B7) contains a short segment L&lt;&lt;341.0,436.0&gt;--&lt;346.0,436.0&gt;&gt;

* uni01EE (U+01EE) contains a short segment L&lt;&lt;341.0,436.0&gt;--&lt;346.0,436.0&gt;&gt;

* a.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* a.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aacute.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aacute.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* abreve.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* abreve.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni01CE.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni01CE.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* acircumflex.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* acircumflex.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* adieresis.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* adieresis.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni0227.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0227.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni1EA1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni1EA1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* agrave.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* agrave.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* amacron.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* amacron.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aogonek.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aogonek.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aring.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aring.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* aringacute.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* aringacute.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* atilde.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* atilde.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;290.0,220.0&gt;--&lt;292.0,220.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;290.0,220.0&gt;--&lt;292.0,220.0&gt;&gt;

* germandbls (U+00DF) contains a short segment B&lt;&lt;440.5,111.0&gt;-&lt;450.0,116.0&gt;-&lt;456.0,127.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;701.0,-86.0&gt;--&lt;730.0,-86.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni049A.ss01 contains a short segment L&lt;&lt;542.0,0.0&gt;--&lt;540.0,0.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;182.0,280.0&gt;--&lt;182.0,280.0&gt;&gt;

* uni04E0 (U+04E0) contains a short segment L&lt;&lt;341.0,436.0&gt;--&lt;346.0,436.0&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;10.0,120.0&gt;--&lt;15.0,120.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;10.0,120.0&gt;--&lt;15.0,120.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;340.0,310.0&gt;--&lt;346.0,310.0&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;290.0,220.0&gt;--&lt;292.0,220.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;10.0,120.0&gt;--&lt;15.0,120.0&gt;&gt;

* ampersand (U+0026) contains a short segment B&lt;&lt;226.0,545.0&gt;-&lt;226.0,529.0&gt;-&lt;232.5,514.5&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;140.0,462.0&gt;--&lt;140.0,456.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;206.0,618.0&gt;--&lt;206.0,624.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[28] Akt-ExtraLight.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;274.0,36.0&gt;--&lt;274.0,83.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;532.0,720.0&gt;--&lt;589.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;568.0,0.0&gt;--&lt;511.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;369.0,500.0&gt;--&lt;423.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;403.0,500.0&gt;--&lt;457.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;87.0,500.0&gt;--&lt;142.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;87.0,500.0&gt;--&lt;142.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;418.0,500.0&gt;--&lt;473.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;698.0,500.0&gt;--&lt;753.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;87.0,500.0&gt;--&lt;141.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;193.0,0.0&gt;--&lt;138.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;442.0,0.0&gt;--&lt;387.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;137.0,183.0&gt;--&lt;133.0,311.0&gt;&gt; -&gt; L&lt;&lt;133.0,311.0&gt;--&lt;133.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;187.0,720.0&gt;--&lt;187.0,311.0&gt;&gt; -&gt; L&lt;&lt;187.0,311.0&gt;--&lt;183.0,183.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;137.0,183.0&gt;--&lt;133.0,311.0&gt;&gt; -&gt; L&lt;&lt;133.0,311.0&gt;--&lt;133.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;187.0,720.0&gt;--&lt;187.0,311.0&gt;&gt; -&gt; L&lt;&lt;187.0,311.0&gt;--&lt;183.0,183.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;457.0,183.0&gt;--&lt;453.0,311.0&gt;&gt; -&gt; L&lt;&lt;453.0,311.0&gt;--&lt;453.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;507.0,720.0&gt;--&lt;507.0,311.0&gt;&gt; -&gt; L&lt;&lt;507.0,311.0&gt;--&lt;503.0,183.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;137.0,317.0&gt;--&lt;133.0,189.0&gt;&gt; -&gt; L&lt;&lt;133.0,189.0&gt;--&lt;133.0,-220.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;187.0,-220.0&gt;--&lt;187.0,189.0&gt;&gt; -&gt; L&lt;&lt;187.0,189.0&gt;--&lt;183.0,317.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* uni0446.loclBGR: L&lt;&lt;426.0,95.0&gt;--&lt;418.0,208.0&gt;&gt; -&gt; L&lt;&lt;418.0,208.0&gt;--&lt;418.0,500.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;700.0,78.0&gt;--&lt;698.0,208.0&gt;&gt; -&gt; L&lt;&lt;698.0,208.0&gt;--&lt;698.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt; -&gt; L&lt;&lt;161.0,251.0&gt;--&lt;494.0,251.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;657.0,183.0&gt;--&lt;653.0,311.0&gt;&gt; -&gt; L&lt;&lt;653.0,311.0&gt;--&lt;653.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;707.0,720.0&gt;--&lt;707.0,311.0&gt;&gt; -&gt; L&lt;&lt;707.0,311.0&gt;--&lt;703.0,183.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;137.0,183.0&gt;--&lt;133.0,311.0&gt;&gt; -&gt; L&lt;&lt;133.0,311.0&gt;--&lt;133.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;187.0,720.0&gt;--&lt;187.0,311.0&gt;&gt; -&gt; L&lt;&lt;187.0,311.0&gt;--&lt;183.0,183.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;106.0,240.0&gt;--&lt;101.0,580.0&gt;&gt; -&gt; L&lt;&lt;101.0,580.0&gt;--&lt;101.0,720.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;159.0,720.0&gt;--&lt;159.0,580.0&gt;&gt; -&gt; L&lt;&lt;159.0,580.0&gt;--&lt;154.0,240.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;134.0,720.0&gt;--&lt;134.0,620.0&gt;&gt; -&gt; L&lt;&lt;134.0,620.0&gt;--&lt;131.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;83.0,380.0&gt;--&lt;80.0,620.0&gt;&gt; -&gt; L&lt;&lt;80.0,620.0&gt;--&lt;80.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>


> 
> This check heuristically detects outline segments which form a particularly
> small angle, indicative of an outline error. This may cause false positives
> in cases such as extreme ink traps, so should be regarded as advisory and
> backed up by manual inspection.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3064





* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* eth (U+00F0): B&lt;&lt;422.0,427.0&gt;-&lt;443.0,401.0&gt;-&lt;448.0,381.0&gt;&gt;/B&lt;&lt;448.0,381.0&gt;-&lt;438.0,506.0&gt;-&lt;409.5,562.5&gt;&gt; = 9.462322208025613

* partialdiff (U+2202): B&lt;&lt;422.0,427.0&gt;-&lt;443.0,401.0&gt;-&lt;448.0,381.0&gt;&gt;/B&lt;&lt;448.0,381.0&gt;-&lt;438.0,506.0&gt;-&lt;409.5,562.5&gt;&gt; = 9.462322208025613

* uni0431 (U+0431): B&lt;&lt;132.5,543.0&gt;-&lt;115.0,490.0&gt;-&lt;109.0,377.0&gt;&gt;/B&lt;&lt;109.0,377.0&gt;-&lt;117.0,407.0&gt;-&lt;142.0,436.5&gt;&gt; = 11.892017609210653

* uni0431.ss01: B&lt;&lt;130.0,536.0&gt;-&lt;114.0,481.0&gt;-&lt;109.0,377.0&gt;&gt;/B&lt;&lt;109.0,377.0&gt;-&lt;117.0,407.0&gt;-&lt;142.0,436.5&gt;&gt; = 12.178931777868874
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* ldot (U+0140): L&lt;&lt;219.19635009765625,407.8531494140625&gt;--&lt;224.196044921875,407.875732421875&gt;&gt;

* ldot (U+0140): L&lt;&lt;224.629638671875,311.881591796875&gt;--&lt;219.62994384765625,311.8590087890625&gt;&gt;

* ldot.ss01: L&lt;&lt;228.19635009765625,407.8531494140625&gt;--&lt;233.196044921875,407.875732421875&gt;&gt;

* ldot.ss01: L&lt;&lt;233.629638671875,311.881591796875&gt;--&lt;228.62994384765625,311.8590087890625&gt;&gt;

* pi (U+03C0): L&lt;&lt;462.0,0.0&gt;--&lt;463.0,451.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;107.0,400.0&gt;--&lt;105.0,720.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;157.0,720.0&gt;--&lt;155.0,400.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;305.0,400.0&gt;--&lt;303.0,720.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;355.0,720.0&gt;--&lt;353.0,400.0&gt;&gt;

* quotesingle (U+0027): L&lt;&lt;121.0,400.0&gt;--&lt;119.0,720.0&gt;&gt;

* quotesingle (U+0027): L&lt;&lt;171.0,720.0&gt;--&lt;169.0,400.0&gt;&gt;

* uni02B9 (U+02B9): L&lt;&lt;139.0,720.0&gt;--&lt;137.0,400.0&gt;&gt;

* uni02B9 (U+02B9): L&lt;&lt;89.0,400.0&gt;--&lt;87.0,720.0&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;722.6917724609375,388.0982666015625&gt;--&lt;723.291748046875,388.1009521484375&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;723.554931640625,329.3033447265625&gt;--&lt;722.9549560546875,329.3006591796875&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;96.6917724609375,389.0982666015625&gt;--&lt;97.291748046875,389.1009521484375&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;97.554931640625,330.3033447265625&gt;--&lt;96.9549560546875,330.3006591796875&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* G (U+0047) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gbreve (U+011E) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gcaron (U+01E6) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gcircumflex (U+011C) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni0122 (U+0122) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gdotaccent (U+0120) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni1E20 (U+1E20) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni01E4 (U+01E4) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni1E9E (U+1E9E) contains a short segment L&lt;&lt;593.0,720.0&gt;--&lt;593.0,699.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;54.0,0.0&gt;--&lt;54.0,14.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;569.0,720.0&gt;--&lt;569.0,706.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;54.0,0.0&gt;--&lt;54.0,14.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;569.0,720.0&gt;--&lt;569.0,706.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;54.0,0.0&gt;--&lt;54.0,14.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;569.0,720.0&gt;--&lt;569.0,706.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;54.0,0.0&gt;--&lt;54.0,14.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;569.0,720.0&gt;--&lt;569.0,706.0&gt;&gt;

* ae (U+00E6) contains a short segment L&lt;&lt;371.0,279.0&gt;--&lt;371.0,295.0&gt;&gt;

* aeacute (U+01FD) contains a short segment L&lt;&lt;371.0,279.0&gt;--&lt;371.0,295.0&gt;&gt;

* uni01E3 (U+01E3) contains a short segment L&lt;&lt;371.0,279.0&gt;--&lt;371.0,295.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;217.0,213.0&gt;--&lt;236.0,213.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;217.0,213.0&gt;--&lt;236.0,213.0&gt;&gt;

* f_f_i contains a short segment L&lt;&lt;323.0,674.0&gt;--&lt;291.0,674.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;726.0,-153.0&gt;--&lt;740.0,-153.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;323.0,674.0&gt;--&lt;291.0,674.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;323.0,674.0&gt;--&lt;291.0,674.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;386.0,-153.0&gt;--&lt;400.0,-153.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* uni041B (U+041B) contains a short segment L&lt;&lt;34.0,53.0&gt;--&lt;49.0,53.0&gt;&gt;

* uni0409 (U+0409) contains a short segment L&lt;&lt;34.0,53.0&gt;--&lt;49.0,53.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;161.0,251.0&gt;--&lt;161.0,251.0&gt;&gt;

* uni0512 (U+0512) contains a short segment L&lt;&lt;34.0,53.0&gt;--&lt;49.0,53.0&gt;&gt;

* uni0431.ss01 contains a short segment L&lt;&lt;488.0,760.0&gt;--&lt;488.0,746.0&gt;&gt;

* uni0436.loclBGR.ss01 contains a short segment L&lt;&lt;59.0,46.0&gt;--&lt;82.0,46.0&gt;&gt;

* uni0436.loclBGR.ss01 contains a short segment L&lt;&lt;801.0,454.0&gt;--&lt;777.0,454.0&gt;&gt;

* uni0436.ss01 contains a short segment L&lt;&lt;59.0,46.0&gt;--&lt;82.0,46.0&gt;&gt;

* uni0436.ss01 contains a short segment L&lt;&lt;801.0,454.0&gt;--&lt;777.0,454.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;43.0,49.0&gt;--&lt;49.0,49.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;43.0,49.0&gt;--&lt;49.0,49.0&gt;&gt;

* uni0497.ss01 contains a short segment L&lt;&lt;59.0,46.0&gt;--&lt;82.0,46.0&gt;&gt;

* uni0497.ss01 contains a short segment L&lt;&lt;801.0,454.0&gt;--&lt;777.0,454.0&gt;&gt;

* uni04C2.ss01 contains a short segment L&lt;&lt;59.0,46.0&gt;--&lt;82.0,46.0&gt;&gt;

* uni04C2.ss01 contains a short segment L&lt;&lt;801.0,454.0&gt;--&lt;777.0,454.0&gt;&gt;

* uni04D5 (U+04D5) contains a short segment L&lt;&lt;371.0,279.0&gt;--&lt;371.0,295.0&gt;&gt;

* uni04DD.ss01 contains a short segment L&lt;&lt;59.0,46.0&gt;--&lt;82.0,46.0&gt;&gt;

* uni04DD.ss01 contains a short segment L&lt;&lt;801.0,454.0&gt;--&lt;777.0,454.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;217.0,213.0&gt;--&lt;236.0,213.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;43.0,49.0&gt;--&lt;49.0,49.0&gt;&gt;

* at (U+0040) contains a short segment L&lt;&lt;521.0,-141.0&gt;--&lt;489.0,-141.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;99.0,447.0&gt;--&lt;99.0,440.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;260.0,633.0&gt;--&lt;259.0,640.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[28] Akt-Light.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;274.0,25.0&gt;--&lt;274.0,85.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;520.0,720.0&gt;--&lt;596.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni040B (U+040B): L&lt;&lt;296.0,0.0&gt;--&lt;220.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;580.0,0.0&gt;--&lt;504.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;360.0,500.0&gt;--&lt;432.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;394.0,500.0&gt;--&lt;466.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;81.0,500.0&gt;--&lt;153.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;81.0,500.0&gt;--&lt;153.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;407.0,216.0&gt;--&lt;407.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;407.0,500.0&gt;--&lt;479.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;687.0,500.0&gt;--&lt;759.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;81.0,500.0&gt;--&lt;151.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;203.0,0.0&gt;--&lt;131.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;453.0,0.0&gt;--&lt;381.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;131.0,194.0&gt;--&lt;124.0,346.0&gt;&gt; -&gt; L&lt;&lt;124.0,346.0&gt;--&lt;124.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,346.0&gt;&gt; -&gt; L&lt;&lt;196.0,346.0&gt;--&lt;189.0,194.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;131.0,194.0&gt;--&lt;124.0,346.0&gt;&gt; -&gt; L&lt;&lt;124.0,346.0&gt;--&lt;124.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,346.0&gt;&gt; -&gt; L&lt;&lt;196.0,346.0&gt;--&lt;189.0,194.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;451.0,194.0&gt;--&lt;444.0,346.0&gt;&gt; -&gt; L&lt;&lt;444.0,346.0&gt;--&lt;444.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;516.0,720.0&gt;--&lt;516.0,346.0&gt;&gt; -&gt; L&lt;&lt;516.0,346.0&gt;--&lt;509.0,194.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;131.0,306.0&gt;--&lt;124.0,154.0&gt;&gt; -&gt; L&lt;&lt;124.0,154.0&gt;--&lt;124.0,-220.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;196.0,-220.0&gt;--&lt;196.0,154.0&gt;&gt; -&gt; L&lt;&lt;196.0,154.0&gt;--&lt;189.0,306.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* uni0446.loclBGR: L&lt;&lt;418.0,93.0&gt;--&lt;407.0,216.0&gt;&gt; -&gt; L&lt;&lt;407.0,216.0&gt;--&lt;407.0,500.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;688.0,77.0&gt;--&lt;687.0,216.0&gt;&gt; -&gt; L&lt;&lt;687.0,216.0&gt;--&lt;687.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt; -&gt; L&lt;&lt;165.0,257.0&gt;--&lt;487.0,257.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;651.0,194.0&gt;--&lt;644.0,346.0&gt;&gt; -&gt; L&lt;&lt;644.0,346.0&gt;--&lt;644.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;716.0,720.0&gt;--&lt;716.0,346.0&gt;&gt; -&gt; L&lt;&lt;716.0,346.0&gt;--&lt;709.0,194.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;131.0,194.0&gt;--&lt;124.0,346.0&gt;&gt; -&gt; L&lt;&lt;124.0,346.0&gt;--&lt;124.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,346.0&gt;&gt; -&gt; L&lt;&lt;196.0,346.0&gt;--&lt;189.0,194.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;168.0,720.0&gt;--&lt;168.0,580.0&gt;&gt; -&gt; L&lt;&lt;168.0,580.0&gt;--&lt;161.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;99.0,240.0&gt;--&lt;92.0,580.0&gt;&gt; -&gt; L&lt;&lt;92.0,580.0&gt;--&lt;92.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;143.0,720.0&gt;--&lt;143.0,620.0&gt;&gt; -&gt; L&lt;&lt;143.0,620.0&gt;--&lt;138.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;76.0,380.0&gt;--&lt;71.0,620.0&gt;&gt; -&gt; L&lt;&lt;71.0,620.0&gt;--&lt;71.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>


> 
> This check heuristically detects outline segments which form a particularly
> small angle, indicative of an outline error. This may cause false positives
> in cases such as extreme ink traps, so should be regarded as advisory and
> backed up by manual inspection.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3064





* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* eth (U+00F0): B&lt;&lt;409.5,432.5&gt;-&lt;431.0,408.0&gt;-&lt;438.0,387.0&gt;&gt;/B&lt;&lt;438.0,387.0&gt;-&lt;428.0,504.0&gt;-&lt;400.5,556.5&gt;&gt; = 13.549746254804694

* partialdiff (U+2202): B&lt;&lt;409.5,432.5&gt;-&lt;431.0,408.0&gt;-&lt;438.0,387.0&gt;&gt;/B&lt;&lt;438.0,387.0&gt;-&lt;428.0,504.0&gt;-&lt;400.5,556.5&gt;&gt; = 13.549746254804694

* uni0431 (U+0431): B&lt;&lt;141.5,537.5&gt;-&lt;125.0,488.0&gt;-&lt;120.0,384.0&gt;&gt;/B&lt;&lt;120.0,384.0&gt;-&lt;128.0,412.0&gt;-&lt;153.0,439.5&gt;&gt; = 13.192910500654156

* uni0431.ss01: B&lt;&lt;140.0,532.5&gt;-&lt;124.0,482.0&gt;-&lt;120.0,384.0&gt;&gt;/B&lt;&lt;120.0,384.0&gt;-&lt;128.0,412.0&gt;-&lt;153.0,439.5&gt;&gt; = 13.608090041799032
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* ldot (U+0140): L&lt;&lt;234.25006103515625,417.25250244140625&gt;--&lt;239.249755859375,417.28607177734375&gt;&gt;

* ldot (U+0140): L&lt;&lt;240.01513671875,303.29302978515625&gt;--&lt;235.01544189453125,303.25946044921875&gt;&gt;

* ldot.ss01: L&lt;&lt;242.25006103515625,417.25250244140625&gt;--&lt;247.249755859375,417.28607177734375&gt;&gt;

* ldot.ss01: L&lt;&lt;248.01513671875,303.29302978515625&gt;--&lt;243.01544189453125,303.25946044921875&gt;&gt;

* pi (U+03C0): L&lt;&lt;206.0,437.0&gt;--&lt;207.0,0.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;452.0,0.0&gt;--&lt;453.0,437.0&gt;&gt;

* uni0414.loclBGR: L&lt;&lt;106.0,0.0&gt;--&lt;105.0,-160.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;688.0,77.0&gt;--&lt;687.0,216.0&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;722.8045654296875,393.8458251953125&gt;--&lt;723.404541015625,393.849853515625&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;723.871826171875,324.252685546875&gt;--&lt;723.2718505859375,324.2486572265625&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;96.8045654296875,394.8458251953125&gt;--&lt;97.404541015625,394.849853515625&gt;&gt;

* uni25CC (U+25CC): L&lt;&lt;97.871826171875,325.252685546875&gt;--&lt;97.2718505859375,325.2486572265625&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni1E9E (U+1E9E) contains a short segment L&lt;&lt;596.0,720.0&gt;--&lt;596.0,694.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;51.0,0.0&gt;--&lt;51.0,17.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;573.0,720.0&gt;--&lt;573.0,703.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;51.0,0.0&gt;--&lt;51.0,17.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;573.0,720.0&gt;--&lt;573.0,703.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;51.0,0.0&gt;--&lt;51.0,17.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;573.0,720.0&gt;--&lt;573.0,703.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;51.0,0.0&gt;--&lt;51.0,17.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;573.0,720.0&gt;--&lt;573.0,703.0&gt;&gt;

* ae (U+00E6) contains a short segment L&lt;&lt;362.0,283.0&gt;--&lt;362.0,301.0&gt;&gt;

* aeacute (U+01FD) contains a short segment L&lt;&lt;362.0,283.0&gt;--&lt;362.0,301.0&gt;&gt;

* uni01E3 (U+01E3) contains a short segment L&lt;&lt;362.0,283.0&gt;--&lt;362.0,301.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;232.0,214.0&gt;--&lt;247.0,214.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;232.0,214.0&gt;--&lt;247.0,214.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;721.0,-140.0&gt;--&lt;738.0,-140.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;327.0,661.0&gt;--&lt;290.0,661.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;327.0,661.0&gt;--&lt;290.0,661.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;381.0,-140.0&gt;--&lt;398.0,-140.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni041B (U+041B) contains a short segment L&lt;&lt;31.0,69.0&gt;--&lt;48.0,69.0&gt;&gt;

* uni0409 (U+0409) contains a short segment L&lt;&lt;31.0,69.0&gt;--&lt;48.0,69.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;165.0,257.0&gt;--&lt;165.0,257.0&gt;&gt;

* uni0512 (U+0512) contains a short segment L&lt;&lt;31.0,69.0&gt;--&lt;48.0,69.0&gt;&gt;

* uni0436.loclBGR.ss01 contains a short segment L&lt;&lt;55.0,59.0&gt;--&lt;80.0,59.0&gt;&gt;

* uni0436.loclBGR.ss01 contains a short segment L&lt;&lt;805.0,441.0&gt;--&lt;779.0,441.0&gt;&gt;

* uni0436.ss01 contains a short segment L&lt;&lt;55.0,59.0&gt;--&lt;80.0,59.0&gt;&gt;

* uni0436.ss01 contains a short segment L&lt;&lt;805.0,441.0&gt;--&lt;779.0,441.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;36.0,63.0&gt;--&lt;42.0,63.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;36.0,63.0&gt;--&lt;42.0,63.0&gt;&gt;

* uni0497.ss01 contains a short segment L&lt;&lt;55.0,59.0&gt;--&lt;80.0,59.0&gt;&gt;

* uni0497.ss01 contains a short segment L&lt;&lt;805.0,441.0&gt;--&lt;779.0,441.0&gt;&gt;

* uni04C2.ss01 contains a short segment L&lt;&lt;55.0,59.0&gt;--&lt;80.0,59.0&gt;&gt;

* uni04C2.ss01 contains a short segment L&lt;&lt;805.0,441.0&gt;--&lt;779.0,441.0&gt;&gt;

* uni04D5 (U+04D5) contains a short segment L&lt;&lt;362.0,283.0&gt;--&lt;362.0,301.0&gt;&gt;

* uni04DD.ss01 contains a short segment L&lt;&lt;55.0,59.0&gt;--&lt;80.0,59.0&gt;&gt;

* uni04DD.ss01 contains a short segment L&lt;&lt;805.0,441.0&gt;--&lt;779.0,441.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;232.0,214.0&gt;--&lt;247.0,214.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;36.0,63.0&gt;--&lt;42.0,63.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;107.0,450.0&gt;--&lt;107.0,443.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;249.0,630.0&gt;--&lt;248.0,637.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[27] Akt-Medium.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;275.0,2.0&gt;--&lt;275.0,89.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;174.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;174.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;174.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;176.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;176.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;496.0,720.0&gt;--&lt;609.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;604.0,0.0&gt;--&lt;491.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;342.0,500.0&gt;--&lt;450.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;377.0,500.0&gt;--&lt;483.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;69.0,500.0&gt;--&lt;174.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;69.0,500.0&gt;--&lt;174.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;384.0,500.0&gt;--&lt;491.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;664.0,500.0&gt;--&lt;771.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;69.0,500.0&gt;--&lt;171.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;223.0,0.0&gt;--&lt;118.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;476.0,0.0&gt;--&lt;369.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;119.0,217.0&gt;--&lt;107.0,416.0&gt;&gt; -&gt; L&lt;&lt;107.0,416.0&gt;--&lt;107.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;213.0,720.0&gt;--&lt;213.0,416.0&gt;&gt; -&gt; L&lt;&lt;213.0,416.0&gt;--&lt;201.0,217.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;119.0,217.0&gt;--&lt;107.0,416.0&gt;&gt; -&gt; L&lt;&lt;107.0,416.0&gt;--&lt;107.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;213.0,720.0&gt;--&lt;213.0,416.0&gt;&gt; -&gt; L&lt;&lt;213.0,416.0&gt;--&lt;201.0,217.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;439.0,217.0&gt;--&lt;427.0,416.0&gt;&gt; -&gt; L&lt;&lt;427.0,416.0&gt;--&lt;427.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;533.0,720.0&gt;--&lt;533.0,416.0&gt;&gt; -&gt; L&lt;&lt;533.0,416.0&gt;--&lt;521.0,217.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;119.0,284.0&gt;--&lt;107.0,85.0&gt;&gt; -&gt; L&lt;&lt;107.0,85.0&gt;--&lt;107.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;213.0,-219.0&gt;--&lt;213.0,85.0&gt;&gt; -&gt; L&lt;&lt;213.0,85.0&gt;--&lt;201.0,284.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;665.0,74.0&gt;--&lt;664.0,233.0&gt;&gt; -&gt; L&lt;&lt;664.0,233.0&gt;--&lt;664.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt; -&gt; L&lt;&lt;173.0,269.0&gt;--&lt;473.0,269.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;639.0,217.0&gt;--&lt;627.0,416.0&gt;&gt; -&gt; L&lt;&lt;627.0,416.0&gt;--&lt;627.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;733.0,720.0&gt;--&lt;733.0,416.0&gt;&gt; -&gt; L&lt;&lt;733.0,416.0&gt;--&lt;721.0,217.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;119.0,217.0&gt;--&lt;107.0,416.0&gt;&gt; -&gt; L&lt;&lt;107.0,416.0&gt;--&lt;107.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;213.0,720.0&gt;--&lt;213.0,416.0&gt;&gt; -&gt; L&lt;&lt;213.0,416.0&gt;--&lt;201.0,217.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;186.0,720.0&gt;--&lt;186.0,580.0&gt;&gt; -&gt; L&lt;&lt;186.0,580.0&gt;--&lt;175.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;85.0,240.0&gt;--&lt;74.0,580.0&gt;&gt; -&gt; L&lt;&lt;74.0,580.0&gt;--&lt;74.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;161.0,720.0&gt;--&lt;161.0,620.0&gt;&gt; -&gt; L&lt;&lt;161.0,620.0&gt;--&lt;152.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;62.0,380.0&gt;--&lt;53.0,620.0&gt;&gt; -&gt; L&lt;&lt;53.0,620.0&gt;--&lt;53.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* pi (U+03C0): L&lt;&lt;225.0,409.0&gt;--&lt;227.0,0.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;433.0,0.0&gt;--&lt;434.0,409.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;606.0,-160.0&gt;--&lt;605.0,0.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;665.0,74.0&gt;--&lt;664.0,233.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;746.0,-160.0&gt;--&lt;745.0,0.0&gt;&gt;

* uni1E9E (U+1E9E): L&lt;&lt;447.0,624.0&gt;--&lt;184.0,626.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni01B7 (U+01B7) contains a short segment L&lt;&lt;310.0,430.0&gt;--&lt;328.0,430.0&gt;&gt;

* uni01EE (U+01EE) contains a short segment L&lt;&lt;310.0,430.0&gt;--&lt;328.0,430.0&gt;&gt;

* ae (U+00E6) contains a short segment L&lt;&lt;345.0,291.0&gt;--&lt;345.0,313.0&gt;&gt;

* aeacute (U+01FD) contains a short segment L&lt;&lt;345.0,291.0&gt;--&lt;345.0,313.0&gt;&gt;

* uni01E3 (U+01E3) contains a short segment L&lt;&lt;345.0,291.0&gt;--&lt;345.0,313.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;261.0,217.0&gt;--&lt;270.0,217.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;261.0,217.0&gt;--&lt;270.0,217.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;711.0,-113.0&gt;--&lt;734.0,-113.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;371.0,-113.0&gt;--&lt;394.0,-113.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni041B (U+041B) contains a short segment L&lt;&lt;26.0,101.0&gt;--&lt;47.0,101.0&gt;&gt;

* uni0409 (U+0409) contains a short segment L&lt;&lt;26.0,101.0&gt;--&lt;47.0,101.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;173.0,269.0&gt;--&lt;173.0,269.0&gt;&gt;

* uni04E0 (U+04E0) contains a short segment L&lt;&lt;310.0,430.0&gt;--&lt;328.0,430.0&gt;&gt;

* uni0512 (U+0512) contains a short segment L&lt;&lt;26.0,101.0&gt;--&lt;47.0,101.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;23.0,91.0&gt;--&lt;29.0,91.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;23.0,91.0&gt;--&lt;29.0,91.0&gt;&gt;

* uni04D5 (U+04D5) contains a short segment L&lt;&lt;345.0,291.0&gt;--&lt;345.0,313.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;261.0,217.0&gt;--&lt;270.0,217.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;23.0,91.0&gt;--&lt;29.0,91.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;123.0,456.0&gt;--&lt;124.0,449.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;227.0,624.0&gt;--&lt;227.0,631.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[27] Akt-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;275.0,13.0&gt;--&lt;275.0,87.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;163.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;163.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;163.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;165.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;165.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;508.0,720.0&gt;--&lt;602.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni040B (U+040B): L&lt;&lt;308.0,0.0&gt;--&lt;214.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;592.0,0.0&gt;--&lt;498.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;351.0,500.0&gt;--&lt;441.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;386.0,500.0&gt;--&lt;474.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;75.0,500.0&gt;--&lt;163.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;75.0,500.0&gt;--&lt;163.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;395.0,500.0&gt;--&lt;485.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;675.0,500.0&gt;--&lt;765.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;75.0,500.0&gt;--&lt;161.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;213.0,0.0&gt;--&lt;125.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;465.0,0.0&gt;--&lt;375.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;125.0,206.0&gt;--&lt;116.0,381.0&gt;&gt; -&gt; L&lt;&lt;116.0,381.0&gt;--&lt;116.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;204.0,720.0&gt;--&lt;204.0,381.0&gt;&gt; -&gt; L&lt;&lt;204.0,381.0&gt;--&lt;195.0,206.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;125.0,206.0&gt;--&lt;116.0,381.0&gt;&gt; -&gt; L&lt;&lt;116.0,381.0&gt;--&lt;116.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;204.0,720.0&gt;--&lt;204.0,381.0&gt;&gt; -&gt; L&lt;&lt;204.0,381.0&gt;--&lt;195.0,206.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;445.0,206.0&gt;--&lt;436.0,381.0&gt;&gt; -&gt; L&lt;&lt;436.0,381.0&gt;--&lt;436.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;524.0,720.0&gt;--&lt;524.0,381.0&gt;&gt; -&gt; L&lt;&lt;524.0,381.0&gt;--&lt;515.0,206.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;125.0,295.0&gt;--&lt;116.0,120.0&gt;&gt; -&gt; L&lt;&lt;116.0,120.0&gt;--&lt;116.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;204.0,-219.0&gt;--&lt;204.0,120.0&gt;&gt; -&gt; L&lt;&lt;204.0,120.0&gt;--&lt;195.0,295.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;677.0,75.0&gt;--&lt;675.0,225.0&gt;&gt; -&gt; L&lt;&lt;675.0,225.0&gt;--&lt;675.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt; -&gt; L&lt;&lt;169.0,263.0&gt;--&lt;480.0,263.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;645.0,206.0&gt;--&lt;636.0,381.0&gt;&gt; -&gt; L&lt;&lt;636.0,381.0&gt;--&lt;636.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;724.0,720.0&gt;--&lt;724.0,381.0&gt;&gt; -&gt; L&lt;&lt;724.0,381.0&gt;--&lt;715.0,206.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;125.0,206.0&gt;--&lt;116.0,381.0&gt;&gt; -&gt; L&lt;&lt;116.0,381.0&gt;--&lt;116.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;204.0,720.0&gt;--&lt;204.0,381.0&gt;&gt; -&gt; L&lt;&lt;204.0,381.0&gt;--&lt;195.0,206.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;177.0,720.0&gt;--&lt;177.0,580.0&gt;&gt; -&gt; L&lt;&lt;177.0,580.0&gt;--&lt;168.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;92.0,240.0&gt;--&lt;83.0,580.0&gt;&gt; -&gt; L&lt;&lt;83.0,580.0&gt;--&lt;83.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;152.0,720.0&gt;--&lt;152.0,620.0&gt;&gt; -&gt; L&lt;&lt;152.0,620.0&gt;--&lt;145.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;69.0,380.0&gt;--&lt;62.0,620.0&gt;&gt; -&gt; L&lt;&lt;62.0,620.0&gt;--&lt;62.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* pi (U+03C0): L&lt;&lt;216.0,423.0&gt;--&lt;217.0,0.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;443.0,0.0&gt;--&lt;444.0,423.0&gt;&gt;

* uni0414.loclBGR: L&lt;&lt;118.0,0.0&gt;--&lt;117.0,-160.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;618.0,-160.0&gt;--&lt;617.0,0.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;758.0,-160.0&gt;--&lt;757.0,0.0&gt;&gt;

* uni1E9E (U+1E9E): L&lt;&lt;466.0,639.0&gt;--&lt;172.0,641.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;49.0,0.0&gt;--&lt;49.0,19.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;577.0,720.0&gt;--&lt;577.0,701.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;49.0,0.0&gt;--&lt;49.0,19.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;577.0,720.0&gt;--&lt;577.0,701.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;49.0,0.0&gt;--&lt;49.0,19.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;577.0,720.0&gt;--&lt;577.0,701.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;49.0,0.0&gt;--&lt;49.0,19.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;577.0,720.0&gt;--&lt;577.0,701.0&gt;&gt;

* ae (U+00E6) contains a short segment L&lt;&lt;354.0,287.0&gt;--&lt;354.0,307.0&gt;&gt;

* aeacute (U+01FD) contains a short segment L&lt;&lt;354.0,287.0&gt;--&lt;354.0,307.0&gt;&gt;

* uni01E3 (U+01E3) contains a short segment L&lt;&lt;354.0,287.0&gt;--&lt;354.0,307.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;246.0,216.0&gt;--&lt;259.0,216.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;246.0,216.0&gt;--&lt;259.0,216.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;716.0,-126.0&gt;--&lt;736.0,-126.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;376.0,-126.0&gt;--&lt;396.0,-126.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* uni041B (U+041B) contains a short segment L&lt;&lt;29.0,85.0&gt;--&lt;48.0,85.0&gt;&gt;

* uni0409 (U+0409) contains a short segment L&lt;&lt;29.0,85.0&gt;--&lt;48.0,85.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;169.0,263.0&gt;--&lt;169.0,263.0&gt;&gt;

* uni0512 (U+0512) contains a short segment L&lt;&lt;29.0,85.0&gt;--&lt;48.0,85.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;30.0,77.0&gt;--&lt;36.0,77.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;30.0,77.0&gt;--&lt;36.0,77.0&gt;&gt;

* uni04D5 (U+04D5) contains a short segment L&lt;&lt;354.0,287.0&gt;--&lt;354.0,307.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;246.0,216.0&gt;--&lt;259.0,216.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;30.0,77.0&gt;--&lt;36.0,77.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;115.0,453.0&gt;--&lt;116.0,446.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;238.0,627.0&gt;--&lt;238.0,634.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[27] Akt-SemiBold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;275.0,-9.0&gt;--&lt;275.0,92.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;185.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;185.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;185.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;187.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;187.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;484.0,720.0&gt;--&lt;615.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;616.0,0.0&gt;--&lt;485.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;334.0,500.0&gt;--&lt;458.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;369.0,500.0&gt;--&lt;491.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;62.0,500.0&gt;--&lt;185.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;62.0,500.0&gt;--&lt;185.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;373.0,500.0&gt;--&lt;498.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;653.0,500.0&gt;--&lt;778.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;62.0,500.0&gt;--&lt;182.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;234.0,0.0&gt;--&lt;111.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;487.0,0.0&gt;--&lt;362.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;112.0,229.0&gt;--&lt;99.0,452.0&gt;&gt; -&gt; L&lt;&lt;99.0,452.0&gt;--&lt;99.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;221.0,720.0&gt;--&lt;221.0,452.0&gt;&gt; -&gt; L&lt;&lt;221.0,452.0&gt;--&lt;208.0,229.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;112.0,229.0&gt;--&lt;99.0,452.0&gt;&gt; -&gt; L&lt;&lt;99.0,452.0&gt;--&lt;99.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;221.0,720.0&gt;--&lt;221.0,452.0&gt;&gt; -&gt; L&lt;&lt;221.0,452.0&gt;--&lt;208.0,229.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;432.0,229.0&gt;--&lt;419.0,452.0&gt;&gt; -&gt; L&lt;&lt;419.0,452.0&gt;--&lt;419.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;541.0,720.0&gt;--&lt;541.0,452.0&gt;&gt; -&gt; L&lt;&lt;541.0,452.0&gt;--&lt;528.0,229.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;112.0,272.0&gt;--&lt;99.0,49.0&gt;&gt; -&gt; L&lt;&lt;99.0,49.0&gt;--&lt;99.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;221.0,-219.0&gt;--&lt;221.0,49.0&gt;&gt; -&gt; L&lt;&lt;221.0,49.0&gt;--&lt;208.0,272.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;654.0,73.0&gt;--&lt;653.0,241.0&gt;&gt; -&gt; L&lt;&lt;653.0,241.0&gt;--&lt;653.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt; -&gt; L&lt;&lt;178.0,274.0&gt;--&lt;466.0,274.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;632.0,229.0&gt;--&lt;619.0,452.0&gt;&gt; -&gt; L&lt;&lt;619.0,452.0&gt;--&lt;619.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;741.0,720.0&gt;--&lt;741.0,452.0&gt;&gt; -&gt; L&lt;&lt;741.0,452.0&gt;--&lt;728.0,229.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;112.0,229.0&gt;--&lt;99.0,452.0&gt;&gt; -&gt; L&lt;&lt;99.0,452.0&gt;--&lt;99.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;221.0,720.0&gt;--&lt;221.0,452.0&gt;&gt; -&gt; L&lt;&lt;221.0,452.0&gt;--&lt;208.0,229.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,580.0&gt;&gt; -&gt; L&lt;&lt;196.0,580.0&gt;--&lt;182.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;78.0,240.0&gt;--&lt;64.0,580.0&gt;&gt; -&gt; L&lt;&lt;64.0,580.0&gt;--&lt;64.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;169.0,720.0&gt;--&lt;169.0,620.0&gt;&gt; -&gt; L&lt;&lt;169.0,620.0&gt;--&lt;159.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;55.0,380.0&gt;--&lt;45.0,620.0&gt;&gt; -&gt; L&lt;&lt;45.0,620.0&gt;--&lt;45.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* pi (U+03C0): L&lt;&lt;235.0,394.0&gt;--&lt;236.0,0.0&gt;&gt;

* pi (U+03C0): L&lt;&lt;423.0,0.0&gt;--&lt;425.0,394.0&gt;&gt;

* uni0414.loclBGR: L&lt;&lt;143.0,0.0&gt;--&lt;142.0,-160.0&gt;&gt;

* uni0426 (U+0426): L&lt;&lt;594.0,-160.0&gt;--&lt;593.0,0.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;654.0,73.0&gt;--&lt;653.0,241.0&gt;&gt;

* uni04B4 (U+04B4): L&lt;&lt;734.0,-160.0&gt;--&lt;733.0,0.0&gt;&gt;

* uni1E9E (U+1E9E): L&lt;&lt;429.0,609.0&gt;--&lt;196.0,611.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>


> 
> This check looks for outline segments which seem particularly short (less
> than 0.6% of the overall path length).
> 
> This check is not run for variable fonts, as they may legitimately have
> short segments. As this check is liable to generate significant numbers
> of false positives, it will pass if there are more than
> 100 reported short segments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* A (U+0041) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Aacute (U+00C1) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Abreve (U+0102) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni01CD (U+01CD) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Acircumflex (U+00C2) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Adieresis (U+00C4) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni0226 (U+0226) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni1EA0 (U+1EA0) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Agrave (U+00C0) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Amacron (U+0100) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Aogonek (U+0104) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Aring (U+00C5) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Aringacute (U+01FA) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* Atilde (U+00C3) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni01B7 (U+01B7) contains a short segment L&lt;&lt;325.0,433.0&gt;--&lt;337.0,433.0&gt;&gt;

* uni01EE (U+01EE) contains a short segment L&lt;&lt;325.0,433.0&gt;--&lt;337.0,433.0&gt;&gt;

* uni0292 (U+0292) contains a short segment L&lt;&lt;275.0,219.0&gt;--&lt;281.0,219.0&gt;&gt;

* uni01EF (U+01EF) contains a short segment L&lt;&lt;275.0,219.0&gt;--&lt;281.0,219.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;706.0,-99.0&gt;--&lt;732.0,-99.0&gt;&gt;

* uni0410 (U+0410) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni0409 (U+0409) contains a short segment L&lt;&lt;23.0,118.0&gt;--&lt;47.0,118.0&gt;&gt;

* uni04D0 (U+04D0) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni04D2 (U+04D2) contains a short segment L&lt;&lt;178.0,274.0&gt;--&lt;178.0,274.0&gt;&gt;

* uni04E0 (U+04E0) contains a short segment L&lt;&lt;325.0,433.0&gt;--&lt;337.0,433.0&gt;&gt;

* uni043B (U+043B) contains a short segment L&lt;&lt;17.0,106.0&gt;--&lt;22.0,106.0&gt;&gt;

* uni0459 (U+0459) contains a short segment L&lt;&lt;17.0,106.0&gt;--&lt;22.0,106.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;334.0,304.0&gt;--&lt;348.0,304.0&gt;&gt;

* uni04E1 (U+04E1) contains a short segment L&lt;&lt;275.0,219.0&gt;--&lt;281.0,219.0&gt;&gt;

* uni0513 (U+0513) contains a short segment L&lt;&lt;17.0,106.0&gt;--&lt;22.0,106.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;132.0,459.0&gt;--&lt;132.0,453.0&gt;&gt;

* uni2120 (U+2120) contains a short segment L&lt;&lt;217.0,621.0&gt;--&lt;217.0,627.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[27] Akt-Thin.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>


> 
> Ensure that no glyph lacks its corresponding upper or lower counterpart
> (but only when unicode supports case-mapping).
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/3230





* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+039E: GREEK CAPITAL LETTER XI</td>
<td align="left">U+03BE: GREEK SMALL LETTER XI</td>
</tr>
<tr>
<td align="left">U+03B1: GREEK SMALL LETTER ALPHA</td>
<td align="left">U+0391: GREEK CAPITAL LETTER ALPHA</td>
</tr>
<tr>
<td align="left">U+1E03: LATIN SMALL LETTER B WITH DOT ABOVE</td>
<td align="left">U+1E02: LATIN CAPITAL LETTER B WITH DOT ABOVE</td>
</tr>
<tr>
<td align="left">U+1E28: LATIN CAPITAL LETTER H WITH CEDILLA</td>
<td align="left">U+1E29: LATIN SMALL LETTER H WITH CEDILLA</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure glyphs do not have components which are themselves components. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#nested-components">nested_components</a></summary>
    <div>


> 
> There have been bugs rendering variable fonts with nested components.
> Additionally, some static fonts with nested components have been reported
> to have rendering and printing issues.
> 
> For more info, see:
> * https://github.com/fonttools/fontbakery/issues/2961
> * https://github.com/arrowtype/recursive/issues/412
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2961





* 🔥 **FAIL** <p>The following glyphs have components which themselves are component glyphs:
* uni01CD
* Adieresis
* uni1EA0
* Agrave
* Ccaron
* Dcaron
* Dcroat
* Ecaron
* Edieresis
* uni1EB8
* Egrave
* uni01EE
* Gcaron
* uni01CF
* Idieresis
* uni1ECA
* Igrave
* uni01E8
* uni01E8.ss02
* uni013B.loclMAH
* uni013B.loclMAH.ss02
* Ldot
* Ldot.ss02
* Ncaron
* uni0145.loclMAH
* Odieresis
* uni1ECC
* Ograve
* Ohungarumlaut
* Rcaron
* Scaron
* Tcaron
* Udieresis
* uni1EE4
* Ugrave
* Uhungarumlaut
* Wdieresis
* Wgrave
* Ydieresis
* Ygrave
* Zcaron
* uni01CE
* uni01CE.cv01
* uni01CE.ss01
* uni01CE.ss01.cv01
* uni01CE.ss02
* uni01CE.ss02.cv01
* adieresis
* adieresis.cv01
* adieresis.ss01
* adieresis.ss01.cv01
* adieresis.ss02
* adieresis.ss02.cv01
* uni1EA1
* uni1EA1.cv01
* uni1EA1.ss01
* uni1EA1.ss01.cv01
* uni1EA1.ss02
* uni1EA1.ss02.cv01
* agrave
* agrave.cv01
* agrave.ss01
* agrave.ss01.cv01
* agrave.ss02
* agrave.ss02.cv01
* b.sub
* c.sub
* c.superior
* ccaron
* d.small
* d.sub
* dcaron
* dcroat
* ecaron
* edieresis
* uni1EB9
* egrave
* uni0259.small
* uni0259.superior
* uni01EF
* f.sub
* f.superior
* g.sub
* g.superior
* gcaron
* gcaron.ss01
* gcaron.ss02
* uni0123
* uni0123.ss01
* uni0123.ss02
* h.superior
* i.small
* i.sub
* uni01D0
* uni1ECB
* uni1ECB
* igrave
* ij
* ij
* j.small
* j.sub
* j.superior
* k.superior
* uni01E9
* uni01E9.ss02
* ncaron
* uni0146.loclMAH
* odieresis
* uni1ECD
* ograve
* ohungarumlaut
* p.small
* p.superior
* q.small
* q.sub
* q.superior
* r.sub
* rcaron
* rcaron.ss02
* scaron
* u.small
* u.sub
* u.superior
* uacute
* ubreve
* ucircumflex
* udieresis
* udieresis
* uni1EE5
* uni1EE5
* ugrave
* ugrave
* uhungarumlaut
* uhungarumlaut
* umacron
* uogonek
* uring
* utilde
* v.sub
* v.superior
* w.sub
* w.superior
* wdieresis
* wgrave
* x.superior
* y.sub
* y.superior
* ydieresis
* ydieresis.ss02
* ygrave
* ygrave.ss02
* z.sub
* z.superior
* zcaron
* uni2090
* uni2091
* uni2092
* uni2094
* uni2093
* ordfeminine
* ordmasculine
* uni2071
* uni207F
* uni0403
* uni0403.ss02
* uni0492
* uni0492.ss02
* uni0494
* uni0494.ss02
* uni0400
* uni0400
* uni0401
* uni0401
* uni0419
* uni0419
* uni040D
* uni040D
* uni0498
* uni04AA
* uni04AA
* uni04D0
* uni04D2
* uni04D2
* uni04D6
* uni04DA
* uni04DA
* uni04DC
* uni04DC.ss01
* uni04DE
* uni04E2
* uni04E4
* uni04E4
* uni04E6
* uni04E6
* uni04EA
* uni04EC
* uni04F0
* uni04F0.ss02
* uni04F2
* uni04F2.ss02
* uni04F4
* uni04F8
* uni0450
* uni0450
* uni0451
* uni0451
* uni0438.loclBGR
* uni0439
* uni0439.loclBGR
* uni0439.loclBGR
* uni045D
* uni0440
* uni045E
* uni0448.loclBGR
* uni0456
* uni0458
* uni0458.cv01
* uni0499
* uni04AB
* uni04D1
* uni04D1.ss01
* uni04D1.ss02
* uni04D3
* uni04D3
* uni04D3.cv01
* uni04D3.ss01
* uni04D3.ss01
* uni04D3.ss01.cv01
* uni04D3.ss02
* uni04D3.ss02
* uni04D3.ss02.cv01
* uni04D7
* uni04DB
* uni04DB
* uni04DD
* uni04DD.ss01
* uni04DF
* uni04E5
* uni04E7
* uni04E7
* uni04EB
* uni04ED
* uni04ED
* uni04EF
* uni04F1
* uni04F1
* uni04F1.ss02
* uni04F3
* uni04F3
* uni04F3.ss02
* uni04F5
* uni04F9
* uni2095
* uni2096
* uni2097
* uni2098
* uni2099
* uni209A
* uni209B
* uni209C
* nine.osf
* nine.small
* uni24FF
* uni2776
* uni2777
* uni2778
* uni2779
* uni277A
* uni277B
* uni277C
* uni277D
* uni277E
* uni24EA
* uni2460
* uni2461
* uni2462
* uni2463
* uni2464
* uni2465
* uni2466
* uni2467
* uni2468
* zero.dnom
* one.dnom
* two.dnom
* three.dnom
* four.dnom
* five.dnom
* six.dnom
* seven.dnom
* eight.dnom
* nine.dnom
* zero.numr
* one.numr
* two.numr
* three.numr
* four.numr
* five.numr
* six.numr
* seven.numr
* eight.numr
* nine.numr
* uni215F
* onehalf
* onehalf
* uni2189
* uni2189
* uni2153
* uni2153
* uni2154
* uni2154
* onequarter
* onequarter
* threequarters
* threequarters
* uni2155
* uni2155
* uni2156
* uni2156
* uni2157
* uni2157
* uni2158
* uni2158
* uni2159
* uni2159
* uni215A
* uni215A
* uni2150
* uni2150
* oneeighth
* oneeighth
* threeeighths
* threeeighths
* fiveeighths
* fiveeighths
* seveneighths
* seveneighths
* uni2151
* uni2151
* uni2152
* uni2152
* uni2152
* uni2080
* uni2081
* uni2082
* uni2083
* uni2084
* uni2085
* uni2086
* uni2087
* uni2088
* uni2089
* uni2070
* uni00B9
* uni00B2
* uni00B3
* uni2074
* uni2075
* uni2076
* uni2077
* uni2078
* uni2079
* period.sub
* period.superior
* comma.sub
* comma.superior
* colon.case
* semicolon.case
* uni2027
* uni2027.case
* backslash.case
* uni00AD.case
* uni2015.case
* uni208E
* uni207E
* quotedblleft
* quotedblright
* quoteleft
* quoteright
* guillemotleft.case
* guillemotright
* guillemotright.case
* guilsinglright.case
* uni2100
* uni2100
* uni2101
* uni2101
* uni2105
* uni2105
* uni2106
* uni2106
* uni208C
* uni207C
* uni208B
* uni207B
* uni228E
* plus.small
* multiply
* equal.small
* greaterequal
* plusminus
* percent
* percent
* perthousand
* perthousand
* uni208A
* uni207A
* uni2ABD
* propersuperset
* uni2ABE
* uni2AF6
* uni22F0
* uni2199
* arrowleft
* arrowboth
* arrowboth
* arrowupdn
* arrowupdn
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* uni25CC
* triaglf
* dieresis
* grave
* hungarumlaut
* caron
* uni02BB
* IJacute
* IJacute
* ijacute and ijacute</p>
 [code: found-nested-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure component transforms do not perform scaling or rotation. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#transformed-components">transformed_components</a></summary>
    <div>


> 
> Some families have glyphs which have been constructed by using
> transformed components e.g the 'u' being constructed from a flipped 'n'.
> 
> From a designers point of view, this sounds like a win (less work).
> However, such approaches can lead to rasterization issues, such as
> having the 'u' not sitting on the baseline at certain sizes after
> running the font through ttfautohint.
> 
> Other issues are outlines that end up reversed when only one dimension
> is flipped while the other isn't.
> 
> As of July 2019, Marc Foley observed that ttfautohint assigns cvt values
> to transformed glyphs as if they are not transformed and the result is
> they render very badly, and that vttLib does not support flipped components.
> 
> When building the font with fontmake, the problem can be fixed by adding
> this to the command line:
> 
> --filter DecomposeTransformedComponentsFilter
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2011





* 🔥 **FAIL** <p>The following glyphs had components with scaling or rotation
or inverted outline direction:</p>
<ul>
<li>uni018E (component E)</li>
<li>uni0281 (component uni044F)</li>
<li>a.small (component a)</li>
<li>b.small (component b)</li>
<li>c.small (component c)</li>
<li>d (component b)</li>
<li>d.small (component d)</li>
<li>dcroat (component uni0335)</li>
<li>e.small (component e)</li>
<li>uni01DD (component e)</li>
<li>uni0259 (component e)</li>
<li>uni0259.small (component uni0259)</li>
<li>f.small (component f)</li>
<li>g.small (component g)</li>
<li>h.small (component h)</li>
<li>i.small (component i)</li>
<li>j.small (component j)</li>
<li>k.small (component k)</li>
<li>l.small (component l)</li>
<li>ldot (component uni0307)</li>
<li>ldot.ss01 (component uni0307)</li>
<li>m.small (component m)</li>
<li>n.small (component n)</li>
<li>o.small (component o)</li>
<li>p (component b)</li>
<li>p.small (component p)</li>
<li>q (component b)</li>
<li>q.small (component q)</li>
<li>r.small (component r)</li>
<li>s.small (component s)</li>
<li>longs (component uni0237)</li>
<li>t.small (component t)</li>
<li>u (component n)</li>
<li>u.small (component u)</li>
<li>v.small (component v)</li>
<li>w.small (component w)</li>
<li>x.small (component x)</li>
<li>y.small (component y)</li>
<li>z.small (component z)</li>
<li>uni0413 (component L)</li>
<li>uni0413.ss02 (component L.ss02)</li>
<li>uni0418 (component N)</li>
<li>uni041B.loclBGR (component V)</li>
<li>uni042C (component P)</li>
<li>uni0404 (component uni042D)</li>
<li>uni040B (component uni0427)</li>
<li>uni042F (component R)</li>
<li>uni04BA (component uni0427)</li>
<li>uni0510 (component uni0417)</li>
<li>uni043B.loclBGR (component v)</li>
<li>uni0448.loclBGR (component uni0442.loclBGR)</li>
<li>uni044D (component uni0454)</li>
<li>uni04D9 (component e)</li>
<li>uni0511 (component uni0437)</li>
<li>nine (component six)</li>
<li>zero.small (component zero)</li>
<li>one.small (component one)</li>
<li>two.small (component two)</li>
<li>three.small (component three)</li>
<li>four.small (component four)</li>
<li>five.small (component five)</li>
<li>six.small (component six)</li>
<li>seven.small (component seven)</li>
<li>eight.small (component eight)</li>
<li>nine.small (component six.small)</li>
<li>zero.dnom (component zero.small)</li>
<li>one.dnom (component one.small)</li>
<li>two.dnom (component two.small)</li>
<li>three.dnom (component three.small)</li>
<li>four.dnom (component four.small)</li>
<li>five.dnom (component five.small)</li>
<li>six.dnom (component six.small)</li>
<li>seven.dnom (component seven.small)</li>
<li>eight.dnom (component eight.small)</li>
<li>nine.dnom (component nine.small)</li>
<li>zero.numr (component zero.small)</li>
<li>one.numr (component one.small)</li>
<li>two.numr (component two.small)</li>
<li>three.numr (component three.small)</li>
<li>four.numr (component four.small)</li>
<li>five.numr (component five.small)</li>
<li>six.numr (component six.small)</li>
<li>seven.numr (component seven.small)</li>
<li>eight.numr (component eight.small)</li>
<li>nine.numr (component nine.small)</li>
<li>period.small (component period)</li>
<li>comma.small (component comma)</li>
<li>exclamdown (component exclam)</li>
<li>questiondown (component question)</li>
<li>backslash (component slash)</li>
<li>backslash.case (component slash.case)</li>
<li>uni208E (component uni208D)</li>
<li>parenright (component parenleft)</li>
<li>parenright.case (component parenleft.case)</li>
<li>parenright.small (component parenleft.small)</li>
<li>braceright (component braceleft)</li>
<li>braceright.case (component braceleft.case)</li>
<li>bracketright (component bracketleft)</li>
<li>bracketright.case (component bracketleft.case)</li>
<li>angleright (component angleleft)</li>
<li>angleright.case (component angleleft.case)</li>
<li>quotedblleft (component quotedblbase)</li>
<li>quoteleft (component quotesinglbase)</li>
<li>guillemotright (component guillemotleft)</li>
<li>guillemotright.case (component guillemotleft.case)</li>
<li>guilsinglright (component guilsinglleft)</li>
<li>guilsinglright.case (component guilsinglleft.case)</li>
<li>plus (component minus)</li>
<li>plus.small (component plus)</li>
<li>minus.small (component minus)</li>
<li>multiply (component plus)</li>
<li>equal.small (component equal)</li>
<li>greater (component less)</li>
<li>greaterequal (component lessequal)</li>
<li>intersection (component union)</li>
<li>integral (component uni0237)</li>
<li>propersubset (component union)</li>
<li>uni2ABD (component uni228D)</li>
<li>propersuperset (component propersubset)</li>
<li>uni2ABE (component uni2ABD)</li>
<li>uni22F0 (component uni22F1)</li>
<li>arrowright (component arrowup)</li>
<li>uni2198 (component uni2197)</li>
<li>arrowdown (component arrowup)</li>
<li>uni2199 (component uni2198)</li>
<li>arrowleft (component arrowright)</li>
<li>uni2196 (component uni2197)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowboth (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>arrowupdn (component arrowright)</li>
<li>uni25D1 (component uni25D0)</li>
<li>uni25D2 (component uni25D0)</li>
<li>uni25D3 (component uni25D0)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>uni25CC (component periodcentered)</li>
<li>triagdn (component triagup)</li>
<li>triagrt (component triagup)</li>
<li>triaglf (component triagrt)</li>
<li>gravecomb (component acutecomb)</li>
<li>uni030C (component uni0302)</li>
<li>uni030C.narrow (component uni0302.narrow)</li>
<li>uni0312 (component uni0326)</li>
<li>ogonekmirrored (component uni0328)</li>
</ul>
 [code: transformed-components]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font family directory name. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-family-directory-name">googlefonts/metadata/family_directory_name</a></summary>
    <div>


> 
> We want the directory name of a font family to be predictable and directly
> derived from the family name, all lowercased and removing spaces.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3421





* 🔥 **FAIL** <p>Family name on METADATA.pb is &quot;Akt&quot;
Directory name is &quot;ttf&quot;
Expected &quot;akt&quot;</p>
 [code: bad-directory-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> METADATA.pb: Font filenames match font.filename entries? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-filenames">googlefonts/metadata/filenames</a></summary>
    <div>


> 
> Note:
> This check only looks for files in the current directory.
> 
> Font files in subdirectories are checked by these other two checks:
> - googlefonts/metadata/undeclared_fonts
> - googlefonts/repo/vf_has_static_fonts
> 
> We may want to merge them all into a single check.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2597





* 🔥 **FAIL** <p>Filename &quot;Akt-ExtraBold.ttf&quot; is listed on METADATA.pb but an actual font file with that name was not found.</p>
 [code: file-not-found]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure METADATA.pb lists all font binaries. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-undeclared-fonts">googlefonts/metadata/undeclared_fonts</a></summary>
    <div>


> 
> The set of font binaries available, except the ones on a "static" subdir,
> must match exactly those declared on the METADATA.pb file.
> 
> Also, to avoid confusion, we expect that font files (other than statics)
> are not placed on subdirectories.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2575





* 🔥 **FAIL** <p>The file &quot;Akt-ExtraBold.ttf&quot; declared on METADATA.pb is not available in this directory.</p>
 [code: file-missing]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Is this a proper HTML snippet? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-description-valid-html">googlefonts/description/valid_html</a></summary>
    <div>


> 
> Sometimes people write malformed HTML markup. This check should ensure the
> file is good.
> 
> Additionally, when packaging families for being pushed to the `google/fonts`
> git repo, if there is no DESCRIPTION.en_us.html file, some older versions of
> the `add_font.py` tool insert a placeholder description file which contains
> invalid html. This file needs to either be replaced with an existing
> description file or edited by hand.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2664
> See also: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>None does not include an HTML &lt;p&gt; tag.</p>
 [code: lacks-paragraph]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>


> 
> The dotted circle character (U+25CC) is inserted by shaping engines before
> mark glyphs which do not have an associated base, especially in the context
> of broken syllabic clusters.
> 
> For fonts containing combining marks, it is recommended that the dotted circle
> character be included so that these isolated marks can be displayed properly;
> for fonts supporting complex scripts, this should be considered mandatory.
> 
> Additionally, when a dotted circle glyph is present, it should be able to
> display all marks correctly, meaning that it should contain anchors for all
> attaching marks.
> 
> A fontmake filter can be used to automatically add a dotted_circle to a font:
> 
> fontmake --filter 'DottedCircleFilter(pre=True)' --filter '...'
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3600





* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- acutecomb

- dotbelowcomb

- gravecomb

- tildecomb

- uni0302

- uni0304

- uni0306

- uni0307

- uni0308

- uni030A

- uni030B

- uni030C

- uni0312

- uni0326

- uni0327

- uni0328

- uni0335
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>


> 
> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only
> be constructured in a handful of ways. This means a glyph's contour count
> will only differ slightly amongst different fonts, e.g a 'g' could either
> be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs
> to a display family.
> 
> This check currently does not cover variable fonts because there's plenty
> of alternative ways of constructing glyphs with multiple outlines for each
> feature in a VarFont. The expected contour count data for this check is
> currently optimized for the typical construction of glyphs in static fonts.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: AE	Contours detected: 3	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Dcroat	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Eth	Contours detected: 3	Expected: 2

- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

- Glyph name: F	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Q	Contours detected: 3	Expected: 2

- Glyph name: Tbar	Contours detected: 2	Expected: 1

- Glyph name: Thorn	Contours detected: 3	Expected: 1 or 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: a	Contours detected: 1	Expected: 2

- Glyph name: aacute	Contours detected: 2	Expected: 3

- Glyph name: abreve	Contours detected: 2	Expected: 3

- Glyph name: acircumflex	Contours detected: 2	Expected: 3

- Glyph name: adieresis	Contours detected: 3	Expected: 4

- Glyph name: agrave	Contours detected: 2	Expected: 3

- Glyph name: amacron	Contours detected: 2	Expected: 3

- Glyph name: aring	Contours detected: 3	Expected: 4

- Glyph name: arrowboth	Contours detected: 2	Expected: 1

- Glyph name: arrowupdn	Contours detected: 2	Expected: 1

- Glyph name: atilde	Contours detected: 2	Expected: 3

- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: currency	Contours detected: 6	Expected: 2

- Glyph name: dcroat	Contours detected: 3	Expected: 2

- Glyph name: e	Contours detected: 1	Expected: 2

- Glyph name: eacute	Contours detected: 2	Expected: 3

- Glyph name: ebreve	Contours detected: 2	Expected: 3

- Glyph name: ecaron	Contours detected: 2	Expected: 3

- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

- Glyph name: edieresis	Contours detected: 3	Expected: 4

- Glyph name: edotaccent	Contours detected: 2	Expected: 3

- Glyph name: egrave	Contours detected: 2	Expected: 3

- Glyph name: emacron	Contours detected: 2	Expected: 3

- Glyph name: eng	Contours detected: 2	Expected: 1

- Glyph name: estimated	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: fi	Contours detected: 1	Expected: 3

- Glyph name: fl	Contours detected: 1	Expected: 2

- Glyph name: hbar	Contours detected: 2	Expected: 1

- Glyph name: infinity	Contours detected: 4	Expected: 3

- Glyph name: integral	Contours detected: 2	Expected: 1

- Glyph name: lslash	Contours detected: 2	Expected: 1

- Glyph name: multiply	Contours detected: 2	Expected: 1

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

- Glyph name: plus	Contours detected: 2	Expected: 1

- Glyph name: plusminus	Contours detected: 3	Expected: 1 or 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni00B5	Contours detected: 2	Expected: 1

- Glyph name: uni018F	Contours detected: 1	Expected: 2

- Glyph name: uni01CE	Contours detected: 2	Expected: 3

- Glyph name: uni01DD	Contours detected: 1	Expected: 2

- Glyph name: uni01E2	Contours detected: 4	Expected: 3

- Glyph name: uni01E4	Contours detected: 2	Expected: 1

- Glyph name: uni01E5	Contours detected: 3	Expected: 2

- Glyph name: uni0227	Contours detected: 2	Expected: 3

- Glyph name: uni0259	Contours detected: 1	Expected: 2

- Glyph name: uni02BB	Contours detected: 2	Expected: 1

- Glyph name: uni0402	Contours detected: 2	Expected: 1

- Glyph name: uni0404	Contours detected: 2	Expected: 1

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 4	Expected: 2

- Glyph name: uni0416	Contours detected: 5	Expected: 1

- Glyph name: uni041A	Contours detected: 3	Expected: 1

- Glyph name: uni042A	Contours detected: 3	Expected: 2

- Glyph name: uni042D	Contours detected: 2	Expected: 1

- Glyph name: uni042E	Contours detected: 3	Expected: 2

- Glyph name: uni0430	Contours detected: 1	Expected: 2

- Glyph name: uni0435	Contours detected: 1	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044A	Contours detected: 3	Expected: 2

- Glyph name: uni044D	Contours detected: 2	Expected: 1

- Glyph name: uni044E	Contours detected: 3	Expected: 2

- Glyph name: uni0450	Contours detected: 2	Expected: 3

- Glyph name: uni0451	Contours detected: 3	Expected: 4

- Glyph name: uni0452	Contours detected: 3	Expected: 1

- Glyph name: uni0454	Contours detected: 2	Expected: 1

- Glyph name: uni045B	Contours detected: 2	Expected: 1

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni0462	Contours detected: 3	Expected: 2

- Glyph name: uni0492	Contours detected: 2	Expected: 1

- Glyph name: uni0493	Contours detected: 2	Expected: 1

- Glyph name: uni0494	Contours detected: 2	Expected: 1

- Glyph name: uni0495	Contours detected: 2	Expected: 1

- Glyph name: uni0496	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni049C	Contours detected: 3	Expected: 1

- Glyph name: uni049E	Contours detected: 4	Expected: 1

- Glyph name: uni049F	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni04A0	Contours detected: 4	Expected: 1

- Glyph name: uni04A1	Contours detected: 4	Expected: 1

- Glyph name: uni04A4	Contours detected: 2	Expected: 1

- Glyph name: uni04A5	Contours detected: 2	Expected: 1

- Glyph name: uni04A6	Contours detected: 2	Expected: 1

- Glyph name: uni04A7	Contours detected: 2	Expected: 1

- Glyph name: uni04A8	Contours detected: 1	Expected: 2

- Glyph name: uni04A9	Contours detected: 1	Expected: 2

- Glyph name: uni04B0	Contours detected: 2	Expected: 1

- Glyph name: uni04B4	Contours detected: 2	Expected: 1

- Glyph name: uni04B5	Contours detected: 2	Expected: 1

- Glyph name: uni04C1	Contours detected: 6	Expected: 2

- Glyph name: uni04C3	Contours detected: 2	Expected: 1

- Glyph name: uni04C7	Contours detected: 2	Expected: 1

- Glyph name: uni04C8	Contours detected: 2	Expected: 1

- Glyph name: uni04D1	Contours detected: 2	Expected: 3

- Glyph name: uni04D3	Contours detected: 3	Expected: 4

- Glyph name: uni04D4	Contours detected: 3	Expected: 2

- Glyph name: uni04D7	Contours detected: 2	Expected: 3

- Glyph name: uni04D8	Contours detected: 1	Expected: 2

- Glyph name: uni04D9	Contours detected: 1	Expected: 2

- Glyph name: uni04DA	Contours detected: 3	Expected: 4

- Glyph name: uni04DB	Contours detected: 3	Expected: 4

- Glyph name: uni04DC	Contours detected: 7	Expected: 3

- Glyph name: uni04EC	Contours detected: 4	Expected: 3

- Glyph name: uni04ED	Contours detected: 4	Expected: 3

- Glyph name: uni1EA1	Contours detected: 2	Expected: 3

- Glyph name: uni1EB9	Contours detected: 2	Expected: 3

- Glyph name: uni1EBD	Contours detected: 2	Expected: 3

- Glyph name: uni207A	Contours detected: 2	Expected: 1

- Glyph name: uni208A	Contours detected: 2	Expected: 1

- Glyph name: uni20BD	Contours detected: 3	Expected: 2

- Glyph name: uni20BF	Contours detected: 5	Expected: 3

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there caret positions declared for every ligature? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#ligature-carets">ligature_carets</a></summary>
    <div>


> 
> All ligatures in a font must have corresponding caret (text cursor) positions
> defined in the GDEF table, otherwhise, users may experience issues with
> caret rendering.
> 
> If using GlyphsApp or UFOs, ligature carets can be defined as anchors with
> names starting with `caret_`. These can be compiled with fontmake as of
> version v2.4.0.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/1225





* ⚠️ **WARN** <p>This font lacks caret position values for ligature glyphs on its GDEF table.</p>
 [code: lacks-caret-pos]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>


> 
> It is a common practice to have math signs sharing the same width
> (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs
> knowing that their design can easily share the same width.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3832





* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, uni2ABD, propersuperset, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;274.0,47.0&gt;--&lt;274.0,80.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;544.0,720.0&gt;--&lt;583.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;556.0,0.0&gt;--&lt;517.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;377.0,500.0&gt;--&lt;415.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;411.0,500.0&gt;--&lt;449.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;94.0,500.0&gt;--&lt;131.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;94.0,500.0&gt;--&lt;131.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0446.loclBGR: L&lt;&lt;429.0,500.0&gt;--&lt;466.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni0449.loclBGR: L&lt;&lt;709.0,500.0&gt;--&lt;746.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;94.0,500.0&gt;--&lt;130.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F (U+049F): L&lt;&lt;183.0,0.0&gt;--&lt;145.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;182.0,0.0&gt;--&lt;145.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;431.0,0.0&gt;--&lt;394.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>


> 
> The 'Soft Hyphen' character (codepoint 0x00AD) is used to mark
> a hyphenation possibility within a word in the absence of or
> overriding dictionary hyphenation.
> 
> It is sometimes designed empty with no width (such as a control character),
> sometimes the same as the traditional hyphen, sometimes double encoded with
> the hyphen.
> 
> That being said, it is recommended to not include it in the font at all,
> because discretionary hyphenation should be handled at the level of the
> shaping engine, not the font. Also, even if present, the software would
> not display that character.
> 
> More discussion at:
> https://typedrawers.com/discussion/2046/special-dash-things-softhyphen-horizontalbar
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4046
> See also: https://github.com/fonttools/fontbakery/issues/3486





* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#stylisticset-description">stylisticset_description</a></summary>
    <div>


> 
> Stylistic sets should provide description text. Programs such as InDesign,
> TextEdit and Inkscape use that info to display to the users so that they know
> what a given stylistic set offers.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3155





* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



* ⚠️ **WARN** <p>The stylistic set ss02 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- CR

- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- f.small

- f.sub

- f.superior

- g.small

- g.sub

- g.superior

- h.superior

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.superior

- nonmarkingreturn

- p.superior

- period.small

- period.sub

- period.superior

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- u.small

- u.sub

- u.superior

- uni0259.superior

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594







* ⚠️ **WARN** <p>Article page is too short!</p>
 [code: length-requirements-not-met]



* ⚠️ **WARN** <p>Article page lacks visual assets.</p>
 [code: missing-visual-asset]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> METADATA.pb: Designers are listed correctly on the Google Fonts catalog? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-designer-profiles">googlefonts/metadata/designer_profiles</a></summary>
    <div>


> 
> Google Fonts has a catalog of designers.
> 
> This check ensures that the online entries of the catalog can be found based
> on the designer names listed on the METADATA.pb file.
> 
> It also validates the URLs and file formats are all correctly set.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3083





* ⚠️ **WARN** <p>It seems that Dmitry Grenev is still not listed on the designers catalog. Please submit a photo and a link to a webpage where people can learn more about the work of this designer/typefoundry.</p>
 [code: profile-not-found]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, coptic, malayalam, duployan, canadian-aboriginal, todhri, math, tifinagh, syriac, hebrew, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, greek, math</li>
<li>U+1EA0 LATIN CAPITAL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EA1 LATIN SMALL LETTER A WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB8 LATIN CAPITAL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EB9 LATIN SMALL LETTER E WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EBC LATIN CAPITAL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1EBD LATIN SMALL LETTER E WITH TILDE: try adding vietnamese</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECC LATIN CAPITAL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECD LATIN SMALL LETTER O WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE4 LATIN CAPITAL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+1EE5 LATIN SMALL LETTER U WITH DOT BELOW: try adding vietnamese</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2010 HYPHEN: try adding one of: armenian, kaithi, coptic, syloti-nagri, sora-sompeng, lisu, yi, arabic, kayah-li, sundanese, cham, hebrew, kharoshthi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, syloti-nagri, arabic</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2023 TRIANGULAR BULLET: not included in any glyphset definition</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2027 HYPHENATION POINT: not included in any glyphset definition</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+203D INTERROBANG: not included in any glyphset definition</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
<li>U+2060 WORD JOINER: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2090 LATIN SUBSCRIPT SMALL LETTER A: try adding math</li>
<li>U+2091 LATIN SUBSCRIPT SMALL LETTER E: try adding math</li>
<li>U+2092 LATIN SUBSCRIPT SMALL LETTER O: try adding math</li>
<li>U+2093 LATIN SUBSCRIPT SMALL LETTER X: try adding math</li>
<li>U+2094 LATIN SUBSCRIPT SMALL LETTER SCHWA: try adding math</li>
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: devanagari, grantha</li>
<li>U+2100 ACCOUNT OF: try adding math</li>
<li>U+2101 ADDRESSED TO THE SUBJECT: try adding math</li>
<li>U+2105 CARE OF: try adding math</li>
<li>U+2106 CADA UNA: try adding math</li>
<li>U+2117 SOUND RECORDING COPYRIGHT: try adding math</li>
<li>U+2120 SERVICE MARK: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+212E ESTIMATED SYMBOL: try adding math</li>
<li>U+2150 VULGAR FRACTION ONE SEVENTH: try adding symbols</li>
<li>U+2151 VULGAR FRACTION ONE NINTH: try adding symbols</li>
<li>U+2152 VULGAR FRACTION ONE TENTH: try adding symbols</li>
<li>U+2153 VULGAR FRACTION ONE THIRD: try adding symbols</li>
<li>U+2154 VULGAR FRACTION TWO THIRDS: try adding symbols</li>
<li>U+2155 VULGAR FRACTION ONE FIFTH: try adding symbols</li>
<li>U+2156 VULGAR FRACTION TWO FIFTHS: try adding symbols</li>
<li>U+2157 VULGAR FRACTION THREE FIFTHS: try adding symbols</li>
<li>U+2158 VULGAR FRACTION FOUR FIFTHS: try adding symbols</li>
<li>U+2159 VULGAR FRACTION ONE SIXTH: try adding symbols</li>
<li>U+215A VULGAR FRACTION FIVE SIXTHS: try adding symbols</li>
<li>U+215B VULGAR FRACTION ONE EIGHTH: try adding symbols</li>
<li>U+215C VULGAR FRACTION THREE EIGHTHS: try adding symbols</li>
<li>U+215D VULGAR FRACTION FIVE EIGHTHS: try adding symbols</li>
<li>U+215E VULGAR FRACTION SEVEN EIGHTHS: try adding symbols</li>
<li>U+215F FRACTION NUMERATOR ONE: try adding symbols</li>
<li>U+2189 VULGAR FRACTION ZERO THIRDS: try adding symbols</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: math, symbols</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: math, symbols</li>
<li>U+2195 UP DOWN ARROW: try adding one of: math, symbols</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: math, symbols</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: math, symbols</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, symbols, tai-tham</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+223C TILDE OPERATOR: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+228D MULTISET MULTIPLICATION: try adding math</li>
<li>U+228E MULTISET UNION: try adding math</li>
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: math, symbols</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, mongolian, symbols</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, mongolian, symbols</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, mongolian, symbols</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, mongolian, symbols</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, mongolian, symbols</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, mongolian, symbols</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, mongolian, symbols</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, mongolian, symbols</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, mongolian, symbols</li>
<li>U+24EA CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+24FF NEGATIVE CIRCLED DIGIT ZERO: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25AA BLACK SMALL SQUARE: try adding symbols</li>
<li>U+25AB WHITE SMALL SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BA BLACK RIGHT-POINTING POINTER: try adding symbols</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C4 BLACK LEFT-POINTING POINTER: try adding symbols</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: ahom, psalter-pahlavi, tibetan, pahawh-hmong, tagalog, tagbanwa, hebrew, caucasian-albanian, bassa-vah, nko, armenian, siddham, tifinagh, yi, kayah-li, javanese, mahajani, new-tai-lue, syloti-nagri, lepcha, chakma, buginese, marchen, tirhuta, gurmukhi, takri, myanmar, sinhala, rejang, elbasan, tai-tham, mende-kikakui, tamil, dogra, malayalam, manichaean, warang-citi, thaana, cham, newa, mandaic, thai, math, grantha, khmer, symbols, osage, telugu, lao, meetei-mayek, khudawadi, buhid, sogdian, canadian-aboriginal, bhaiksuki, devanagari, adlam, tai-le, kharoshthi, limbu, miao, gunjala-gondi, modi, sharada, masaram-gondi, phags-pa, saurashtra, batak, kaithi, duployan, khojki, tai-viet, mongolian, wancho, balinese, oriya, old-permic, coptic, bengali, kannada, syriac, hanifi-rohingya, music, gujarati, brahmi, hanunoo, sundanese, soyombo, zanabazar-square</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2630 TRIGRAM FOR HEAVEN: try adding symbols</li>
<li>U+2713 CHECK MARK: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2729 STRESS OUTLINED WHITE STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2776 DINGBAT NEGATIVE CIRCLED DIGIT ONE: try adding symbols</li>
<li>U+2777 DINGBAT NEGATIVE CIRCLED DIGIT TWO: try adding symbols</li>
<li>U+2778 DINGBAT NEGATIVE CIRCLED DIGIT THREE: try adding symbols</li>
<li>U+2779 DINGBAT NEGATIVE CIRCLED DIGIT FOUR: try adding symbols</li>
<li>U+277A DINGBAT NEGATIVE CIRCLED DIGIT FIVE: try adding symbols</li>
<li>U+277B DINGBAT NEGATIVE CIRCLED DIGIT SIX: try adding symbols</li>
<li>U+277C DINGBAT NEGATIVE CIRCLED DIGIT SEVEN: try adding symbols</li>
<li>U+277D DINGBAT NEGATIVE CIRCLED DIGIT EIGHT: try adding symbols</li>
<li>U+277E DINGBAT NEGATIVE CIRCLED DIGIT NINE: try adding symbols</li>
<li>U+27D0 WHITE DIAMOND WITH CENTRED DOT: try adding math</li>
<li>U+2ABD SUBSET WITH DOT: try adding math</li>
<li>U+2ABE SUPERSET WITH DOT: try adding math</li>
<li>U+2AF6 TRIPLE COLON OPERATOR: try adding math</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code>, <code>menu</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>


> 
> This check uses a heuristic to determine which GF glyphsets a font supports.
> Then it checks the font for correct shaping behaviour for all languages in
> those glyphsets.
> 




> Original proposal: https://github.com/googlefonts/fontbakery/issues/4147





* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian) and mn_Cyrl (Mongolian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>


> 
> A known licensing description must be provided in the NameID 14
> (LICENSE DESCRIPTION) entries of the name table.
> 
> The source of truth for this check (to determine which license is in use) is
> a file placed side-by-side to your font project including the licensing terms.
> 
> Depending on the chosen license, one of the following string snippets is
> expected to be found on the NameID 13 (LICENSE DESCRIPTION) entries of the
> name table:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set
> of legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>


> 
> A known license URL must be provided in the NameID 14 (LICENSE INFO URL)
> entry of the name table.
> 
> The source of truth for this check is the licensing text found on the NameID 13
> entry (LICENSE DESCRIPTION).
> 
> The string snippets used for detecting licensing terms are:
> 
> - "This Font Software is licensed under the SIL Open Font License, Version 1.1.
> This license is available with a FAQ at: openfontlicense.org"
> 
> - "Licensed under the Apache License, Version 2.0"
> 
> - "Licensed under the Ubuntu Font Licence 1.0."
> 
> 
> Currently accepted licenses are Apache or Open Font License. For a small set of
> legacy families the Ubuntu Font License may be acceptable as well.
> 
> When in doubt, please choose OFL for new font projects.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4358
> See also: https://github.com/fonttools/fontbakery/issues/4829







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=1, enc=0, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>


> 
> An accent placed on characters with a "soft dot", like i or j, causes
> the dot to disappear.
> An explicit dot above can be added where required.
> See "Diacritics on i and j" in Section 7.1, "Latin" in The Unicode Standard.
> 
> Characters with the Soft_Dotted property are listed in
> https://www.unicode.org/Public/UCD/latest/ucd/PropList.txt
> 
> See also:
> https://googlefonts.github.io/gf-guide/diacritics.html#soft-dotted-glyphs
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4059





* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: į̀ į́ į̂ į̃ į̄ į̌ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i⃰ i̦⃰ i̧⃰ i̵⃰ j⃰ j̣⃰ j̦⃰ j̧⃰ j̨⃰ j̵⃰ į̆ į̇ į̈ į̊ į̋ į̒ į⃰ į̣̀ į̣́ į̣̂</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>


> 
> This check looks for consecutive line segments which have the same angle. This
> normally happens if an outline point has been added by accident.
> 
> This check is not run for variable fonts, as they may legitimately have
> colinear vectors.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* A (U+0041): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Aacute (U+00C1): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Abreve (U+0102): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Acircumflex (U+00C2): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Adieresis (U+00C4): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Agrave (U+00C0): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Amacron (U+0100): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Aogonek (U+0104): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Aring (U+00C5): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Aringacute (U+01FA): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* Atilde (U+00C3): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;144.0,171.0&gt;--&lt;141.0,275.0&gt;&gt; -&gt; L&lt;&lt;141.0,275.0&gt;--&lt;141.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;179.0,720.0&gt;--&lt;179.0,275.0&gt;&gt; -&gt; L&lt;&lt;179.0,275.0&gt;--&lt;176.0,171.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;144.0,171.0&gt;--&lt;141.0,275.0&gt;&gt; -&gt; L&lt;&lt;141.0,275.0&gt;--&lt;141.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;179.0,720.0&gt;--&lt;179.0,275.0&gt;&gt; -&gt; L&lt;&lt;179.0,275.0&gt;--&lt;176.0,171.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;464.0,171.0&gt;--&lt;461.0,275.0&gt;&gt; -&gt; L&lt;&lt;461.0,275.0&gt;--&lt;461.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;499.0,720.0&gt;--&lt;499.0,275.0&gt;&gt; -&gt; L&lt;&lt;499.0,275.0&gt;--&lt;496.0,171.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;144.0,329.0&gt;--&lt;141.0,225.0&gt;&gt; -&gt; L&lt;&lt;141.0,225.0&gt;--&lt;141.0,-220.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;179.0,-220.0&gt;--&lt;179.0,225.0&gt;&gt; -&gt; L&lt;&lt;179.0,225.0&gt;--&lt;176.0,329.0&gt;&gt;

* uni01CD (U+01CD): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* uni0226 (U+0226): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* uni0410 (U+0410): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* uni0446.loclBGR: L&lt;&lt;435.0,96.0&gt;--&lt;429.0,200.0&gt;&gt; -&gt; L&lt;&lt;429.0,200.0&gt;--&lt;429.0,500.0&gt;&gt;

* uni0449.loclBGR: L&lt;&lt;711.0,79.0&gt;--&lt;709.0,200.0&gt;&gt; -&gt; L&lt;&lt;709.0,200.0&gt;--&lt;709.0,500.0&gt;&gt;

* uni04D0 (U+04D0): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* uni04D2 (U+04D2): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* uni1EA0 (U+1EA0): L&lt;&lt;156.0,246.0&gt;--&lt;156.0,246.0&gt;&gt; -&gt; L&lt;&lt;156.0,246.0&gt;--&lt;501.0,246.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;664.0,171.0&gt;--&lt;661.0,275.0&gt;&gt; -&gt; L&lt;&lt;661.0,275.0&gt;--&lt;661.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;699.0,720.0&gt;--&lt;699.0,275.0&gt;&gt; -&gt; L&lt;&lt;699.0,275.0&gt;--&lt;696.0,171.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;144.0,171.0&gt;--&lt;141.0,275.0&gt;&gt; -&gt; L&lt;&lt;141.0,275.0&gt;--&lt;141.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;179.0,720.0&gt;--&lt;179.0,275.0&gt;&gt; -&gt; L&lt;&lt;179.0,275.0&gt;--&lt;176.0,171.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;113.0,240.0&gt;--&lt;111.0,580.0&gt;&gt; -&gt; L&lt;&lt;111.0,580.0&gt;--&lt;111.0,720.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;149.0,720.0&gt;--&lt;149.0,580.0&gt;&gt; -&gt; L&lt;&lt;149.0,580.0&gt;--&lt;147.0,240.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;126.0,720.0&gt;--&lt;126.0,620.0&gt;&gt; -&gt; L&lt;&lt;126.0,620.0&gt;--&lt;124.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;90.0,380.0&gt;--&lt;88.0,620.0&gt;&gt; -&gt; L&lt;&lt;88.0,620.0&gt;--&lt;88.0,720.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>


> 
> In TrueType fonts, the outermost contour of a glyph should be oriented
> clockwise, while the inner contours should be oriented counter-clockwise.
> Getting the path direction wrong can lead to rendering issues in some
> software.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2056





* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* Agrave (U+00C0) has a counter-clockwise outer contour

* Ccaron (U+010C) has a counter-clockwise outer contour

* Dcaron (U+010E) has a counter-clockwise outer contour

* Ecaron (U+011A) has a counter-clockwise outer contour

* Egrave (U+00C8) has a counter-clockwise outer contour

* Gcaron (U+01E6) has a counter-clockwise outer contour

* Igrave (U+00CC) has a counter-clockwise outer contour

* Ncaron (U+0147) has a counter-clockwise outer contour

* Ograve (U+00D2) has a counter-clockwise outer contour

* Rcaron (U+0158) has a counter-clockwise outer contour

* Scaron (U+0160) has a counter-clockwise outer contour

* Tcaron (U+0164) has a counter-clockwise outer contour

* Ugrave (U+00D9) has a counter-clockwise outer contour

* Wgrave (U+1E80) has a counter-clockwise outer contour

* Ygrave (U+1EF2) has a counter-clockwise outer contour

* Zcaron (U+017D) has a counter-clockwise outer contour

* agrave (U+00E0) has a counter-clockwise outer contour

* agrave.cv01 has a counter-clockwise outer contour

* agrave.ss01 has a counter-clockwise outer contour

* agrave.ss01.cv01 has a counter-clockwise outer contour

* agrave.ss02 has a counter-clockwise outer contour

* agrave.ss02.cv01 has a counter-clockwise outer contour

* angleright (U+232A) has a counter-clockwise outer contour

* angleright.case has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowboth (U+2194) has a counter-clockwise outer contour

* arrowdown (U+2193) has a counter-clockwise outer contour

* arrowleft (U+2190) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* arrowupdn (U+2195) has a counter-clockwise outer contour

* backslash (U+005C) has a counter-clockwise outer contour

* backslash.case has a counter-clockwise outer contour

* braceright (U+007D) has a counter-clockwise outer contour

* braceright.case has a counter-clockwise outer contour

* bracketright (U+005D) has a counter-clockwise outer contour

* bracketright.case has a counter-clockwise outer contour

* caron (U+02C7) has a counter-clockwise outer contour

* ccaron (U+010D) has a counter-clockwise outer contour

* d (U+0064) has a counter-clockwise outer contour

* d.small has a counter-clockwise outer contour

* d.sub has a counter-clockwise outer contour

* dcaron (U+010F) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* dcroat (U+0111) has a counter-clockwise outer contour

* ecaron (U+011B) has a counter-clockwise outer contour

* egrave (U+00E8) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* exclamdown (U+00A1) has a counter-clockwise outer contour

* gcaron (U+01E7) has a counter-clockwise outer contour

* gcaron.ss01 has a counter-clockwise outer contour

* gcaron.ss02 has a counter-clockwise outer contour

* grave (U+0060) has a counter-clockwise outer contour

* gravecomb (U+0300) has a counter-clockwise outer contour

* greater (U+003E) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* greaterequal (U+2265) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright (U+00BB) has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guillemotright.case has a counter-clockwise outer contour

* guilsinglright (U+203A) has a counter-clockwise outer contour

* guilsinglright.case has a counter-clockwise outer contour

* igrave (U+00EC) has a counter-clockwise outer contour

* intersection (U+2229) has a counter-clockwise outer contour

* ncaron (U+0148) has a counter-clockwise outer contour

* ogonekmirrored has a counter-clockwise outer contour

* ograve (U+00F2) has a counter-clockwise outer contour

* p (U+0070) has a counter-clockwise outer contour

* p.small has a counter-clockwise outer contour

* p.superior has a counter-clockwise outer contour

* parenright (U+0029) has a counter-clockwise outer contour

* parenright.case has a counter-clockwise outer contour

* parenright.small has a counter-clockwise outer contour

* propersubset (U+2282) has a counter-clockwise outer contour

* rcaron (U+0159) has a counter-clockwise outer contour

* rcaron.ss02 has a counter-clockwise outer contour

* scaron (U+0161) has a counter-clockwise outer contour

* triagdn (U+25BC) has a counter-clockwise outer contour

* triagrt (U+25BA) has a counter-clockwise outer contour

* ugrave (U+00F9) has a counter-clockwise outer contour

* uni018E (U+018E) has a counter-clockwise outer contour

* uni01CD (U+01CD) has a counter-clockwise outer contour

* uni01CE (U+01CE) has a counter-clockwise outer contour

* uni01CE.cv01 has a counter-clockwise outer contour

* uni01CE.ss01 has a counter-clockwise outer contour

* uni01CE.ss01.cv01 has a counter-clockwise outer contour

* uni01CE.ss02 has a counter-clockwise outer contour

* uni01CE.ss02.cv01 has a counter-clockwise outer contour

* uni01CF (U+01CF) has a counter-clockwise outer contour

* uni01D0 (U+01D0) has a counter-clockwise outer contour

* uni01DD (U+01DD) has a counter-clockwise outer contour

* uni01E8 (U+01E8) has a counter-clockwise outer contour

* uni01E8.ss02 has a counter-clockwise outer contour

* uni01E9 (U+01E9) has a counter-clockwise outer contour

* uni01E9.ss02 has a counter-clockwise outer contour

* uni01EE (U+01EE) has a counter-clockwise outer contour

* uni01EF (U+01EF) has a counter-clockwise outer contour

* uni0281 (U+0281) has a counter-clockwise outer contour

* uni030C (U+030C) has a counter-clockwise outer contour

* uni030C.narrow has a counter-clockwise outer contour

* uni0400 (U+0400) has a counter-clockwise outer contour

* uni0403 (U+0403) has a counter-clockwise outer contour

* uni0403.ss02 has a counter-clockwise outer contour

* uni0404 (U+0404) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni040D (U+040D) has a counter-clockwise outer contour

* uni0413 (U+0413) has a counter-clockwise outer contour

* uni0413.ss02 has a counter-clockwise outer contour

* uni0418 (U+0418) has a counter-clockwise outer contour

* uni0419 (U+0419) has a counter-clockwise outer contour

* uni042C (U+042C) has a counter-clockwise outer contour

* uni042F (U+042F) has a counter-clockwise outer contour

* uni0440 (U+0440) has a counter-clockwise outer contour

* uni044D (U+044D) has a counter-clockwise outer contour

* uni0450 (U+0450) has a counter-clockwise outer contour

* uni045D (U+045D) has a counter-clockwise outer contour

* uni0492 (U+0492) has a counter-clockwise outer contour

* uni0492.ss02 has a counter-clockwise outer contour

* uni0494 (U+0494) has a counter-clockwise outer contour

* uni0494.ss02 has a counter-clockwise outer contour

* uni0498 (U+0498) has a counter-clockwise outer contour

* uni0499 (U+0499) has a counter-clockwise outer contour

* uni04AA (U+04AA) has a counter-clockwise outer contour

* uni04AB (U+04AB) has a counter-clockwise outer contour

* uni04E2 (U+04E2) has a counter-clockwise outer contour

* uni04E4 (U+04E4) has a counter-clockwise outer contour

* uni04ED (U+04ED) has a counter-clockwise outer contour

* uni0510 (U+0510) has a counter-clockwise outer contour

* uni0511 (U+0511) has a counter-clockwise outer contour

* uni207E (U+207E) has a counter-clockwise outer contour

* uni208E (U+208E) has a counter-clockwise outer contour

* uni209A (U+209A) has a counter-clockwise outer contour

* uni2196 (U+2196) has a counter-clockwise outer contour

* uni2198 (U+2198) has a counter-clockwise outer contour

* uni228E (U+228E) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni22F0 (U+22F0) has a counter-clockwise outer contour

* uni25D1 (U+25D1) has a counter-clockwise outer contour

* uni25D2 (U+25D2) has a counter-clockwise outer contour

* uni2ABE (U+2ABE) has a counter-clockwise outer contour

* wgrave (U+1E81) has a counter-clockwise outer contour

* ygrave (U+1EF3) has a counter-clockwise outer contour

* ygrave.ss02 has a counter-clockwise outer contour

* zcaron (U+017E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>


> 
> This check heuristically detects outline segments which form a particularly
> small angle, indicative of an outline error. This may cause false positives
> in cases such as extreme ink traps, so should be regarded as advisory and
> backed up by manual inspection.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3064





* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* eth (U+00F0): B&lt;&lt;433.5,422.0&gt;-&lt;454.0,395.0&gt;-&lt;459.0,376.0&gt;&gt;/B&lt;&lt;459.0,376.0&gt;-&lt;447.0,509.0&gt;-&lt;417.5,569.0&gt;&gt; = 9.587978519064421

* g (U+0067): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* g (U+0067): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* g.small: B&lt;&lt;251.22579956054688,273.8697814941406&gt;-&lt;266.831787109375,255.8157958984375&gt;-&lt;271.11578369140625,238.6798095703125&gt;&gt;/L&lt;&lt;271.11578369140625,238.6798095703125&gt;--&lt;271.11578369140625,305.999755859375&gt;&gt; = 14.036243467926484

* g.small: L&lt;&lt;271.11578369140625,1.83599853515625&gt;--&lt;271.11578369140625,83.84393310546875&gt;&gt;/B&lt;&lt;271.11578369140625,83.84393310546875&gt;-&lt;266.831787109375,66.095947265625&gt;-&lt;251.22579956054688,48.041961669921875&gt;&gt; = 13.570434385161475

* g.sub: B&lt;&lt;251.22579956054688,193.86978149414062&gt;-&lt;266.831787109375,175.8157958984375&gt;-&lt;271.11578369140625,158.6798095703125&gt;&gt;/L&lt;&lt;271.11578369140625,158.6798095703125&gt;--&lt;271.11578369140625,225.999755859375&gt;&gt; = 14.036243467926484

* g.sub: L&lt;&lt;271.11578369140625,-78.16400146484375&gt;--&lt;271.11578369140625,3.84393310546875&gt;&gt;/B&lt;&lt;271.11578369140625,3.84393310546875&gt;-&lt;266.831787109375,-13.904052734375&gt;-&lt;251.22579956054688,-31.958038330078125&gt;&gt; = 13.570434385161475

* g.superior: B&lt;&lt;251.22579956054688,687.8697814941406&gt;-&lt;266.831787109375,669.8157958984375&gt;-&lt;271.11578369140625,652.6798095703125&gt;&gt;/L&lt;&lt;271.11578369140625,652.6798095703125&gt;--&lt;271.11578369140625,719.999755859375&gt;&gt; = 14.036243467926484

* g.superior: L&lt;&lt;271.11578369140625,415.83599853515625&gt;--&lt;271.11578369140625,497.84393310546875&gt;&gt;/B&lt;&lt;271.11578369140625,497.84393310546875&gt;-&lt;266.831787109375,480.095947265625&gt;-&lt;251.22579956054688,462.0419616699219&gt;&gt; = 13.570434385161475

* gbreve (U+011F): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* gbreve (U+011F): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* gcaron (U+01E7): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* gcaron (U+01E7): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* gcircumflex (U+011D): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* gcircumflex (U+011D): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* gdotaccent (U+0121): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* gdotaccent (U+0121): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* partialdiff (U+2202): B&lt;&lt;433.5,422.0&gt;-&lt;454.0,395.0&gt;-&lt;459.0,376.0&gt;&gt;/B&lt;&lt;459.0,376.0&gt;-&lt;447.0,509.0&gt;-&lt;417.5,569.0&gt;&gt; = 9.587978519064421

* uni0123 (U+0123): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* uni0123 (U+0123): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* uni01E5 (U+01E5): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* uni01E5 (U+01E5): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* uni0431 (U+0431): B&lt;&lt;122.5,548.5&gt;-&lt;104.0,492.0&gt;-&lt;99.0,371.0&gt;&gt;/B&lt;&lt;99.0,371.0&gt;-&lt;105.0,401.0&gt;-&lt;131.0,433.0&gt;&gt; = 8.943684482564363

* uni0431.ss01: B&lt;&lt;120.5,540.0&gt;-&lt;104.0,481.0&gt;-&lt;99.0,371.0&gt;&gt;/B&lt;&lt;99.0,371.0&gt;-&lt;105.0,401.0&gt;-&lt;131.0,433.0&gt;&gt; = 8.707370271520347

* uni0434.loclBGR: L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* uni1E21 (U+1E21): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* uni1E21 (U+1E21): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* uni25CC (U+25CC): B&lt;&lt;114.34539794921875,342.59197998046875&gt;-&lt;107.46044921875,335.976806640625&gt;-&lt;97.2608642578125,335.9539794921875&gt;&gt;/L&lt;&lt;97.2608642578125,335.9539794921875&gt;--&lt;97.2608642578125,335.9539794921875&gt;&gt; = 0.1282304216411991

* uni25CC (U+25CC): B&lt;&lt;740.3453979492188,341.59197998046875&gt;-&lt;733.46044921875,334.976806640625&gt;-&lt;723.2608642578125,334.9539794921875&gt;&gt;/L&lt;&lt;723.2608642578125,334.9539794921875&gt;--&lt;723.2608642578125,334.9539794921875&gt;&gt; = 0.1282304216411991

* uni25CC (U+25CC): L&lt;&lt;723.2608642578125,334.9539794921875&gt;--&lt;723.2608642578125,334.9539794921875&gt;&gt;/B&lt;&lt;723.2608642578125,334.9539794921875&gt;-&lt;713.061279296875,334.93115234375&gt;-&lt;706.44677734375,341.51611328125&gt;&gt; = 0.1282304216411991

* uni25CC (U+25CC): L&lt;&lt;97.2608642578125,335.9539794921875&gt;--&lt;97.2608642578125,335.9539794921875&gt;&gt;/B&lt;&lt;97.2608642578125,335.9539794921875&gt;-&lt;87.061279296875,335.93115234375&gt;-&lt;80.44677734375,342.51611328125&gt;&gt; = 0.1282304216411991
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>


> 
> This check detects line segments which are nearly, but not quite, exactly
> horizontal or vertical. Sometimes such lines are created by design, but often
> they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright
> lines.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* ldot (U+0140): L&lt;&lt;205.13775634765625,399.4227294921875&gt;--&lt;209.13775634765625,399.4317626953125&gt;&gt;

* ldot (U+0140): L&lt;&lt;209.31390380859375,321.4317626953125&gt;--&lt;205.31390380859375,321.4227294921875&gt;&gt;

* ldot.ss01: L&lt;&lt;214.13775634765625,399.4227294921875&gt;--&lt;218.13775634765625,399.4317626953125&gt;&gt;

* ldot.ss01: L&lt;&lt;218.31390380859375,321.4317626953125&gt;--&lt;214.31390380859375,321.4227294921875&gt;&gt;

* pi (U+03C0): L&lt;&lt;187.0,466.0&gt;--&lt;188.0,0.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;114.0,400.0&gt;--&lt;113.0,720.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;149.0,720.0&gt;--&lt;148.0,400.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;312.0,400.0&gt;--&lt;311.0,720.0&gt;&gt;

* quotedbl (U+0022): L&lt;&lt;347.0,720.0&gt;--&lt;346.0,400.0&gt;&gt;

* quotesingle (U+0027): L&lt;&lt;128.0,400.0&gt;--&lt;127.0,720.0&gt;&gt;

* quotesingle (U+0027): L&lt;&lt;163.0,720.0&gt;--&lt;162.0,400.0&gt;&gt;

* uni02B9 (U+02B9): L&lt;&lt;133.0,720.0&gt;--&lt;132.0,400.0&gt;&gt;

* uni02B9 (U+02B9): L&lt;&lt;98.0,400.0&gt;--&lt;97.0,720.0&gt;&gt;

* uni0414.loclBGR: L&lt;&lt;81.0,0.0&gt;--&lt;80.0,-160.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;113.0,240.0&gt;--&lt;111.0,580.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;149.0,580.0&gt;--&lt;147.0,240.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;126.0,620.0&gt;--&lt;124.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;90.0,380.0&gt;--&lt;88.0,620.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGN' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 64 | 154 | 483 | 57 | 1011 | 0 | 
| 0% | 0% | 4% | 9% | 27% | 3% | 57% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
