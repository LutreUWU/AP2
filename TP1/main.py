########################################
"""Exo 1 Question 1"""
def saisir_information(AllStudent:list):
    """
    Fonction qui permet de créer un dictionnaire avec les informations d'un étudiant :
    (Numéro Etudiant, Nom Prenom, Date de naissance, note AP1).
    Puis on l'ajoute à la liste des etudiants.
    Quelques paramètres ont été ajouté pour éviter qu'on écrive n'importe quoi.
    Attention si vous faites une erreur il faut tout recommencer du début
    (La seule solution que j'avais trouvé était de séparer en plusieurs fonctions chaque paramètres mais comme le TP demandait UNE SEULE fonction)
    
    Paramètres:
    - AllStudent: liste des étudiants, vide à l'origine
    
    Return:
    AllStudent remplis     
    """
    StudentInformation = {}
    # Numéro étudiant
    numero = input('Ecrire un numéro étudiant: ')
    # On vérifie si on a écrit un chiffre et qu'on a écrit 6 chiffres.
    if len(numero) != 6 or not numero.isnumeric(): # Si ce n'est pas le cas on recommence la fonction
        print('Numéro étudiant incorrect')
        saisir_information([])
    # Si la vérification est validé, on peut le mettre dans le dictionnaire 
    StudentInformation['Numero'] = numero
    # Nom et prenom
    nom, prenom = input('Ecrire un Nom: '), input('Ecrire un Prenom: ')
    # Même chose pour le Nom et Prenom
    # On vérifie si on a écrit du texte 
    if nom.isnumeric() or prenom.isnumeric():
        print('Nom ou Prénom incorrect, recommencez du début: ')
        saisir_information([])
    StudentInformation['Nom'] = nom
    StudentInformation['Prenom'] = prenom
    # Date de naissance
    Jour = input('Jour de naissance: ')
    Mois = input('Mois de naissance: ')
    Annee = input('Annee de naissance: ')
    # On vérifie on a écrit du chiffre 
    if Jour.isnumeric() and Mois.isnumeric() and Annee.isnumeric():
        Jour, Mois, Annee = int(Jour), int(Mois), int(Annee)
        if Jour <= 31 and Mois <= 12 and Annee < 2024: # La vérification n'est pas précise et j'ai trouvé aucune solution (Le module datetime peut être ?)
            StudentInformation['Date_de_naissance'] = f'{Jour}/{Mois}/{Annee}'
    else:
        print('Date de naissance incorrect, recommencez du début: ')
        saisir_information([]) 
    # Note obtenue
    Note = input('Note obtenu en AP1 (Chiffre entier seulement): ')
    # On vérifie si on a écrit un chiffre 
    if Note.isnumeric():
        Note = int(Note)
        if Note <= 20: # On suppose que c'est une note sur 20
            StudentInformation['Note_AP1'] = Note
    else:
        print('Note ILLOGIQUE, recommencez du début: ')
        saisir_information([]) 
    AllStudent.append(StudentInformation)
    return AllStudent

"""Exo 1 Question 2"""
def cree_liste_etudiant(nombre_etudiant:int):
    """
    Fonction qui permet de créer la liste qui contient les étudiants 
    en fonction du nombre d'étudiants qu'on a spécifié.
    
    Paramètres:
    nombre_etudiant: nombre d'étudiants

    Return:
    Liste où chaque éléments est un dictionnaire avec les paramètres d'un étudiants
    """
    AllStudent = []
    for i in range(nombre_etudiant):
        saisir_information(AllStudent)
    return AllStudent

"""Exo 1 Question 3"""
def afficher_etudiant(AllStudent:list):
    """
    Fonction qui permet d'afficher les paramètres de chaque étudiants
    sur le terminal
    
    Paramètres:
    AllStudent: Liste de dictionnaire 

    Return:
    Terminal
    """
    for elem in AllStudent:
        print(f'{elem["Numero"]} : {elem["Nom"]} {elem["Prenom"]} {elem["Date_de_naissance"]} -  Note :{elem["Note_AP1"]}')

"""ListStudent = cree_liste_etudiant(2)
afficher_etudiant(ListStudent)"""
########################################
"""Exo 2 Question 1"""
def ajoute_occurence(dico:dict, mot:str):
    """
    Fonction qui vérifie dans un dictionnaire si le mot
    en paramètre est dans le dictionnaire ou non.
    Si c'est le cas elle ajoute +1, sinon elle le crée.
    
    Paramètres:
        dico : Dictionnaire
        mot : mot qu'on souhaite savoir s'il est dans le dictionnaire ou non
    Return:
        dico après avoir vérifier     
    """
    # Si le mot est dans le dictionnaire 
    if mot in dico.keys():
        dico[mot] += 1 # Alors on ajoute +1
    else:
        dico[mot] = 1 # Sinon on la crée avec 1 comme origine 
    return dico
"""Exo 2 Question 2"""
def supprime_ponctuation(mot:str):
    """
    Fonction qui permet d'enlever les ponctuations
    dérangeants grâce au module string 
    
    Paramètres:
        mot : mot qu'on souhaite vérifier s'il y a la ponctuation ou non
    Return:
        Le mot sans les ponctuations    
    """
    import string
    # Variable pour créer le nouveau mot sans les ponctuations 
    new_world = ""
    # Pour chaque lettre dans le mot
    for elem in mot: 
        # Si la lettre n'est pas la liste des ponctuations interdites 
        if elem not in string.punctuation:
            new_world += elem # Alors on peut ajouter cette lettre 
    # Si la variable n'est pas vide c'est que une ponctuation a été détecter alors on return le nouveau mot
    if new_world != "":
        return new_world
    # Sinon on retourne le mot d'origine 
    return mot

"""Exo 2 Question 3"""
def compte_mots(dico:dict, chaine:str):
    """
    Fonction qui prend un dictionnaire et une chaîne de caractères en paramètre
    et renvoie le même dictionnaire contenant le nombre d’occurrences de chaque mot de la chaîne.
    Paramètres:
        dico : Dictionnaire vide à l'origine
        chaine : Mot dont on souhaite savoir le nombre d'occurence 
    Return:
        Le mot sans les ponctuations   
    """
    # On supprime les ponctuations du mots
    new_world = supprime_ponctuation(chaine)
    # Pour chaque lettre dans le mot
    for elem in new_world:
        # On réutilise la fonction de la Question 1 
        dico = ajoute_occurence(dico, elem)
    return dico
"""Exo 2 Question 4"""
# Je ne sais pas si c'est ce qu'il fallait faire, mais on l'a fait en 1 ligne, on a récupérer la valeurs de chaque clé du dictionnaire et on les a additionné
def compte_mots_total(dico:dict):
    return sum(dico.values())
"""Exo 2 Question 5 & 6"""
from sys import argv
fichier = argv
texte = open(fichier[1], "r")
lignes = texte.readlines()
dico = {}
i = 0 # Pour savoir combien de mot on a dans le fichier
# Pour chaque ligne de texte  
for ligne in lignes:
    # On crée une liste où chaque élément est un mot de la ligne 
    ligne = ligne.split(" ")
    for world in ligne: # Pour chaque mot dans la liste 
        i += 1
        world = world.replace("\n", "") # On retire les sauts à la ligne
        # On réutilise une fonction pour connaître le nombre d’occurrences dans la fichier texte 
        dico = compte_mots(dico, world) 
"""Exo 2 Question 7"""
def affiche_mots(fichier):
    """
    Fonction qui prend en paramètre un fichier, puis elle affiche sur le terminal
    le nombre de mots, de mots différents, et le nombre d'occurences de chaque mots dans le fichier

    Args:
        fichier: fichier .txt

    Returns:
        Les informations sur le terminal
    """
    # C'est quasiment la même chose que la Question 5 et 6 
    dicoQ7 = {}
    texte = open(fichier, "r")
    lignes = texte.readlines()
    for ligne in lignes:
        ligne = ligne.split(" ")
        for world in ligne:
            world = world.replace("\n", "")
            world = supprime_ponctuation(world)
            # Sauf qu'on appelle la fonction pour les mots et pas celle pour les lettres 
            dicoQ7 = ajoute_occurence(dicoQ7, world)
    nb_mots = compte_mots_total(dicoQ7) # Pour récupérer le nombre de mot total
    nb_mots_différent = len(dicoQ7) # Pour récumer le nombre de mots différent
    for elem in dicoQ7: # On print le nombre d’occurrences de chaque mot dans le fichier.
        print(f"{elem} : {dicoQ7[elem]}")
    # Et on print les données sur le nombre de mots / mots différents 
    print(f"nombre de mots: {nb_mots} - nombre de mots différents: {nb_mots_différent}") 
dic_world = affiche_mots("sense_short.txt")

"""Exo 2 Question 8"""
'Pour faire les améliorations:'
'''- Filtrer par taille de mots: On crée une liste avec tous les mots, puis on parcoure la longuer de chaque mot avec len(),
     puis quand on aura len(mot) > len(longest_worlds), alors len(longest_worlds) = len(mot). Puis on print le mot et on supprime le mot de la liste
   - Filtrer par nombre d'occurence, même chose mais cette fois-ci, on crée une liste où chaque éléments est un dictionnaire puis on regarde la valeur de chaque clés ...

'''

