import random
import os
import json

"""
fonction chargement mots
"""

# Fonction pour charger les mots du fichier
def charger_mots(fichier):
    if not os.path.exists(fichier):
        with open(fichier, "w") as file:
            pass  # Crée un fichier vide si le fichier n'existe pas encore
    with open(fichier, "r") as file:
        mots = file.read().splitlines()  # Charge les mots ligne par ligne
    return mots

# Fonction pour ajouter un mot au fichier
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
json pour score
"""

# Fonction pour charger les scores depuis un fichier JSON
def charger_scores(fichier_scores):
    if not os.path.exists(fichier_scores):
        with open(fichier_scores, "w") as file:
            json.dump({}, file)  # Crée un fichier JSON vide avec un dictionnaire
    with open(fichier_scores, "r") as file:
        scores = json.load(file)
        
        return scores

# Fonction pour sauvegarder les scores dans un fichier JSON
# Fonction pour sauvegarder les scores dans un fichier JSON
def sauvegarder_scores(fichier_scores, scores):
    with open(fichier_scores, "w") as file:
        json.dump(scores, file, indent=4)

   


# Fonction pour mettre à jour le score d'un joueur après une victoire
def mettre_a_jour_score(fichier_scores, joueur, points):
    scores = charger_scores(fichier_scores) #charge les  scores
    joueur = joueur.lower()#converti le nom du joueur en minuscule

    if joueur not in scores:
        scores[joueur] = {"points": points, "victoires": 1, "defaites": 0, "defaites_consecutives": 0}  # Si le joueur n'existe pas, l'ajouter avec les points
    else:
        scores[joueur]["points"] += points  # Ajouter les points au joueur existant
        scores[joueur]["victoires"] += 1  # Incrémenter le nombre de victoires
        scores[joueur]["defaites_consecutives"] = 0  # Réinitialiser le compteur de défaites consécutives

    sauvegarder_scores(fichier_scores, scores)

"""
fonction mettre à jour le score du joueur
"""

# Fonction pour mettre à jour le score d'un joueur après une défaite
def mettre_a_jour_score_defaite(fichier_scores, joueur):
    scores = charger_scores(fichier_scores)
    joueur = joueur.lower()

    if joueur not in scores:
        # Initialiser le joueur avec 0 points, 0 victoires et 1 défaite
        scores[joueur] = {"points": 0, "victoires": 0, "defaites": 1, "defaites_consecutives": 1}
        
    else:
        scores[joueur]["defaites"] += 1  # Incrémenter le nombre de défaites
        scores[joueur]["defaites_consecutives"] += 1  # Incrémenter le nombre de défaites consécutives
       

        # Réduire les points en fonction des défaites consécutives
        if scores[joueur]["defaites_consecutives"] == 2:
            scores[joueur]["points"] -= 3  # Réduire de 3 points pour 2 défaites consécutives (1 point pour chaque défaite + 1 point supplémentaire)
           
        else:
            scores[joueur]["points"] -= 1  # Réduire de 1 point pour chaque défaite
            print(f"{joueur} a perdu 1 point pour une défaite.")

    sauvegarder_scores(fichier_scores, scores)



# Fonction pour afficher les scores
def afficher_scores(fichier_scores):
    scores = charger_scores(fichier_scores)
    if not scores:
        print("\nAucun score enregistré pour le moment.")
    else:
        print("\n=== Scores ===")
        for joueur, data in scores.items():
            print(f"{joueur.capitalize()}: {data['points']} points (Victoires : {data['victoires']} - Défaites : {data['defaites']})")

# Menu principal du jeu
def menu_principal(fichier_mots, fichier_scores):
    while True:
        print("\n=== Menu Principal ===")
        print("1. Jouer")
        print("2. Ajouter un mot")
        print("3. Afficher les scores")
        print("4. Quitter")

        choix = input("Choisissez une option (1-4) : ")

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

# Fonction pour jouer une partie
def jouer(fichier_mots, fichier_scores):
    mots = charger_mots(fichier_mots)
    if not mots:
        print("La liste des mots est vide. Ajoutez des mots avant de jouer.")
        return

    mot_mystere = random.choice(mots).lower()  # Choisir un mot aléatoire
    mot_public = "_" * len(mot_mystere)  # Créer le mot à deviner avec des underscores
    lettres_proposees = []  # Liste des lettres déjà proposées
    nb_vies = 7  # Nombre de vies initiales

    joueur = input("Entrez votre nom : ")

    while nb_vies > 0 and mot_public != mot_mystere:
        print(f"\nMot à deviner : {mot_public}")
        print(f"Vies restantes : {nb_vies}")
        lettre = input("Entrez une lettre : ").lower()

        # Vérifier que l'utilisateur entre bien une seule lettre
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide.")
            continue

        # Vérifier si la lettre a déjà été proposée
        if lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre.")
            continue
        lettres_proposees.append(lettre)

        # Si la lettre est dans le mot mystère, révéler ses positions
        if lettre in mot_mystere:
            for i in range(len(mot_mystere)):
                if mot_mystere[i] == lettre:
                    mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
        else:
            nb_vies -= 1  # Si la lettre n'est pas dans le mot, perdre une vie
            print(f"Erreur ! La lettre '{lettre}' n'est pas dans le mot.")

    # Vérification du résultat du jeu
    if mot_public == mot_mystere:
        print(f"\nBravo, {joueur}, vous avez trouvé le mot : {mot_mystere} !")
        mettre_a_jour_score(fichier_scores, joueur, 5)  # Ajouter 5 points pour une victoire
    else:
        print(f"\nDésolé, {joueur}, vous avez perdu... Le mot était : {mot_mystere}.")
        mettre_a_jour_score_defaite(fichier_scores, joueur)

if __name__ == "__main__":
    mots_file = "mots.txt"  # Fichier contenant les mots
    scores_file = "scores.json"  # Fichier contenant les scores
    menu_principal(mots_file, scores_file)
