from .bd import BD

class Commentaire:
    """
    Représente un commentaire ajouté à une publication dans PyForum.
    """
    dernier_id = 0

    def __init__(self, auteur_id: int, contenu: str, publication_id: int, bd: BD = None):
        """
        Initialise une nouvelle instance de la classe Commentaire.

        Args:
            auteur_id (int): L'identifiant de l'utilisateur qui a écrit le commentaire.
            contenu (str): Le contenu du commentaire.
            publication_id (int): L'identifiant de la publication à laquelle le commentaire est associé.
            bd (BD, optional): L'instance de la classe BD pour la gestion des données (par défaut: None).
        """
        Commentaire.dernier_id += 1
        self.id = Commentaire.dernier_id
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id
        self.bd = bd
        if self.bd:
            self.bd.sauvegarder_commentaire(self) # Simuler la sauvegarde lors de la création

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de l'objet Commentaire.

        Returns:
            str: Une chaîne formatée contenant les informations du commentaire.
        """
        return f"Commentaire(id={self.id}, auteur_id={self.auteur_id}, contenu='{self.contenu[:20]}...', publication_id={self.publication_id})"