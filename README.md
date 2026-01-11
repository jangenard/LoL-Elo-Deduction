# Détection de rang sur League of Legends

## Présentation
Ce projet a pour but de prédire le rang actuel d'un joueur de League of Legends à partir 
de statistiques en jeu comme le score global, le score personnel, le nombre de sbires tués et la durée. 
L’approche repose sur l’extraction automatique de ces statistiques à partir de captures d’écran, suivie de l’apprentissage de modèles de classification supervisée. Le projet met l’accent sur la reproductibilité et l’analyse comparative de différents modèles.

À partir de ce dépôt, il est possible de :
- exécuter le projet depuis un notebook présent dans le dossier /notebooks
- cloner et installer le projet avec toutes ses librairies
- tester localement le pipeline avec un échantillon de données
- accéder au dataset Kaggle utilisé (140 images et 140 annotations).

## Prérequis
- Python >=3.10 64-bit
- Environnement virtuel conseillé :
``` bash
python -m venv .env
source .env/bin/activate   # Linux / macOS
.env\Scripts\activate      # Windows
```
## Dataset

Les données utilisées dans ce projet sont mises à disposition publiquement sous la forme d’un dataset Kaggle, afin de garantir la reproductibilité des expériences.
Le dataset est composé de 140 captures d’écran leur annotations format .json couvrant sept rangs de classement de bronze à challenger.

## Installation :
Cloner le dépot localement puis installer le projet en mode éditable : 
```bash
pip install -e .
```
Ou utiliser le notebook présent dans /notebooks.

## Utilisation :

L’entraînement et l’évaluation des modèles ont été réalisés principalement à l’aide de notebooks Jupyter, disponibles dans le dossier /notebooks. Cette approche facilite l’exploration des données, l’analyse des résultats et la visualisation des performances des modèles.

Le pipeline expérimental comprend :
- le chargement des images et des annotations depuis le dataset Kaggle,
- le prétraitement des captures d’écran (rognage, segmentation des zones pertinentes),
- l’extraction des statistiques numériques par OCR,
- la construction d’un jeu de données tabulaire à partir de ratios temporels,
- l’entraînement et la validation de plusieurs modèles de classification.

En cas de contraintes matérielles locales, il est recommandé d’exécuter les expériences directement sur Kaggle, où l’environnement et les dépendances sont compatibles avec le projet. Les scripts Python présents dans le dépôt permettent néanmoins de reproduire l’ensemble du pipeline sur un environnement local disposant des ressources nécessaires.
