
def open_fasta (filename):
    f= open (filename , "r")
    sequence = []
    for line in f :
        if line[0] != ">":
            sequence.append(line.strip())
    return "".join(sequence)
    f.close()


def tableau_suffixes(tab):
    tab_s = []
    n = len(tab)
    for i in range(n):
        tab_s.append([tab[i:],i])
    return tab_s


def classement (tab_s):
    for i in sorted(tab_s):
        print(i)

def main():
    filename = "/home/yayu/Documents/BIN1002/TP3/ORF.fasta"
    tab = open_fasta(filename)
    tab_s =tableau_suffixes(tab)
    classement(tab_s)
main()
