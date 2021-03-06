# Input: 3 Positive integers
# Output: Probability that two randomly selected mating org will produce an organism possing a dominate alle (show in phenotype)
# PROT - https://rosalind.info/problems/prot/

def traverseCodon(codons):
    codonList = []
    s = ''
    for c in codons:
        if len(s) == 3:
            codonList.append(s)
            s = ''
        s += c
    protienString = ''
    for codon in codonList:
        protien = decodeCodon(codon)
        if protien == 'Stop':
            return protienString
        protienString += protien
    return protienString
  
def decodeCodon(codon):
    if (codon == 'UUU'):
        return 'F'
    elif (codon == 'UUC'):
        return 'F'
    elif (codon == 'UUA'):
        return 'L'
    elif (codon == 'UUG'):
        return 'L'
    elif (codon == 'UCU'):
        return 'S'
    elif (codon == 'UCC'):
        return 'S'
    elif (codon == 'UCA'):
        return 'S'
    elif (codon == 'UCG'):
        return 'S'
    elif (codon == 'UAU'):
        return 'Y'
    elif (codon == 'UAC'):
        return 'Y'
    elif (codon == 'UAA'):
        return 'Stop'
    elif (codon == 'UAG'):
        return 'Stop'
    elif (codon == 'UGU'):
        return 'C'
    elif (codon == 'UGC'):
        return 'C'
    elif (codon == 'UGA'):
        return 'Stop'
    elif (codon == 'UGG'):
        return 'W'
    elif (codon == 'CUU'):
        return 'L'
    elif (codon == 'CUC'):
        return 'L'
    elif (codon == 'CUA'):
        return 'L'
    elif (codon == 'CUG'):
        return 'L'
    elif (codon == 'CCU'):
        return 'P'
    elif (codon == 'CCC'):
        return 'P'
    elif (codon == 'CCA'):
        return 'P'
    elif (codon == 'CCG'):
        return 'P'
    elif (codon == 'CAU'):
        return 'H'
    elif (codon == 'CAC'):
        return 'H'
    elif (codon == 'CAA'):
        return 'Q'
    elif (codon == 'CAG'):
        return 'Q'
    elif (codon == 'CGU'):
        return 'R'
    elif (codon == 'CGC'):
        return 'R'
    elif (codon == 'CGA'):
        return 'R'
    elif (codon == 'CGG'):
        return 'R'
    elif (codon == 'AUU'):
        return 'I'
    elif (codon == 'AUC'):
        return 'I'
    elif (codon == 'AUA'):
        return 'I'
    elif (codon == 'AUG'):
        return 'M'
    elif (codon == 'ACU'):
        return 'T'
    elif (codon == 'ACC'):
        return 'T'
    elif (codon == 'ACA'):
        return 'T'
    elif (codon == 'ACG'):
        return 'T'
    elif (codon == 'AAU'):
        return 'N'
    elif (codon == 'AAC'):
        return 'N'
    elif (codon == 'AAA'):
        return 'K'
    elif (codon == 'AAG'):
        return 'K'
    elif (codon == 'AGU'):
        return 'S'
    elif (codon == 'AGC'):
        return 'S'
    elif (codon == 'AGA'):
        return 'R'
    elif (codon == 'AGG'):
        return 'R'
    elif (codon == 'GUU'):
        return 'V'
    elif (codon == 'GUC'):
        return 'V'
    elif (codon == 'GUA'):
        return 'V'
    elif (codon == 'GUG'):
        return 'V'
    elif (codon == 'GCU'):
        return 'A'
    elif (codon == 'GCC'):
        return 'A'
    elif (codon == 'GCA'):
        return 'A'
    elif (codon == 'GCG'):
        return 'A'
    elif (codon == 'GAU'):
        return 'D'
    elif (codon == 'GAC'):
        return 'D'
    elif (codon == 'GAA'):
        return 'E'
    elif (codon == 'GAG'):
        return 'E'
    elif (codon == 'GGU'):
        return 'G'
    elif (codon == 'GGC'):
        return 'G'
    elif (codon == 'GGA'):
        return 'G'
    elif (codon == 'GGG'):
        return 'G'
        
s = 'AUGUUGUCAGCUUUCUCCGAGAGAAGCAUAUUCAUGGGUAAUAGCAAUAUUGUAUACCAAGAUGGUCUCCCCUCAAGUCCAGGUGACUGUUCAUCCCUUGAAAUGGGUAUAGGUCUCUUCCGCUUGCUGAAUUCCGUGAUGGGGUCGUUGCGUGGCUGUUGUCAGCAUGUUUACGCAGUAUCCUCGCGACUGGUCGUACCUCUUACUUCGGUAAGGCACCUGCCGGGUCUGAUGUCCGGAGCUAGGUCCCCUUCUGAAUCACGAGCAGACCUUGAAGGGAGCAGCACGGCUAACUACAGAAGUGCAAAAGAGCAAACAUGUAGCGUAGUGGUCCCCUGGUACCCGAGAUUGAACUCUCACAUGUCUUUCGGUGUCGAAAUUAGUCCAGCAGGGCGGCUCGCACACCCAAACACAUGUCCGGGACCUGGCGCUCCCCAAAUAAUGAACCUCGUAUCCCGGUACUCACGGCAAUGUCGAUAUCUCCAAGAUACGGAACGGCCGUUGCCUACAAGUGAACGGGGCACGUUGCGCUUAUCAGUACGGUCUGAAUCCACUUCUCGCUUCUGCUAUCGAGCAGUCUCAAUCAAUGAUACAGCCCCUAAACAUUCCUCUCACCAUAACUCAUCCCCGAUACGGUCUUCGACCACCCAGGGGGCUUUGAGGUUAAUUGAAGGUAUUCCUGUAUCCAUCCCCCGCUCUCAGCGAUGGUCUUUCCGGCGGCGUCAUCUGGAACGAAGUAGAUAUGCAUUGGCAUCUCCGUAUCCCGGUGUAUUAAUUACGUCUAAUGACCCUGCAGCUCUCACACUCGCAUCCCCUCUGAGCGAUCUCUACGACUCACCUCAGAUCGUUCGUUUCCAGCUCGAGGGAGGUGACCUGGCUUGGGUGCUCCGACGCUCUAAAGAGUUCGAGGGUUUAACGAACAGCAAGCCAACUUUUUGCCUUCCGUUGCGAUGGGCUUCGCUGCAUUGCAAUCGGCUGCAUUCGUGUCCCAGAGACCAUCUCCGCUCCUCGACACGUGAGGAUAUACACACUUUUACACGUAUUCACACGCCCCGUGUCGUACCUGCCCUGCGUGUCUUUGUAAAGUAUCAUCAUGUACAGGUCGCGAGGCUGGUUGUACUAGCGAGUCCAUGGCGAGGACGCAGAAGCAAGGUGCUCCAACACACUCUAAUAAGCGGCCACCACGUUUGGCUGACCUUCCAAUUACACGACUCUGAGAAUGAGUGGCGGCAAUUGAAAUCCUCGUAUGCUGCCCCUAGAAUGGAUAGAGAUCCGUGUCACCCAAAUAGCCCCACUGAACCUAUCGCGUCAAACGGCAGAUCUGACUGCAGUCGGUCGUAUCAAGCUAUUGGCCUAAGAGUCGCCGUGUACGAGAGCGGCUUUGUCUUUUUCCCUAACCUGCAAACGAUGUCUCGGAUGAUUAUGCAGCGAGAGUUAACGGACAUGUCCUCACAUCGAUCACUGCCGCACCCGGCGCUGAGAAAUCGCGUAGUACGAUUUGCGUCUAUUUAUUAUGGGGGACUUCGGCCGAUGGGUUCUCUCAUAUAUCGGACCCACCCGCUAAGCGCGAUAGGCCCGAUGCAAGCGACCCAGCAGAUGUCGACACCACGAAUUAAAACCGGAUCUGCUCAACGCCGCAUACUGGCACACUCCUCUAUGUUACGCGCGAAAGAUGUUACCGGAAGGGCCGCCAUAACCGCACCCACUCUAUGUGCAAUUGUAUCGCGGAAAGGAACAACCUCAAGUCUCGGCCUAUCCAGGUCCAGCAGAGGGCUUCAUCUGUCCGGGAAGUAUUGCUUAGGUAGUCGGAGCACCCGGAUGGACGUAGAAAGCUGGGUUAUAAGUGAAUGGAUGUCGAAACUUUAUCCAACGAACCCAAUGUGCGUUCUGGGCAGCGGGGAAGUCGCGAGCUUAUACCAAAGCCUGCGCUGGGUUUGUACGACCUGCACUGAUAUGUGUACACCUUUAUUUGGGCUGAAUACCAAAAGGAGACCUAUCGUGCGGCCGCUAUACUCUAUACGUUUUCGUUCUGAAUCACGUUGGGUCCUAUUCUUAGAAAAAACUUCGUUUAUUGAGGUUGUAGAGAAAACGGCUGCUGUGCUGGCUCGCCUGCUUUCAUCUGGACGAGUUGUAUUUCAUCUUCGGGGCACCCCACCGUGGUGGCAACGGGGCAAGUCAUAUCAUCGACCCCGACUAAUACCGUACAAUCUAGGCAUCGGUGUUGUUCUUGUCUCCGACUUUUGUUAUCCUCCGGGGGUGGCCAGGGUUAUCGGUCGAGGUUGUCUGAAGACAUCGUCACACUGUACGUUUUCCUGGUUCCUUAUUUCUAUUGACUACAGCCGGACGAAAAUCGAAGUCUACUUCUGCCCUGUAGCUCCACCUAUCCAGUCCCCCCAUCGUCGCAGGCUACCACCUAUACUGAUGAUGUGGUCCCUCGCCGUUUGUAUACAGAUUCAAUUGGUCCAAUGGCUCGUCGUGCGGUCCAGGAAGUGCAUUACCAAUCAGCACGAUCUCGCUGCAGCUAUGGGUGCGGAGACUCUCAGGGCAUGCCUGUCUUCGAAACUUAGGCAUAUGGGAUACGUCUGCUCCUCAAAUGGUAUCAGGUAUUGCCCGACGACUCAUUUAAGUCAUAACAGUCUGUACGAGUUUACCACUGUGACCCGACCGCGGGCUUCAAUCAGAAAGUCACCGCCUAGACUGUAUAUGGCGCGCAGCCGGAACUUGAAACAUACCAACGAAUGCCUAACAGAUCCGUGGGGGGUGAAUAGUGACUGGCUGAGAACAAAAGCUCCGUUCGUACUAAGUGCUGAUGGGAUGAUGGCCUGUACCGCUACGCGUUUGCUACUUCGGCGGGAGGCGGGUUGCCACUCCACACUCAGGGGGCUACCCAGUCUCUCACACCAGGUUUUAAACCCGCGUAUCCGAAAGAGAAGGAGCGAAUAUGCAGGGUACCAUACUGCUGUGUUACCCCAAGUAACGGUUGCCAUGGCCCACGCCCGGGCUCAAGGUACACGUUACCCCCUACUUGAACCAGUACGAUUUAAGGAAGUCCCAAGUAUAGGUACCAUCAGGGUGACCCAUAUGAAGUUUUCUGCCUCCGAAGGAGAUCGUUUCGAGGCUCCGGACUUUACACGCGGUCGAACGGACGCGCCCAUCCCCCAAACAGUUAUCCGUUACCUACUCCAAAUAAGGCCUGUGCACUACGCUGCCCCGGCAGAAUCCGAUGUUAGAACGCGAACCAAUACCACUCAGAUUCGUAAGUCGAUAUCGCGCCGACUAGGAAUUCCCAAGUCGACGUUUUUGUGGAGGGCUAUUUCGCCAUUGGUCUUAGUGGCGCGUGGGCCAGGAGUGGGGGGGGGCGAGCCCUUAAGAAAUCGAUGCCACACCCACUCGCGAACUUCAUUAAUGGCCAUUAUCGGCCACCAAUGGUUGAGAUGCGCUAGAUUUUCAGAUCUUCAAAAGACUGGACCGGAAGUACGGUGUUUUGGGUGCCUGGUCCUUCCACGAAAUCAGAAAUGCCCACGAACGUCACCCAGAUACGUCCUUAUGUGUCCAGCCCCUGAGCUAAGGUAUCGUUCUCACUCUCGGUAUUCGCGAAGCACCCCUUGUUCCCCCAGGGUCCCGGUAAGAGGAGAGUUAAAAAUUAGUACUAUCACUAUGCGUUGGGCGUGUUUGACUACUCCAGGUUAUGGGCAGCUUAAAGCUGCAGCGAGUUUACAGAUAGCUUCCCUAAUCGUACCUUGCUACCAUUGCAUACAUUUAUACCGUCGCCCAGCAAUAAUUUUGAAGCUGUCUAUUUUAUUGAAGCUGCAUUAUGAAGUUGUUUCCGAUGCCCCAAGAGUUCGUCAAGAACCUAUCCCAUGGCCUGUUAAAGCCCAUGGACUCGUCGGUGUUAGCCGUCUUGGAGAAAUUAUAAGACGCUACUCUGUCGUUACAUGUGAAGGGACCACCAGUUGUCACGGUUCACUCUGCGGGCUUUCACCCCCUGGACCGAUUCACGUUUUUUCGUGCCCUAGGGUACCGACAAAAACUCCUGCAUCGUGCGAUUCCAUGGACUCAUCGUGGUUACCCCUGGCUGUUAAUCGCAAGGGCACCGGCAGACCACACAGAAUUAAUACCAACUUGGAAGAACUCGAAAACGGAAGUACUCGGCCACGCGGCCGGUACCCCGGGACGUCGGGUUGGACAGGCGUGACAUUCCAAUGUAAGACGGAAACUCGAAUUACUAUAUUCAUUCAGCCGUGGUUCCGAGACAUCUACGCCUGCCGGCAUAGUCAAGACGCUAUUUCGAUGGCGGGUACCUUGACACUGACAGAAACGACUCUUUUUCCGCAGGGGCAACCUUACCGCUACGAGCACUUUGAUGAGUCAACGUAUCCAUCGGUGCCUCAGAGAACGUAUAACGGCCUAGUCGUCCUAGAUGGCCUCGGUUCUGGUACAACCAGCCCUGUGCUGUUAUUAUUAACAGUCGACCCAAUUCGCUGCAGCUCAGACCACUUAUCAGUGCCAUACAGCACGAACUGGUCGAACCUCAGACUAAUCGCGCAGCGGAUACUAAAUCUUUGGCCCUGCGCUUUUGUAUGUACCCAUGGCCAUACUCCGAUUCAUACUAUGGUGGAUCAGAACCGUACUGAUAGGCAUGAACUGGCGUGCCUCGAAUGCUUUCUGGGGUCUUUAGAAAUACAGAUACCCAAUCCCCAGGAGGGUGGCUACAUCGGCACCUUCCCCGUAGGUAUACUGUUGUGGUUUACGGCCGUGCCUGCCAUCGCAAACGACCUUAUCGCGCCCUCUGGACUUCGCGGCUUAGUAUCUACGGCGCCCAGGUGUUCGCGAAGGUGGUAUAAACACUACGUCCCUCAUGUUUAUUCGCAAGAGUUUGCGCGUCCCUCCAUCGUGUACCUAACGUUACCAAACACGAGUAGAUUCAUAACCAAAAUACUAAUCUUGCUCAUGGGACUUCCAAAAACCAUGCAGUGGAGCAAAGCGCACCAGCUAUGUCAGGUAGGCUCUCUCCGGUUCAAAGGAUUGCUACAGACGUUCGCCUUGGAAUAUUAUACAAAACACGUGUCGGAGGUUGGUUUGAGUUUAAGGCAUCUUAUUACUCGUUUGGCACACAUAGCGCAUCCUGACGUGACGAAUUCGGUUUUUAAGAUCCCGUUUGCUCAGCGUAACGGAGUCUCAGAUUUAGCACGCACAUCUCCACCUACGCAGCCCAUUUUCGCACGUAAACGACCGGAGACAAGACAGGUCGCCCGAGGGGAACAAAUCCCCCGUGAGCGUAAUUUCGAGCUGAGGAAACUGGCGCGUACUAGCACUAACUCCGAGAAUCCCAAGCAAAAUAGAGGGACGGUUUCCUACGUCAGUAUGUGUGCCACAUGUAAUUAUCAGCGCCCUGCGAACACGCAAUGUUGUACCCGUUCCGGCGCGAUAUCAGUUGCCGAAUGGUAUGGACCUCAUAUCGGGCGUUGUCGCGUAUUUACGCUACAUGCGACGGCCAAAAACAAGUGCAUACACUAUGGCAGGCGCCACUUGAACUGGGCCGCGCCCGAGGUCCCGAAAAGCAUAGGGCCGAUGUCGUGCGGGGACUUUCUGUGGGUCAGUACCCCAGAGACCCGAAAUGCUACGUCCGGCAUUCCCGACCUAAGACCCAUGUUGCGUCCGCUGAAUCGGCCAUCCUGGGACAGACGAGGACUCUCGGGUACCCUCAUGUGGCGGACCAGAAGCGAUAUUCUGCGUGUGGCUAUACAUUUGUUGGCGAUCGCUAACAGCCUAUCCCUAUUGCUUAAGCUCUGGCAUCUUAUCUCGAAUCCAUUGAAGAAACCUGAAGAUUGGCUAAUCCUAUCCAGCUUAAGGCCGGAGUUAUGCCGCUUAUAUCCGAGACGUCCUGUCACCCCCCGGGUAAGUUAUGUCUAUAAUAGGCCCCUAUCAUCGCUUAUAAUUCAUAGGCCUGAUGUGAAUCUUGUACGCCCCUGUAUUCUCAAGUCGUGGAAUUAUCACAUGCAAAGGUACACAGUUCGACUGAGUCAGCAGCGGACAUAUAAGAAGUUAUUCAUAUGUUUCAAGCUAGGUGCGCCUUUUCUUCUAAUCUGUUUUUACGUCGUAGGAACUCUUCUUCUGUGGCCGUCUCACCUGGGGAACCGCAAGAACCAUCGACGCUAUCACUGCCGAAUAGUCUUGAGAGGACAAAAUAUAUUCCUCCACGGUUCUCUACCGUAUACACCCGUUAUCCACUUAGAGAGACAACCAAUUCGAUUCGGAGAUGUCUCUAGCCCGUUCUGUCCGUUGUACCAUUGUAGUUCUGGACAUCACUGCCUCUGGUCCACGAGUACCCGUUCGAGCCUUGUUAGAGAGGGGCCCGUUGACUUCAUCCCGUCUCGUGUACUACGACCGUCUGAGCUAUCGAAUGCUUGCGUCGGGGCGGGUCUUAGAGUUGAUCGAAGUGAGGGUGCAAAGAAAUAUGGUGUUGGUCGCCUUCCGUGUAGUGGCAAGGCUGUCAACGCAGGCCGGGCCGCCUCUCGGCUGUUACUGGACAAACCGACGCCUUUUACGCCUAAUUGUGAGCUGCCAUGGUACAGAUUAUGUCCGUGUUUCAACAGCUCGCCGAUAUGGGACAGACUUCCACAAGCCCUGCAGCCAAUGGAUUUCAGGGGAGGUCAUAAGACCACGUGGACGAAGACAUCUCAUAGAUGGUCUAAUGGACGUGGGACAGACACAGUCGCUAUACGUCGAGGCGGAUUAUGCAUUUUGAAUGUCAUUCAUCCGUUGAUCGUCUCGGUGCGUUUGCUUCAGACCCAGCCUCGGCUUCAUUAUCAUCGCCAAUCGAUUGGCCACCUUCCCGCUGGGGUAAGCCCCUCAAUAGAGUUCACUCGCCUGCGACUGUAUAUUGUACACCGCUUGUUUGCUGCGAGCCUACUUCUUACAUCACACAGAGGUGGGCAACUCCGGUGGCUCCUAUACUCACUACACUCCAGCGCUUUAAUACCGUGCAUGAUUAACAACCUUCGUUUAUCACUUGCCGUUUCAGACACGGAGAGUCAGAGUAGGUGGAACUUAAUAGUAGGGGUCCAGUGGCUAUUCCCUAACGUUUGGAAUGGUGUUAGUUUGUUUUCGUCGCGUCAGAGAGAGGGUCGUCAGAAGGCUAGUUGCGUACCUAUUUUCUACGACAUGCGGUGCAGAUGCGGGGACUUUACCUUUAGGAAGAUACAUGAUACGCGGAGUAUGUCGAUGUGCCGUGUCUAUCAUGAACCGCCUAGGCGAUUGGUGCGAAGUUCAUUGAUUAUACCCUUACAGCCAAAGCACUUCUUCGAGGAGUUACGUGCAAAACACCUCCACAACCUCCUACGCAAGAUUAACGGAAUAACGGUAAGAUCCUACUUUUCUGUAGCAAUAGAGUUAGAGCAUCGGAUGUUGCCAUCACUCCCGAGUACACCCUUCAAGAUCUCAUUGAUAACUUUCAGGCUACAAUACAAAUGCGCGCGUGGCGGUUGGUCCUUCCCACCCUCAGUGGAUUCUCAAUUUGAGUGCGUGUCUGGUCCCGCGCAGGUCCGCUGGCCGUCUAUCUUGUACCCUAUCGUAGAGAAAUGUGGCUUAGGAAAAGGCAUUCAUCCAAACAGUUACGCGAAUGCCACGAUGAACGUACUGGUCAGAAGUACAGGAACUUUACAUCGGGACGGGUCACUCGCCGAAUCGUUACUUUGGUGUGUUUAUCCGACUACACGAGUUAUUGCAGAUCUAAAAGCCGGGUUCUUUGUACUUGCAGCUCCAAGUUGGCGUACGCGCGUGACGCAGAGGGGGGUCCACAUUUAUGAAAACAGAGUACGGCCAAACUGUAAUAGGUUACGAAAUUCGCACGCUCGAGGACGGUGCCCCCUCCAAGGAGUAGAUUAUCCCAUUGAAUGGAAUAGAACUCUUACGACUGGAACGAAUCUUCUGCGGGAACCGGCCAUGGCCCAAGAGAGGUUGAGCUAUGAGCUUUAUCUGAGAUUACACCGAUCCGUCACACUGACCUGGCGUCCCGUUUAUGCGUAUGUGCCUUGCCGCAGGAGCGGCGACGAAGUAGUGUCAACUGUGAGAAUCCAACAAGGGGAACGUAUGCCAAAGGUUAUGCAUUUUCGCGAACGCCGGGGGAUUCUACCUAAAGGAGAAUUCGGAGAGCGCACCUCGCAAGGCCUACGACGCAUAUCCUUACUACUGUUCGAGACUCGCCAUGUGCCAUGGAUCCUUAAAGCCGCUUGUUUAGAUGCUUGGCCCCUUUUUAAUCGGUACCCUGUGGCAGAAUUGACGCGAAGAUAUAUAGGUUGCGCACAACGGGUGGCUUGGCCGCAAUCGGCUGUGUCGAUUUUGGACCGACAUCACCUUACACGCUGGCUCUACAAAAUGGGCGGGCACGACGGCGAUCACAGAUUGCGUACUUACCAAAGAAAUUUCAAUUUCUACAACGAUUGGCAGACUUCUCACUCUGAAGCGUUGGGUUUGGACACGAUCCCGCGGAUGCAAAGGUCCUCCAACCGUUAUUGCGAGAGAACGGCCCGGCGCCCAGUUCAAAACGUUGGCAGCAUUAUGUUUAUCCGACCCCUGGCCCCCACAAAGCCAAGCCGCUUCCGCAUCCUGGCCAGUAUUGUCAGCCCAAGAACCAAUGGGCCUGCAUAG'

p = traverseCodon(s)
print (p)
