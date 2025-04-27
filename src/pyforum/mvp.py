# Importation des classes nécessaires
from time import sleep
from pyforum.bd import BD


def afficher_menu():
    """Affiche les options du menu."""
    print("\n---- Menu ----")
    print("1. Créer un utilisateur")
    print("2. Créer un forum")
    print("3. Créer une publication")
    print("4. Ajouter un commentaire à une publication")
    print("5. Joindre un forum")
    print("6. Quitter")


def main():

    # Initialisation de la base de données
    db = BD()

    while True:
        afficher_menu()

        # Demander à l'utilisateur de choisir une option
        choix = input("Choisissez une option (1-6): ")

        if choix == '1':
            # Créer un utilisateur
            print("\nCréation d'un utilisateur...")

            # Voici un exemple trivial de création d'un utilisateur. Vous devez le bonifier,
            # car il ne prend en compte que le nom d'utilisateur.
            username = input("Entrez le nom d'utilisateur: ")
            utilisateur = {'username': username}
            
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            email = input("Entrez l'adresse courriel: ")
            mot_de_passe = input("Entrez le mot de passe: ")
            # Le **utilisateur est une syntaxe Python pour déballer un dictionnaire.
            # C'est à dire que les clés du dictionnaire deviennent des arguments nommés.
            db.creer_utilisateur(**utilisateur)
            
            utilisateur_data = {
                'username': username,
                'email': email,
                'password': mot_de_passe
            }
            utilisateur = db.creer_utilisateur(**utilisateur_data)
            if utilisateur:
                print(f"Utilisateur '{utilisateur.username}' créé avec l'ID: {utilisateur.id}")


        elif choix == '2':
            # Créer un forum
            print("\nCréation d'un forum...")
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            nom_forum = input("Entrez le nom du forum: ")
            description_forum = input("Entrez une description (optionnel): ")


            # TODO: Ajouter l'appel à la base de donnée pour créer le forum
            forum_data = {
                'nom': nom_forum,
                'description': description_forum if description_forum else None
            }
            forum = db.creer_forum(**forum_data)
            if forum:
                print(f"Forum '{forum.nom}' créé avec l'ID: {forum.id}")

        elif choix == '3':
            # Créer une publication
            print("\nCréation d'une publication...")
            
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            auteur_id = input("Entrez l'ID de l'auteur: ")
            forum_id = input("Entrez l'ID du forum: ")
            titre_publication = input("Entrez le titre de la publication: ")
            contenu_publication = input("Entrez le contenu de la publication: ")

            
            # TODO: Ajouter l'appel à la base de donnée pour créer la publication
            publication_data = {
                'auteur_id': auteur_id,
                'forum_id': forum_id,
                'titre': titre_publication,
                'contenu': contenu_publication
            }
            publication = db.creer_publication(**publication_data)
            if publication:
                print(f"Publication '{publication.titre}' créée avec l'ID: {publication.id} dans le forum {publication.forum_id}")

        elif choix == '4':
            # Ajouter un commentaire
            print("\nAjouter un commentaire...")
            
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            auteur_id_commentaire = input("Entrez l'ID de l'auteur du commentaire: ")
            publication_id_commentaire = input("Entrez l'ID de la publication à commenter: ")
            contenu_commentaire = input("Entrez le contenu du commentaire: ")
            
            # TODO: Ajouter l'appel à la base de donnée pour créer le commentaire
            commentaire_data = {
                'auteur_id': auteur_id_commentaire,
                'publication_id': publication_id_commentaire,
                'contenu': contenu_commentaire
            }
            commentaire = db.ajouter_commentaire(**commentaire_data)
            if commentaire:
                print(f"Commentaire ajouté avec l'ID: {commentaire.id} à la publication {commentaire.publication_id}")


        elif choix == '5':
            # Joindre un forum
            print("\nJoindre un forum...")
            # TODO: Ajouter ici la logique pour demander des informations à l'utilisateur
            utilisateur_id_joindre = input("Entrez votre ID d'utilisateur: ")
            forum_id_joindre = input("Entrez l'ID du forum à joindre: ")

            # TODO: Ajouter les appels à la base de donnée pour ajouter l'utilisateur au forum
            succes = db.joindre_forum(utilisateur_id_joindre, forum_id_joindre)
            if succes:
                print(f"L'utilisateur {utilisateur_id_joindre} a rejoint le forum {forum_id_joindre}")
            else:
                print("Impossible de joindre le forum. Vérifiez les IDs.")


        elif choix == '6':
            # Quitter le programme
            print("\nMerci d'avoir utilisé PyForum. À bientôt!")
            break

        else:
            print("Option invalide. Veuillez essayer à nouveau.")

        sleep(1)  # Pause de 1 secondes pour rendre l'interface plus agréable


