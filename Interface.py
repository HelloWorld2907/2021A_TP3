# -*- coding: utf-8 -*-

import random


def saisirMatrice():
    #To do: Saisit une matrice d’adjacence au clavier
    resultat=[]
    nbdenoeuds=int(input('Donner le nombre de noeuds dans la matrice:'))
    nbdepoids=int(input('Donner le nombre de poids dans la matrice:'))

    if nbdenoeuds==0:
        return None

    noeudsinit=[-1]*nbdenoeuds

    for i in range(nbdenoeuds):
        noeudsinit2=noeudsinit[:]
        resultat.append(noeudsinit2)
    print('')
    for p in range(nbdepoids):
        print(f'	 saisir le poids {p}:')
        rep1=int(input(f"		 saisir le noeud d'extremité 1:"))
        rep2=int(input(f"		 saisir le noeud d'extremité 2:"))
        poids=int(input(f"		 saisir le poids:"))
        (resultat[1])[2] = poids
        if rep1!=rep2:
            (resultat[rep1])[rep2]=poids
            (resultat[rep2])[rep1]=poids

    
    return resultat
def genereMatriceAleatoire(nb_noeuds):
    #To do: Génère une matrice d’adjacence de manière aléatoire
    resultat=[]
    noeudsinit = [-1] * nb_noeuds

    for i in range(nb_noeuds):
        noeudsinit2 = noeudsinit[:]
        resultat.append(noeudsinit2)
    for ligneindex in range(len(resultat)):
        compteur=0
        listrempli=[]

        while compteur<(nb_noeuds/2):
            nb=random.randint(1,99)
            index=random.randint(0,nb_noeuds-1)
            a=(resultat[ligneindex])[index]

            if a<0 and index!=ligneindex:
                (resultat[ligneindex])[index]=nb
                (resultat[index])[ligneindex] = nb
            compteur += 1


    
    return resultat

def afficheChemin(predecesseurs, depart, arrive):
    #To do: Affiche le chemin entre un nœud de départ et d’arrivé à partir du tableau de prédécesseurs
    listechemin=[]
    listetemporaire=[]


    noeud=arrive
    while predecesseurs[noeud]!=depart:
        noeud=predecesseurs[noeud]
        listetemporaire.append(noeud)




    for i in range(len(listetemporaire)-1,-1,-1):
        listechemin.append(listetemporaire[i])



    #Création de la phrase chemin
    chemin = "DEBUT : {}".format(depart)
    for val in listechemin:
        chemin += "  ==> {}".format(val)
    chemin += "  ==> {}: FIN \n".format(arrive)
    chemin = "Le chemin à parcourir est:\n\t" + chemin
    return chemin
