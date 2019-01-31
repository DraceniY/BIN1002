# -*- coding: utf-8 -*-
# TP 4 alignement :
# Le programme aligne deux séquences et affiche une matrice d'alignement
# Si la séquence A a un match avec la séquence B le programme affiche "-" si c'est un mismatch le programme affiche "*"

def analyse_fasta ():
    # Cette fonction ouvre le fichier fasta et retourne les deux séquences
    f = open ("/home/yayu/Documents/BIN1002/TP4/data.fasta")
    sequences = []
    for line in f :
        if line[0] != ">":
            sequences.append(line.strip())
    return sequences

def alignement(sequences):
    # Cette fonction aligne les deux séquences et retourne un tableau d'alignement
    seq1 = sequences[0]
    seq2 = sequences[1]
    n = len(seq1)
    m = len(seq2)
    tableau_alignement=[]
    for i in range(n):
      for j in range(m):
        if seq1[i] == seq2[j]:
            tableau_alignement.append("-")
        elif seq1[i] != seq2[j]:
          tableau_alignement.append("*")


    return tableau_alignement

def afficher_alignement (tableau_alignement):
    # cette fonction affiche l'alignement
    ligne =""
    for j in range(len(tableau_alignement)):
        if j == 0 :
            ligne += str(tableau_alignement[j])
        elif j % 50 == 0 :
            ligne += str(tableau_alignement[j]) + "\n"
        else:
            ligne += str(tableau_alignement[j])
    print ligne

def main():
    # fonction main qui appele les autres fonctions
    sequences = analyse_fasta()
    tableau_alignement = alignement(sequences)
    afficher_alignement(tableau_alignement)


main()
