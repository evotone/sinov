# join-duc-luong.sh
# get vPhon here: https://github.com/kirbyj/vPhon
# get Viet74K.txt here: http://www.informatik.uni-leipzig.de/~duc/software/misc/wordlist.html
# get common-vietnamese-syllables.txt here: http://www.hieuthi.com/blog/2017/04/03/vietnamese-syllables-usage.html

# create a sorted version of the Luong list
sort common-vietnamese-syllables.txt > luong-sorted.txt

# create a list of unique syllables from the filtered Đức 74k list
# not very specific: we 
cat Viet74K.txt | tr ' ' '\n' | tr '[:upper:]' '[:lower:]' | grep -v "[[:punct:]]" | grep -v ".*[aieuoăươ]k$" | sort | uniq | sed '/^$/d' > tmp.txt

# next we want the line numbers from this that we want to delete, which we can get using vPhon and grep
# vPhon puts [ ] around anything that it can’t produce IPA for (i.e. which it judges to be not phonotactically permissible)
# so by grepping for non-alphanumeric characters we can easily find the line numbers of interest
# change to location of vPhon on your system 
python ~/Projects/vPhon/vPhon.py < tmp.txt | grep -n '[[:punct:]]' | cut -d: -f1 > to-delete.txt

# how many lines are being deleted?
wc -l to-delete.txt

# we can use this list of line numbers to filter Đức list using a little awk:
awk 'FNR == NR { h[$1]; next } !(FNR in h)' to-delete.txt tmp.txt > duc-filtered.txt
wc -l duc-filtered.txt
rm to-delete.txt

# that leaves 7618 syllables, compare to 7184 in common-vietnamese-syllables.txt
# how much overlap is there?
awk 'a[$0]++' duc-filtered.txt common-vietnamese-syllables.txt | wc -l

# 6321 items common to both, meaning there are c. 1300 items in Đức that are not in Lương’s list
# join them on the unique items:
cat duc-filtered.txt luong-sorted.txt | sort -u > join-duc-luong.txt

