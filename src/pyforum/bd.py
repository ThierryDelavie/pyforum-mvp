from pyforum.utilisateur import Utilisateur
from src.pyforum.bd import BD

import json
import csv
import os
from pyforum.forum import Forum
from pyforum.publication import Publication
from pyforum.commentaire import Commentaire

class BD:
    """Responsable de la gestion de la base de données via des fichiers CSV et JSON."""
   
    Utilisateurs_file = 'data/utilisateurs.json'
    Forum_file = 'data/forums.json'
    Publications_file = 'data/publications.json'
    Commentaire_file = 'data/commentaires.json'
    Utilisateurs_Forum_file = 'data/utilisateurs_forums.csv'

    def _init_(self):
        os.makedirs(os.path.dirname(self.Utilisateurs_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.Forum_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.Publications_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.Commentaire_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.Utilisateurs_Forum_file), exist_ok=True)

        self.utilisateurs: list[Utilisateur] = self._charger_utilisateurs()
        self.forums: list[Forum] = self._charger_forums()
        self.publications: list[Publication] = self._charger_publications()
        self.commentaires: list[Commentaire] = self._charger_commentaires()
        self.utilisateurs_forums: dict[int, list[int]] = self._charger_utilisateurs_forums()
        print("Base de données initialisée.")
   
    def creer_utilisateur(self, username: str, adresse_courriel: str, mot_de_passe: str, bd: BD):
        # TODO: Ajouter les autres paramètres requis
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            return None
        if adresse_courriel in [u.adresse_courriel for u in self.utilisateurs]:
            print(f"[Simulé] L'adresse courriel {adresse_courriel} est déjà utilisée.")
            return None

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(username, adresse_courriel, mot_de_passe, bd)
        u.id = new_id
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        return u

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u

    def creer_forum(self, nom, auteur_id, description=""):
        # TODO: Implanter la logique pour créer un forum
        new_id = max([f.id for f in self.forums], default=0) + 1
        forum = Forum(nom, auteur_id, description, self)
        forum.id = new_id
        self.forums.append(forum)
        self._sauvegarder_forums()
        print(f"[Simulé] Forum créé: {forum}")
        return forum

    def creer_publication(self, titre: str, contenu: str, auteur_id: int, forum_id: int):
        # TODO: Implanter la logique pour créer une publication
        new_id = max([p.id for p in self.publications], default=0) + 1
        publication = Publication(titre, contenu, auteur_id, forum_id, self)
        publication.id = new_id
        self.publications.append(publication)
        self._sauvegarder_publications()
        print(f"[Simulé] Publication créée: {publication}")
        return publication

    def creer_commentaire(self, auteur_id: int, contenu: str, publication_id: int):
        # TODO: Implanter la logique pour créer un commentaire
        new_id = max([c.id for c in self.commentaires], default=0) + 1
        commentaire = Commentaire(auteur_id, contenu, publication_id, self)
        commentaire.id = new_id
        self.commentaires.append(commentaire)
        self._sauvegarder_commentaires()
        print(f"[Simulé] Commentaire créé: {commentaire}")
        return commentaire

    def obtenir_forum_par_nom(self, nom_forum):
        for forum in self.forums:
            if forum.nom == nom_forum:
                return forum
        return None

    def obtenir_publication_par_titre(self, titre_publication):
        for pub in self.publications:
            if pub.titre == titre_publication:
                return pub
        return None

    def mettre_a_jour_forum(self, forum: Forum, nom: str, description: str):
        # TODO: Implanter la logique pour mettre à jour le forum et retourner le forum mis à jour
        for i, f in enumerate(self.forums):
            if f.id == forum.id:
                self.forums[i] = forum
                self._sauvegarder_forums()
                print(f"[Simulé] Mise à jour du forum: {forum}")
                return forum
        print(f"[Simulé] Forum avec l'ID {forum.id} non trouvé pour la mise à jour.")
        return None
   
   
def sauvegarder_donnees(self):
    """Sauvegarde toutes les données dans les fichiers appropriés."""
    self._sauvegarder_utilisateurs()
    self._sauvegarder_forums()
    self._sauvegarder_publications()
    self._sauvegarder_commentaires()
    self._sauvegarder_utilisateurs_forums()