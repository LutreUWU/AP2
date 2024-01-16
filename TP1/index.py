########################################
"""Exo 3"""
from sys import argv

fichier = argv
texte = open("couplet1.txt", "r")
lignes = texte.readlines()
lineList= [] # Future liste où chaque élément sera une liste (= une ligne de texte) où chaque élément est un mot  
dico = {}
for ligne in lignes:
    lineWorld = []
    ligne = ligne.split(" ")
    for world in ligne:
        world = world.replace("\n", "")
        lineWorld.append(world)
        if world not in dico.keys():
            dico[world] = 1
        else:
            dico[world] += 1
    lineList.append(lineWorld)
for elem in dico: # Pour chaque mot dans le dictionnaire
    IndexWorld = []
    for i, ligne in enumerate(lineList): # On parcoure la liste qui permettra de savoir la ligne où le mot apparaît 
        for world in ligne:
            if elem == world:
                IndexWorld.append(i)
    print(f"{elem} : {IndexWorld}")
            
