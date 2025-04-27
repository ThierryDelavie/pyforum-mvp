from .bd import BD
from .publication import Publication

class Forum:
    """Représentation d'un forum de discussion."""
    dernier_id = 0

    def _init_(self, nom: str, auteur_id: int, description: str = "", bd: BD = None):
        Forum.dernier_id += 1
        self.id = Forum.dernier_id
        self.nom = nom
        self.description = description
        self.publications = []  # Liste d'objets Publication ou leurs IDs
        self.auteur_id = auteur_id
        self.bd = bd

        if self.bd:
            # Sauvegarde dans la base de données
            self.bd.sauvegarder_forum(self)

    def _str_(self):
        """Retourne une représentation en chaîne de caractères de l'objet Forum."""
        desc_str = f", description='{self.description}'" if self.description else ""
        return f"Forum(id={self.id}, nom='{self.nom}', auteur_id={self.auteur_id}{desc_str}, nb_publications={len(self.publications)})"

    def creer_publication(self, titre: str, contenu: str, auteur_id: int):
        """Création d'une nouvelle publication dans le forum."""
        publication = Publication(titre, contenu, auteur_id, self.id, self.bd)

        self.publications.append(publication.id)

        if self.bd:
            self.bd.ajouter_publication_au_forum(self.id, publication.id)

        print(f"Publication '{titre}' créée dans le forum '{self.nom}'.")
        return publication