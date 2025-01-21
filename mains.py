import random
import os
import json

"""
Créer une fonction qui charge les mots du fichier
"""
def charger_mots(fichier):
    if not os.path.exists(fichier):
        with open(fichier, "w") as file:
            pass  # Crée un fichier vide
    with open(fichier, "r") as file:
        mots = file.read().splitlines()
    return mots

"""
Ajouter un mot à mon fichier texte
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
Charger les scores depuis un fichier JSON
"""
def charger_scores(fichier_scores):
    if not os.path.exists(fichier_scores):
        with open(fichier_scores, "w") as file:
            json.dump({}, file)  # Crée un fichier JSON vide avec un dictionnaire
    with open(fichier_scores, "r") as file:
        return json.load(file)

"""
Sauvegarder les scores dans un fichier JSON
"""
def sauvegarder_scores(fichier_scores, scores):
    with open(fichier_scores, "w") as file:
        json.dump(scores, file, indent=4)

"""
Mettre à jour le score d'un joueur
"""
def mettre_a_jour_score(fichier_scores, joueur, points):
    scores = charger_scores(fichier_scores)
    if joueur not in scores:
        scores[joueur] = {"points": points, "defaites": 0}  # Assurez-vous que c'est un dictionnaire
    else:
        scores[joueur]["points"] += points
    sauvegarder_scores(fichier_scores, scores)

"""
Mettre à jour le score en cas de défaite
"""
def mettre_a_jour_score_defaite(fichier_scores, joueur):
    scores = charger_scores(fichier_scores)
    if joueur not in scores:
        scores[joueur] = {"points": 0, "defaites": 1}  # Assurez-vous que c'est un dictionnaire
    else:
        if scores[joueur]["points"] == 0:
            scores[joueur]["defaites"] += 1
        else:
            scores[joueur]["defaites"] = 1

        if scores[joueur]["defaites"] >= 2:
            scores[joueur]["points"] += 2
            print(f"{joueur} a reçu 2 points en moins pour avoir perdu.")
    sauvegarder_scores(fichier_scores, scores)

"""
Afficher les scores
"""
def afficher_scores(fichier_scores):
    scores = charger_scores(fichier_scores)
    if not scores:
        print("\nAucun score enregistré pour le moment.")
    else:
        print("\n=== Scores ===")
        for joueur, data in scores.items():
            # Assurez-vous que data est un dictionnaire avec les clés 'points' et 'defaites_consecutives'
            if isinstance(data, dict):  # Vérifiez si 'data' est bien un dictionnaire
                print(f"{joueur}: {data['points']} points (Défaites consécutives : {data['defaites_consecutives']})")
            else:
                print(f"Erreur avec les données de {joueur}. Les données ne sont pas sous la forme attendue.")

"""
Créer le menu principal
"""
def menu_principal(fichier_mots, fichier_scores):
    while True:
        print("\n=== Menu Principal ===")
        print("1. Jouer")
        print("2. Ajouter un mot")
        print("3. Afficher les scores")
        print("4. Quitter")

        choix = input("Choisissez une option (1-4) :")

        if choix == "1":
            jouer(fichier_mots, fichier_scores)
        elif choix == "2":
            ajouter_mot(fichier_mots)
        elif choix == "3":
            afficher_scores(fichier_scores)
        elif choix == "4":
            print("À la prochaine !!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

"""
Fonction jouer
"""
def jouer(fichier_mots, fichier_scores):
    mots = charger_mots(fichier_mots)
    if not mots:
        print("La liste des mots est vide. Ajoutez des mots avant de jouer.")
        return

    mot_mystere = random.choice(mots).lower()
    mot_public = "_" * len(mot_mystere)
    lettres_proposees = []
    nb_vies = 7

    joueur = input("Entrez votre nom : ")

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
        print(f"\nBravo, {joueur}, vous avez trouvé le mot : {mot_mystere} !")
        mettre_a_jour_score(fichier_scores, joueur, 10)  # Ajouter 10 points pour une victoire
    else:
        print(f"\nDésolé, {joueur}, vous avez perdu... Le mot était : {mot_mystere}.")
        mettre_a_jour_score_defaite(fichier_scores, joueur)

if __name__ == "__main__":
    mots_file = "mots.txt"
    scores_file = "scores.json
    "
    menu_principal(mots_file, scores_file)
