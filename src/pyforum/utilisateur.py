from src.pyforum.bd import BD

class Utilisateur():
    dernier_id = 0 

    def __init__(self, username: str, adresse_courriel: str, mot_de_passe: str, bd: BD):
        # TODO: Ajouter les autres attributs nécessaires
        self.id = id
        self.username = username
        self.adresse_courriel = adresse_courriel
        self.mot_de_passe = mot_de_passe
        self.forums_inscrits = []  # Liste pour stocker les instances de Forum auxquels l'utilisateur est inscrit
        self.bd = bd
        self.bd.sauvegarder_utilisateur(self) # Simuler la sauvegarde lors de la création

    def __str__(self):
        return f"Utilisateur(id={self.id}, nom_utilisateur='{self.nom_utilisateur}', courriel='{self.adresse_courriel}')"

    def rejoindre_forum(self, forum):
        """
        Ajoute un forum à la liste des forums auxquels l'utilisateur est inscrit.

        Args:
            forum (Forum): L'instance de la classe Forum que l'utilisateur souhaite rejoindre.
        """
        if forum not in self.forums_inscrits:
            self.forums_inscrits.append(forum)
            self.bd.ajouter_utilisateur_au_forum(self.id, forum.id) # Simuler l'ajout dans la BD
            print(f"L'utilisateur '{self.nom_utilisateur}' a rejoint le forum '{forum.nom}'.")
        else:
            print(f"L'utilisateur '{self.nom_utilisateur}' est déjà inscrit au forum '{forum.nom}'.")
