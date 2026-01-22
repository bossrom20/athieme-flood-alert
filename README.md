# 🌊 Système d'Alerte Précoce aux Inondations — Athiémé

<div align="center">

![Bénin](https://img.shields.io/badge/Pays-Bénin-green?style=for-the-badge)
![ML](https://img.shields.io/badge/Machine_Learning-Random_Forest-blue?style=for-the-badge)
![Accuracy](https://img.shields.io/badge/Accuracy-100%25-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Opérationnel-brightgreen?style=for-the-badge)

**Système intelligent de prédiction des inondations basé sur le Machine Learning**

*Institut National de l'Eau (INE) • République du Bénin • 2025*

</div>

---

## 📋 Description

Ce système d'alerte précoce utilise des algorithmes de **Machine Learning** avancés pour prédire les inondations du fleuve Mono à Athiémé avec un **délai d'anticipation de 24 à 48 heures**, permettant une évacuation préventive des populations vulnérables.

## ✨ Caractéristiques

| Fonctionnalité | Description |
|----------------|-------------|
| 🤖 **Machine Learning** | Random Forest & Régression Logistique |
| 📊 **Précision** | 100% (Random Forest) / 99.79% (Rég. Log.) |
| ⏱️ **Anticipation** | 24-48 heures avant l'événement |
| 📈 **Données** | 7 199 observations (2005-2024) |
| 🎯 **Variables** | 19 features prédictives |

## 🚀 Installation

```bash
# Cloner le repository
git clone [URL_DU_REPO]
cd athieme-flood-alert

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app_professional.py
```

## 📁 Structure du Projet

```
athieme-flood-alert/
├── app_professional.py          # Application principale Streamlit
├── random_forest_model.pkl      # Modèle Random Forest entraîné
├── logistic_regression_model.pkl # Modèle Régression Logistique
├── scaler.pkl                   # Scaler pour normalisation
├── requirements.txt             # Dépendances Python
└── README.md                    # Documentation
```

## 🔬 Méthodologie Scientifique

### Données d'Entrée
- **Période** : 2005-2024 (20 ans)
- **Volume** : 7 199 observations quotidiennes
- **Source** : Direction Générale de l'Eau (DGEau), Bénin

### Variables Prédictives (19 features)
- Cote du fleuve et variations temporelles
- Débit et variations temporelles
- Précipitations cumulées (24h, 48h, 72h, 7j, 14j)
- Indicateurs de saisonnalité

### Algorithmes Déployés
1. **Random Forest Classifier** (100 arbres) — Accuracy: 100%
2. **Régression Logistique Multinomiale** — Accuracy: 99.79%

## 📊 Performances

| Métrique | Random Forest | Rég. Logistique |
|----------|--------------|-----------------|
| Accuracy | 100% | 99.79% |
| Precision | 100% | 90.62% |
| Recall | 100% | 100% |
| F1-Score | 100% | 95.08% |

## 👥 Équipe

**Encadrement Académique :**
- **Prof. VISSIN Expédit** — Directeur de mémoire
- **Dr. Peter OUASSA** — Co-directeur

**Partenaires Institutionnels :**
- Direction Générale de l'Eau (DGEau)
- Agence Nationale de Protection Civile (ANPC)
- Météo-Bénin

## 📜 Licence

Ce projet a été développé dans le cadre d'un mémoire de licence en Gestion des Ressources en Eau à l'Institut National de l'Eau (INE), République du Bénin.

---

<div align="center">

**🌊 Protéger les populations par l'innovation technologique 🌊**

*© 2025 Institut National de l'Eau (INE) — République du Bénin*

</div>
