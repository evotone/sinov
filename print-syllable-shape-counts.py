'''
April 2021

We assume:

- 24 "plain" plain (including /ʔ/ but excluding /w/); note that this distinguishes <d> <gi> in addition to <s> <x>
- 12 nuclei [aː e əː ɛ i ɨ ɔ o u iə ɨə uə] with unrestricted distribution following non-labialized plain
- 2 nuclei [a ə] that cannot occur in open syllables
- 17 "labializable" plain [ɗw tw tʰw sw zw lw rw cw ʂw ɲw ʈw kw xw ɣw ŋw hw w] (we treat /w/ here like a labialized ʔw for co-occurrence reasons) which may not be followed by [ɨ ɔ o u ɨə uə] (ostensibly the single exception is quốc but it is typically pronounced [kwək])
- 3 nasal codas [m n ŋ] and 3 unreleased plosive codas [p t k]
- 2 semivowels [w j] with restricted distribution: /j/ cannot follow [i iə e ɛ] and /w/ cannot follow [əː ɔ o u uə] (is absence of /əːw/, but not /əw/ an accidental gap? Cf. dao/rau, mới/mấy)
- a "null coda" that can only occur with 12 of the 14 nuclei
- 6 tones that can occur with sonorant or null finals
- 2 tones that can occur with obstruent codas

'''

def possible_syllables():
    '''Create the dict of lists of possible syllables.'''
    
    # first, build up lists of hypothetical syllables by shape-type in a dict of lists
    h = {'CV': [], 'CwV': [], 'CVN': [], 'CwVN': [], 'CVT': [], 'CwVT': [], 'CVj': [], 'CwVj': [], 'CVw': [], 'CwVw': []}

    # CV 
    for o in plain:
        for n in long_v:
            for c in null_final:
                for t in tones:
                    h['CV'].append((o, n, c, t))

    # CwV 
    for o in lab_o:
        for n in [item for item in lab_v if item not in ['a', 'ə']]:
            for c in null_final:
                for t in tones:
                    h['CwV'].append((o, n, c, t))

    # CVN
    for o in plain:
        for n in all_v:
            for c in nas_finals:
                for t in tones:
                    h['CVN'].append((o, n, c, t))
    # CwVN
    for o in lab_o:
        for n in lab_v:
            for c in nas_finals:
                for t in tones:
                    h['CwVN'].append((o, n, c, t))

    # CVT 
    for o in plain:
        for n in all_v:
            for c in obs_finals:
                for t in ['5', '6']:
                    h['CVT'].append((o, n, c, t))

    # CwVT 
    for o in lab_o:
        for n in lab_v:
            for c in obs_finals:
                for t in ['5', '6']:
                    h['CwVT'].append((o, n, c, t))

    # CVj 
    for o in plain:
        for n in [item for item in all_v if item not in ['i', 'iə', 'e', 'ɛ']]:
            for c in ['j']:
                for t in tones:
                    h['CVj'].append((o, n, c, t))

    # CwVj 
    for o in lab_o:
        for n in ['a', 'aː', 'ə', 'əː']:
            for c in ['j']:
                for t in tones:
                    h['CwVj'].append((o, n, c, t))

    # CVw 
    for o in plain:
        for n in [item for item in all_v if item not in ['əː', 'ɔ', 'o', 'u', 'uə']]:
            for c in ['w']:
                for t in tones:
                    h['CVw'].append((o, n, c, t))

    # CwVw 
    for o in lab_o:
        for n in ['aː', 'a', 'ɛ', 'e', 'ə', 'i', 'iə']:
            for c in ['w']:
                for t in tones:
                    h['CwVw'].append((o, n, c, t))

    return(h)   

def count_syls(f):
    '''Sort the syllables in a file by shape.'''

    d = {'CV': [], 'CwV': [], 'CVN': [], 'CwVN': [], 'CVT': [], 'CwVT': [], 'CVj': [], 'CwVj': [], 'CVw': [], 'CwVw': []}

    for s in f.readlines():
        o, m, n, c, t = '', '', '', '', ''
        e = s.strip().split(',')
        o = e[0]
        m = e[1]
        n = e[2]
        c = e[3]
        if len(e) == 5: t = e[4]
        else:
            print('Something is wrong.')
            exit(1)

        # now assign to a list
        shape = ''
        #if o in lab_o:
        if m == 'w' or o == 'w':
            if c == 'w': shape = 'CwVw'
            elif c == 'j': shape = 'CwVj'
            elif c in obs_finals: shape = 'CwVT'
            elif c in nas_finals: shape = 'CwVN'
            else: shape = 'CwV' 
        else:
            if c == 'w': shape = 'CVw'
            elif c == 'j': shape = 'CVj'
            elif c in obs_finals: shape = 'CVT'
            elif c in nas_finals: shape = 'CVN'
            else: shape = 'CV' 

        d[shape].append((o,m,n,c,t))

    return(d)


if __name__ == '__main__':

    # note we are treating onset == /w/ as "labialized" 
    plain = ['ʔ', 'ɓ', 'm', 'v', 'f', 'ɗ', 't', 'tʰ', 'n', 'z', 's', 'ʈ', 'ʑ', 'ʂ', 'c', 'ɲ', 'k', 'ɣ', 'x', 'ŋ', 'l', 'r', 'j', 'h']
    lab_o = ['ɗw', 'tw', 'tʰw', 'sw', 'zw', 'lw', 'rw', 'cw', 'ʂw', 'ɲw', 'ʈw', 'kw', 'xw', 'ɣw', 'ŋw', 'hw', 'w']

    # note that we are intentionally omitting oː and ɔː from this analysis
    all_v = ['aː', 'a', 'ɛ', 'e', 'ə', 'əː', 'ɔ', 'o', 'i', 'ɨ', 'u', 'iə', 'ɨə', 'uə']
    long_v = ['aː', 'ɛ', 'e', 'əː', 'ɔ', 'o', 'i', 'ɨ', 'u', 'iə', 'ɨə', 'uə']
    lab_v = ['aː', 'a', 'ɛ', 'e', 'ə', 'əː', 'i', 'iə']
    
    nas_finals = ['m', 'n', 'ŋ']
    obs_finals = ['p', 't', 'k']
    null_final = ['']

    tones = ['1', '2', '3', '4', '5', '6']

    hypothetical = possible_syllables()

    for l in hypothetical: print('possible,%s,%d' % (l, len(hypothetical[l])))
    
    # now, read in the SV and NSV lists and parse each item accordingly
    sv = open('sino-vietnamese-syllables.csv', 'r')
    s_syl = count_syls(sv)
    sv.close()
    for l in s_syl: print('SV,%s,%d' % (l, len(s_syl[l])))

    nv = open('no-known-sv-syllables.csv', 'r')
    n_syl = count_syls(nv)
    nv.close()
    for l in n_syl: print('NSV,%s,%d' % (l, len(n_syl[l])))

    # print as list
    #for h in hypothetical:
    #    for s in hypothetical[h]:
    #        print(' '.join(filter(None, s)))
    
