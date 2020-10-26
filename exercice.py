#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici



# TODO: Définissez vos fonction ici

def compare(nom_fichier1, nom_fichier2):
    with open(nom_fichier1, "r") as fichier1, open(nom_fichier2, "r") as fichier2:
        
        same = True

        while same:
            a = fichier1.read()
            b = fichier2.read()

            same = a == b
    
        return -1 if same else fichier1.tell()

#2. Écrire un programme qui recopie un fichier texte en triplant tous les 
#espaces entre les mots. 
#(vous pouvez ouvrir deux fichiers avec l’instruction with).
def espace(nom_fichier1, nom_fichier2):
    with open(nom_fichier1, "r") as fichier1, open(nom_fichier2, "w") as fichier2:
        fichier2.write(fichier1.read().replace(" ","   "))
    



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(compare("test1.txt", "test2.txt"))
    print(espace("test1.txt", "rallonge"))
    pass
