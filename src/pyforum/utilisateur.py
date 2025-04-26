from src.pyforum.bd import BD

class Utilisateur:
    dernier_id = 0

    def __init__(self, username: str, adresse_courriel: str, mot_de_passe: str, bd: BD):
        Utilisateur.dernier_id += 1
        self.id = Utilisateur.dernier_id
        self.username = username
        self.adresse_courriel = adresse_courriel
        self.mot_de_passe = mot_de_passe
        self.forums_inscrits = []  # Liste d'IDs de forums
        self.bd = bd

        self.bd.sauvegarder_utilisateur(self)  # Sauvegarde dans les fichiers

    def __str__(self):
        return f"Utilisateur(id={self.id}, nom_utilisateur='{self.username}', courriel='{self.adresse_courriel}')"

    def rejoindre_forum(self, forum):
        """
        Ajoute un forum à la liste des forums auxquels l'utilisateur est inscrit.

        Args:
            forum (Forum): Instance de Forum
        """
        if forum.id not in self.forums_inscrits:
            self.forums_inscrits.append(forum.id)
            self.bd.ajouter_utilisateur_au_forum(self.id, forum.id)
            print(f"L'utilisateur '{self.username}' a rejoint le forum '{forum.nom}'.")
        else:
            print(f"L'utilisateur '{self.username}' est déjà inscrit au forum '{forum.nom}'.")
