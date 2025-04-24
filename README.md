# pyforum-mvp
Création d'un forum
# PyForum - Travail Pratique 2

## Description

Ce projet est le travail pratique 2 pour le cours 420-2C3-MA Programmation objet. Il consiste à développer une interface en ligne de commande (REPL) pour la création et la manipulation de forums de discussion. Les fonctionnalités incluent la création d'utilisateurs, de forums, de publications et de commentaires, ainsi que la possibilité pour les utilisateurs de rejoindre des forums.

## Membres de l'équipe

* [Thierry Delavie Dossouh]
* [Udeh Aîyath Ogechukwu]

## Instructions

Pour exécuter le projet :

1.  **Cloner le dépôt :**
    ```bash
    git clone https://github.com/ThierryDelavie/pyforum-mvp/tree/main/src/pyforum
    cd 2025H-420-2C3-MA-Pyforum-tp2
    ```

2.  **Créer un dossier `data` :**
    Assurez-vous de créer un dossier nommé `data` à la racine du projet. Ce dossier sera utilisé pour stocker les fichiers CSV et JSON de la base de données.
    ```bash
    mkdir data
    ```

3.  **Exécuter l'application :**
    ```bash
    python src/pyforum/mvp.py
    ```
    L'application démarrera en mode REPL dans votre terminal, affichant un menu d'options.

## Structure du code

Le projet est structuré de la manière suivante :

* `src/pyforum/`: Contient les fichiers sources du projet.
    * `bd.py`: Définit la classe `BD` responsable de la gestion de la base de données (lecture et écriture de fichiers CSV et JSON).
    * `mvp.py`: Contient la boucle interactive (REPL) et fait le lien entre l'interface utilisateur et la base de données.
    * `utilisateur.py`: Définit la classe `Utilisateur`.
    * `forum.py`: Définit la classe `Forum`.
    * `publication.py`: Définit la classe `Publication`.
    * `commentaire.py`: Définit la classe `Commentaire`.
* `data/`: (À créer) Contient les fichiers de données (CSV et JSON) pour la persistance des informations.
* `README.md`: Le présent fichier, fournissant des informations sur le projet.

## Utilisation de Git

Ce projet a été développé en utilisant Git pour la gestion de versions. Des commits réguliers et significatifs ont été effectués tout au long du développement. Des branches ont été utilisées pour implémenter les différentes fonctionnalités, et celles-ci ont été fusionnées avec la branche `main` une fois terminées.

Le dépôt distant de ce projet est disponible sur [Lien vers votre dépôt GitHub ou GitLab]. La branche `main` contient la version finale du code pour la remise.

