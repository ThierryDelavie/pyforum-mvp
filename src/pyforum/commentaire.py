from .bd import BD

class Commentaire:
    """Représentation d'un commentaire ajouté à une publication"""
    dernier_id = 0

    def _init_(self, auteur_id: int, contenu: str, publication_id: int, bd: BD = None):
        # Incrémentation du dernier ID
        Commentaire.dernier_id += 1
        self.id = Commentaire.dernier_id
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id
        self.bd = bd

        # Sauvegarde du commentaire dans la base de données
        if self.bd:
            self.bd.sauvegarder_commentaire(self)

    def _str_(self):
        """Retourne une représentation sous forme de chaîne du commentaire"""
        contenu_str = self.contenu[:20] + "..." if len(self.contenu) > 20 else self.contenu
        return f"Commentaire(id={self.id}, auteur_id={self.auteur_id}, contenu='{contenu_str}', publication_id={self.publication_id})"