from .bd import BD
from .publication import Publication  # Import pour la relation 

class Forum:
    """
    Représente un forum au sein de la plateforme PyForum.
    """
    dernier_id = 0  # Attribut de classe pour gérer l'identifiant unique

    def __init__(self, nom: str, auteur_id: int, description: str = "", bd: BD = None):
        """
        Initialise une nouvelle instance de la classe Forum.

        Args:
            nom (str): Le nom unique du forum.
            auteur_id (int): L'identifiant de l'utilisateur qui a créé le forum.
            description (str, optional): Une description du forum (par défaut: "").
            bd (BD, optional): L'instance de la classe BD pour la gestion des données (par défaut: None).
        """
        Forum.dernier_id += 1
        self.id = Forum.dernier_id  # Attribut d'instance pour l'identifiant unique
        self.nom = nom
        self.description = description
        self.publications = []  # Liste pour stocker les instances de Publication de ce forum
        self.auteur_id = auteur_id # L'ID de l'utilisateur créateur
        self.bd = bd
        if self.bd:
            self.bd.sauvegarder_forum(self) # Simuler la sauvegarde lors de la création

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'objet Forum.

        Returns:
            str: Une chaîne formatée contenant les informations du forum.
        """
        desc_str = f", description='{self.description}'" if self.description else ""
        return f"Forum(id={self.id}, nom='{self.nom}', auteur_id={self.auteur_id}{desc_str}, nb_publications={len(self.publications)})"

    def creer_publication(self, titre: str, contenu: str, auteur_id: int):
        """
        Crée une nouvelle publication dans ce forum.
        """
        publication = Publication(titre, contenu, auteur_id, self.id, self.bd)
        self.publications.append(publication)
        if self.bd:
            self.bd.ajouter_publication_au_forum(self.id, publication.id) # Simuler l'ajout à la BD
        print(f"Publication '{publication.titre}' créée dans le forum '{self.nom}'.")
        return publication

