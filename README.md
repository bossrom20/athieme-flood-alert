# 🌊 Système d'Alerte Précoce aux Inondations - Athiémé

<div align="center">

![Version](https://img.shields.io/badge/Version-2.0-00d4ff?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-100%25-27ae60?style=for-the-badge)

**Plateforme Intelligente de Prédiction des Inondations du Fleuve Mono**

*Mémoire de Licence Professionnelle • Institut National de l'Eau (INE) • Bénin*

[🚀 Lancer l'Application](#-installation) • [📖 Documentation](#-documentation) • [📊 Performances](#-performances)

</div>

---

## 📋 Sommaire

- [À Propos](#-à-propos)
- [Fonctionnalités](#-fonctionnalités)
- [Performances](#-performances)
- [Installation](#-installation)
- [Utilisation](#-utilisation)
- [Architecture](#-architecture)
- [Équipe](#-équipe)

---

## 🎯 À Propos

Ce système d'alerte précoce utilise le **Machine Learning** pour prédire les inondations du fleuve Mono à la station d'Athiémé (Bénin) avec **24 à 48 heures d'anticipation**.

### Contexte

La commune d'Athiémé est régulièrement affectée par les crues du fleuve Mono, impactant **89% de ses villages** et plus de **56 000 habitants**. Ce système vise à améliorer l'anticipation par rapport au système actuel basé sur des seuils statiques.

### Objectifs

- ✅ Prédire l'occurrence d'inondations 24-48h à l'avance
- ✅ Atteindre une accuracy minimale de 75% (objectif largement dépassé : **100%**)
- ✅ Fournir une interface opérationnelle pour les gestionnaires
- ✅ Valider le système sur des événements historiques récents

---

## ✨ Fonctionnalités

### 🎯 Module de Prédiction
- Saisie des paramètres hydrométriques en temps réel
- Prédiction par Random Forest ou Régression Logistique
- Calcul de la probabilité d'inondation
- Classification en 3 niveaux de risque (Faible/Moyen/Élevé)
- Recommandations opérationnelles personnalisées

### 📊 Dashboard Analytique
- Métriques clés en temps réel
- Évolution historique des niveaux d'eau
- Analyse de la saisonnalité des crues
- Statistiques descriptives complètes

### 🏆 Suivi des Performances
- Comparaison des modèles ML
- Matrices de confusion interactives
- Importance des variables prédictives
- Courbes ROC et métriques d'évaluation

### 📈 Analyse Historique
- Timeline des événements majeurs (2005-2024)
- Distribution annuelle des inondations
- Détail des 10 crues historiques

### 📖 Documentation Intégrée
- Méthodologie complète
- Description des données
- Informations sur l'équipe et les partenaires

---

## 🏆 Performances

| Métrique | Random Forest | Régression Logistique |
|----------|:-------------:|:---------------------:|
| **Accuracy** | 100.00% | 99.58% |
| **Precision** | 100.00% | 82.86% |
| **Recall** | 100.00% | 100.00% |
| **F1-Score** | 100.00% | 90.62% |
| **ROC-AUC** | 1.0000 | 1.0000 |

### Variables les Plus Importantes

1. 🥇 Distance au seuil critique (23.22%)
2. 🥈 Cote actuelle (22.96%)
3. 🥉 Distance au seuil d'alerte (15.43%)
4. Débit (13.86%)
5. Moyenne mobile débit 7j (10.08%)

---

## 🚀 Installation

### Prérequis

- Python 3.9 ou supérieur
- pip (gestionnaire de packages Python)

### Installation Locale

```bash
# 1. Cloner ou extraire le projet
cd athieme_platform

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
streamlit run app.py
```

### Déploiement sur Streamlit Cloud

1. Créer un compte sur [share.streamlit.io](https://share.streamlit.io)
2. Connecter votre dépôt GitHub
3. Déployer l'application

---

## 💻 Utilisation

### Étapes pour une Prédiction

1. **Ouvrir la plateforme** dans votre navigateur
2. **Renseigner les paramètres** dans le panneau latéral :
   - Cote actuelle (m)
   - Débit (m³/s)
   - Variations sur 24h et 48h
   - Précipitations récentes
3. **Cliquer sur "ANALYSER LE RISQUE"**
4. **Interpréter les résultats** :
   - Niveau de risque (code couleur)
   - Probabilité d'inondation
   - Recommandations d'actions

### Niveaux de Risque

| Niveau | Probabilité | Action |
|--------|-------------|--------|
| 🟢 **Faible** | < 30% | Surveillance de routine |
| 🟠 **Moyen** | 30-70% | Vigilance renforcée |
| 🔴 **Élevé** | > 70% | Actions immédiates |

---

## 🏗️ Architecture

```
athieme_platform/
├── app.py                          # Application Streamlit principale
├── requirements.txt                # Dépendances Python
├── README.md                       # Documentation
├── random_forest_model.pkl         # Modèle Random Forest entraîné
├── logistic_regression_model.pkl   # Modèle Régression Logistique
├── scaler.pkl                      # Scaler pour normalisation
└── dataset_athieme_features_2005_2024.csv  # Données historiques
```

### Stack Technique

- **Frontend**: Streamlit, Plotly
- **Backend**: Python, Pandas, NumPy
- **ML**: Scikit-learn, imbalanced-learn
- **Visualisation**: Plotly, CSS personnalisé

---

## 👥 Équipe

### Auteur

**BOSSOU Kossèni Affoladé Roméo**  
Étudiant en Licence Professionnelle  
Filière: Gestion des Crises et Risques liés à l'Eau et au Climat (GCREC)

### Encadrement Académique

- **Prof. VISSIN Expédit** - Directeur de mémoire
- **Dr. Pierre OUASSA** - Co-encadrant

### Institution

**Institut National de l'Eau (INE)**  
Université d'Abomey-Calavi  
Bénin

---

## 🤝 Partenaires

- 🏛️ **DGEau** - Direction Générale de l'Eau
- 🚨 **ANPC** - Agence Nationale de Protection Civile
- 🌤️ **Météo-Bénin** - Service Météorologique National

---

## 📄 Licence

Ce projet est développé dans le cadre d'un mémoire de licence professionnelle.  
© 2025 BOSSOU Kossèni Affoladé Roméo - Institut National de l'Eau, Bénin

---

<div align="center">

**🌊 SAP Athiémé v2.0**

*Protéger les populations par l'intelligence artificielle*

</div>
