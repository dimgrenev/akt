## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[19] Akt[wght].ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking font version fields (head and name table). <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-font-version">opentype/font_version</a></summary>
    <div>







* 🔥 **FAIL** <p>head version is &quot;0.30000&quot; while name version string (for platform 3, encoding 1) is &quot;Version 1.000&quot;.</p>
 [code: mismatch]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsSelection value. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-fsselection">opentype/fsselection</a></summary>
    <div>







* 🔥 **FAIL** <p>fsSelection Regular flag False does not match font style Regular</p>
 [code: bad-REGULAR]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Validates subfamilyNameID and postScriptNameID for the default instance record <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-varfont-valid-default-instance-nameids">opentype/varfont/valid_default_instance_nameids</a></summary>
    <div>







* 🔥 **FAIL** <p>'Thin' instance has the same coordinates as the default instance; its subfamily name should be '0'.</p>
<p>Note: It is alternatively possible that Name ID 17 is incorrect, and should be set to the default instance subfamily name, 'Thin', rather than ''0''. If the default instance is 'Thin', NameID 17 is probably the problem.</p>
 [code: invalid-default-instance-subfamily-name]



* 🔥 **FAIL** <p>'Thin' instance has the same coordinates as the default instance; its postscript name should be 'Akt', instead of 'Akt-Thin'.</p>
 [code: invalid-default-instance-postscript-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#dotted-circle">dotted_circle</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs could not be attached to the dotted circle glyph:</p>
<pre><code>- uni0328
</code></pre>
 [code: unattached-dotted-circle-marks]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font names are correct <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-font-names">googlefonts/font_names</a></summary>
    <div>







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
<td align="left"><strong>Akt</strong></td>
<td align="left"><strong>Akt Thin</strong></td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left">Regular</td>
<td align="left">Regular</td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left"><strong>Akt 0</strong></td>
<td align="left"><strong>Akt Thin</strong></td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left"><strong>Akt</strong></td>
<td align="left"><strong>Akt-Thin</strong></td>
</tr>
<tr>
<td align="left">Typographic Family Name</td>
<td align="left">Akt</td>
<td align="left">Akt</td>
</tr>
<tr>
<td align="left">Typographic Subfamily Name</td>
<td align="left"><strong>0</strong></td>
<td align="left"><strong>Thin</strong></td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>







* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 1 start point differs in glyph 'cent' between location wght=100 and location wght=400

- Contour 1 in glyph 'cent': becomes underweight between wght=100 and wght=400.
</code></pre>
 [code: interpolation-issues]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#mandatory-avar-table">mandatory_avar_table</a></summary>
    <div>







* ⚠️ **WARN** <p>This variable font does not have an avar table. Most variable fonts should include an avar table to correctly define axes progression rates.</p>
 [code: missing-avar]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
uni2ABD, propersuperset, uni2ABE, propersubset</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* g.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* gbreve.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* gcaron.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* gcircumflex.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* uni0123.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* gdotaccent.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* uni1E21.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E5.ss02: L&lt;&lt;274.0,58.0&gt;--&lt;274.0,78.0&gt;&gt; has the same coordinates as a previous segment.

* k.ss02: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.ss02: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.ss02: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C.ss02: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0416 (U+0416): L&lt;&lt;335.0,370.0&gt;--&lt;308.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni0416 (U+0416): L&lt;&lt;692.0,370.0&gt;--&lt;665.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni040A (U+040A): L&lt;&lt;556.0,720.0&gt;--&lt;576.0,720.0&gt;&gt; has the same coordinates as a previous segment.

* uni040B (U+040B): L&lt;&lt;260.0,0.0&gt;--&lt;240.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0496 (U+0496): L&lt;&lt;335.0,370.0&gt;--&lt;308.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni0496 (U+0496): L&lt;&lt;692.0,370.0&gt;--&lt;665.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;544.0,0.0&gt;--&lt;524.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04BC (U+04BC): L&lt;&lt;818.0,378.0&gt;--&lt;818.0,358.0&gt;&gt; has the same coordinates as a previous segment.

* uni04BE (U+04BE): L&lt;&lt;818.0,378.0&gt;--&lt;818.0,358.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C1 (U+04C1): L&lt;&lt;335.0,370.0&gt;--&lt;308.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C1 (U+04C1): L&lt;&lt;692.0,370.0&gt;--&lt;665.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni04DC (U+04DC): L&lt;&lt;335.0,370.0&gt;--&lt;308.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni04DC (U+04DC): L&lt;&lt;692.0,370.0&gt;--&lt;665.0,370.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;406.0,0.0&gt;--&lt;386.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;440.0,0.0&gt;--&lt;420.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;120.0,0.0&gt;--&lt;100.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F (U+049F): L&lt;&lt;172.0,0.0&gt;--&lt;152.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;172.0,0.0&gt;--&lt;152.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;420.0,0.0&gt;--&lt;400.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-hyphen">soft_hyphen</a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- IJacute

- NULL

- b.small

- b.sub

- c.sub

- c.superior

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

- uni0306.cy

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







* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, old-permic, coptic, todhri, malayalam, duployan, tifinagh, syriac, hebrew, math, tai-le</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0391 GREEK CAPITAL LETTER ALPHA: try adding one of: math, elbasan, greek</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: math, elbasan, greek</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: math, elbasan, greek</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: math, elbasan, greek</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: math, greek</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: math, greek</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: math, greek</li>
<li>U+03BE GREEK SMALL LETTER XI: try adding one of: math, greek</li>
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: yi, math, greek</li>
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
<li>U+2010 HYPHEN: try adding one of: arabic, cham, coptic, lisu, kaithi, kharoshthi, armenian, yi, kayah-li, hebrew, syloti-nagri, sora-sompeng, sundanese</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: yi, arabic, syloti-nagri</li>
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
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: yi, symbols, tai-tham, math</li>
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
<li>U+22C5 DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2329 LEFT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+232A RIGHT-POINTING ANGLE BRACKET: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: yi, symbols, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: yi, symbols, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: yi, symbols, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: yi, symbols, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: yi, symbols, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: yi, symbols, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: yi, symbols, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: yi, symbols, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: yi, symbols, mongolian</li>
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
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: saurashtra, malayalam, miao, masaram-gondi, thai, syriac, elbasan, kaithi, tagalog, batak, warang-citi, ahom, dogra, tai-viet, gunjala-gondi, math, canadian-aboriginal, manichaean, chakma, osage, new-tai-lue, rejang, sogdian, takri, kannada, kharoshthi, newa, marchen, siddham, bassa-vah, lepcha, mongolian, music, gujarati, symbols, tai-le, armenian, psalter-pahlavi, bengali, balinese, tagbanwa, telugu, yi, bhaiksuki, hanifi-rohingya, javanese, coptic, adlam, tamil, sinhala, zanabazar-square, meetei-mayek, hanunoo, old-permic, buhid, pahawh-hmong, khmer, brahmi, syloti-nagri, myanmar, oriya, cham, hebrew, devanagari, mandaic, soyombo, sharada, tirhuta, caucasian-albanian, mende-kikakui, nko, gurmukhi, lao, tibetan, limbu, thaana, buginese, wancho, grantha, khudawadi, tai-tham, tifinagh, phags-pa, sundanese, mahajani, modi, khojki, kayah-li, duployan</li>
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
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







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
    <summary>⚠️ <b>WARN</b> Check OFL body text is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-body-text">googlefonts/license/OFL_body_text</a></summary>
    <div>







* ⚠️ **WARN** <p>The OFL.txt body text is incorrect. Please use <a href="https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt">https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt</a> as a template. You should only modify the first line.</p>
<p>Lines changed:</p>
<p>+ This license is available with a FAQ at: <a href="https://openfontlicense.org%5Cn">https://openfontlicense.org\n</a></p>
<p>- This license is copied below, and is also available with a FAQ at:\n</p>
<p>- <a href="https://openfontlicense.org%5Cn">https://openfontlicense.org\n</a></p>
<p>- \n</p>
<p>- \n</p>
<p>- PERMISSION &amp; CONDITIONS\n</p>
<p>+ PERMISSION AND CONDITIONS\n</p>
<p>- Copyright Holder. This restriction only applies to the primary font name as\n</p>
<p>+ Copyright Holder. This restriction only applies to the primary font name\n</p>
<p>- presented to the users.\n</p>
<p>+ as presented to the users.\n</p>
<p>- OTHER DEALINGS IN THE FONT SOFTWARE.</p>
<p>+ OTHER DEALINGS IN THE FONT SOFTWARE.\n</p>
 [code: incorrect-ofl-body-text]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̒ i⃰ i̦̒ i̦⃰ i̧̒ i̧⃰ j̒ j⃰ j̦̒ j̦⃰ j̧̒ j̧⃰ і̒ і⃰ і̦̒ і̦⃰ і̧̒ і̧⃰ ј̀ ј́</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* g.sub: X=56.0,Y=1.0 (should be at baseline 0?)

* y (U+0079): X=246.0,Y=-2.0 (should be at baseline 0?)

* y.small: X=151.0,Y=-1.0 (should be at baseline 0?)

* y.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* yacute (U+00FD): X=246.0,Y=-2.0 (should be at baseline 0?)

* yacute.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* ycircumflex (U+0177): X=246.0,Y=-2.0 (should be at baseline 0?)

* ycircumflex.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* ydieresis (U+00FF): X=246.0,Y=-2.0 (should be at baseline 0?)

* ydieresis.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* ygrave (U+1EF3): X=246.0,Y=-2.0 (should be at baseline 0?)

* ygrave.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni0233 (U+0233): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni0233.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni1EF9 (U+1EF9): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni1EF9.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni0490.ss02: X=476.5,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=490.0,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=510.0,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=50.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=76.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=924.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=950.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=490.0,Y=721.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=510.0,Y=721.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=50.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=76.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=924.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=950.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=490.0,Y=721.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=510.0,Y=721.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=50.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=76.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=924.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=950.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=490.0,Y=721.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=510.0,Y=721.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=50.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=76.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=924.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=950.0,Y=719.0 (should be at cap-height 720?)

* uni0437 (U+0437): X=147.0,Y=2.0 (should be at baseline 0?)

* uni0437 (U+0437): X=332.5,Y=2.0 (should be at baseline 0?)

* uni0443 (U+0443): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni0443.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni045E (U+045E): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni045E.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni0499 (U+0499): X=147.0,Y=2.0 (should be at baseline 0?)

* uni0499 (U+0499): X=332.5,Y=2.0 (should be at baseline 0?)

* uni04DF (U+04DF): X=147.0,Y=2.0 (should be at baseline 0?)

* uni04DF (U+04DF): X=332.5,Y=2.0 (should be at baseline 0?)

* uni04EF (U+04EF): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni04EF.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni04F1 (U+04F1): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni04F1.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni04F3 (U+04F3): X=246.0,Y=-2.0 (should be at baseline 0?)

* uni04F3.ss02: X=247.0,Y=-2.0 (should be at baseline 0?)

* uni0511 (U+0511): X=157.5,Y=2.0 (should be at baseline 0?)

* uni0511 (U+0511): X=343.0,Y=2.0 (should be at baseline 0?)

* four.osf: X=410.0,Y=-2.0 (should be at baseline 0?)

* four.osf: X=48.0,Y=-2.0 (should be at baseline 0?)

* four.osf: X=594.0,Y=-2.0 (should be at baseline 0?)

* four.osf: X=430.0,Y=-2.0 (should be at baseline 0?)

* period.small: X=57.0,Y=1.5 (should be at baseline 0?)

* period.small: X=83.0,Y=1.5 (should be at baseline 0?)

* comma.small: X=57.0,Y=1.5 (should be at baseline 0?)

* comma.small: X=83.0,Y=1.5 (should be at baseline 0?)

* braceleft.case: X=243.0,Y=721.0 (should be at cap-height 720?)

* braceright.case: X=157.0,Y=721.0 (should be at cap-height 720?)

* uni208A (U+208A): X=190.0,Y=1.0 (should be at baseline 0?)

* uni208A (U+208A): X=177.0,Y=1.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGR' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 5 | 14 | 89 | 7 | 121 | 0 | 
| 0% | 0% | 2% | 6% | 38% | 3% | 51% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
