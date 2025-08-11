## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[27] AktGrotesk-ExtraLight.ttf</summary>
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
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>


> 
> Hinted fonts must have head table flag bit 3 set.
> 
> Per https://docs.microsoft.com/en-us/typography/opentype/spec/head,
> bit 3 of Head::flags decides whether PPEM should be rounded. This bit should
> always be set for hinted fonts.
> 
> Note:
> Bit 3 = Force ppem to integer values for all internal scaler math;
> May use fractional ppem sizes if this bit is clear;
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2338





* 🔥 **FAIL** <p>This is a hinted font, so it must have bit 3 set on the flags of the head table, so that PPEM values will be rounded into an integer value.</p>
<p>This can be accomplished by using the 'gftools fix-hinting' command:</p>
<pre><code># create virtualenv
python3 -m venv venv
# activate virtualenv
source venv/bin/activate
# install gftools
pip install git+https://www.github.com/googlefonts/gftools
</code></pre>
 [code: bad-flags]



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
* uni1EB8 and 430 more.</p>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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

- 7 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-names">googlefonts/font_names</a></summary>
    <div>


> 
> Google Fonts has several rules which need to be adhered to when
> setting a font's name table. Please read:
> https://googlefonts.github.io/gf-guide/statics.html#supported-styles
> https://googlefonts.github.io/gf-guide/statics.html#style-linking
> https://googlefonts.github.io/gf-guide/statics.html#unsupported-styles
> https://googlefonts.github.io/gf-guide/statics.html#single-weight-families
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3800





* 🔥 **FAIL** <p>Font names are incorrect:</p>
<table>
<thead>
<tr>
<th align="left">nameID</th>
<th align="left">current</th>
<th align="left">expected</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Family Name</td>
<td align="left">Akt Grotesk ExtraLight</td>
<td align="left">Akt Grotesk ExtraLight</td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left">Regular</td>
<td align="left">Regular</td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left">Akt Grotesk ExtraLight</td>
<td align="left">Akt Grotesk ExtraLight</td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left"><strong>Akt-ExtraLight</strong></td>
<td align="left"><strong>AktGrotesk-ExtraLight</strong></td>
</tr>
<tr>
<td align="left">Typographic Family Name</td>
<td align="left">Akt Grotesk</td>
<td align="left">Akt Grotesk</td>
</tr>
<tr>
<td align="left">Typographic Subfamily Name</td>
<td align="left">ExtraLight</td>
<td align="left">ExtraLight</td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>


> 
> For Google Fonts, the version string must be in the format "Version X.Y".
> The version number must be greater than or equal to 1.000. (Additional
> information following the numeric version number is acceptable.)
> The "Version " prefix is a recommendation given by the OpenType spec.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



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

- 270 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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
uni2ABD, propersubset, uni2ABE, propersuperset</p>
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

* 14 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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
<pre><code>- IJacute

- NULL

- b.small

- b.sub

- c.sub

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- 42 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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





* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: tifinagh, hebrew, todhri, canadian-aboriginal, old-permic, duployan, syriac, tai-le, malayalam, coptic, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math
198 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
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

* 25 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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

* 135 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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

* 7 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
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

* 56 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-short-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>


> 
> The OpenType 'meta' table originated at Apple. Microsoft added it to OT with
> just two DataMap records:
> 
> - dlng: comma-separated ScriptLangTags that indicate which scripts,
> or languages and scripts, with possible variants, the font is designed for.
> 
> - slng: comma-separated ScriptLangTags that indicate which scripts,
> or languages and scripts, with possible variants, the font supports.
> 
> 
> The slng structure is intended to describe which languages and scripts the
> font overall supports. For example, a Traditional Chinese font that also
> contains Latin characters, can indicate Hant,Latn, showing that it supports
> Hant, the Traditional Chinese variant of the Hani script, and it also
> supports the Latn script.
> 
> The dlng structure is far more interesting. A font may contain various glyphs,
> but only a particular subset of the glyphs may be truly "leading" in the design,
> while other glyphs may have been included for technical reasons. Such a
> Traditional Chinese font could only list Hant there, showing that it’s designed
> for Traditional Chinese, but the font would omit Latn, because the developers
> don’t think the font is really recommended for purely Latin-script use.
> 
> The tags used in the structures can comprise just script, or also language
> and script. For example, if a font has Bulgarian Cyrillic alternates in the
> locl feature for the cyrl BGR OT languagesystem, it could also indicate in
> dlng explicitly that it supports bul-Cyrl. (Note that the scripts and languages
> in meta use the ISO language and script codes, not the OpenType ones).
> 
> This check ensures that the font has the meta table containing the
> slng and dlng structures.
> 
> All families in the Google Fonts collection should contain the 'meta' table.
> Windows 10 already uses it when deciding on which fonts to fall back to.
> The Google Fonts API and also other environments could use the data for
> smarter filtering. Most importantly, those entries should be added
> to the Noto fonts.
> 
> In the font making process, some environments store this data in external
> files already. But the meta table provides a convenient way to store this
> inside the font file, so some tools may add the data, and unrelated tools
> may read this data. This makes the solution much more portable and universal.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3349





* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



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
| 0 | 0 | 7 | 20 | 108 | 6 | 95 | 0 | 
| 0% | 0% | 3% | 8% | 46% | 3% | 40% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
