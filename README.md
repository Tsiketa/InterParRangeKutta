# INTERVENTION PAR RANGE KUTTA

## Description
    Ce projet est une application de simulation de coûts pour des interventions, utilisant le modèle MVC (Modèle-Vue-Contrôleur). L'interface graphique est développée avec PyQt5, et la simulation de l'évolution des coûts est calculée en utilisant la méthode de Runge-Kutta d'ordre 4 sur une fonction de coût trigonometrique.
    
    L'utilisateur peut entrer les paramètres suivants dans l'application:
        -Durée de l'intervention en jours
        -Coût journalier de base (Ar)
        -Coût initial (Ar)
        
    Le résultat est affiché sous forme de graphique, avec la possibilité d'afficher dynamiquement les coordonnées des points du graphique.
    
## Fonctionnalités
    - **Interface Utilisateur Personnalisée** : Un design propre et moderne avec des champs de saisie stylisés, des boutons colorés, et un grand titre centré.
    - **Affichage Dynamique des Coordonnées** : Affichage en temps réel des coordonnées des points lorsque l'utilisateur survole le graphique avec la souris.
    - **Simulation de Coût Trigonométrique** : Utilisation d'une fonction sinus pour modéliser les variations de coût au fil du temps.
## Structure du Projet
    InterParRangeKutta/
    │
    ├── app   
    │    ├── model/
    │    │     └── simulationModel.py
    │    │──view/
    │    │     └── simulationView.py
    ├    ├── controller/
    │          └── simulationController.py
    ├── merise/
    │      └── MCD.jpg
    ├── main.py
    └── README.md

    - **app/** : Contient les dossiers MVC.
    - **model/** : Contient le fichier simulationmodel.py, qui gère la logique métier et les calculs.
    - **view/** : Contient le fichier simulationview.py, qui gère l'interface graphique et l'affichage du graphique.
    - **controller/*** : Contient le fichier simulationcontroller.py, qui gère les interactions entre le modèle et la vue.
    - **merise/** : Contient le MCD et MCT
    -**main.py** : Fichier principal pour démarrer l'application.

## Prérequis
    -Python 3.x
    -PyQt5
    -Matplotlib
    -NumPy
    
## Installation
    -Accédez au répertoire du projet :
        cd InterParRangeKutta
    -tInstallezles dépendances requises :
        pip install -r requirements.txt
    -Utilisation Pour lancer l'application,exécutez le fichier main.py:
        python main.py
        
    Une interface graphique apparaîtra, vous permettant d'entrer les paramètres de simulation et de visualiser l'évolution des coûts.
