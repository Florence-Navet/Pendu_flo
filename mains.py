import random
import os

"""
Creer une fonction qui charge les mots du fichier
"""
def charger_mots(fichier):
    if not os.path.exists(fichier):
        with open(fichier, "w") as file:
            pass  # Crée un fichier vide
    with open(fichier, "r") as file:
        mots = file.read().splitlines()
    return mots

"""
ajouter un mot à mon fichier texte
"""
def ajouter_mot(fichier):
    mots_existants = charger_mots(fichier)
    nouveau_mot = input("Entrez un mot à ajouter : ").lower()
    if not nouveau_mot.isalpha():
        print("Veuillez entrer un mot valide.")
        return

    if nouveau_mot in mots_existants:
        print(f"Le mot '{nouveau_mot}' existe déjà.")
    else:
        with open(fichier, "a") as file:
            file.write(nouveau_mot + "\n")
        print(f"Le mot '{nouveau_mot}' a été ajouté avec succès.")

"""
Créer le menu principal
"""
def menu_principal(fichier):
    while True:
        print("\n=== Menu Principal ===")
        print("1. Jouer")
        print("2. Ajouter un mot")
        print("3. Quitter")

        choix = input("Choisissez une option (1-3) :")

        if choix == "1":
            jouer(fichier)
        elif choix == "2":
            ajouter_mot(fichier)
        elif choix == "3":
            print("À la prochaine !!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

"""
fonction jouer
"""
def jouer(fichier):
    mots = charger_mots(fichier)
    mot_mystere = random.choice(mots).lower()
    mot_public = "_" * len(mot_mystere)
    lettres_proposees = []
    nb_vies = 7

    while nb_vies > 0 and mot_public != mot_mystere:
        print(f"\nMot à deviner : {mot_public}")
        print(f"Vies restantes : {nb_vies}")
        lettre = input("Entrez une lettre : ").lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue

        if lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre.")
            continue
        lettres_proposees.append(lettre)

        if lettre in mot_mystere:
            for i in range(len(mot_mystere)):
                if mot_mystere[i] == lettre:
                    mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
        else:
            nb_vies -= 1
            print(f"Erreur ! La lettre '{lettre}' n'est pas dans le mot.")

    if mot_public == mot_mystere:
        print(f"\nBravo, vous avez trouvé le mot : {mot_mystere} !")
    else:
        print(f"\nDésolé, vous avez perdu... Le mot était : {mot_mystere}.")

if __name__ == "__main__":
    menu_principal("mots.txt")
