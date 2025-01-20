nb_vies = 7
mot_mystere = "python"
mot_public = "_" * len(mot_mystere)
lettres_proposees = []

while nb_vies > 0 and mot_public != mot_mystere:
    print(f"\nMot à deviner : {mot_public}")
    print(f"Vies restantes : {nb_vies}")
    lettre = input("Entrez une lettre : ").lower()

    # Vérification de la saisie utilisateur
    if len(lettre) != 1 or not lettre.isalpha():
        print("Veuillez entrer une seule lettre valide.")
        continue

    # Vérification des lettres déjà proposées
    if lettre in lettres_proposees:
        print("Vous avez déjà proposé cette lettre.")
        continue
    lettres_proposees.append(lettre)

    # Mise à jour du mot public
    if lettre in mot_mystere:
        for i in range(len(mot_mystere)):
            if mot_mystere[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i+1:]
    else:
        nb_vies -= 1
        print(f"Erreur ! La lettre '{lettre}' n'est pas dans le mot.")

# Résultat final
if mot_public == mot_mystere:
    print(f"\nBravo, vous avez trouvé le mot : {mot_mystere} !")
else:
    print(f"\nDésolé, vous avez perdu... Le mot était : {mot_mystere}.")
