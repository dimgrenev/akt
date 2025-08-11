## FontBakery report

fontbakery version: 1.0.1







## Check results



<details><summary>[22] Akt-Black.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni0436.loclBGR: L&lt;&lt;467.0,0.0&gt;--&lt;325.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;500.0,0.0&gt;--&lt;360.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;192.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;244.0,0.0&gt;--&lt;104.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;498.0,0.0&gt;--&lt;356.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
<pre><code>* Aring (U+00C5): X=239.5,Y=959.5 (should be at ascender 960?)

* Aring (U+00C5): X=420.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=239.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=420.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=249.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=430.5,Y=959.5 (should be at ascender 960?)

* b.small: X=175.5,Y=-1.5 (should be at baseline 0?)

* c.sub: X=207.5,Y=-0.5 (should be at baseline 0?)

* d.small: X=181.5,Y=-1.5 (should be at baseline 0?)

* f (U+0066): X=98.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=240.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=98.0,Y=2.0 (should be at baseline 0?)

* f.small: X=60.0,Y=1.0 (should be at baseline 0?)

* f.small: X=147.0,Y=1.0 (should be at baseline 0?)

* f.small: X=60.0,Y=1.0 (should be at baseline 0?)

* g.small: X=143.0,Y=2.0 (should be at baseline 0?)

* g.superior: X=177.0,Y=721.5 (should be at cap-height 720?)

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

* h.superior: X=172.5,Y=718.5 (should be at cap-height 720?)

* n (U+006E): X=282.0,Y=498.0 (should be at x-height 500?)

* oe (U+0153): X=333.0,Y=1.0 (should be at baseline 0?)

* p.small: X=175.5,Y=-1.5 (should be at baseline 0?)

* p.superior: X=175.5,Y=721.5 (should be at cap-height 720?)

* q.small: X=181.5,Y=-1.5 (should be at baseline 0?)

* q.superior: X=181.5,Y=721.5 (should be at cap-height 720?)

* u (U+0075): X=278.0,Y=2.0 (should be at baseline 0?)

* u.small: X=170.0,Y=1.5 (should be at baseline 0?)

* u.sub: X=137.5,Y=-2.0 (should be at baseline 0?)

* u.sub: X=190.5,Y=-2.0 (should be at baseline 0?)

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

* uni2091 (U+2091): X=217.0,Y=-1.5 (should be at baseline 0?)

* uni2094 (U+2094): X=106.5,Y=1.0 (should be at baseline 0?)

* uni207F (U+207F): X=172.5,Y=718.5 (should be at cap-height 720?)

* uni0407 (U+0407): X=196.0,Y=958.0 (should be at ascender 960?)

* uni0407 (U+0407): X=74.0,Y=958.0 (should be at ascender 960?)

* uni0431 (U+0431): X=295.0,Y=718.0 (should be at cap-height 720?)

* uni0431.loclSRB: X=302.0,Y=719.0 (should be at cap-height 720?)

* uni0438.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni0439.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=786.0,Y=-1.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=671.0,Y=-1.0 (should be at baseline 0?)

* uni03BC (U+03BC): X=278.0,Y=2.0 (should be at baseline 0?)

* uni2085 (U+2085): X=221.0,Y=-2.0 (should be at baseline 0?)

* uni2086 (U+2086): X=236.0,Y=0.5 (should be at baseline 0?)

* uni2086 (U+2086): X=157.5,Y=0.5 (should be at baseline 0?)

* uni2079 (U+2079): X=147.0,Y=721.5 (should be at cap-height 720?)

* uni2079 (U+2079): X=225.5,Y=721.5 (should be at cap-height 720?)

* uni208D (U+208D): X=53.0,Y=0.5 (should be at baseline 0?)

* uni208E (U+208E): X=147.0,Y=0.5 (should be at baseline 0?)

* braceleft.case: X=302.0,Y=722.0 (should be at cap-height 720?)

* braceright.case: X=98.0,Y=722.0 (should be at cap-height 720?)

* uni207D (U+207D): X=53.0,Y=718.5 (should be at cap-height 720?)

* uni207E (U+207E): X=147.0,Y=718.5 (should be at cap-height 720?)

* uni00B5 (U+00B5): X=278.0,Y=2.0 (should be at baseline 0?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=76.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;426.0,240.0&gt;--&lt;410.0,487.0&gt;&gt; -&gt; L&lt;&lt;410.0,487.0&gt;--&lt;410.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;550.0,720.0&gt;--&lt;550.0,487.0&gt;&gt; -&gt; L&lt;&lt;550.0,487.0&gt;--&lt;534.0,240.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;214.0,261.0&gt;--&lt;230.0,14.0&gt;&gt; -&gt; L&lt;&lt;230.0,14.0&gt;--&lt;230.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;90.0,-219.0&gt;--&lt;90.0,14.0&gt;&gt; -&gt; L&lt;&lt;90.0,14.0&gt;--&lt;106.0,261.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;626.0,240.0&gt;--&lt;610.0,487.0&gt;&gt; -&gt; L&lt;&lt;610.0,487.0&gt;--&lt;610.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;750.0,720.0&gt;--&lt;750.0,487.0&gt;&gt; -&gt; L&lt;&lt;750.0,487.0&gt;--&lt;734.0,240.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;205.0,720.0&gt;--&lt;205.0,580.0&gt;&gt; -&gt; L&lt;&lt;205.0,580.0&gt;--&lt;205.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;55.0,240.0&gt;--&lt;55.0,580.0&gt;&gt; -&gt; L&lt;&lt;55.0,580.0&gt;--&lt;55.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;178.0,720.0&gt;--&lt;178.0,620.0&gt;&gt; -&gt; L&lt;&lt;178.0,620.0&gt;--&lt;178.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;36.0,380.0&gt;--&lt;36.0,620.0&gt;&gt; -&gt; L&lt;&lt;36.0,620.0&gt;--&lt;36.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* three.dnom: B&lt;&lt;273.0,227.0&gt;-&lt;255.0,214.0&gt;-&lt;230.0,210.0&gt;&gt;/B&lt;&lt;230.0,210.0&gt;-&lt;255.0,208.0&gt;-&lt;275.5,194.0&gt;&gt; = 13.664198180723144

* three.numr: B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* three.small: B&lt;&lt;300.5,250.0&gt;-&lt;281.0,236.0&gt;-&lt;253.0,231.0&gt;&gt;/B&lt;&lt;253.0,231.0&gt;-&lt;281.0,229.0&gt;-&lt;303.5,213.5&gt;&gt; = 14.210288435372686

* threeeighths (U+215C): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* threequarters (U+00BE): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* uni00B3 (U+00B3): B&lt;&lt;300.5,610.0&gt;-&lt;281.0,596.0&gt;-&lt;253.0,591.0&gt;&gt;/B&lt;&lt;253.0,591.0&gt;-&lt;281.0,589.0&gt;-&lt;303.5,573.5&gt;&gt; = 14.210288435372686

* uni2083 (U+2083): B&lt;&lt;300.5,170.0&gt;-&lt;281.0,156.0&gt;-&lt;253.0,151.0&gt;&gt;/B&lt;&lt;253.0,151.0&gt;-&lt;281.0,149.0&gt;-&lt;303.5,133.5&gt;&gt; = 14.210288435372686

* uni2153 (U+2153): B&lt;&lt;717.0,227.0&gt;-&lt;699.0,214.0&gt;-&lt;674.0,210.0&gt;&gt;/B&lt;&lt;674.0,210.0&gt;-&lt;699.0,208.0&gt;-&lt;719.5,194.0&gt;&gt; = 13.664198180723144

* uni2154 (U+2154): B&lt;&lt;795.0,227.0&gt;-&lt;777.0,214.0&gt;-&lt;752.0,210.0&gt;&gt;/B&lt;&lt;752.0,210.0&gt;-&lt;777.0,208.0&gt;-&lt;797.5,194.0&gt;&gt; = 13.664198180723144

* uni2157 (U+2157): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* uni2189 (U+2189): B&lt;&lt;817.0,227.0&gt;-&lt;799.0,214.0&gt;-&lt;774.0,210.0&gt;&gt;/B&lt;&lt;774.0,210.0&gt;-&lt;799.0,208.0&gt;-&lt;819.5,194.0&gt;&gt; = 13.664198180723144

* uni2462 (U+2462): B&lt;&lt;527.0,387.0&gt;-&lt;509.0,374.0&gt;-&lt;484.0,370.0&gt;&gt;/B&lt;&lt;484.0,370.0&gt;-&lt;509.0,368.0&gt;-&lt;529.5,354.0&gt;&gt; = 13.664198180723144

* uni2778 (U+2778): B&lt;&lt;527.0,387.0&gt;-&lt;509.0,374.0&gt;-&lt;484.0,370.0&gt;&gt;/B&lt;&lt;484.0,370.0&gt;-&lt;509.0,368.0&gt;-&lt;529.5,354.0&gt;&gt; = 13.664198180723144
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* a.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

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

* f_f_j contains a short segment L&lt;&lt;701.0,-86.0&gt;--&lt;730.0,-86.0&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;340.0,310.0&gt;--&lt;346.0,310.0&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* ampersand (U+0026) contains a short segment B&lt;&lt;226.0,545.0&gt;-&lt;226.0,529.0&gt;-&lt;232.5,514.5&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[23] Akt-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



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
<td align="left">Akt</td>
<td align="left">Akt</td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left">Bold</td>
<td align="left">Bold</td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left">Akt Bold</td>
<td align="left">Akt Bold</td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left">Akt-Bold</td>
<td align="left">Akt-Bold</td>
</tr>
<tr>
<td align="left">Typographic Family Name</td>
<td align="left"><strong>Akt</strong></td>
<td align="left"><strong>N/A</strong></td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni0436.loclBGR: L&lt;&lt;467.0,0.0&gt;--&lt;325.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;500.0,0.0&gt;--&lt;360.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;192.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;244.0,0.0&gt;--&lt;104.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;498.0,0.0&gt;--&lt;356.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
<pre><code>* Aring (U+00C5): X=239.5,Y=959.5 (should be at ascender 960?)

* Aring (U+00C5): X=420.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=239.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=420.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=249.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=430.5,Y=959.5 (should be at ascender 960?)

* b.small: X=175.5,Y=-1.5 (should be at baseline 0?)

* c.sub: X=207.5,Y=-0.5 (should be at baseline 0?)

* d.small: X=181.5,Y=-1.5 (should be at baseline 0?)

* f (U+0066): X=98.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=240.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=98.0,Y=2.0 (should be at baseline 0?)

* f.small: X=60.0,Y=1.0 (should be at baseline 0?)

* f.small: X=147.0,Y=1.0 (should be at baseline 0?)

* f.small: X=60.0,Y=1.0 (should be at baseline 0?)

* g.small: X=143.0,Y=2.0 (should be at baseline 0?)

* g.superior: X=177.0,Y=721.5 (should be at cap-height 720?)

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

* h.superior: X=172.5,Y=718.5 (should be at cap-height 720?)

* n (U+006E): X=282.0,Y=498.0 (should be at x-height 500?)

* oe (U+0153): X=333.0,Y=1.0 (should be at baseline 0?)

* p.small: X=175.5,Y=-1.5 (should be at baseline 0?)

* p.superior: X=175.5,Y=721.5 (should be at cap-height 720?)

* q.small: X=181.5,Y=-1.5 (should be at baseline 0?)

* q.superior: X=181.5,Y=721.5 (should be at cap-height 720?)

* u (U+0075): X=278.0,Y=2.0 (should be at baseline 0?)

* u.small: X=170.0,Y=1.5 (should be at baseline 0?)

* u.sub: X=137.5,Y=-2.0 (should be at baseline 0?)

* u.sub: X=190.5,Y=-2.0 (should be at baseline 0?)

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

* uni2091 (U+2091): X=217.0,Y=-1.5 (should be at baseline 0?)

* uni2094 (U+2094): X=106.5,Y=1.0 (should be at baseline 0?)

* uni207F (U+207F): X=172.5,Y=718.5 (should be at cap-height 720?)

* uni0407 (U+0407): X=196.0,Y=958.0 (should be at ascender 960?)

* uni0407 (U+0407): X=74.0,Y=958.0 (should be at ascender 960?)

* uni0431 (U+0431): X=295.0,Y=718.0 (should be at cap-height 720?)

* uni0431.loclSRB: X=302.0,Y=719.0 (should be at cap-height 720?)

* uni0438.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni0439.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=786.0,Y=-1.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=671.0,Y=-1.0 (should be at baseline 0?)

* uni03BC (U+03BC): X=278.0,Y=2.0 (should be at baseline 0?)

* uni2085 (U+2085): X=221.0,Y=-2.0 (should be at baseline 0?)

* uni2086 (U+2086): X=236.0,Y=0.5 (should be at baseline 0?)

* uni2086 (U+2086): X=157.5,Y=0.5 (should be at baseline 0?)

* uni2079 (U+2079): X=147.0,Y=721.5 (should be at cap-height 720?)

* uni2079 (U+2079): X=225.5,Y=721.5 (should be at cap-height 720?)

* uni208D (U+208D): X=53.0,Y=0.5 (should be at baseline 0?)

* uni208E (U+208E): X=147.0,Y=0.5 (should be at baseline 0?)

* braceleft.case: X=302.0,Y=722.0 (should be at cap-height 720?)

* braceright.case: X=98.0,Y=722.0 (should be at cap-height 720?)

* uni207D (U+207D): X=53.0,Y=718.5 (should be at cap-height 720?)

* uni207E (U+207E): X=147.0,Y=718.5 (should be at cap-height 720?)

* uni00B5 (U+00B5): X=278.0,Y=2.0 (should be at baseline 0?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=76.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;426.0,240.0&gt;--&lt;410.0,487.0&gt;&gt; -&gt; L&lt;&lt;410.0,487.0&gt;--&lt;410.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;550.0,720.0&gt;--&lt;550.0,487.0&gt;&gt; -&gt; L&lt;&lt;550.0,487.0&gt;--&lt;534.0,240.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;214.0,261.0&gt;--&lt;230.0,14.0&gt;&gt; -&gt; L&lt;&lt;230.0,14.0&gt;--&lt;230.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;90.0,-219.0&gt;--&lt;90.0,14.0&gt;&gt; -&gt; L&lt;&lt;90.0,14.0&gt;--&lt;106.0,261.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;626.0,240.0&gt;--&lt;610.0,487.0&gt;&gt; -&gt; L&lt;&lt;610.0,487.0&gt;--&lt;610.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;750.0,720.0&gt;--&lt;750.0,487.0&gt;&gt; -&gt; L&lt;&lt;750.0,487.0&gt;--&lt;734.0,240.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;205.0,720.0&gt;--&lt;205.0,580.0&gt;&gt; -&gt; L&lt;&lt;205.0,580.0&gt;--&lt;205.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;55.0,240.0&gt;--&lt;55.0,580.0&gt;&gt; -&gt; L&lt;&lt;55.0,580.0&gt;--&lt;55.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;178.0,720.0&gt;--&lt;178.0,620.0&gt;&gt; -&gt; L&lt;&lt;178.0,620.0&gt;--&lt;178.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;36.0,380.0&gt;--&lt;36.0,620.0&gt;&gt; -&gt; L&lt;&lt;36.0,620.0&gt;--&lt;36.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* three.dnom: B&lt;&lt;273.0,227.0&gt;-&lt;255.0,214.0&gt;-&lt;230.0,210.0&gt;&gt;/B&lt;&lt;230.0,210.0&gt;-&lt;255.0,208.0&gt;-&lt;275.5,194.0&gt;&gt; = 13.664198180723144

* three.numr: B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* three.small: B&lt;&lt;300.5,250.0&gt;-&lt;281.0,236.0&gt;-&lt;253.0,231.0&gt;&gt;/B&lt;&lt;253.0,231.0&gt;-&lt;281.0,229.0&gt;-&lt;303.5,213.5&gt;&gt; = 14.210288435372686

* threeeighths (U+215C): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* threequarters (U+00BE): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* uni00B3 (U+00B3): B&lt;&lt;300.5,610.0&gt;-&lt;281.0,596.0&gt;-&lt;253.0,591.0&gt;&gt;/B&lt;&lt;253.0,591.0&gt;-&lt;281.0,589.0&gt;-&lt;303.5,573.5&gt;&gt; = 14.210288435372686

* uni2083 (U+2083): B&lt;&lt;300.5,170.0&gt;-&lt;281.0,156.0&gt;-&lt;253.0,151.0&gt;&gt;/B&lt;&lt;253.0,151.0&gt;-&lt;281.0,149.0&gt;-&lt;303.5,133.5&gt;&gt; = 14.210288435372686

* uni2153 (U+2153): B&lt;&lt;717.0,227.0&gt;-&lt;699.0,214.0&gt;-&lt;674.0,210.0&gt;&gt;/B&lt;&lt;674.0,210.0&gt;-&lt;699.0,208.0&gt;-&lt;719.5,194.0&gt;&gt; = 13.664198180723144

* uni2154 (U+2154): B&lt;&lt;795.0,227.0&gt;-&lt;777.0,214.0&gt;-&lt;752.0,210.0&gt;&gt;/B&lt;&lt;752.0,210.0&gt;-&lt;777.0,208.0&gt;-&lt;797.5,194.0&gt;&gt; = 13.664198180723144

* uni2157 (U+2157): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* uni2189 (U+2189): B&lt;&lt;817.0,227.0&gt;-&lt;799.0,214.0&gt;-&lt;774.0,210.0&gt;&gt;/B&lt;&lt;774.0,210.0&gt;-&lt;799.0,208.0&gt;-&lt;819.5,194.0&gt;&gt; = 13.664198180723144

* uni2462 (U+2462): B&lt;&lt;527.0,387.0&gt;-&lt;509.0,374.0&gt;-&lt;484.0,370.0&gt;&gt;/B&lt;&lt;484.0,370.0&gt;-&lt;509.0,368.0&gt;-&lt;529.5,354.0&gt;&gt; = 13.664198180723144

* uni2778 (U+2778): B&lt;&lt;527.0,387.0&gt;-&lt;509.0,374.0&gt;-&lt;484.0,370.0&gt;&gt;/B&lt;&lt;484.0,370.0&gt;-&lt;509.0,368.0&gt;-&lt;529.5,354.0&gt;&gt; = 13.664198180723144
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* a.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

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

* f_f_j contains a short segment L&lt;&lt;701.0,-86.0&gt;--&lt;730.0,-86.0&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;340.0,310.0&gt;--&lt;346.0,310.0&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* ampersand (U+0026) contains a short segment B&lt;&lt;226.0,545.0&gt;-&lt;226.0,529.0&gt;-&lt;232.5,514.5&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[22] Akt-ExtraBold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni0436.loclBGR: L&lt;&lt;467.0,0.0&gt;--&lt;325.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;500.0,0.0&gt;--&lt;360.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;196.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;192.0,0.0&gt;--&lt;56.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;244.0,0.0&gt;--&lt;104.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;498.0,0.0&gt;--&lt;356.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
<pre><code>* Aring (U+00C5): X=239.5,Y=959.5 (should be at ascender 960?)

* Aring (U+00C5): X=420.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=239.5,Y=959.5 (should be at ascender 960?)

* Aringacute (U+01FA): X=420.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=249.5,Y=959.5 (should be at ascender 960?)

* Uring (U+016E): X=430.5,Y=959.5 (should be at ascender 960?)

* b.small: X=175.5,Y=-1.5 (should be at baseline 0?)

* c.sub: X=207.5,Y=-0.5 (should be at baseline 0?)

* d.small: X=181.5,Y=-1.5 (should be at baseline 0?)

* f (U+0066): X=98.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=240.0,Y=2.0 (should be at baseline 0?)

* f (U+0066): X=98.0,Y=2.0 (should be at baseline 0?)

* f.small: X=60.0,Y=1.0 (should be at baseline 0?)

* f.small: X=147.0,Y=1.0 (should be at baseline 0?)

* f.small: X=60.0,Y=1.0 (should be at baseline 0?)

* g.small: X=143.0,Y=2.0 (should be at baseline 0?)

* g.superior: X=177.0,Y=721.5 (should be at cap-height 720?)

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

* h.superior: X=172.5,Y=718.5 (should be at cap-height 720?)

* n (U+006E): X=282.0,Y=498.0 (should be at x-height 500?)

* oe (U+0153): X=333.0,Y=1.0 (should be at baseline 0?)

* p.small: X=175.5,Y=-1.5 (should be at baseline 0?)

* p.superior: X=175.5,Y=721.5 (should be at cap-height 720?)

* q.small: X=181.5,Y=-1.5 (should be at baseline 0?)

* q.superior: X=181.5,Y=721.5 (should be at cap-height 720?)

* u (U+0075): X=278.0,Y=2.0 (should be at baseline 0?)

* u.small: X=170.0,Y=1.5 (should be at baseline 0?)

* u.sub: X=137.5,Y=-2.0 (should be at baseline 0?)

* u.sub: X=190.5,Y=-2.0 (should be at baseline 0?)

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

* uni2091 (U+2091): X=217.0,Y=-1.5 (should be at baseline 0?)

* uni2094 (U+2094): X=106.5,Y=1.0 (should be at baseline 0?)

* uni207F (U+207F): X=172.5,Y=718.5 (should be at cap-height 720?)

* uni0407 (U+0407): X=196.0,Y=958.0 (should be at ascender 960?)

* uni0407 (U+0407): X=74.0,Y=958.0 (should be at ascender 960?)

* uni0431 (U+0431): X=295.0,Y=718.0 (should be at cap-height 720?)

* uni0431.loclSRB: X=302.0,Y=719.0 (should be at cap-height 720?)

* uni0438.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni0439.loclBGR: X=278.0,Y=2.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=786.0,Y=-1.0 (should be at baseline 0?)

* uni04A9 (U+04A9): X=671.0,Y=-1.0 (should be at baseline 0?)

* uni03BC (U+03BC): X=278.0,Y=2.0 (should be at baseline 0?)

* uni2085 (U+2085): X=221.0,Y=-2.0 (should be at baseline 0?)

* uni2086 (U+2086): X=236.0,Y=0.5 (should be at baseline 0?)

* uni2086 (U+2086): X=157.5,Y=0.5 (should be at baseline 0?)

* uni2079 (U+2079): X=147.0,Y=721.5 (should be at cap-height 720?)

* uni2079 (U+2079): X=225.5,Y=721.5 (should be at cap-height 720?)

* uni208D (U+208D): X=53.0,Y=0.5 (should be at baseline 0?)

* uni208E (U+208E): X=147.0,Y=0.5 (should be at baseline 0?)

* braceleft.case: X=302.0,Y=722.0 (should be at cap-height 720?)

* braceright.case: X=98.0,Y=722.0 (should be at cap-height 720?)

* uni207D (U+207D): X=53.0,Y=718.5 (should be at cap-height 720?)

* uni207E (U+207E): X=147.0,Y=718.5 (should be at cap-height 720?)

* uni00B5 (U+00B5): X=278.0,Y=2.0 (should be at baseline 0?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=76.0,Y=721.0 (should be at cap-height 720?)

* uni0312 (U+0312): X=196.0,Y=721.0 (should be at cap-height 720?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;426.0,240.0&gt;--&lt;410.0,487.0&gt;&gt; -&gt; L&lt;&lt;410.0,487.0&gt;--&lt;410.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;550.0,720.0&gt;--&lt;550.0,487.0&gt;&gt; -&gt; L&lt;&lt;550.0,487.0&gt;--&lt;534.0,240.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;214.0,261.0&gt;--&lt;230.0,14.0&gt;&gt; -&gt; L&lt;&lt;230.0,14.0&gt;--&lt;230.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;90.0,-219.0&gt;--&lt;90.0,14.0&gt;&gt; -&gt; L&lt;&lt;90.0,14.0&gt;--&lt;106.0,261.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;626.0,240.0&gt;--&lt;610.0,487.0&gt;&gt; -&gt; L&lt;&lt;610.0,487.0&gt;--&lt;610.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;750.0,720.0&gt;--&lt;750.0,487.0&gt;&gt; -&gt; L&lt;&lt;750.0,487.0&gt;--&lt;734.0,240.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;106.0,240.0&gt;--&lt;90.0,487.0&gt;&gt; -&gt; L&lt;&lt;90.0,487.0&gt;--&lt;90.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;230.0,720.0&gt;--&lt;230.0,487.0&gt;&gt; -&gt; L&lt;&lt;230.0,487.0&gt;--&lt;214.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;205.0,720.0&gt;--&lt;205.0,580.0&gt;&gt; -&gt; L&lt;&lt;205.0,580.0&gt;--&lt;205.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;55.0,240.0&gt;--&lt;55.0,580.0&gt;&gt; -&gt; L&lt;&lt;55.0,580.0&gt;--&lt;55.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;178.0,720.0&gt;--&lt;178.0,620.0&gt;&gt; -&gt; L&lt;&lt;178.0,620.0&gt;--&lt;178.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;36.0,380.0&gt;--&lt;36.0,620.0&gt;&gt; -&gt; L&lt;&lt;36.0,620.0&gt;--&lt;36.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* three.dnom: B&lt;&lt;273.0,227.0&gt;-&lt;255.0,214.0&gt;-&lt;230.0,210.0&gt;&gt;/B&lt;&lt;230.0,210.0&gt;-&lt;255.0,208.0&gt;-&lt;275.5,194.0&gt;&gt; = 13.664198180723144

* three.numr: B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* three.small: B&lt;&lt;300.5,250.0&gt;-&lt;281.0,236.0&gt;-&lt;253.0,231.0&gt;&gt;/B&lt;&lt;253.0,231.0&gt;-&lt;281.0,229.0&gt;-&lt;303.5,213.5&gt;&gt; = 14.210288435372686

* threeeighths (U+215C): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* threequarters (U+00BE): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* uni00B3 (U+00B3): B&lt;&lt;300.5,610.0&gt;-&lt;281.0,596.0&gt;-&lt;253.0,591.0&gt;&gt;/B&lt;&lt;253.0,591.0&gt;-&lt;281.0,589.0&gt;-&lt;303.5,573.5&gt;&gt; = 14.210288435372686

* uni2083 (U+2083): B&lt;&lt;300.5,170.0&gt;-&lt;281.0,156.0&gt;-&lt;253.0,151.0&gt;&gt;/B&lt;&lt;253.0,151.0&gt;-&lt;281.0,149.0&gt;-&lt;303.5,133.5&gt;&gt; = 14.210288435372686

* uni2153 (U+2153): B&lt;&lt;717.0,227.0&gt;-&lt;699.0,214.0&gt;-&lt;674.0,210.0&gt;&gt;/B&lt;&lt;674.0,210.0&gt;-&lt;699.0,208.0&gt;-&lt;719.5,194.0&gt;&gt; = 13.664198180723144

* uni2154 (U+2154): B&lt;&lt;795.0,227.0&gt;-&lt;777.0,214.0&gt;-&lt;752.0,210.0&gt;&gt;/B&lt;&lt;752.0,210.0&gt;-&lt;777.0,208.0&gt;-&lt;797.5,194.0&gt;&gt; = 13.664198180723144

* uni2157 (U+2157): B&lt;&lt;273.0,547.0&gt;-&lt;255.0,534.0&gt;-&lt;230.0,530.0&gt;&gt;/B&lt;&lt;230.0,530.0&gt;-&lt;255.0,528.0&gt;-&lt;275.5,514.0&gt;&gt; = 13.664198180723144

* uni2189 (U+2189): B&lt;&lt;817.0,227.0&gt;-&lt;799.0,214.0&gt;-&lt;774.0,210.0&gt;&gt;/B&lt;&lt;774.0,210.0&gt;-&lt;799.0,208.0&gt;-&lt;819.5,194.0&gt;&gt; = 13.664198180723144

* uni2462 (U+2462): B&lt;&lt;527.0,387.0&gt;-&lt;509.0,374.0&gt;-&lt;484.0,370.0&gt;&gt;/B&lt;&lt;484.0,370.0&gt;-&lt;509.0,368.0&gt;-&lt;529.5,354.0&gt;&gt; = 13.664198180723144

* uni2778 (U+2778): B&lt;&lt;527.0,387.0&gt;-&lt;509.0,374.0&gt;-&lt;484.0,370.0&gt;&gt;/B&lt;&lt;484.0,370.0&gt;-&lt;509.0,368.0&gt;-&lt;529.5,354.0&gt;&gt; = 13.664198180723144
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* a.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

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

* f_f_j contains a short segment L&lt;&lt;701.0,-86.0&gt;--&lt;730.0,-86.0&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni0430.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;340.0,310.0&gt;--&lt;346.0,310.0&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D1.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;466.0,134.0&gt;-&lt;466.0,123.0&gt;-&lt;470.5,118.5&gt;&gt;

* uni04D3.ss01 contains a short segment B&lt;&lt;470.5,118.5&gt;-&lt;475.0,114.0&gt;-&lt;486.0,114.0&gt;&gt;

* ampersand (U+0026) contains a short segment B&lt;&lt;226.0,545.0&gt;-&lt;226.0,529.0&gt;-&lt;232.5,514.5&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[23] Akt-ExtraLight.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni040B (U+040B): L&lt;&lt;284.0,0.0&gt;--&lt;227.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;568.0,0.0&gt;--&lt;511.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;423.0,0.0&gt;--&lt;369.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;457.0,0.0&gt;--&lt;403.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;142.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;141.0,0.0&gt;--&lt;87.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;193.0,0.0&gt;--&lt;138.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;442.0,0.0&gt;--&lt;387.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
<pre><code>* b.small: X=147.0,Y=2.0 (should be at baseline 0?)

* b.sub: X=276.0,Y=1.5 (should be at baseline 0?)

* b.sub: X=98.5,Y=1.5 (should be at baseline 0?)

* c.sub: X=80.5,Y=1.0 (should be at baseline 0?)

* d.small: X=210.5,Y=2.0 (should be at baseline 0?)

* d.sub: X=258.5,Y=1.5 (should be at baseline 0?)

* d.sub: X=81.0,Y=1.5 (should be at baseline 0?)

* f (U+0066): X=135.0,Y=1.0 (should be at baseline 0?)

* f (U+0066): X=190.0,Y=1.0 (should be at baseline 0?)

* f (U+0066): X=135.0,Y=1.0 (should be at baseline 0?)

* g.sub: X=264.0,Y=-1.0 (should be at baseline 0?)

* g.sub: X=48.5,Y=-0.5 (should be at baseline 0?)

* p.small: X=147.0,Y=2.0 (should be at baseline 0?)

* p.superior: X=147.0,Y=718.0 (should be at cap-height 720?)

* q.small: X=210.5,Y=2.0 (should be at baseline 0?)

* q.sub: X=81.0,Y=1.5 (should be at baseline 0?)

* q.sub: X=258.5,Y=1.5 (should be at baseline 0?)

* q.superior: X=210.5,Y=718.0 (should be at cap-height 720?)

* y.small: X=141.0,Y=-2.0 (should be at baseline 0?)

* uni2090 (U+2090): X=30.0,Y=1.0 (should be at baseline 0?)

* uni2090 (U+2090): X=266.0,Y=2.0 (should be at baseline 0?)

* uni2091 (U+2091): X=79.5,Y=-1.0 (should be at baseline 0?)

* uni2092 (U+2092): X=262.0,Y=1.5 (should be at baseline 0?)

* uni2092 (U+2092): X=81.0,Y=1.5 (should be at baseline 0?)

* uni0494 (U+0494): X=482.5,Y=0.5 (should be at baseline 0?)

* uni0494.ss02: X=482.5,Y=0.5 (should be at baseline 0?)

* uni0416 (U+0416): X=472.0,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=528.0,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=43.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=105.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=895.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=957.0,Y=719.0 (should be at cap-height 720?)

* uni0402 (U+0402): X=680.0,Y=0.5 (should be at baseline 0?)

* uni0496 (U+0496): X=472.0,Y=721.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=528.0,Y=721.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=43.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=105.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=895.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=957.0,Y=719.0 (should be at cap-height 720?)

* uni04A6 (U+04A6): X=886.5,Y=0.5 (should be at baseline 0?)

* uni04C1 (U+04C1): X=472.0,Y=721.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=528.0,Y=721.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=43.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=105.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=895.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=957.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=472.0,Y=721.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=528.0,Y=721.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=43.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=105.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=895.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=957.0,Y=719.0 (should be at cap-height 720?)

* uni0431 (U+0431): X=297.0,Y=719.0 (should be at cap-height 720?)

* uni0431.loclSRB: X=212.0,Y=718.0 (should be at cap-height 720?)

* uni04FD (U+04FD): X=490.0,Y=1.5 (should be at baseline 0?)

* delta (U+03B4): X=235.0,Y=718.0 (should be at cap-height 720?)

* uni209A (U+209A): X=98.5,Y=1.5 (should be at baseline 0?)

* uni209A (U+209A): X=276.0,Y=1.5 (should be at baseline 0?)

* uni209B (U+209B): X=267.0,Y=1.0 (should be at baseline 0?)

* uni2085 (U+2085): X=278.5,Y=-0.5 (should be at baseline 0?)

* uni2086 (U+2086): X=294.5,Y=-1.0 (should be at baseline 0?)

* uni2086 (U+2086): X=94.0,Y=-0.5 (should be at baseline 0?)

* braceleft.case: X=259.5,Y=721.5 (should be at cap-height 720?)

* braceright.case: X=140.5,Y=721.5 (should be at cap-height 720?)

* quotedblright (U+201D): X=160.0,Y=719.0 (should be at cap-height 720?)

* quotedblright (U+201D): X=400.0,Y=719.0 (should be at cap-height 720?)

* paunch1: X=354.5,Y=0.5 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;137.0,183.0&gt;--&lt;133.0,311.0&gt;&gt; -&gt; L&lt;&lt;133.0,311.0&gt;--&lt;133.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;187.0,720.0&gt;--&lt;187.0,311.0&gt;&gt; -&gt; L&lt;&lt;187.0,311.0&gt;--&lt;183.0,183.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;137.0,183.0&gt;--&lt;133.0,311.0&gt;&gt; -&gt; L&lt;&lt;133.0,311.0&gt;--&lt;133.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;187.0,720.0&gt;--&lt;187.0,311.0&gt;&gt; -&gt; L&lt;&lt;187.0,311.0&gt;--&lt;183.0,183.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;457.0,183.0&gt;--&lt;453.0,311.0&gt;&gt; -&gt; L&lt;&lt;453.0,311.0&gt;--&lt;453.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;507.0,720.0&gt;--&lt;507.0,311.0&gt;&gt; -&gt; L&lt;&lt;507.0,311.0&gt;--&lt;503.0,183.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;133.0,-220.0&gt;--&lt;133.0,190.0&gt;&gt; -&gt; L&lt;&lt;133.0,190.0&gt;--&lt;137.0,317.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;183.0,317.0&gt;--&lt;187.0,190.0&gt;&gt; -&gt; L&lt;&lt;187.0,190.0&gt;--&lt;187.0,-220.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;657.0,183.0&gt;--&lt;653.0,311.0&gt;&gt; -&gt; L&lt;&lt;653.0,311.0&gt;--&lt;653.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;707.0,720.0&gt;--&lt;707.0,311.0&gt;&gt; -&gt; L&lt;&lt;707.0,311.0&gt;--&lt;703.0,183.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;137.0,183.0&gt;--&lt;133.0,311.0&gt;&gt; -&gt; L&lt;&lt;133.0,311.0&gt;--&lt;133.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;187.0,720.0&gt;--&lt;187.0,311.0&gt;&gt; -&gt; L&lt;&lt;187.0,311.0&gt;--&lt;183.0,183.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;101.0,240.0&gt;--&lt;101.0,580.0&gt;&gt; -&gt; L&lt;&lt;101.0,580.0&gt;--&lt;101.0,720.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;159.0,720.0&gt;--&lt;159.0,580.0&gt;&gt; -&gt; L&lt;&lt;159.0,580.0&gt;--&lt;159.0,240.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;134.0,720.0&gt;--&lt;134.0,620.0&gt;&gt; -&gt; L&lt;&lt;134.0,620.0&gt;--&lt;134.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;80.0,380.0&gt;--&lt;80.0,620.0&gt;&gt; -&gt; L&lt;&lt;80.0,620.0&gt;--&lt;80.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* eth (U+00F0): B&lt;&lt;422.0,427.0&gt;-&lt;443.0,401.0&gt;-&lt;448.0,381.0&gt;&gt;/B&lt;&lt;448.0,381.0&gt;-&lt;438.0,506.0&gt;-&lt;409.5,562.5&gt;&gt; = 9.462322208025613

* partialdiff (U+2202): B&lt;&lt;422.0,427.0&gt;-&lt;443.0,401.0&gt;-&lt;448.0,381.0&gt;&gt;/B&lt;&lt;448.0,381.0&gt;-&lt;438.0,506.0&gt;-&lt;409.5,562.5&gt;&gt; = 9.462322208025613

* three.dnom: B&lt;&lt;254.5,224.0&gt;-&lt;236.0,211.0&gt;-&lt;215.0,207.0&gt;&gt;/B&lt;&lt;215.0,207.0&gt;-&lt;232.0,206.0&gt;-&lt;253.5,194.5&gt;&gt; = 14.150758530992416

* three.numr: B&lt;&lt;254.5,544.0&gt;-&lt;236.0,531.0&gt;-&lt;215.0,527.0&gt;&gt;/B&lt;&lt;215.0,527.0&gt;-&lt;232.0,526.0&gt;-&lt;253.5,514.5&gt;&gt; = 14.150758530992416

* threeeighths (U+215C): B&lt;&lt;254.5,544.0&gt;-&lt;236.0,531.0&gt;-&lt;215.0,527.0&gt;&gt;/B&lt;&lt;215.0,527.0&gt;-&lt;232.0,526.0&gt;-&lt;253.5,514.5&gt;&gt; = 14.150758530992416

* threequarters (U+00BE): B&lt;&lt;254.5,544.0&gt;-&lt;236.0,531.0&gt;-&lt;215.0,527.0&gt;&gt;/B&lt;&lt;215.0,527.0&gt;-&lt;232.0,526.0&gt;-&lt;253.5,514.5&gt;&gt; = 14.150758530992416

* uni0431 (U+0431): B&lt;&lt;132.5,543.0&gt;-&lt;115.0,490.0&gt;-&lt;109.0,377.0&gt;&gt;/B&lt;&lt;109.0,377.0&gt;-&lt;117.0,407.0&gt;-&lt;142.0,436.5&gt;&gt; = 11.892017609210653

* uni0431.ss01: B&lt;&lt;130.0,536.0&gt;-&lt;114.0,481.0&gt;-&lt;109.0,377.0&gt;&gt;/B&lt;&lt;109.0,377.0&gt;-&lt;117.0,407.0&gt;-&lt;142.0,436.5&gt;&gt; = 12.178931777868874

* uni2153 (U+2153): B&lt;&lt;698.5,224.0&gt;-&lt;680.0,211.0&gt;-&lt;659.0,207.0&gt;&gt;/B&lt;&lt;659.0,207.0&gt;-&lt;676.0,206.0&gt;-&lt;697.5,194.5&gt;&gt; = 14.150758530992416

* uni2154 (U+2154): B&lt;&lt;776.5,224.0&gt;-&lt;758.0,211.0&gt;-&lt;737.0,207.0&gt;&gt;/B&lt;&lt;737.0,207.0&gt;-&lt;754.0,206.0&gt;-&lt;775.5,194.5&gt;&gt; = 14.150758530992416

* uni2157 (U+2157): B&lt;&lt;254.5,544.0&gt;-&lt;236.0,531.0&gt;-&lt;215.0,527.0&gt;&gt;/B&lt;&lt;215.0,527.0&gt;-&lt;232.0,526.0&gt;-&lt;253.5,514.5&gt;&gt; = 14.150758530992416

* uni2189 (U+2189): B&lt;&lt;798.5,224.0&gt;-&lt;780.0,211.0&gt;-&lt;759.0,207.0&gt;&gt;/B&lt;&lt;759.0,207.0&gt;-&lt;776.0,206.0&gt;-&lt;797.5,194.5&gt;&gt; = 14.150758530992416

* uni2462 (U+2462): B&lt;&lt;508.5,384.0&gt;-&lt;490.0,371.0&gt;-&lt;469.0,367.0&gt;&gt;/B&lt;&lt;469.0,367.0&gt;-&lt;486.0,366.0&gt;-&lt;507.5,354.5&gt;&gt; = 14.150758530992416

* uni2778 (U+2778): B&lt;&lt;508.5,384.0&gt;-&lt;490.0,371.0&gt;-&lt;469.0,367.0&gt;&gt;/B&lt;&lt;469.0,367.0&gt;-&lt;486.0,366.0&gt;-&lt;507.5,354.5&gt;&gt; = 14.150758530992416
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-semi-vertical">outline_semi_vertical</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* uni0459 (U+0459): L&lt;&lt;148.0,329.0&gt;--&lt;149.0,500.0&gt;&gt;

* uni0459 (U+0459): L&lt;&lt;200.0,449.0&gt;--&lt;199.0,321.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* G (U+0047) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gbreve (U+011E) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gcaron (U+01E6) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gcircumflex (U+011C) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni0122 (U+0122) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* Gdotaccent (U+0120) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni1E20 (U+1E20) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* uni01E4 (U+01E4) contains a short segment B&lt;&lt;675.0,373.0&gt;-&lt;677.0,365.0&gt;-&lt;677.0,350.0&gt;&gt;

* f_f_i contains a short segment L&lt;&lt;323.0,674.0&gt;--&lt;291.0,674.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;726.0,-153.0&gt;--&lt;740.0,-153.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;323.0,674.0&gt;--&lt;291.0,674.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;323.0,674.0&gt;--&lt;291.0,674.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;386.0,-153.0&gt;--&lt;400.0,-153.0&gt;&gt;

* uni0431.ss01 contains a short segment L&lt;&lt;488.0,760.0&gt;--&lt;488.0,746.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[22] Akt-Light.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni0436.loclBGR: L&lt;&lt;432.0,0.0&gt;--&lt;360.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;466.0,0.0&gt;--&lt;394.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;153.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;151.0,0.0&gt;--&lt;81.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;203.0,0.0&gt;--&lt;131.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;453.0,0.0&gt;--&lt;381.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;131.0,194.0&gt;--&lt;124.0,346.0&gt;&gt; -&gt; L&lt;&lt;124.0,346.0&gt;--&lt;124.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,346.0&gt;&gt; -&gt; L&lt;&lt;196.0,346.0&gt;--&lt;189.0,194.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;131.0,194.0&gt;--&lt;124.0,346.0&gt;&gt; -&gt; L&lt;&lt;124.0,346.0&gt;--&lt;124.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,346.0&gt;&gt; -&gt; L&lt;&lt;196.0,346.0&gt;--&lt;189.0,194.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;451.0,194.0&gt;--&lt;444.0,346.0&gt;&gt; -&gt; L&lt;&lt;444.0,346.0&gt;--&lt;444.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;516.0,720.0&gt;--&lt;516.0,346.0&gt;&gt; -&gt; L&lt;&lt;516.0,346.0&gt;--&lt;509.0,194.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;124.0,-220.0&gt;--&lt;124.0,155.0&gt;&gt; -&gt; L&lt;&lt;124.0,155.0&gt;--&lt;131.0,306.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;189.0,306.0&gt;--&lt;196.0,155.0&gt;&gt; -&gt; L&lt;&lt;196.0,155.0&gt;--&lt;196.0,-220.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;651.0,194.0&gt;--&lt;644.0,346.0&gt;&gt; -&gt; L&lt;&lt;644.0,346.0&gt;--&lt;644.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;716.0,720.0&gt;--&lt;716.0,346.0&gt;&gt; -&gt; L&lt;&lt;716.0,346.0&gt;--&lt;709.0,194.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;131.0,194.0&gt;--&lt;124.0,346.0&gt;&gt; -&gt; L&lt;&lt;124.0,346.0&gt;--&lt;124.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,346.0&gt;&gt; -&gt; L&lt;&lt;196.0,346.0&gt;--&lt;189.0,194.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;168.0,720.0&gt;--&lt;168.0,580.0&gt;&gt; -&gt; L&lt;&lt;168.0,580.0&gt;--&lt;168.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;92.0,240.0&gt;--&lt;92.0,580.0&gt;&gt; -&gt; L&lt;&lt;92.0,580.0&gt;--&lt;92.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;143.0,720.0&gt;--&lt;143.0,620.0&gt;&gt; -&gt; L&lt;&lt;143.0,620.0&gt;--&lt;143.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;71.0,380.0&gt;--&lt;71.0,620.0&gt;&gt; -&gt; L&lt;&lt;71.0,620.0&gt;--&lt;71.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







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







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* uni0459 (U+0459): L&lt;&lt;139.0,333.0&gt;--&lt;140.0,500.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* f_f_j contains a short segment L&lt;&lt;721.0,-140.0&gt;--&lt;738.0,-140.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;327.0,661.0&gt;--&lt;290.0,661.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;327.0,661.0&gt;--&lt;290.0,661.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;381.0,-140.0&gt;--&lt;398.0,-140.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[20] Akt-Medium.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni040B (U+040B): L&lt;&lt;320.0,0.0&gt;--&lt;207.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;604.0,0.0&gt;--&lt;491.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;450.0,0.0&gt;--&lt;342.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;483.0,0.0&gt;--&lt;377.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;174.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;174.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;171.0,0.0&gt;--&lt;69.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;223.0,0.0&gt;--&lt;118.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;476.0,0.0&gt;--&lt;369.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;119.0,217.0&gt;--&lt;107.0,416.0&gt;&gt; -&gt; L&lt;&lt;107.0,416.0&gt;--&lt;107.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;213.0,720.0&gt;--&lt;213.0,416.0&gt;&gt; -&gt; L&lt;&lt;213.0,416.0&gt;--&lt;201.0,217.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;119.0,217.0&gt;--&lt;107.0,416.0&gt;&gt; -&gt; L&lt;&lt;107.0,416.0&gt;--&lt;107.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;213.0,720.0&gt;--&lt;213.0,416.0&gt;&gt; -&gt; L&lt;&lt;213.0,416.0&gt;--&lt;201.0,217.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;439.0,217.0&gt;--&lt;427.0,416.0&gt;&gt; -&gt; L&lt;&lt;427.0,416.0&gt;--&lt;427.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;533.0,720.0&gt;--&lt;533.0,416.0&gt;&gt; -&gt; L&lt;&lt;533.0,416.0&gt;--&lt;521.0,217.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;107.0,-219.0&gt;--&lt;107.0,84.0&gt;&gt; -&gt; L&lt;&lt;107.0,84.0&gt;--&lt;119.0,284.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;201.0,284.0&gt;--&lt;213.0,84.0&gt;&gt; -&gt; L&lt;&lt;213.0,84.0&gt;--&lt;213.0,-219.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;639.0,217.0&gt;--&lt;627.0,416.0&gt;&gt; -&gt; L&lt;&lt;627.0,416.0&gt;--&lt;627.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;733.0,720.0&gt;--&lt;733.0,416.0&gt;&gt; -&gt; L&lt;&lt;733.0,416.0&gt;--&lt;721.0,217.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;119.0,217.0&gt;--&lt;107.0,416.0&gt;&gt; -&gt; L&lt;&lt;107.0,416.0&gt;--&lt;107.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;213.0,720.0&gt;--&lt;213.0,416.0&gt;&gt; -&gt; L&lt;&lt;213.0,416.0&gt;--&lt;201.0,217.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;186.0,720.0&gt;--&lt;186.0,580.0&gt;&gt; -&gt; L&lt;&lt;186.0,580.0&gt;--&lt;186.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;74.0,240.0&gt;--&lt;74.0,580.0&gt;&gt; -&gt; L&lt;&lt;74.0,580.0&gt;--&lt;74.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;161.0,720.0&gt;--&lt;161.0,620.0&gt;&gt; -&gt; L&lt;&lt;161.0,620.0&gt;--&lt;161.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;53.0,380.0&gt;--&lt;53.0,620.0&gt;&gt; -&gt; L&lt;&lt;53.0,620.0&gt;--&lt;53.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* f_f_j contains a short segment L&lt;&lt;711.0,-113.0&gt;--&lt;734.0,-113.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;371.0,-113.0&gt;--&lt;394.0,-113.0&gt;&gt;

* uni0497.ss01 contains a short segment L&lt;&lt;764.0,0.0&gt;--&lt;767.0,0.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[22] Akt-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



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
<td align="left">Akt</td>
<td align="left">Akt</td>
</tr>
<tr>
<td align="left">Subfamily Name</td>
<td align="left">Regular</td>
<td align="left">Regular</td>
</tr>
<tr>
<td align="left">Full Name</td>
<td align="left">Akt Regular</td>
<td align="left">Akt Regular</td>
</tr>
<tr>
<td align="left">Postscript Name</td>
<td align="left">Akt-Regular</td>
<td align="left">Akt-Regular</td>
</tr>
<tr>
<td align="left">Typographic Family Name</td>
<td align="left"><strong>Akt</strong></td>
<td align="left"><strong>N/A</strong></td>
</tr>
</tbody>
</table>
 [code: bad-names]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni0436.loclBGR: L&lt;&lt;441.0,0.0&gt;--&lt;351.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;474.0,0.0&gt;--&lt;386.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;163.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;163.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;161.0,0.0&gt;--&lt;75.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;213.0,0.0&gt;--&lt;125.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;465.0,0.0&gt;--&lt;375.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;125.0,206.0&gt;--&lt;116.0,381.0&gt;&gt; -&gt; L&lt;&lt;116.0,381.0&gt;--&lt;116.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;204.0,720.0&gt;--&lt;204.0,381.0&gt;&gt; -&gt; L&lt;&lt;204.0,381.0&gt;--&lt;195.0,206.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;125.0,206.0&gt;--&lt;116.0,381.0&gt;&gt; -&gt; L&lt;&lt;116.0,381.0&gt;--&lt;116.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;204.0,720.0&gt;--&lt;204.0,381.0&gt;&gt; -&gt; L&lt;&lt;204.0,381.0&gt;--&lt;195.0,206.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;445.0,206.0&gt;--&lt;436.0,381.0&gt;&gt; -&gt; L&lt;&lt;436.0,381.0&gt;--&lt;436.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;524.0,720.0&gt;--&lt;524.0,381.0&gt;&gt; -&gt; L&lt;&lt;524.0,381.0&gt;--&lt;515.0,206.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;116.0,-219.0&gt;--&lt;116.0,119.0&gt;&gt; -&gt; L&lt;&lt;116.0,119.0&gt;--&lt;125.0,295.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;195.0,295.0&gt;--&lt;204.0,119.0&gt;&gt; -&gt; L&lt;&lt;204.0,119.0&gt;--&lt;204.0,-219.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;645.0,206.0&gt;--&lt;636.0,381.0&gt;&gt; -&gt; L&lt;&lt;636.0,381.0&gt;--&lt;636.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;724.0,720.0&gt;--&lt;724.0,381.0&gt;&gt; -&gt; L&lt;&lt;724.0,381.0&gt;--&lt;715.0,206.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;125.0,206.0&gt;--&lt;116.0,381.0&gt;&gt; -&gt; L&lt;&lt;116.0,381.0&gt;--&lt;116.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;204.0,720.0&gt;--&lt;204.0,381.0&gt;&gt; -&gt; L&lt;&lt;204.0,381.0&gt;--&lt;195.0,206.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;177.0,720.0&gt;--&lt;177.0,580.0&gt;&gt; -&gt; L&lt;&lt;177.0,580.0&gt;--&lt;177.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;83.0,240.0&gt;--&lt;83.0,580.0&gt;&gt; -&gt; L&lt;&lt;83.0,580.0&gt;--&lt;83.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;152.0,720.0&gt;--&lt;152.0,620.0&gt;&gt; -&gt; L&lt;&lt;152.0,620.0&gt;--&lt;152.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;62.0,380.0&gt;--&lt;62.0,620.0&gt;&gt; -&gt; L&lt;&lt;62.0,620.0&gt;--&lt;62.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* three.small: B&lt;&lt;288.5,248.5&gt;-&lt;269.0,234.0&gt;-&lt;243.0,230.0&gt;&gt;/B&lt;&lt;243.0,230.0&gt;-&lt;266.0,228.0&gt;-&lt;289.0,214.0&gt;&gt; = 13.71590299066549

* uni00B3 (U+00B3): B&lt;&lt;288.5,608.5&gt;-&lt;269.0,594.0&gt;-&lt;243.0,590.0&gt;&gt;/B&lt;&lt;243.0,590.0&gt;-&lt;266.0,588.0&gt;-&lt;289.0,574.0&gt;&gt; = 13.71590299066549

* uni2083 (U+2083): B&lt;&lt;288.5,168.5&gt;-&lt;269.0,154.0&gt;-&lt;243.0,150.0&gt;&gt;/B&lt;&lt;243.0,150.0&gt;-&lt;266.0,148.0&gt;-&lt;289.0,134.0&gt;&gt; = 13.71590299066549
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* f_f_j contains a short segment L&lt;&lt;716.0,-126.0&gt;--&lt;736.0,-126.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;376.0,-126.0&gt;--&lt;396.0,-126.0&gt;&gt;

* uni049A.ss01 contains a short segment L&lt;&lt;578.0,0.0&gt;--&lt;576.0,0.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[20] Akt-SemiBold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni040B (U+040B): L&lt;&lt;332.0,0.0&gt;--&lt;201.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;616.0,0.0&gt;--&lt;485.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;458.0,0.0&gt;--&lt;334.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;491.0,0.0&gt;--&lt;369.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;185.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;185.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;182.0,0.0&gt;--&lt;62.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni049F.ss01: L&lt;&lt;234.0,0.0&gt;--&lt;111.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A5 (U+04A5): L&lt;&lt;487.0,0.0&gt;--&lt;362.0,0.0&gt;&gt; has the same coordinates as a previous segment.
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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;112.0,229.0&gt;--&lt;99.0,452.0&gt;&gt; -&gt; L&lt;&lt;99.0,452.0&gt;--&lt;99.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;221.0,720.0&gt;--&lt;221.0,452.0&gt;&gt; -&gt; L&lt;&lt;221.0,452.0&gt;--&lt;208.0,229.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;112.0,229.0&gt;--&lt;99.0,452.0&gt;&gt; -&gt; L&lt;&lt;99.0,452.0&gt;--&lt;99.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;221.0,720.0&gt;--&lt;221.0,452.0&gt;&gt; -&gt; L&lt;&lt;221.0,452.0&gt;--&lt;208.0,229.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;432.0,229.0&gt;--&lt;419.0,452.0&gt;&gt; -&gt; L&lt;&lt;419.0,452.0&gt;--&lt;419.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;541.0,720.0&gt;--&lt;541.0,452.0&gt;&gt; -&gt; L&lt;&lt;541.0,452.0&gt;--&lt;528.0,229.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;208.0,272.0&gt;--&lt;221.0,49.0&gt;&gt; -&gt; L&lt;&lt;221.0,49.0&gt;--&lt;221.0,-219.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;99.0,-219.0&gt;--&lt;99.0,49.0&gt;&gt; -&gt; L&lt;&lt;99.0,49.0&gt;--&lt;112.0,272.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;632.0,229.0&gt;--&lt;619.0,452.0&gt;&gt; -&gt; L&lt;&lt;619.0,452.0&gt;--&lt;619.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;741.0,720.0&gt;--&lt;741.0,452.0&gt;&gt; -&gt; L&lt;&lt;741.0,452.0&gt;--&lt;728.0,229.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;112.0,229.0&gt;--&lt;99.0,452.0&gt;&gt; -&gt; L&lt;&lt;99.0,452.0&gt;--&lt;99.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;221.0,720.0&gt;--&lt;221.0,452.0&gt;&gt; -&gt; L&lt;&lt;221.0,452.0&gt;--&lt;208.0,229.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;196.0,720.0&gt;--&lt;196.0,580.0&gt;&gt; -&gt; L&lt;&lt;196.0,580.0&gt;--&lt;196.0,240.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;64.0,240.0&gt;--&lt;64.0,580.0&gt;&gt; -&gt; L&lt;&lt;64.0,580.0&gt;--&lt;64.0,720.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;169.0,720.0&gt;--&lt;169.0,620.0&gt;&gt; -&gt; L&lt;&lt;169.0,620.0&gt;--&lt;169.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;45.0,380.0&gt;--&lt;45.0,620.0&gt;&gt; -&gt; L&lt;&lt;45.0,620.0&gt;--&lt;45.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* f_f_j contains a short segment L&lt;&lt;706.0,-99.0&gt;--&lt;732.0,-99.0&gt;&gt;

* uni049D.ss01 contains a short segment L&lt;&lt;334.0,304.0&gt;--&lt;348.0,304.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[22] Akt-Thin.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> PPEM must be an integer on hinted fonts. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#integer-ppem-if-hinted">integer_ppem_if_hinted</a></summary>
    <div>







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
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0237 when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



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
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian), ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'ї́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian), uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0430 when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0435 when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0451 when shaping the text 'ё́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to dotlessi when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni043E when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0443 when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044B when shaping the text 'ы́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044E when shaping the text 'ю́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian), be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0430 when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni043E when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0443 when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044E when shaping the text 'ю̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian), bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0430 when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0435 when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni043E when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0443 when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian), sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
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
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Edotaccent when shaping the text 'Ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Edotaccent when shaping the text 'Ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Idotaccent when shaping the text 'İ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to Idotaccent when shaping the text 'İ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Idotaccent when shaping the text 'İ̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to M when shaping the text 'M̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Uogonek when shaping the text 'Ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Uogonek when shaping the text 'Ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Umacron when shaping the text 'Ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Umacron when shaping the text 'Ū̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to edotaccent when shaping the text 'ė́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to edotaccent when shaping the text 'ė̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni0307 when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to dotlessi when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0328 when shaping the text 'į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0307 when shaping the text 'į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0328 when shaping the text 'į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0328 to dotlessi when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0328 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0237 when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to uni0237 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uni0307 when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to m when shaping the text 'm̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uogonek when shaping the text 'ų́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to uogonek when shaping the text 'ų̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to umacron when shaping the text 'ū́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to umacron when shaping the text 'ū̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2024, the akt project authors (<a href="https://github.com/grenev/akt">https://github.com/grenev/akt</a>).&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* 🔥 **FAIL** <p>License file OFL.txt exists but NameID 13 (LICENSE DESCRIPTION) value on platform 3 (WINDOWS) is not specified for that. Value was: &quot;openfontlicense.org&quot; Must be changed to &quot;This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: <a href="https://openfontlicense.org">https://openfontlicense.org</a>&quot;</p>
 [code: wrong]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 fsType does not impose restrictions. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-fstype">googlefonts/fstype</a></summary>
    <div>







* 🔥 **FAIL** <p>In this font fsType is set to 8 meaning that:
The font may be embedded but must only be installed temporarily on other systems.</p>
<p>No such DRM restrictions can be enabled on the Google Fonts collection, so the fsType field must be set to zero (Installable Embedding) instead.</p>
 [code: drm]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Version format is correct in 'name' table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-version-format">googlefonts/name/version_format</a></summary>
    <div>







* 🔥 **FAIL** <p>The NameID.VERSION_STRING (nameID=5) value must follow the pattern &quot;Version X.Y&quot; with X.Y greater than or equal to 1.000. The &quot;Version &quot; prefix is a recommendation given by the OpenType spec. Current version string is: &quot;0.3; ttfautohint (v1.8.4.16-eb64)&quot;</p>
 [code: bad-version-strings]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>









* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>tcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

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

- Glyph name: uni1ECB	Contours detected: 2	Expected: 3

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
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 600 among a set of 16 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 820:
propersubset, propersuperset, uni2ABD, uni2ABE</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







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

* uni040B (U+040B): L&lt;&lt;272.0,0.0&gt;--&lt;233.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni04A4 (U+04A4): L&lt;&lt;556.0,0.0&gt;--&lt;517.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR: L&lt;&lt;415.0,0.0&gt;--&lt;377.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni0436.loclBGR.ss01: L&lt;&lt;449.0,0.0&gt;--&lt;411.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR: L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni043A.loclBGR.ss01: L&lt;&lt;131.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni044E.loclBGR: L&lt;&lt;130.0,0.0&gt;--&lt;94.0,0.0&gt;&gt; has the same coordinates as a previous segment.

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

- a.small

- b.small

- b.sub

- c.small

- c.sub

- c.superior

- comma.small

- comma.sub

- comma.superior

- d.small

- d.sub

- e.small

- eight.small

- equal.small

- f.small

- f.sub

- f.superior

- five.small

- four.small

- g.small

- g.sub

- g.superior

- h.small

- h.superior

- hook1

- hook2

- i.small

- i.sub

- ijacute

- j.small

- j.sub

- j.superior

- k.small

- k.superior

- l.small

- m.small

- minus.small

- n.small

- nine.small

- numCircle

- o.small

- ogonekmirrored

- one.small

- p.small

- p.superior

- parenleft.small

- parenright.small

- paunch1

- paunch2

- period.small

- period.sub

- period.superior

- plus.small

- q.small

- q.sub

- q.superior

- r.small

- r.sub

- s.small

- seven.small

- six.small

- t.small

- three.small

- tildecomb.narrow

- two.small

- u.small

- u.sub

- u.superior

- uni0259.small

- uni0259.superior

- uni0302.narrow

- uni0304.narrow

- uni0306.cy

- uni0306.narrow

- uni0308.narrow

- uni030C.alt

- uni030C.narrow

- v.small

- v.sub

- v.superior

- vertical.1

- vertical.2

- vertical.3

- w.small

- w.sub

- w.superior

- x.small

- x.superior

- y.small

- y.sub

- y.superior

- z.small

- z.sub

- z.superior

- zero.small
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, math, cherokee, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: coptic, duployan, malayalam, tifinagh, old-permic, hebrew, syriac, todhri, tai-le, canadian-aboriginal, math</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
<li>U+03C0 GREEK SMALL LETTER PI: try adding one of: greek, math, yi</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, lisu, hebrew, kayah-li, sundanese, sora-sompeng, kharoshthi, kaithi, arabic, armenian, syloti-nagri, yi, cham</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
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
<li>U+20F0 COMBINING ASTERISK ABOVE: try adding one of: grantha, devanagari</li>
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
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, math, yi, tai-tham</li>
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
<li>U+2460 CIRCLED DIGIT ONE: try adding one of: mongolian, symbols, yi</li>
<li>U+2461 CIRCLED DIGIT TWO: try adding one of: mongolian, symbols, yi</li>
<li>U+2462 CIRCLED DIGIT THREE: try adding one of: mongolian, symbols, yi</li>
<li>U+2463 CIRCLED DIGIT FOUR: try adding one of: mongolian, symbols, yi</li>
<li>U+2464 CIRCLED DIGIT FIVE: try adding one of: mongolian, symbols, yi</li>
<li>U+2465 CIRCLED DIGIT SIX: try adding one of: mongolian, symbols, yi</li>
<li>U+2466 CIRCLED DIGIT SEVEN: try adding one of: mongolian, symbols, yi</li>
<li>U+2467 CIRCLED DIGIT EIGHT: try adding one of: mongolian, symbols, yi</li>
<li>U+2468 CIRCLED DIGIT NINE: try adding one of: mongolian, symbols, yi</li>
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
<li>U+25CC DOTTED CIRCLE: try adding one of: kannada, old-permic, saurashtra, thai, pahawh-hmong, miao, new-tai-lue, kayah-li, tagbanwa, kaithi, siddham, syloti-nagri, gujarati, phags-pa, music, caucasian-albanian, adlam, syriac, psalter-pahlavi, bhaiksuki, rejang, modi, balinese, soyombo, ahom, devanagari, meetei-mayek, gunjala-gondi, newa, myanmar, symbols, javanese, masaram-gondi, warang-citi, elbasan, khojki, hebrew, sundanese, kharoshthi, sinhala, grantha, mongolian, batak, coptic, armenian, manichaean, math, bengali, hanunoo, lao, tai-le, cham, tibetan, tagalog, oriya, dogra, tamil, lepcha, yi, tai-tham, duployan, thaana, gurmukhi, buginese, khmer, wancho, telugu, canadian-aboriginal, marchen, sogdian, khudawadi, takri, tifinagh, malayalam, brahmi, chakma, zanabazar-square, osage, buhid, tai-viet, mende-kikakui, mandaic, limbu, hanifi-rohingya, mahajani, nko, tirhuta, bassa-vah, sharada</li>
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
<pre><code>* c.sub: X=254.0,Y=2.0 (should be at baseline 0?)

* c.sub: X=276.0,Y=2.0 (should be at baseline 0?)

* g.small: X=271.0,Y=2.0 (should be at baseline 0?)

* g.small: X=294.0,Y=2.0 (should be at baseline 0?)

* y.small: X=146.0,Y=-2.0 (should be at baseline 0?)

* uni2090 (U+2090): X=55.0,Y=2.0 (should be at baseline 0?)

* uni2091 (U+2091): X=257.0,Y=2.0 (should be at baseline 0?)

* uni2091 (U+2091): X=280.0,Y=2.0 (should be at baseline 0?)

* uni0416 (U+0416): X=481.0,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=519.0,Y=721.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=47.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=91.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=909.0,Y=719.0 (should be at cap-height 720?)

* uni0416 (U+0416): X=953.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=481.0,Y=721.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=519.0,Y=721.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=47.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=91.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=909.0,Y=719.0 (should be at cap-height 720?)

* uni0496 (U+0496): X=953.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=481.0,Y=721.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=519.0,Y=721.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=47.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=91.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=909.0,Y=719.0 (should be at cap-height 720?)

* uni04C1 (U+04C1): X=953.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=481.0,Y=721.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=519.0,Y=721.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=47.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=91.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=909.0,Y=719.0 (should be at cap-height 720?)

* uni04DC (U+04DC): X=953.0,Y=719.0 (should be at cap-height 720?)

* uni209B (U+209B): X=42.0,Y=2.0 (should be at baseline 0?)

* uni209B (U+209B): X=65.0,Y=2.0 (should be at baseline 0?)

* uni209B (U+209B): X=241.0,Y=-2.0 (should be at baseline 0?)

* uni209B (U+209B): X=264.0,Y=-1.0 (should be at baseline 0?)

* uni2080 (U+2080): X=299.5,Y=0.5 (should be at baseline 0?)

* uni2080 (U+2080): X=80.0,Y=0.5 (should be at baseline 0?)

* uni2070 (U+2070): X=299.5,Y=720.5 (should be at cap-height 720?)

* uni2070 (U+2070): X=80.0,Y=720.5 (should be at cap-height 720?)

* asterisk (U+002A): X=55.0,Y=719.0 (should be at cap-height 720?)

* asterisk (U+002A): X=365.0,Y=719.0 (should be at cap-height 720?)

* braceleft.case: X=251.5,Y=721.0 (should be at cap-height 720?)

* braceright.case: X=148.5,Y=721.0 (should be at cap-height 720?)

* uni208A (U+208A): X=194.0,Y=-2.0 (should be at baseline 0?)

* uni208A (U+208A): X=173.0,Y=-2.0 (should be at baseline 0?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* exclam (U+0021): L&lt;&lt;144.0,171.0&gt;--&lt;141.0,275.0&gt;&gt; -&gt; L&lt;&lt;141.0,275.0&gt;--&lt;141.0,720.0&gt;&gt;

* exclam (U+0021): L&lt;&lt;179.0,720.0&gt;--&lt;179.0,275.0&gt;&gt; -&gt; L&lt;&lt;179.0,275.0&gt;--&lt;176.0,171.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;144.0,171.0&gt;--&lt;141.0,275.0&gt;&gt; -&gt; L&lt;&lt;141.0,275.0&gt;--&lt;141.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;179.0,720.0&gt;--&lt;179.0,275.0&gt;&gt; -&gt; L&lt;&lt;179.0,275.0&gt;--&lt;176.0,171.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;464.0,171.0&gt;--&lt;461.0,275.0&gt;&gt; -&gt; L&lt;&lt;461.0,275.0&gt;--&lt;461.0,720.0&gt;&gt;

* exclamdbl (U+203C): L&lt;&lt;499.0,720.0&gt;--&lt;499.0,275.0&gt;&gt; -&gt; L&lt;&lt;499.0,275.0&gt;--&lt;496.0,171.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;141.0,-220.0&gt;--&lt;141.0,225.0&gt;&gt; -&gt; L&lt;&lt;141.0,225.0&gt;--&lt;144.0,329.0&gt;&gt;

* exclamdown (U+00A1): L&lt;&lt;176.0,329.0&gt;--&lt;179.0,225.0&gt;&gt; -&gt; L&lt;&lt;179.0,225.0&gt;--&lt;179.0,-220.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;664.0,171.0&gt;--&lt;661.0,275.0&gt;&gt; -&gt; L&lt;&lt;661.0,275.0&gt;--&lt;661.0,720.0&gt;&gt;

* uni2048 (U+2048): L&lt;&lt;699.0,720.0&gt;--&lt;699.0,275.0&gt;&gt; -&gt; L&lt;&lt;699.0,275.0&gt;--&lt;696.0,171.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;144.0,171.0&gt;--&lt;141.0,275.0&gt;&gt; -&gt; L&lt;&lt;141.0,275.0&gt;--&lt;141.0,720.0&gt;&gt;

* uni2049 (U+2049): L&lt;&lt;179.0,720.0&gt;--&lt;179.0,275.0&gt;&gt; -&gt; L&lt;&lt;179.0,275.0&gt;--&lt;176.0,171.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;111.0,240.0&gt;--&lt;111.0,580.0&gt;&gt; -&gt; L&lt;&lt;111.0,580.0&gt;--&lt;111.0,720.0&gt;&gt;

* uniA78B (U+A78B): L&lt;&lt;149.0,720.0&gt;--&lt;149.0,580.0&gt;&gt; -&gt; L&lt;&lt;149.0,580.0&gt;--&lt;149.0,240.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;126.0,720.0&gt;--&lt;126.0,620.0&gt;&gt; -&gt; L&lt;&lt;126.0,620.0&gt;--&lt;126.0,380.0&gt;&gt;

* uniA78C (U+A78C): L&lt;&lt;88.0,380.0&gt;--&lt;88.0,620.0&gt;&gt; -&gt; L&lt;&lt;88.0,620.0&gt;--&lt;88.0,720.0&gt;&gt;

* xi (U+03BE): L&lt;&lt;150.0,16.0&gt;--&lt;188.0,30.0&gt;&gt; -&gt; L&lt;&lt;188.0,30.0&gt;--&lt;246.0,56.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-jaggy-segments">outline_jaggy_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* eth (U+00F0): B&lt;&lt;433.5,422.0&gt;-&lt;454.0,395.0&gt;-&lt;459.0,376.0&gt;&gt;/B&lt;&lt;459.0,376.0&gt;-&lt;447.0,509.0&gt;-&lt;417.5,569.0&gt;&gt; = 9.587978519064421

* g (U+0067): B&lt;&lt;410.5,447.5&gt;-&lt;436.0,418.0&gt;-&lt;443.0,390.0&gt;&gt;/L&lt;&lt;443.0,390.0&gt;--&lt;443.0,500.0&gt;&gt; = 14.036243467926484

* g (U+0067): L&lt;&lt;443.0,3.0&gt;--&lt;443.0,137.0&gt;&gt;/B&lt;&lt;443.0,137.0&gt;-&lt;436.0,108.0&gt;-&lt;410.5,78.5&gt;&gt; = 13.570434385161475

* g.small: B&lt;&lt;251.5,274.0&gt;-&lt;267.0,256.0&gt;-&lt;271.0,239.0&gt;&gt;/L&lt;&lt;271.0,239.0&gt;--&lt;271.0,306.0&gt;&gt; = 13.240519915187184

* g.small: L&lt;&lt;271.0,2.0&gt;--&lt;271.0,84.0&gt;&gt;/B&lt;&lt;271.0,84.0&gt;-&lt;267.0,66.0&gt;-&lt;251.5,48.0&gt;&gt; = 12.528807709151492

* g.sub: B&lt;&lt;251.5,194.0&gt;-&lt;267.0,176.0&gt;-&lt;271.0,159.0&gt;&gt;/L&lt;&lt;271.0,159.0&gt;--&lt;271.0,226.0&gt;&gt; = 13.240519915187184

* g.sub: L&lt;&lt;271.0,-78.0&gt;--&lt;271.0,4.0&gt;&gt;/B&lt;&lt;271.0,4.0&gt;-&lt;267.0,-14.0&gt;-&lt;251.5,-32.0&gt;&gt; = 12.528807709151492

* g.superior: B&lt;&lt;251.5,688.0&gt;-&lt;267.0,670.0&gt;-&lt;271.0,653.0&gt;&gt;/L&lt;&lt;271.0,653.0&gt;--&lt;271.0,720.0&gt;&gt; = 13.240519915187184

* g.superior: L&lt;&lt;271.0,416.0&gt;--&lt;271.0,498.0&gt;&gt;/B&lt;&lt;271.0,498.0&gt;-&lt;267.0,480.0&gt;-&lt;251.5,462.0&gt;&gt; = 12.528807709151492

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
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are any segments inordinately short? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-short-segments">outline_short_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have segments which seem very short:</p>
<pre><code>* uni01B7 (U+01B7) contains a short segment L&lt;&lt;515.0,720.0&gt;--&lt;515.0,700.0&gt;&gt;

* uni01EE (U+01EE) contains a short segment L&lt;&lt;515.0,720.0&gt;--&lt;515.0,700.0&gt;&gt;

* G (U+0047) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* Gbreve (U+011E) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* Gcaron (U+01E6) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* Gcircumflex (U+011C) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* uni0122 (U+0122) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* Gdotaccent (U+0120) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* uni1E20 (U+1E20) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* uni01E4 (U+01E4) contains a short segment B&lt;&lt;671.0,367.0&gt;-&lt;673.0,362.0&gt;-&lt;673.0,350.0&gt;&gt;

* M (U+004D) contains a short segment L&lt;&lt;435.0,0.0&gt;--&lt;406.0,0.0&gt;&gt;

* uni1E9E (U+1E9E) contains a short segment L&lt;&lt;573.0,720.0&gt;--&lt;573.0,699.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;57.0,0.0&gt;--&lt;57.0,17.0&gt;&gt;

* Z (U+005A) contains a short segment L&lt;&lt;564.0,720.0&gt;--&lt;564.0,703.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;57.0,0.0&gt;--&lt;57.0,17.0&gt;&gt;

* Zacute (U+0179) contains a short segment L&lt;&lt;564.0,720.0&gt;--&lt;564.0,703.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;57.0,0.0&gt;--&lt;57.0,17.0&gt;&gt;

* Zcaron (U+017D) contains a short segment L&lt;&lt;564.0,720.0&gt;--&lt;564.0,703.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;57.0,0.0&gt;--&lt;57.0,17.0&gt;&gt;

* Zdotaccent (U+017B) contains a short segment L&lt;&lt;564.0,720.0&gt;--&lt;564.0,703.0&gt;&gt;

* uni01DD (U+01DD) contains a short segment L&lt;&lt;62.0,248.0&gt;--&lt;62.0,267.0&gt;&gt;

* z (U+007A) contains a short segment L&lt;&lt;55.0,0.0&gt;--&lt;55.0,14.0&gt;&gt;

* z (U+007A) contains a short segment L&lt;&lt;425.0,500.0&gt;--&lt;425.0,486.0&gt;&gt;

* z.small contains a short segment L&lt;&lt;34.0,0.0&gt;--&lt;34.0,9.0&gt;&gt;

* z.small contains a short segment L&lt;&lt;260.0,306.0&gt;--&lt;260.0,297.0&gt;&gt;

* z.sub contains a short segment L&lt;&lt;34.0,-80.0&gt;--&lt;34.0,-71.0&gt;&gt;

* z.sub contains a short segment L&lt;&lt;260.0,226.0&gt;--&lt;260.0,217.0&gt;&gt;

* z.superior contains a short segment L&lt;&lt;34.0,414.0&gt;--&lt;34.0,423.0&gt;&gt;

* z.superior contains a short segment L&lt;&lt;260.0,720.0&gt;--&lt;260.0,711.0&gt;&gt;

* zacute (U+017A) contains a short segment L&lt;&lt;55.0,0.0&gt;--&lt;55.0,14.0&gt;&gt;

* zacute (U+017A) contains a short segment L&lt;&lt;425.0,500.0&gt;--&lt;425.0,486.0&gt;&gt;

* zcaron (U+017E) contains a short segment L&lt;&lt;55.0,0.0&gt;--&lt;55.0,14.0&gt;&gt;

* zcaron (U+017E) contains a short segment L&lt;&lt;425.0,500.0&gt;--&lt;425.0,486.0&gt;&gt;

* zdotaccent (U+017C) contains a short segment L&lt;&lt;55.0,0.0&gt;--&lt;55.0,14.0&gt;&gt;

* zdotaccent (U+017C) contains a short segment L&lt;&lt;425.0,500.0&gt;--&lt;425.0,486.0&gt;&gt;

* f_f contains a short segment L&lt;&lt;311.0,687.0&gt;--&lt;285.0,687.0&gt;&gt;

* f_f contains a short segment L&lt;&lt;651.0,687.0&gt;--&lt;625.0,687.0&gt;&gt;

* f_f_i contains a short segment L&lt;&lt;37.0,466.0&gt;--&lt;37.0,500.0&gt;&gt;

* f_f_i contains a short segment L&lt;&lt;318.0,720.0&gt;--&lt;318.0,687.0&gt;&gt;

* f_f_i contains a short segment L&lt;&lt;318.0,687.0&gt;--&lt;291.0,687.0&gt;&gt;

* f_f_i contains a short segment L&lt;&lt;760.0,720.0&gt;--&lt;760.0,687.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;731.0,-200.0&gt;--&lt;731.0,-167.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;731.0,-167.0&gt;--&lt;742.0,-167.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;527.0,0.0&gt;--&lt;489.0,0.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;187.0,0.0&gt;--&lt;149.0,0.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;37.0,466.0&gt;--&lt;37.0,500.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;318.0,720.0&gt;--&lt;318.0,687.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;318.0,687.0&gt;--&lt;291.0,687.0&gt;&gt;

* f_f_j contains a short segment L&lt;&lt;760.0,720.0&gt;--&lt;760.0,687.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;37.0,466.0&gt;--&lt;37.0,500.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;318.0,720.0&gt;--&lt;318.0,687.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;318.0,687.0&gt;--&lt;291.0,687.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;868.0,0.0&gt;--&lt;830.0,0.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;744.0,500.0&gt;--&lt;744.0,466.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;527.0,0.0&gt;--&lt;489.0,0.0&gt;&gt;

* f_f_l contains a short segment L&lt;&lt;187.0,0.0&gt;--&lt;149.0,0.0&gt;&gt;

* f_j contains a short segment L&lt;&lt;391.0,-167.0&gt;--&lt;402.0,-167.0&gt;&gt;

* uni0490 (U+0490) contains a short segment L&lt;&lt;503.0,800.0&gt;--&lt;503.0,786.0&gt;&gt;

* uni0416.ss01 contains a short segment L&lt;&lt;80.0,0.0&gt;--&lt;80.0,34.0&gt;&gt;

* uni0416.ss01 contains a short segment L&lt;&lt;80.0,34.0&gt;--&lt;117.0,34.0&gt;&gt;

* uni0416.ss01 contains a short segment L&lt;&lt;86.0,686.0&gt;--&lt;86.0,720.0&gt;&gt;

* uni0416.ss01 contains a short segment L&lt;&lt;994.0,720.0&gt;--&lt;994.0,686.0&gt;&gt;

* uni0416.ss01 contains a short segment L&lt;&lt;1000.0,34.0&gt;--&lt;1000.0,0.0&gt;&gt;

* uni041C (U+041C) contains a short segment L&lt;&lt;435.0,0.0&gt;--&lt;406.0,0.0&gt;&gt;

* uni0429 (U+0429) contains a short segment L&lt;&lt;986.0,-160.0&gt;--&lt;950.0,-160.0&gt;&gt;

* uni0496.ss01 contains a short segment L&lt;&lt;80.0,0.0&gt;--&lt;80.0,34.0&gt;&gt;

* uni0496.ss01 contains a short segment L&lt;&lt;80.0,34.0&gt;--&lt;117.0,34.0&gt;&gt;

* uni0496.ss01 contains a short segment L&lt;&lt;86.0,686.0&gt;--&lt;86.0,720.0&gt;&gt;

* uni0496.ss01 contains a short segment L&lt;&lt;994.0,720.0&gt;--&lt;994.0,686.0&gt;&gt;

* uni0496.ss01 contains a short segment L&lt;&lt;1000.0,34.0&gt;--&lt;1000.0,0.0&gt;&gt;

* uni04A8 (U+04A8) contains a short segment L&lt;&lt;903.0,34.0&gt;--&lt;903.0,0.0&gt;&gt;

* uni04C1.ss01 contains a short segment L&lt;&lt;80.0,0.0&gt;--&lt;80.0,34.0&gt;&gt;

* uni04C1.ss01 contains a short segment L&lt;&lt;80.0,34.0&gt;--&lt;117.0,34.0&gt;&gt;

* uni04C1.ss01 contains a short segment L&lt;&lt;86.0,686.0&gt;--&lt;86.0,720.0&gt;&gt;

* uni04C1.ss01 contains a short segment L&lt;&lt;994.0,720.0&gt;--&lt;994.0,686.0&gt;&gt;

* uni04C1.ss01 contains a short segment L&lt;&lt;1000.0,34.0&gt;--&lt;1000.0,0.0&gt;&gt;

* uni04DC.ss01 contains a short segment L&lt;&lt;80.0,0.0&gt;--&lt;80.0,34.0&gt;&gt;

* uni04DC.ss01 contains a short segment L&lt;&lt;80.0,34.0&gt;--&lt;117.0,34.0&gt;&gt;

* uni04DC.ss01 contains a short segment L&lt;&lt;86.0,686.0&gt;--&lt;86.0,720.0&gt;&gt;

* uni04DC.ss01 contains a short segment L&lt;&lt;994.0,720.0&gt;--&lt;994.0,686.0&gt;&gt;

* uni04DC.ss01 contains a short segment L&lt;&lt;1000.0,34.0&gt;--&lt;1000.0,0.0&gt;&gt;

* uni04E0 (U+04E0) contains a short segment L&lt;&lt;515.0,720.0&gt;--&lt;515.0,700.0&gt;&gt;

* uni0431.ss01 contains a short segment L&lt;&lt;483.0,760.0&gt;--&lt;483.0,752.0&gt;&gt;

* at (U+0040) contains a short segment L&lt;&lt;621.0,495.0&gt;--&lt;659.0,495.0&gt;&gt;

* at (U+0040) contains a short segment L&lt;&lt;605.0,-112.0&gt;--&lt;605.0,-145.0&gt;&gt;
</code></pre>
 [code: found-short-segments]



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







* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 56 | 140 | 939 | 46 | 807 | 0 | 
| 0% | 0% | 3% | 7% | 47% | 2% | 41% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
