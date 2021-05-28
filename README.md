# sinov
Data and code accompanying Kirby & Alves (2021), "Exploring statistical regularities in the syllable canon of Sino-Vietnamese loanmorph phonology"

## I just want to see the tables

You want [stats-plots.html](stats-plots.html). You can download it and view it in a web browser, or we've hosted a version [here](https://evotone.github.io/sinov-suppmat.html).

## Contents

|File|Description|
|---|---|
|`attested-vietnamese-syllables.csv`|The attested syllable list in `o,m,n,c,t` format|
|`attested-vietnamese-syllables.txt`|The attested syllable list in `orthography,I P A` format|
|`create-lists.sh`|Bash script documenting how the lists were created and filtered|
|`duc-filtered.txt`|Unique syllables from [Hồ Ngọc Đức's 74K wordlist](http://www.informatik.uni-leipzig.de/~duc/software/misc/wordlist.html), filtered to remove junk (see `join-duc-luong.sh`)|
|`join-duc-luong.sh`|Bash script documenting how the web source files were filtered and combined|
|`join-duc-luong.txt`|`duc-filtered.txt` and `luong-sorted.txt` run through `sort -u`|
|`luong-sorted.txt`|[Hieu-Thi Luong's GitHub List](https://gist.github.com/hieuthi/1f5d80fca871f3642f61f7e3de883f3a) run through `sort(1)`|
|`no-known-sv-syllables.csv`| The NSV list in `o,m,n,c,t` format|
|`no-known-sv-syllables.txt`| The NSV list in `orthography,I P A` format|
|`print-syllable-shape-counts.py`|Python helper script that calculates the number of possible syllables|
|`sino-vietnamese-readings.csv`|An edited CSV version of Chiang list with one duplicate entry manually removed (8090 lines)
|`sino-vietnamese-syllables.csv`|The SV list in `o,m,n,c,t` format|
|`sino-vietnamese-syllables.txt`|The SV list in `orthography,I P A` format|
|`slot-format.py`|Python helper script that takes the IPA from the `*.txt` files and produces comma-delimited (`ons,med,nuc,cod,ton`) output|
|`stats-plots.Rmd`|R Markdown file to generate tables and heatmaps|
|`stats-plots.html`|Sortable tables and heatmaps|
|`syllable-shape-counts.csv`|Output of `print-syllable-shape-counts.py`|
|`unique-sino-vietnamese-syllables.txt`|Just the unique Vietnamese syllables from `sino-vietnamese-readings.csv`(1940 lines)|

## A note on the Sino-Vietnamese word list

The `sino-vietnamese-readings.csv` file is based on the dissertation of Chia-lu Chiang:

江佳路 [Chiang, Chia-lu]. 2011. 越南漢子音的歷史層次研究 [The study on phonological strata of Sino-Vietnamese]. Unpublished dissertation. 國立台灣師範大學 [National Taiwan Normal University].

We do not use Chiang's phonetic representations directly, although our representations should be broadly equivalent. More importantly, we have **not** verified the accuracy of this list ourselves, so *cave usor*. For example, there may be alternative pronunciations for some characters that are not in this list, and/or pronunciations that have been "normalized" somewhere along the line. *Further research is needed.*

This is also not a unique list; other Sino-Vietnamese word lists and dictionaries can easily be found by searching the Web.
