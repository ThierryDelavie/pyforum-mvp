from .bd import BD
" Import pour la relation"
from .publication import Publication 
def creer_publication(self, titre: str, contenu: str, auteur_id: int):
        
        "crétaion d'une nouvelle publication "
        publication = Publication(titre, contenu, auteur_id, self.id, self.bd)
        self.publications.append(publication)
        if self.bd:
            self.bd.ajouter_publication_au_forum(self.id, publication.id) 
        print(f"Publication '{publication.titre}' créée dans le forum '{self.nom}'.")
        return publication