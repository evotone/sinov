# given vPhon output with raised aspiration but separated labial, create comma-delimited output
# expects command line / piped input

import sys, io

onsets = ['ʔ', 'ɓ','k', 'c', 'w', 'ɗ','ɣ', 'z', 'h', 'x', 'l', 'm', 'n', 'ŋ', 'ɲ', 'f', 'p', 'r', 'ʑ', 'ʂ', 't', 'tʰ',  'ʈ', 'v', 's']
# note that we are intentionally omitting oː and ɔː from this analysis
nuclei = ['a', 'aː', 'ɛ', 'e', 'ə', 'əː', 'ɔ', 'o', 'i', 'ɨ', 'u', 'iə', 'ɨə', 'uə']
codas = ['p', 't', 'k', 'm', 'n', 'ŋ', 'j', 'w']
tones = ['1', '2', '3', '4', '5', '6']

fh = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

for line in fh:

    ons = ''
    med = ''
    nuc = ''
    cod = ''
    ton = ''

    elem = line.split()

    ons = elem[0]

    # depending on what the first char is, the second might be a glide
    if elem[1] == 'w' and elem[0] in onsets: med = 'w'
         
    # if the second char isn't <w>, it's the nucleus (or it had better be)
    if elem[1] is not 'w': nuc = elem[1]
    else: nuc = elem[2]

    # check if we're dealing with tonal or non-tonal input
    if elem[-1] in tones:
        ton = elem[-1] 
        # if the second to last char is in the coda list, it's a coda, otherwise there is no coda
        if elem[-2] in codas: cod = elem[-2] 
        #else: cod = None
    else:
        if elem[-1] in codas: cod = elem[-1] 
        #else: cod = None

    if ton: syl = '%s,%s,%s,%s,%s' % (ons, med, nuc, cod, ton)
    else: syl = '%s,%s,%s,%s' % (ons, med, nuc, cod)

    print(syl)

fh.close()
