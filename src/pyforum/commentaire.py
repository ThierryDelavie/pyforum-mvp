from .bd import BD

class Commentaire:
    "ajout d'un commentaire à une publication"
    dernier_id = 0

    def __init__(self, auteur_id: int, contenu: str, publication_id: int, bd: BD = None):
       
        Commentaire.dernier_id = Commentaire.dernier_id+1
        self.id = Commentaire.dernier_id
        self.auteur_id = auteur_id
        self.contenu = contenu
        self.publication_id = publication_id
        self.bd = bd
        if self.bd:
            self.bd.sauvegarder_commentaire(self) 
    def __str__(self):
       
        return f"Commentaire(id={self.id}, auteur_id={self.auteur_id}, contenu='{self.contenu[:20]}...', publication_id={self.publication_id})"