## 📘 Description du projet

Ce projet est un système expert conçu pour assister les professionnels de santé dans le diagnostic des maladies cardiovasculaires.
Le programme repose sur une base de connaissances médicales et un moteur d’inférence qui évalue les symptômes afin de proposer un diagnostic ou un avis préliminaire.

## 🎯 Objectifs

Fournir un outil d’aide à la décision médicale rapide et fiable.

Réduire les erreurs de diagnostic liées à la complexité des symptômes.

Offrir une interface simple permettant aux utilisateurs d’entrer des données patients et d’obtenir un diagnostic.

## 🧩 Fonctionnalités principales

🧠 Moteur d’inférence basé sur des règles.

💾 Base de connaissances contenant les symptômes et pathologies cardiovasculaires (essouflement, problèmes de rythmes cardiaques, cardiopathie etc.).

🧍 Saisie interactive des symptômes et facteurs de risque.

📊 Génération d’un rapport de diagnostic détaillant la probabilité des maladies suspectées.

## ⚙️ Architecture du système
+-------------------------+
| Interface utilisateur   |
+-----------+-------------+
            |
+-----------v-------------+
| Moteur d'inférence       |
| (règles, chaînes avant)  |
+-----------+-------------+
            |
+-----------v-------------+
| Base de connaissances   |
| (symptômes, maladies)   |
+-------------------------+

## 🧠 Technologies utilisées

### Langage : Python

### Interface : Streamlit 

### Format des règles : Prolog-like 

### Librairies possibles :

experta (pour la logique d’inférence en Python)

## 🚀 Installation et exécution
1. Cloner le dépôt
git clone https://github.com/Therighteous2/ExpertSysCardio.git
cd ExpertSysCardio

2. Installer les dépendances
pip install -r requirements.txt

3. Lancer le système expert
Streamlit run AppMaladie.py

🧪 Exemple d’utilisation

→ Voir l'interface utilisateur 

📚 Structure du projet
diagnostic-cardio-expert/
│
├── AppMaladie.py         # Interface utilisateur 
├── ExpertMaladie.py      # Base de connaissances(Règles et faits médicaux)
├── requirements.txt      # Dépendances Python
└── README.md             # Documentation du projet

## 👨‍⚕️ Auteur

Abel M. – Développeur principal

## 💬 Remarques

⚠️ Ce système expert est un outil d’aide à la décision, et ne remplace pas un avis médical professionnel.
Les diagnostics proposés sont basés sur des règles médicales simplifiées.