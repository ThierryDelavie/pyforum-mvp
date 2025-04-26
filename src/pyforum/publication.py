from .bd import BD
from .publication import Publication

class Forum:
    dernier_id = 0

    def __init__(self, nom: str, auteur_id: int, description: str = "", bd: BD = None):
        Forum.dernier_id += 1
        self.id = Forum.dernier_id
        self.nom = nom
        self.description = description
        self.publications = []  # Liste des publications par ID
        self.auteur_id = auteur_id
        self.bd = bd

        if self.bd:
            # Sauvegarde dans la base de données
            self.bd.sauvegarder_forum(self)

    def creer_publication(self, titre: str, contenu: str, auteur_id: int):
        """Création d'une nouvelle publication dans un forum"""
        # Création de la publication
        publication = Publication(titre, contenu, auteur_id, self.id, self.bd)

        # Ajout de l'ID de la publication à la liste des publications du forum
        self.publications.append(publication.id)

        # Sauvegarde de la publication dans la base de données
        if self.bd:
            self.bd.ajouter_publication_au_forum(self.id, publication.id)

        print(f"Publication '{publication.titre}' créée dans le forum '{self.nom}'.")
        return publication
