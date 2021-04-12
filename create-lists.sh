# create-lists.sh
# generate CSV files of orthography + vPhon spelling pronunciations
# James Kirby
# April 11, 2021

# generate text file of unique SV syllables
cut -d , -f 2 sino-vietnamese-readings.csv | 
	awk 'NR>1' | 
	tr '[:upper:]' '[:lower:]' | 
	sort -f | 
	uniq | 
	grep -v "[[:punct:]]" > unique-sino-vietnamese-syllables.txt 

echo ""
echo "How many unique (orthographic) SV syllables?"
wc -l unique-sino-vietnamese-syllables.txt

echo "How many orthographic SV syllables appear in the joined HTL and Duc lists?"
#awk 'a[$0]++' join-duc-luong.txt unique-sino-vietnamese-syllables.txt | wc -l
ggrep -xf unique-sino-vietnamese-syllables.txt join-duc-luong.txt | wc -l

echo "How many orthographic syllables are unique to the SV list? (i.e. which are missing from the HTL/Duc list)"
# reads as: select lines of unique-sino-vietnamese-syllables that do not match any line in join-duc-luong.txt
ggrep -xvf join-duc-luong.txt unique-sino-vietnamese-syllables.txt | wc -l
# some of these are pretty obscure, probably just spelling pronunciations of MC words

echo ""
echo -n "Generating spelling pronunciations and filtering duplicates..."
python ~/Projects/vPhon/vPhon.py -d o -8 -n -p -m ' ' -o ',' < join-duc-luong.txt > tmp.txt
sed -i '' -E 's/7/5/' tmp.txt
sed -i '' -E 's/8/6/' tmp.txt
sed -i '' -E 's/,th/,tʰ/' tmp.txt
# here we sort and filter based on the second column to deal with there being multiple spellings that map to the same pronunciation
# note that this doesn't let us select WHICH spelling, so we retain e.g. khoẻ instead of khỏe
#sort -t, -k2n tmp.txt | uniq -f1  > attested-vietnamese/syllables.txt
awk -F, '!seen[$2]++' tmp.txt > attested-vietnamese-syllables.txt
#sort -u tmp.txt > attested-vietnamese-syllables.txt # awk '!visited[$0]++' would also work
rm tmp.txt

python ~/Projects/vPhon/vPhon.py -d o -8 -n -p -m ' ' -o ',' < unique-sino-vietnamese-syllables.txt > tmp.txt
sed -i '' -E 's/7/5/' tmp.txt
sed -i '' -E 's/8/6/' tmp.txt
sed -i '' -E 's/,th/,tʰ/' tmp.txt
awk -F, '!seen[$2]++' tmp.txt > sino-vietnamese-syllables.txt
rm tmp.txt
echo "done."

echo -n "Removing junk from 'attested' list..."
# uncomment ggreps to see what is actually getting removed
# things that vPhon didn't know how to deal with:
#ggrep '\[' attested-vietnamese-syllables.txt
sed -i '' -E '/\[/d' attested-vietnamese-syllables.txt
# things that have double medial glides for some reason:
#ggrep 'kw w' attested-vietnamese-syllables.txt
sed -i '' -E '/kw w/d' attested-vietnamese-syllables.txt
# checked syllables with tones other than 5 or 6:
#ggrep '[ptk] [1-4]' attested-vietnamese-syllables.txt
sed -i '' -E '/[ptk] [1-4]/d' attested-vietnamese-syllables.txt
echo "done."

echo -n "Deleting forms with marginal long vowels..."
# uncomment ggreps to see what is actually getting removed
#ggrep '[oɔ]ː' attested-vietnamese-syllables.txt
sed -i '' -E '/[oɔ]ː/d' attested-vietnamese-syllables.txt
#ggrep '[oɔ]ː' sino-vietnamese-syllables.txt
sed -i '' -E '/[oɔ]ː/d' sino-vietnamese-syllables.txt
echo "done."
echo ""

echo "How many syllables are in the phonetized SV list?"
wc -l sino-vietnamese-syllables.txt

echo "How many of these phonetized SV syllables are in the Attested list?"
awk -F, 'NR==FNR{seen[$2]++;next}seen[$2] > 0' attested-vietnamese-syllables.txt sino-vietnamese-syllables.txt | wc -l
#ggrep only works on entire lines
#ggrep -xf sino-vietnamese-syllables.txt attested-vietnamese-syllables.txt | wc -l

echo "...which means, how many are UNIQUE to the SV list?"
awk -F, 'NR==FNR{!seen[$2]++;next}!seen[$2] > 0' attested-vietnamese-syllables.txt sino-vietnamese-syllables.txt | wc -l
#ggrep -vxf attested-vietnamese-syllables.txt sino-vietnamese-syllables.txt | wc -l
echo "Those numbers better add up..."
# again, these are super-marginal MC items, unlikely to show up in any 'normal' dictionary
echo ""

echo -n "Removing SV items from Attested list and renaming as 'no-known-sv-syllables' list."
# read as: retain everything from file2 that is not matched by something in file1
#ggrep -xvf sino-vietnamese-syllables.txt attested-vietnamese-syllables.txt > no-known-sv-syllables.txt
awk -F, 'NR==FNR{!seen[$2]++;next}!seen[$2] > 0' sino-vietnamese-syllables.txt attested-vietnamese-syllables.txt > no-known-sv-syllables.txt
echo ""
echo ""
wc -l attested-vietnamese-syllables.txt 
wc -l no-known-sv-syllables.txt 
wc -l sino-vietnamese-syllables.txt

echo ""
echo "Note that SV + NSV > Attested, because of the 72 items in the SV list that are not in our Attested list."
echo ""

echo "Creating comma-delimited .csv files (without orthography)."
cut -d , -f 2 attested-vietnamese-syllables.txt | python slot-format.py > attested-vietnamese-syllables.csv
cut -d , -f 2 sino-vietnamese-syllables.txt | python slot-format.py > sino-vietnamese-syllables.csv
cut -d , -f 2 no-known-sv-syllables.txt | python slot-format.py > no-known-sv-syllables.csv

echo "Writing syllable shape distribution file."
python print-syllable-shape-counts.py > syllable-shape-counts.csv
echo "All done."

