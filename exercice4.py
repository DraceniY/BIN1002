from util2 import *

def translateCodon(s):
    su = s.upper()
    if len(su) != 3:
        return '?'
    if not su in aminoAcidMap:
        return '?'
    return aminoAcidMap[su]

#print translateCodon("ACT")
#print translateCodon("act")
#print translateCodon("ac")
#print translateCodon("acgt")
#print translateCodon("XKK")

def splitCodons(s):
    if len(s) % 3 != 0:
        print "sequence is not a multiple of 3"
        return None
    L = []
    for i in range(0,len(s),3):
        L.append(s[i:i+3])
    return L

#print splitCodons("aCgTaaCCTTggCGT")
#print splitCodons("aCgTaaCCTTggCG")
#print splitCodons("")

def translateSequence(s):
    codons = splitCodons(s)
    res = ""
    if codons == None:
        return None
    for c in codons:
        res += translateCodon(c)
    return res

#print translateSequence("aCgTaaCCTTggCGT")
#print translateSequence("aCgTaaCCTTggCG")
#print translateSequence("")

def findStartPositions(s):
    su = s.upper()
    L = []
    for i in range(0,len(su)-2):
        if su[i:i+3] == startCodon:
            L.append(i)
    return L

#print findStartPositions("ATG")
#print findStartPositions("AATATG")
#print findStartPositions("AATGGGTCCGT")
#print findStartPositions(approximateGenes[0])

def findNextCodon(s,spos,codon):
    codonu = codon.upper()
    su = s.upper()
    for i in range(spos,len(su)-2,3):
        if su[i:i+3] == codonu:
            return i

#print findNextCodon("ACG",0,"acg" )
#print findNextCodon("AACG",1,"acg" )
#print findNextCodon("CG",1,"acg" )
#print findNextCodon("gtaagta",1,"gta" )
#print findNextCodon('aaaaabbbaabbaa', 1, 'bba')

def findNextStopCodon(s,start):
    pos = len(s)
    for scodon in stopCodons:
        idx = findNextCodon(s,start,scodon)
        if idx != None:
            pos = min(pos,idx)
    if pos == len(s):
        return None
    return pos

#print findNextStopCodon("TGA",0)
#print findNextStopCodon("TgA",1)
#print findNextStopCodon("TTgA",0)
#print findNextStopCodon("TTgA",1)
#print findNextStopCodon('AAATAGATGAAAA', 1)

def findOpenReadingFrames(s):
    L = []
    for i in range(3):
        start = i
        while start != None:
            start = findNextCodon(s,start,startCodon)
            if start != None:
                stop = findNextStopCodon(s,start)
                if stop != None:
                    L.append((start,stop))
                start += 3
    return L

#print findOpenReadingFrames(approximateGenes[0])
#print findOpenReadingFrames(approximateGenes[1])


def translateOpenReadingFrames(s):
    orfs = findOpenReadingFrames(s)
    L = []
    for i,j in orfs:
        aas = translateSequence(s[i:j+3])
        if aas == None:
            print "ERROR"
            return None
        L.append(aas)
    return L

#print translateOpenReadingFrames("ATGCTGTAA")
#print translateOpenReadingFrames("ATGCTGTAAA")
#print translateOpenReadingFrames("ATGCTzTAA")
#print translateOpenReadingFrames(approximateGenes[0])
#print translateOpenReadingFrames(approximateGenes[1])

def findCodonBias(s):
    """
    Computes the codon bias by using a dictionary mapping amino acids (aa) to dictionaries (d_aa). For each aa the associated dictionary, d_aa, is used to count the number of times different codons code for a specific amino acids.
    """
    su = s.upper() #make all letters in the sequence upper case
    dict = {} # create an empty dictionary
    # the following fills dict with amino acids as keys and dictionaries as values. The dictionary associated with each amino acid is used to count the number of codons which codes for the amino acid in the sequence
    for k,v in aminoAcidMap.items(): #run through all codon -> amino acid pairs
        if v in dict: # if an amino acid is already in the dictionary
            dict[v][k] = 0 # look up the amino acid which gives us another dictionary. Then we look up the codon in the second dictionary and set it to 0
        else: # if the amino acid is not in the dictionary
            temp = {k : 0} # make a new dictionary with one codon mapping to a zero
            dict[v] = temp # insert the new dictionary in dict with the amino acid 'v' as the key
    # Now we have a dictionary with dictionaries which we can use to compute the codon bias
    protein = translateSequence(su) #translate the sequence into amino acids
    for i in range(len(protein)): # Run through the length of the protein
        codon = su[i*3:i*3+3] # retrieve the codon
        aa = protein[i] # retrieve the amino acid
        dict[aa][codon] += 1 # add one to the number with key=codon in the dictionary with key=aa
    # now we have counted the number of times that each codon have coded for their amino acid
    for k,v in dict.items(): #run through all key -> value pairs in dict
        total = 0 # make a variable to count stuff
        for l,m in v.items(): # run through all key -> value pairs in dictionary associated with the key 'k'
            total += m # count the total number of codons which code for the amino acid 'k'
        if total == 0: # if there's no codons coding for this amino acid
            del dict[k] # delete the entry (we don't) want to display unused amino acids
        else:
            for l,m in v.items(): # run through all the codons coding for the amino acid 'k'
                v[l] = m/float(total) # compute frequency by wich this codon code for the amino acid 'k' relative to other codons coding for the same amino acid
    return dict # return the dictionary

#print findCodonBias(exactGenes[0])

def printCodonBias(s):
    dict = findCodonBias(s)
    for k,v in dict.items():
        print k + ":"
        for l,m in v.items():
            print "  " + l + ":" + str(int(m*100)) + "%"

#printCodonBias(exactGenes[0])
