# sinov
Data and code accompanying Kirby & Alves (2021), "Exploring statistical regularities in the syllable canon of Sino-Vietnamese loanword phonology"

## I just want to see the tables

Go [here](stats-plots.html).

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
|`print-syllable-shape-counts.py`|Python helper script that takes calculates the number of possible syllables|
|`sino-vietnamese-readings.csv`|A CSV version of Chia-Lu Chiang's list with one duplicate entry manually removed (8090 lines)
|`sino-vietnamese-syllables.csv`|The SV list in `o,m,n,c,t` format|
|`sino-vietnamese-syllables.txt`|The SV list in `orthography,I P A` format|
|`slot-format.py`|Python helper script that takes the IPA from the `*.txt` files and produces comma-delimited (`ons,med,nuc,cod,ton`) output|
|`stats-plots.Rmd`|R Markdown file to generate tables and heatmaps|
|`stats-plots.html`|Sortable tables and heatmaps|
|`syllable-shape-counts.csv`|Output of `print-syallble-shape-counts.py`|
|`unique-sino-vietnamese-syllables.txt`|Just the unique Vietnamese syllables from the above (1940 lines)|

