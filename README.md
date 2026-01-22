# 🌊 Système d'Alerte Précoce aux Inondations - Athiémé

Système de prédiction des inondations du fleuve Mono à Athiémé (Bénin) basé sur le Machine Learning.

## 📋 Description

Ce système utilise des algorithmes de Machine Learning (Random Forest et Régression Logistique) pour prédire les inondations du fleuve Mono avec **24 à 48 heures d'anticipation**, permettant une évacuation préventive des populations vulnérables.

### 🎯 Objectifs

- Prédire les inondations avec un délai d'anticipation de 24-48 heures
- Fournir un système d'alerte à 3 niveaux (Faible, Moyen, Élevé)
- Permettre aux autorités locales de prendre des décisions éclairées
- Réduire les impacts socio-économiques des inondations

### 📊 Données

- **Période**: 2005-2024 (7 199 jours d'observations)
- **Source**: Direction Générale de l'Eau (DGEau), Bénin
- **Variables**: 19 features (cote, débit, variations, précipitations, saisonnalité)
- **Événements**: 145 jours d'inondation identifiés sur 10 événements majeurs

### 🤖 Modèles

1. **Random Forest**
   - Accuracy: 100%
   - Precision: 100%
   - Recall: 100%
   - F1-Score: 100%

2. **Régression Logistique**
   - Accuracy: 99.79%
   - Precision: 90.62%
   - Recall: 100%
   - F1-Score: 95.08%

## 🚀 Installation locale

```bash
# Cloner le repository
git clone https://github.com/votre-username/athieme-flood-alert.git
cd athieme-flood-alert

# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
streamlit run app.py
```

## 🌐 Déploiement sur Streamlit Cloud

1. Fork ce repository sur votre compte GitHub
2. Allez sur [share.streamlit.io](https://share.streamlit.io)
3. Connectez-vous avec GitHub
4. Sélectionnez votre repository
5. Cliquez sur "Deploy"

L'application sera accessible à l'URL: `https://votre-app.streamlit.app`

## 📱 Fonctionnalités

### 🏠 Tableau de bord
- Visualisation en temps réel des données hydrométriques
- État d'alerte actuel avec niveau de risque
- Recommandations d'actions selon le niveau de risque
- Graphiques de tendance sur 7 jours
- Statistiques de la saison

### 🔮 Prédiction
- Formulaire de saisie des données
- Prédiction par Random Forest et Régression Logistique
- Affichage du niveau de risque
- Recommandations personnalisées
- Comparaison des modèles

### 📊 Visualisations
- Performance des modèles ML
- Importance des variables
- Historique des événements majeurs
- Graphiques interactifs

### 📚 Documentation
- Méthodologie complète
- Résultats détaillés
- Perspectives d'amélioration

## 🎓 Contexte académique

Ce système a été développé dans le cadre d'un mémoire de licence en Gestion des Ressources en Eau à l'Institut National de l'Eau (INE), République du Bénin.

**Encadrement:**
- Professeur VISSIN Expédit
- Docteur Peter OUASSA

**Partenaires:**
- Direction Générale de l'Eau (DGEau)
- Agence Nationale de Protection Civile (ANPC)
- Météo-Bénin

## 📈 Perspectives d'amélioration

1. Intégration de données pluviométriques réelles (CHIRPS, GPM)
2. Ajout des données du barrage de Nangbéto
3. Système multi-horizons temporels (12h, 24h, 48h, 72h)
4. Utilisation de Deep Learning (LSTM) pour les séries temporelles
5. Extension à d'autres sites du bassin du Mono
6. Couplage avec imagerie satellite (Sentinel-1, Landsat)
7. Développement d'une application mobile

## 📄 Licence

Ce projet est développé à des fins académiques et de recherche.

## 📧 Contact

Institut National de l'Eau (INE)
République du Bénin
Site web: [www.ine.bj](http://www.ine.bj)

## 🙏 Remerciements

Nous remercions la Direction Générale de l'Eau du Bénin pour la mise à disposition des données hydrométriques, ainsi que l'Agence Nationale de Protection Civile pour les échanges sur la gestion opérationnelle des alertes.

---

**Développé avec ❤️ pour la protection des populations vulnérables d'Athiémé**
