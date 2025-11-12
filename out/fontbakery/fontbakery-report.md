## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[12] Akt[wght].ttf</summary>
<div>
<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontdata-namecheck">fontdata_namecheck</a></summary>
    <div>







* 💥 **ERROR** <p>Failed to access: <a href="https://namecheck.fontdata.com/api/?q=Akt">https://namecheck.fontdata.com/api/?q=Akt</a>.
This check relies on the external service <a href="http://namecheck.fontdata.com">http://namecheck.fontdata.com</a> via the internet. While the service cannot be reached or does not respond this check is broken.</p>
<pre><code>	You can exclude this check with the command line option:
	-x fontdata_namecheck

	Or you can wait until the service is available again.
	If the problem persists please report this issue at: https://github.com/fonttools/fontbakery/issues

	Original error message:
	&lt;class 'requests.exceptions.ConnectionError'&gt;
</code></pre>
 [code: namecheck-service]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Do we have the latest version of FontBakery installed? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#fontbakery-version">fontbakery_version</a></summary>
    <div>







* 🔥 **FAIL** <p>Current FontBakery version is 1.0.1, while a newer 1.1.0 is already available. Please upgrade it with 'pip install -U fontbakery'</p>
 [code: outdated-fontbakery]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* k (U+006B): L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* k.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni006B0307: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni006B0307.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni006B0302: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni006B0302.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9 (U+01E9): L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni01E9.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137 (U+0137): L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0137.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni027C (U+027C): L&lt;&lt;71.0,500.0&gt;--&lt;165.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni04F6.ss05: L&lt;&lt;184.0,0.0&gt;--&lt;84.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0416.ss04: L&lt;&lt;504.0,306.0&gt;--&lt;504.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni0416.ss04: L&lt;&lt;576.0,394.0&gt;--&lt;576.0,306.0&gt;&gt; has the same coordinates as a previous segment.

* uni041A.ss04: L&lt;&lt;124.0,306.0&gt;--&lt;124.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni040C.ss04: L&lt;&lt;124.0,306.0&gt;--&lt;124.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni0496.ss04: L&lt;&lt;504.0,306.0&gt;--&lt;504.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni0496.ss04: L&lt;&lt;576.0,394.0&gt;--&lt;576.0,306.0&gt;&gt; has the same coordinates as a previous segment.

* uni049A.ss04: L&lt;&lt;124.0,306.0&gt;--&lt;124.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni049C.ss04: L&lt;&lt;224.0,306.0&gt;--&lt;224.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni049E.ss04: L&lt;&lt;124.0,306.0&gt;--&lt;124.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A0.ss04: L&lt;&lt;264.0,306.0&gt;--&lt;264.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C1.ss04: L&lt;&lt;504.0,306.0&gt;--&lt;504.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C1.ss04: L&lt;&lt;576.0,394.0&gt;--&lt;576.0,306.0&gt;&gt; has the same coordinates as a previous segment.

* uni04DC.ss04: L&lt;&lt;504.0,306.0&gt;--&lt;504.0,394.0&gt;&gt; has the same coordinates as a previous segment.

* uni04DC.ss04: L&lt;&lt;576.0,394.0&gt;--&lt;576.0,306.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;477.0,0.0&gt;--&lt;383.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.cv07: L&lt;&lt;477.0,0.0&gt;--&lt;383.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.ss04: L&lt;&lt;440.0,210.0&gt;--&lt;440.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.ss04: L&lt;&lt;420.0,290.0&gt;--&lt;420.0,210.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.ss04.loclBGR: L&lt;&lt;476.0,0.0&gt;--&lt;384.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.ss04.loclBGR: L&lt;&lt;440.0,210.0&gt;--&lt;440.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.ss04.loclBGR: L&lt;&lt;420.0,290.0&gt;--&lt;420.0,210.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.ss04: L&lt;&lt;160.0,210.0&gt;--&lt;160.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.ss04.loclBGR: L&lt;&lt;166.0,0.0&gt;--&lt;72.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.ss04.loclBGR: L&lt;&lt;160.0,210.0&gt;--&lt;160.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni045C.ss04: L&lt;&lt;160.0,210.0&gt;--&lt;160.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni0497.ss04: L&lt;&lt;440.0,210.0&gt;--&lt;440.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni0497.ss04: L&lt;&lt;420.0,290.0&gt;--&lt;420.0,210.0&gt;&gt; has the same coordinates as a previous segment.

* uni049B.ss04: L&lt;&lt;160.0,210.0&gt;--&lt;160.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni049D.ss04: L&lt;&lt;260.0,210.0&gt;--&lt;260.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F (U+049F): L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.cv07: L&lt;&lt;165.0,0.0&gt;--&lt;71.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss04: L&lt;&lt;166.0,0.0&gt;--&lt;72.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss04: L&lt;&lt;160.0,210.0&gt;--&lt;160.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A1.ss04: L&lt;&lt;260.0,210.0&gt;--&lt;260.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni04BD (U+04BD): L&lt;&lt;244.0,218.0&gt;--&lt;244.0,284.0&gt;&gt; has the same coordinates as a previous segment.

* uni04BF (U+04BF): L&lt;&lt;244.0,218.0&gt;--&lt;244.0,284.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C2.ss04: L&lt;&lt;440.0,210.0&gt;--&lt;440.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni04C2.ss04: L&lt;&lt;420.0,290.0&gt;--&lt;420.0,210.0&gt;&gt; has the same coordinates as a previous segment.

* uni04DD.ss04: L&lt;&lt;440.0,210.0&gt;--&lt;440.0,290.0&gt;&gt; has the same coordinates as a previous segment.

* uni04DD.ss04: L&lt;&lt;420.0,290.0&gt;--&lt;420.0,210.0&gt;&gt; has the same coordinates as a previous segment.

* zeta (U+03B6): L&lt;&lt;52.0,204.0&gt;--&lt;146.0,216.0&gt;&gt; has the same coordinates as a previous segment.

* uni03BC (U+03BC): L&lt;&lt;67.0,500.0&gt;--&lt;161.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni03BC.ss05: L&lt;&lt;62.0,500.0&gt;--&lt;156.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* xi (U+03BE): L&lt;&lt;52.0,204.0&gt;--&lt;146.0,216.0&gt;&gt; has the same coordinates as a previous segment.

* uni03C2 (U+03C2): L&lt;&lt;44.0,204.0&gt;--&lt;138.0,216.0&gt;&gt; has the same coordinates as a previous segment.

* uni00B5 (U+00B5): L&lt;&lt;67.0,500.0&gt;--&lt;161.0,500.0&gt;&gt; has the same coordinates as a previous segment.

* uni00B5.ss05: L&lt;&lt;62.0,500.0&gt;--&lt;156.0,500.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- halfsection

- hookabove

- horn

- uni004B0302

- uni004B0307

- uni00500302

- uni00510302

- uni00510307

- uni00540302

- uni00580302

- uni006B0302

- uni006B0307

- uni00700302

- uni00710302

- uni00710307

- uni00740302

- uni00780302

- uni03020300

- uni03020301

- uni03020303

- uni03020309

- uni03060300

- uni03060301

- uni03060303

- uni03060309

- uni04100304

- uni04150304

- uni041E0304

- uni042D0304

- uni04300304

- uni04350304

- uni0436.ss04.loclBGR

- uni043E0304

- uni044D0304

- uni048F.001

- uni0496.cv

- uni04B60306.cy

- uni04B70306.cy

- uni04E80304

- uni04E90304
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts does not have an article.</p>
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
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, tifinagh, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, malayalam, todhri, tifinagh, math, syriac, old-permic, tai-le, hebrew, duployan, canadian-aboriginal</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+2007 FIGURE SPACE: try adding symbols2</li>
<li>U+2008 PUNCTUATION SPACE: try adding symbols2</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
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
<li>U+2095 LATIN SUBSCRIPT SMALL LETTER H: try adding math</li>
<li>U+2096 LATIN SUBSCRIPT SMALL LETTER K: try adding math</li>
<li>U+2097 LATIN SUBSCRIPT SMALL LETTER L: try adding math</li>
<li>U+2098 LATIN SUBSCRIPT SMALL LETTER M: try adding math</li>
<li>U+2099 LATIN SUBSCRIPT SMALL LETTER N: try adding math</li>
<li>U+209A LATIN SUBSCRIPT SMALL LETTER P: try adding math</li>
<li>U+209B LATIN SUBSCRIPT SMALL LETTER S: try adding math</li>
<li>U+209C LATIN SUBSCRIPT SMALL LETTER T: try adding math</li>
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
<li>U+2160 ROMAN NUMERAL ONE: try adding symbols</li>
<li>U+2161 ROMAN NUMERAL TWO: try adding symbols</li>
<li>U+2162 ROMAN NUMERAL THREE: try adding symbols</li>
<li>U+2163 ROMAN NUMERAL FOUR: try adding symbols</li>
<li>U+2164 ROMAN NUMERAL FIVE: try adding symbols</li>
<li>U+2165 ROMAN NUMERAL SIX: try adding symbols</li>
<li>U+2166 ROMAN NUMERAL SEVEN: try adding symbols</li>
<li>U+2167 ROMAN NUMERAL EIGHT: try adding symbols</li>
<li>U+2168 ROMAN NUMERAL NINE: try adding symbols</li>
<li>U+2169 ROMAN NUMERAL TEN: try adding symbols</li>
<li>U+216A ROMAN NUMERAL ELEVEN: try adding symbols</li>
<li>U+216B ROMAN NUMERAL TWELVE: try adding symbols</li>
<li>U+216C ROMAN NUMERAL FIFTY: try adding symbols</li>
<li>U+216D ROMAN NUMERAL ONE HUNDRED: try adding symbols</li>
<li>U+216E ROMAN NUMERAL FIVE HUNDRED: try adding symbols</li>
<li>U+216F ROMAN NUMERAL ONE THOUSAND: try adding symbols</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, yi, tai-tham, math</li>
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
<li>U+22A1 SQUARED DOT OPERATOR: try adding math</li>
<li>U+22C5 DOT OPERATOR: try adding one of: symbols, math</li>
<li>U+22EE VERTICAL ELLIPSIS: try adding math</li>
<li>U+22EF MIDLINE HORIZONTAL ELLIPSIS: try adding math</li>
<li>U+22F0 UP RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+22F1 DOWN RIGHT DIAGONAL ELLIPSIS: try adding math</li>
<li>U+2300 DIAMETER SIGN: try adding symbols</li>
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: symbols, yi, mongolian</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: symbols, yi, mongolian</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: symbols, yi, mongolian</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: symbols, yi, mongolian</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: symbols, yi, mongolian</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: symbols, yi, mongolian</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: symbols, yi, mongolian</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: symbols, yi, mongolian</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: symbols, yi, mongolian</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: hanunoo, kannada, miao, modi, armenian, thaana, kharoshthi, brahmi, coptic, saurashtra, gujarati, tagbanwa, bengali, nko, yi, lao, oriya, tagalog, balinese, tifinagh, rejang, tai-le, duployan, adlam, siddham, javanese, batak, sogdian, newa, math, dogra, manichaean, mahajani, kayah-li, thai, elbasan, mende-kikakui, takri, masaram-gondi, mongolian, lepcha, buhid, khudawadi, ahom, buginese, bassa-vah, limbu, cham, tibetan, psalter-pahlavi, devanagari, myanmar, sundanese, tirhuta, warang-citi, hebrew, telugu, wancho, grantha, khojki, symbols, gunjala-gondi, soyombo, syriac, old-permic, tamil, khmer, caucasian-albanian, new-tai-lue, osage, tai-viet, marchen, sinhala, kaithi, sharada, malayalam, chakma, bhaiksuki, syloti-nagri, mandaic, zanabazar-square, phags-pa, hanifi-rohingya, tai-tham, music, canadian-aboriginal, gurmukhi, meetei-mayek, pahawh-hmong</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25D0 CIRCLE WITH LEFT HALF BLACK: try adding symbols</li>
<li>U+25D1 CIRCLE WITH RIGHT HALF BLACK: try adding symbols</li>
<li>U+25D2 CIRCLE WITH LOWER HALF BLACK: try adding symbols</li>
<li>U+25D3 CIRCLE WITH UPPER HALF BLACK: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
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
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>vietnamese</code></p>
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
<td align="left">The following auxiliary characters are missing from the font: ѣ</td>
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
<td align="left">The following auxiliary characters are missing from the font: ἀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἠ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: j̉ j̛̉ j̦̉ j̧̉ j̶̉ ʲ̀ ʲ́ ʲ̂ ʲ̃ ʲ̄ ʲ̆ ʲ̇ ʲ̈ ʲ̉ ʲ̊ ʲ̋ ʲ̌ ʲ̒ ʲ̛̀ ʲ̛́</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* m (U+006D): X=379.0,Y=499.0 (should be at x-height 500?)

* m (U+006D): X=532.5,Y=499.0 (should be at x-height 500?)

* p.ss05: X=237.0,Y=-2.0 (should be at baseline 0?)

* q.ss05: X=323.0,Y=-2.0 (should be at baseline 0?)

* x (U+0078): X=525.0,Y=501.0 (should be at x-height 500?)

* u.small: X=208.5,Y=1.5 (should be at baseline 0?)

* binferior: X=287.5,Y=-1.0 (should be at baseline 0?)

* binferior: X=145.0,Y=-1.0 (should be at baseline 0?)

* bsuperior: X=198.0,Y=700.5 (should be at cap-height 700?)

* dinferior: X=275.0,Y=-1.0 (should be at baseline 0?)

* dinferior: X=132.5,Y=-1.0 (should be at baseline 0?)

* dsuperior: X=222.0,Y=700.5 (should be at cap-height 700?)

* psuperior: X=198.0,Y=700.5 (should be at cap-height 700?)

* qsuperior: X=222.0,Y=700.5 (should be at cap-height 700?)

* uinferior: X=254.0,Y=-2.0 (should be at baseline 0?)

* yinferior: X=196.0,Y=-2.0 (should be at baseline 0?)

* uni2092 (U+2092): X=269.5,Y=1.5 (should be at baseline 0?)

* uni2092 (U+2092): X=130.5,Y=1.5 (should be at baseline 0?)

* uni2093 (U+2093): X=199.0,Y=-1.0 (should be at baseline 0?)

* hsuperior: X=193.0,Y=699.0 (should be at cap-height 700?)

* uni02B0 (U+02B0): X=193.0,Y=699.0 (should be at cap-height 700?)

* uni207F (U+207F): X=193.5,Y=698.5 (should be at cap-height 700?)

* uni02E2 (U+02E2): X=106.0,Y=698.5 (should be at cap-height 700?)

* uni02E2 (U+02E2): X=249.0,Y=699.0 (should be at cap-height 700?)

* uni0416.cv07: X=492.0,Y=702.0 (should be at cap-height 700?)

* uni0416.cv07: X=590.0,Y=702.0 (should be at cap-height 700?)

* uni0496.cv: X=492.0,Y=702.0 (should be at cap-height 700?)

* uni0496.cv: X=590.0,Y=702.0 (should be at cap-height 700?)

* uni0498 (U+0498): X=286.0,Y=-2.0 (should be at baseline 0?)

* uni04C1.cv07: X=492.0,Y=702.0 (should be at cap-height 700?)

* uni04C1.cv07: X=590.0,Y=702.0 (should be at cap-height 700?)

* uni04DC.cv07: X=492.0,Y=702.0 (should be at cap-height 700?)

* uni04DC.cv07: X=590.0,Y=702.0 (should be at cap-height 700?)

* uni0431.loclSRB: X=224.0,Y=702.0 (should be at cap-height 700?)

* uni0440.ss05: X=237.0,Y=-2.0 (should be at baseline 0?)

* uni0448.loclBGR: X=461.0,Y=1.0 (should be at baseline 0?)

* uni0448.loclBGR: X=307.5,Y=1.0 (should be at baseline 0?)

* uni0449.loclBGR: X=467.0,Y=1.0 (should be at baseline 0?)

* uni0449.loclBGR: X=313.5,Y=1.0 (should be at baseline 0?)

* uni048F (U+048F): X=514.0,Y=-1.0 (should be at baseline 0?)

* uni048F.001: X=237.0,Y=-2.0 (should be at baseline 0?)

* uni048F.001: X=514.0,Y=-1.0 (should be at baseline 0?)

* beta (U+03B2): X=250.0,Y=1.0 (should be at baseline 0?)

* delta (U+03B4): X=162.0,Y=698.0 (should be at cap-height 700?)

* delta (U+03B4): X=338.0,Y=702.0 (should be at cap-height 700?)

* rho (U+03C1): X=237.0,Y=-2.0 (should be at baseline 0?)

* uni00B3 (U+00B3): X=368.0,Y=698.0 (should be at cap-height 700?)

* uni2078 (U+2078): X=56.0,Y=698.0 (should be at cap-height 700?)

* uni2078 (U+2078): X=384.0,Y=698.0 (should be at cap-height 700?)

* uni2101 (U+2101): X=640.5,Y=2.0 (should be at baseline 0?)

* uni2101 (U+2101): X=796.0,Y=1.0 (should be at baseline 0?)

* uni2106 (U+2106): X=728.5,Y=1.5 (should be at baseline 0?)

* plusminus (U+00B1): X=57.0,Y=-1.0 (should be at baseline 0?)

* plusminus (U+00B1): X=543.0,Y=-1.0 (should be at baseline 0?)

* plusminus.case: X=57.0,Y=1.0 (should be at baseline 0?)

* plusminus.case: X=543.0,Y=1.0 (should be at baseline 0?)

* plusminus.case: X=57.0,Y=1.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-direction">outline_direction</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have a counter-clockwise outer contour:</p>
<pre><code>* uni24FF (U+24FF) has a counter-clockwise outer contour

* uni2776 (U+2776) has a counter-clockwise outer contour

* uni2777 (U+2777) has a counter-clockwise outer contour

* uni2778 (U+2778) has a counter-clockwise outer contour

* uni2779 (U+2779) has a counter-clockwise outer contour

* uni277A (U+277A) has a counter-clockwise outer contour

* uni277B (U+277B) has a counter-clockwise outer contour

* uni277C (U+277C) has a counter-clockwise outer contour

* uni277D (U+277D) has a counter-clockwise outer contour

* uni277E (U+277E) has a counter-clockwise outer contour
</code></pre>
 [code: ccw-outer-contour]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 1 | 0 | 1 | 10 | 89 | 7 | 128 | 0 | 
| 0% | 0% | 0% | 4% | 38% | 3% | 54% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
