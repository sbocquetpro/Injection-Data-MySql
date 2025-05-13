# Injection de données CSV vers MySQL

Ce projet simple permet de **charger des données à partir d’un fichier CSV** et de les **insérer dans une base de données MySQL**.

## Description

Le script lit un fichier CSV (`client.csv`), le convertit en DataFrame avec `pandas`, puis insère les données dans la table `client` d'une base de données MySQL.  
En cas de doublon sur la clé primaire (`id`), les données sont mises à jour automatiquement.

## Structure du projet

├── client.csv # Fichier CSV contenant les données clients \
├── load_csv1.py # Chargement du CSV avec pandas \
├── main.py # Point d’entrée du script \
├── mysql_connection1.py # Connexion et insertion dans MySQL \
└── README.md # \

## Prérequis

- Python 3.x
- MySQL installé et accessible
- Bibliothèques Python :

```bash
pip install pandas mysql-connector-python

## Configuration MySQL

Le fichier mysql_connection1.py contient les informations de connexion. Exemple :

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Test1234",
    database="etl_project"
)
