from pyforum.utilisateur import Utilisateur
from src.pyforum.bd import BD

import json
import csv
import os
from pyforum.utilisateur import Utilisateur
from pyforum.forum import Forum
from pyforum.publication import Publication 
from pyforum.commentaire import Commentaire
"from pyforum-mvp.src.pyforum import forum"

class BD:
    
    "Responsable de la gestion de la base de données via des fichiers CSV et JSON."
    
    Utilisateurs_file = 'data/utilisateurs.json'
    Forum_file = 'data/forums.json'
    Publications_file = 'data/publications.json'
    Commentaire_file = 'data/commentaires.json'
    Utilisateurs_Forum_file = 'data/utilisateurs_forums.csv'

    def __init__(self):
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
    
        
    def __init__(self):
        self.utilisateurs: list[Utilisateur] = []
        self.forums = []
        self.publications = []
        self.commentaires = []
        self.utilisateurs_forums = {}
        print("Base de données initialisée.")
        

    def creer_utilisateur(self, username: str,adresse_courriel: str, mot_de_passe: str,bd: BD) :
        #                       ^^^^^^^^^^^^^^
        #            # TODO:    Vous devez ajouter les autres paramètres requis

        # Vérifier si l'utilisateur existe déjà
        if username in [u.username for u in self.utilisateurs]:
            print(f"[Simulé] L'utilisateur {username} existe déjà.")
            return None
        if adresse_courriel in [u.adresse_courriel for u in self.utilisateurs]:
            print(f"[Simulé] L'adresse courriel {adresse_courriel} est déjà utilisée.")
            return None 

        # Créer un nouvel identifiant pour l'utilisateur
        new_id = max([u.id for u in self.utilisateurs], default=0) + 1

        # Instancier un nouvel utilisateur et l'ajouter à la liste
        u = Utilisateur(new_id, username, adresse_courriel, mot_de_passe, bd)
        self.utilisateurs.append(u)
        print(f"[Simulé] Sauvegarde de l'utilisateur: {u}")

        # Retourner l'utilisateur créé
        return u
    

    def obtenir_utilisateur_par_nom(self, nom_utilisateur: str):
        for u in self.utilisateurs:
            if u.username == nom_utilisateur:
                return u
            

    def creer_forum(self, nom, auteur_id, description=""):
        #                ^^^^^^
        #                Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un forum
        forums = []
        if os.path.exists(self.Forums_file):
            try:
                with open(self.Forums_file, 'r') as f:
                    data = json.load(f)
                    for forum_data in data:
                        forum = Forum(forum_data['nom'], forum_data['auteur_id'], forum_data['description'], self)
                        forum.id = forum_data['id']
                        Forum.dernier_id = max(Forum.dernier_id, forum.id)
                        forum.publications = [self._obtenir_publication_par_id(pub_id) for pub_id in forum_data.get('publications', []) if self._obtenir_publication_par_id(pub_id)]
                        forums.append(forum)
            except FileNotFoundError:
                pass
            except json.JSONDecodeError:
                print(f"Erreur de décodage JSON dans {self.Forums_file}.")
        return forums



    def creer_publication(self, publication:str,titre:str,contenu:str, auteur_id:int, forum_id:int):
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer une publication
        new_id = max([p.id for p in self.publications], default=0) + 1
        publication = Publication(titre, contenu, auteur_id, forum_id, self)
        publication.id = new_id
        self.publications.append(publication)
        self._sauvegarder_publications()
        print(f"[Simulé] Sauvegarde de la publication: {publication}")
        return publication


    def creer_commentaire(self, commentaire: bool, auteur_id:int, contenu:str, publication_id:int): 
        #                       ^^^^^^^^^^^
        #                       Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour créer un commentaire
        new_id = max([c.id for c in self.commentaires], default=0) + 1
        commentaire = Commentaire(auteur_id, contenu, publication_id, self)
        commentaire.id = new_id
        self.commentaires.append(commentaire)
        self._sauvegarder_commentaires()
        print(f"[Simulé] Sauvegarde du commentaire: {commentaire}")
        return commentaire
    
    
    # TODO: Implanter la logique pour chercher un forum à partir de son nom
    def obtenir_forum_par_nom(self, nom_forum):
        
        for forum in self.forums:
            if forum.nom == nom_forum:
                return forum
        return None
    
    
# TODO: Implanter la logique pour chercher une publication à partir de son titre
    def obtenir_publication_par_titre(self, titre_publication):
        
        for pub in self.publications:
            if pub.titre == titre_publication:
                return pub
        return None



    def mettre_a_jour_forum(self, forum: Forum, nom: str, description: str):
        #                         ^^^^^^
        #                         Vous devez ajouter les autres paramètres requis
        # TODO: Implanter la logique pour mettre à jour le forum et retourner le forum mis à jour
        for i, f in enumerate(self.forums):
            if f.id == forum.id:
                self.forums[i] = forum
                self._sauvegarder_forums()
                print(f"[Simulé] Mise à jour du forum: {forum}")
                return forum
        print(f"[Simulé] Forum avec l'ID {forum.id} non trouvé pour la mise à jour.")
        return None
