def enregistrer_paiement():
    nom_client = input("Nom du client : ")
    montant = float(input("Montant du paiement : "))
    date = input("Date du paiement (format JJ/MM/AAAA) : ")

    # Création de la chaîne de données à enregistrer dans le fichier
    donnees = f"Client: {nom_client}\tMontant: {montant}\tDate: {date}\n"

    # Ouverture du fichier en mode ajout
    with open("paiements.txt", "a") as fichier:
        fichier.write(donnees)

    print("Paiement enregistré avec succès.")

# Appel de la fonction pour enregistrer un paiement
enregistrer_paiement()