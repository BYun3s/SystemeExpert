# Système Expert pour la Gestion des Pannes

Ce projet est une application Python Flask qui implémente un système expert pour la gestion des pannes. Il utilise le chaînage avant pour l'inférence des pannes potentielles en fonction des faits fournis. L'application fournit une interface utilisateur pour interagir avec le système expert, permettant aux utilisateurs d'accéder à un espace expert pour gérer les règles et les faits.


## Structure du Projet

- **app.py**: Fichier principal de l'application Flask qui définit les routes et la logique de l'application.
- **data.json**: Fichier JSON contenant les données statiques et les règles du système expert.
- **facts.json**: Fichier JSON contenant les faits et leur état pour le système expert choisi par l'utilisateur.
- **MoteurInference.py**: Module Python contenant les classes et la logique du moteur d'inférence.
- **templates** : Dossier contient les fichiers HTML pour les vues de l'application Flask.

## Fonctionnalités Principales

- Authentification d'expert avec gestion des faits et règles.
    - Accès à l'espace expert via l'username `admin` et le mot de passe `admin`.
- Interface utilisateur pour interagir avec le système expert.
- Inférence des pannes potentielles en fonction des règles définies.
- Affichage des résultats de l'inférence sur une page resultat.html.

## Dépendances

- Flask: Framework web utilisé pour développer l'application. Pour l'installer, vous pouvez exécuter cette commande dans votre terminal <code>pip install flask</code>
- Flask-Login: Extension Flask pour la gestion de l'authentification des utilisateurs. Pour l'installer, vous pouvez exécuter cette commande dans votre terminal <code>pip install flask_login</code>
- Python 3.11

## Utilisation

1. Cloner le dépôt localement.
2. Installer les dépendances Python via `pip install -r requirements.txt`.
3. Exécuter l'application avec `python app.py`.
4. Accéder à l'application dans un navigateur à l'adresse `http://localhost:{port}`.

## Auteur

- Ce script a été développé par **Younes BASRAOUI**
