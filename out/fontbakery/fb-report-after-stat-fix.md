## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[6] Akt[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#interpolation-issues">interpolation_issues</a></summary>
    <div>


> 
> When creating a variable font, the designer must make sure that corresponding
> paths have the same start points across masters, as well as that corresponding
> component shapes are placed in the same order within a glyph across masters.
> If this is not done, the glyph will not interpolate correctly.
> 
> Here we check for the presence of potential interpolation errors using the
> fontTools.varLib.interpolatable module.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3930





* ⚠️ **WARN** <p>Interpolation issues were found in the font:</p>
<pre><code>- Contour 1 start point differs in glyph 'uni0496.ss01' between location wght=400 and location wght=100

- Contour 1 in glyph 'uni0496.ss01': becomes underweight between wght=400 and wght=100.

- Contour 1 start point differs in glyph 'uni0496.ss01' between location wght=100 and location wght=271

- Contour 1 in glyph 'uni0496.ss01': becomes underweight between wght=100 and wght=271.

- Contour 0 start point differs in glyph 'uni0416.ss01' between location wght=400 and location wght=100

- Contour 0 in glyph 'uni0416.ss01': becomes underweight between wght=400 and wght=100.

- Contour 0 start point differs in glyph 'uni0416.ss01' between location wght=100 and location wght=271

- Contour 0 in glyph 'uni0416.ss01': becomes underweight between wght=100 and wght=271.
</code></pre>
 [code: interpolation-issues]



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





* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, coptic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: malayalam, coptic, syriac, hebrew, old-permic, tai-le, duployan, todhri, tifinagh, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0391 GREEK CAPITAL LETTER ALPHA: try adding one of: greek, math, elbasan</li>
<li>U+0394 GREEK CAPITAL LETTER DELTA: try adding one of: greek, math, elbasan</li>
<li>U+039E GREEK CAPITAL LETTER XI: try adding one of: greek, math, elbasan</li>
<li>U+03A9 GREEK CAPITAL LETTER OMEGA: try adding one of: greek, math, elbasan</li>
<li>U+03B1 GREEK SMALL LETTER ALPHA: try adding one of: greek, math</li>
<li>U+03B4 GREEK SMALL LETTER DELTA: try adding one of: greek, math</li>
<li>U+03BC GREEK SMALL LETTER MU: try adding one of: greek, math</li>
<li>U+03BE GREEK SMALL LETTER XI: try adding one of: greek, math</li>
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
<li>U+2010 HYPHEN: try adding one of: yi, coptic, syloti-nagri, hebrew, kharoshthi, sundanese, armenian, kayah-li, sora-sompeng, cham, lisu, arabic, kaithi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: syloti-nagri, yi, arabic</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2024 ONE DOT LEADER: try adding armenian</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+203C DOUBLE EXCLAMATION MARK: try adding math</li>
<li>U+2043 HYPHEN BULLET: try adding math</li>
<li>U+2047 DOUBLE QUESTION MARK: try adding math</li>
<li>U+2048 QUESTION EXCLAMATION MARK: try adding mongolian</li>
<li>U+2049 EXCLAMATION QUESTION MARK: try adding mongolian</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: yi, math, tai-tham, symbols</li>
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
<li>U+25CA LOZENGE: try adding one of: math, symbols</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CC DOTTED CIRCLE: try adding one of: khudawadi, sundanese, dogra, syriac, hebrew, khojki, thai, sogdian, javanese, old-permic, marchen, soyombo, lepcha, mandaic, masaram-gondi, kaithi, nko, wancho, tirhuta, hanunoo, manichaean, symbols, brahmi, tai-viet, grantha, zanabazar-square, hanifi-rohingya, kharoshthi, tai-le, thaana, new-tai-lue, sinhala, miao, adlam, caucasian-albanian, gunjala-gondi, mongolian, rejang, telugu, ahom, tifinagh, coptic, batak, khmer, bengali, balinese, tagalog, phags-pa, malayalam, tai-tham, meetei-mayek, gurmukhi, saurashtra, mahajani, canadian-aboriginal, math, buhid, modi, sharada, takri, oriya, music, yi, syloti-nagri, chakma, bhaiksuki, armenian, devanagari, cham, tagbanwa, tibetan, pahawh-hmong, siddham, gujarati, myanmar, duployan, mende-kikakui, tamil, kayah-li, bassa-vah, kannada, elbasan, psalter-pahlavi, warang-citi, buginese, osage, limbu, lao, newa</li>
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
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



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





* ⚠️ **WARN** <p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: ⁱ̀ ⁱ́ ⁱ̂ ⁱ̃ ⁱ̄ ⁱ̆ ⁱ̇ ⁱ̈ ⁱ̊ ⁱ̋ ⁱ̌ ⁱ̒ ⁱ⃰ ⁱ̣̀ ⁱ̣́ ⁱ̣̂ ⁱ̣̃ ⁱ̣̄ ⁱ̣̆ ⁱ̣̇</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>


> 
> This check heuristically looks for on-curve points which are close to, but
> do not sit on, significant boundary coordinates. For example, a point which
> has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as
> the baseline, here we also check for points near the x-height (but only for
> lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design
> may call for points in locations near the boundaries. As this check is liable
> to generate significant numbers of false positives, it will pass if there are
> more than 100 reported misalignments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Aring (U+00C5): X=259.5,Y=959.5 (should be at ascender 960?)

* Aring (U+00C5): X=440.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=259.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=440.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=249.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=430.5,Y=959.5 (should be at ascender 960?)

* a (U+0061): X=244.5,Y=-1.0 (should be at baseline 0?)

* aacute (U+00E1): X=244.5,Y=-1.0 (should be at baseline 0?)

* abreve (U+0103): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni01CE (U+01CE): X=244.5,Y=-1.0 (should be at baseline 0?)

* acircumflex (U+00E2): X=244.5,Y=-1.0 (should be at baseline 0?)

* adieresis (U+00E4): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni0227 (U+0227): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni1EA1 (U+1EA1): X=244.5,Y=-1.0 (should be at baseline 0?)

* agrave (U+00E0): X=244.5,Y=-1.0 (should be at baseline 0?)

* amacron (U+0101): X=244.5,Y=-1.0 (should be at baseline 0?)

* aogonek (U+0105): X=244.5,Y=-1.0 (should be at baseline 0?)

* aring (U+00E5): X=244.5,Y=-1.0 (should be at baseline 0?)

* aringacute (U+01FB): X=244.5,Y=-1.0 (should be at baseline 0?)

* atilde (U+00E3): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni0123 (U+0123): X=381.0,Y=721.0 (should be at cap-height 720?)

* uni0123 (U+0123): X=261.0,Y=721.0 (should be at cap-height 720?)

* uni0123 (U+0123): X=381.0,Y=721.0 (should be at cap-height 720?)

* uni0123.ss01: X=383.0,Y=721.0 (should be at cap-height 720?)

* uni0123.ss01: X=263.0,Y=721.0 (should be at cap-height 720?)

* uni0123.ss01: X=383.0,Y=721.0 (should be at cap-height 720?)

* uni0123.ss02: X=381.0,Y=721.0 (should be at cap-height 720?)

* uni0123.ss02: X=261.0,Y=721.0 (should be at cap-height 720?)

* uni0123.ss02: X=381.0,Y=721.0 (should be at cap-height 720?)

* h (U+0068): X=282.0,Y=498.0 (should be at x-height 500?)

* n (U+006E): X=282.0,Y=498.0 (should be at x-height 500?)

* oe (U+0153): X=333.0,Y=1.0 (should be at baseline 0?)

* u (U+0075): X=278.0,Y=2.0 (should be at baseline 0?)

* uacute (U+00FA): X=278.0,Y=2.0 (should be at baseline 0?)

* ubreve (U+016D): X=278.0,Y=2.0 (should be at baseline 0?)

* ucircumflex (U+00FB): X=278.0,Y=2.0 (should be at baseline 0?)

* udieresis (U+00FC): X=278.0,Y=2.0 (should be at baseline 0?)

* uni1EE5 (U+1EE5): X=278.0,Y=2.0 (should be at baseline 0?)

* ugrave (U+00F9): X=278.0,Y=2.0 (should be at baseline 0?)

* uhungarumlaut (U+0171): X=278.0,Y=2.0 (should be at baseline 0?)

* umacron (U+016B): X=278.0,Y=2.0 (should be at baseline 0?)

* uogonek (U+0173): X=278.0,Y=2.0 (should be at baseline 0?)

* uring (U+016F): X=278.0,Y=2.0 (should be at baseline 0?)

* utilde (U+0169): X=278.0,Y=2.0 (should be at baseline 0?)

* ginferior: X=30.5,Y=1.0 (should be at baseline 0?)

* gsuperior: X=186.5,Y=721.5 (should be at cap-height 720?)

* psuperior: X=228.5,Y=721.0 (should be at cap-height 720?)

* qsuperior: X=181.5,Y=721.0 (should be at cap-height 720?)

* uni2090 (U+2090): X=153.0,Y=-1.0 (should be at baseline 0?)

* uni2091 (U+2091): X=197.0,Y=-2.0 (should be at baseline 0?)

* uni2091 (U+2091): X=215.5,Y=1.0 (should be at baseline 0?)

* uni2094 (U+2094): X=164.0,Y=-0.5 (should be at baseline 0?)

* uni2094 (U+2094): X=208.0,Y=0.5 (should be at baseline 0?)

* uni02B0: X=219.5,Y=718.0 (should be at cap-height 720?)

* uni207F (U+207F): X=219.5,Y=718.0 (should be at cap-height 720?)

* uni0407 (U+0407): X=196.0,Y=958.0 (should be at ascender 960?)

* uni0407 (U+0407): X=74.0,Y=958.0 (should be at ascender 960?)

* uni0430 (U+0430): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni0431 (U+0431): X=295.0,Y=718.0 (should be at cap-height 720?)

* uni0431.loclSRB: X=302.0,Y=719.0 (should be at cap-height 720?)

* uni0438.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni0439.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni046B (U+046B): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=786.0,Y=-1.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=671.0,Y=-1.0 (should be at baseline 0?)

* uni04D1 (U+04D1): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni04D3 (U+04D3): X=244.5,Y=-1.0 (should be at baseline 0?)

* uni03BC (U+03BC): X=288.0,Y=-1.0 (should be at baseline 0?)

* uni209B (U+209B): X=148.0,Y=2.0 (should be at baseline 0?)

* uni208D (U+208D): X=61.0,Y=0.5 (should be at baseline 0?)

* uni208D (U+208D): X=230.0,Y=2.0 (should be at baseline 0?)

* uni208E (U+208E): X=10.0,Y=2.0 (should be at baseline 0?)

* uni208E (U+208E): X=179.0,Y=0.5 (should be at baseline 0?)

* braceleft.case: X=312.0,Y=722.0 (should be at cap-height 720?)

* braceright.case: X=88.0,Y=722.0 (should be at cap-height 720?)

* uni207D (U+207D): X=61.0,Y=718.5 (should be at cap-height 720?)

* uni207D (U+207D): X=230.0,Y=718.0 (should be at cap-height 720?)

* uni207E (U+207E): X=10.0,Y=718.0 (should be at cap-height 720?)

* uni207E (U+207E): X=179.0,Y=718.5 (should be at cap-height 720?)

* uni2101 (U+2101): X=802.0,Y=1.5 (should be at baseline 0?)

* uni00B5 (U+00B5): X=288.0,Y=-1.0 (should be at baseline 0?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=76.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)
</code></pre>
 [code: found-misalignments]



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





* ⚠️ **WARN** <p>OS/2 VendorID value 'DMGR' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 6 | 89 | 8 | 133 | 0 | 
| 0% | 0% | 0% | 3% | 38% | 3% | 56% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
