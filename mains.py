import random
import pygame

"""
Creer une fonction qui charge les mots du fichier
"""
def charger_mots(fichier):
    
    with open(fichier, "r") as file :
        mots = file.read().splitlines()
    return mots 


"""
ajouter un mot un mot à mon fichier texte
"""
def ajouter_mot(fichier):
    nouveau_mot = input("Entrez un mot à ajouter : ").lower()
    if nouveau_mot.isalpha():  # Vérifie que le mot ne contient que des lettres
        with open(fichier, "a") as file: # pour append
            file.write(nouveau_mot + "\n")
        print(f"Le mot '{nouveau_mot}' a été ajouté avec succès.")
    else:
        print("Veuillez entre un mot valide.")


"""
Créer le menu principal
"""
def menu_principal(fichier):
    while True:
        print("\n=== Menu Principal ===")
        print("\n=== 1. Jouer ===")
        print("\n=== 2. Ajouter un mot ===")
        print("\n=== 3. Quitter ===")

        choix = input("Choissisez une option (1-3) :")

        if choix == "1":
            jouer(fichier)
        elif choix == "2":
            ajouter_mot(fichier)
        elif choix == "3":
            print("A la prochaine !!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


"""
fonction jouer
"""
def jouer(fichier):
    mots = charger_mots(fichier)
    mot_mystere = random.choice(mots)
    mot_affiche = "_"  * len(mot_mystere)
    lettres_proposes = []
    nnb_vies = 0
    max_vies = 7


if __name__ == "__main__":
    menu_principal("mots.txt")


