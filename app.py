import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import json

# Configuration de la page
st.set_page_config(
    page_title="Système d'Alerte Précoce - Athiémé",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .alert-high {
        background-color: #ffebee;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #f44336;
    }
    .alert-medium {
        background-color: #fff3e0;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ff9800;
    }
    .alert-low {
        background-color: #e8f5e9;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4caf50;
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour charger les modèles (simulé pour démo)
@st.cache_resource
def load_models():
    """Charge les modèles ML - À remplacer par vos vrais modèles"""
    # Pour la démo, on simule les modèles
    # Dans la vraie version, utilisez : pickle.load(open('model_rf.pkl', 'rb'))
    return {
        'rf': None,  # Remplacer par votre modèle Random Forest
        'lr': None   # Remplacer par votre modèle Logistic Regression
    }

def predict_flood(data, models):
    """Fait une prédiction d'inondation"""
    # Simulation pour démo - remplacer par vraie prédiction
    # rf_pred = models['rf'].predict_proba(data)[0][1]
    # lr_pred = models['lr'].predict_proba(data)[0][1]
    
    # Pour démo, calcul basé sur cote et débit
    cote = data['Cote_m']
    risk_score = (cote - 3.5) / 5.0  # Normalisation simple
    risk_score = max(0, min(1, risk_score))  # Clip entre 0 et 1
    
    return {
        'rf_proba': risk_score,
        'lr_proba': risk_score * 0.98,
        'risk_level': 'Élevé' if risk_score > 0.7 else 'Moyen' if risk_score > 0.3 else 'Faible'
    }

def get_risk_color(risk_level):
    """Retourne la couleur selon le niveau de risque"""
    colors = {
        'Faible': '#4caf50',
        'Moyen': '#ff9800',
        'Élevé': '#f44336'
    }
    return colors.get(risk_level, '#999')

def get_recommendations(risk_level):
    """Retourne les recommandations selon le niveau de risque"""
    recommendations = {
        'Faible': [
            "✅ Situation normale - Surveillance de routine",
            "📊 Continuer la collecte des données hydrométriques",
            "📢 Pas d'alerte à diffuser aux populations",
            "🔄 Vérifier les équipements de mesure"
        ],
        'Moyen': [
            "⚠️ Vigilance accrue requise",
            "👥 Informer les chefs de village et la Protection Civile",
            "📋 Préparer les plans d'évacuation préventifs",
            "📡 Intensifier la surveillance (mesures 2x/jour)",
            "🚨 Pré-positionner les équipes d'intervention",
            "📱 Activer la chaîne de communication d'urgence"
        ],
        'Élevé': [
            "🚨 ALERTE MAXIMALE - Action immédiate requise",
            "📢 Déclencher l'alerte générale aux populations",
            "🏃 Évacuation préventive des zones à risque",
            "🚁 Mobiliser tous les moyens d'intervention (ANPC, Croix-Rouge)",
            "🏥 Préparer les centres d'hébergement d'urgence",
            "📞 Coordination avec DGEau, Météo-Bénin, Préfecture",
            "⛔ Interdire accès aux zones inondables",
            "🆘 Activer le plan ORSEC communal"
        ]
    }
    return recommendations.get(risk_level, [])

# Titre principal
st.markdown('<div class="main-header">🌊 Système d\'Alerte Précoce aux Inondations</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Commune d\'Athiémé - Fleuve Mono, République du Bénin</div>', unsafe_allow_html=True)

# Barre latérale
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Benin.svg/320px-Flag_of_Benin.svg.png", width=100)
    st.title("Navigation")
    
    page = st.radio(
        "Sélectionnez une page",
        ["🏠 Tableau de bord", "🔮 Faire une prédiction", "📊 Visualisations", "📚 À propos"]
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ Information")
    st.info("""
    **Institut National de l'Eau (INE)**
    
    Système développé dans le cadre d'un mémoire de licence.
    
    **Encadrants:**
    - Prof. VISSIN Expédit
    - Dr. Peter OUASSA
    """)
    
    st.markdown("---")
    st.markdown("**📅 Données:** 2005-2024")
    st.markdown("**🎯 Précision:** 100% (RF)")

# Charger les modèles
models = load_models()

# PAGE 1: TABLEAU DE BORD
if page == "🏠 Tableau de bord":
    st.header("📊 Tableau de Bord Principal")
    
    # Métriques simulées (à remplacer par vraies données)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Cote actuelle",
            value="7.85 m",
            delta="+0.15 m (24h)",
            delta_color="inverse"
        )
    
    with col2:
        st.metric(
            label="Débit actuel",
            value="520 m³/s",
            delta="+45 m³/s (24h)",
            delta_color="inverse"
        )
    
    with col3:
        st.metric(
            label="Risque actuel",
            value="MOYEN",
            delta="45%"
        )
    
    with col4:
        st.metric(
            label="Délai anticipation",
            value="48 heures",
            delta="En surveillance"
        )
    
    st.markdown("---")
    
    # Alerte actuelle
    col_alert, col_reco = st.columns([1, 1])
    
    with col_alert:
        st.markdown("### ⚠️ État d'alerte actuel")
        st.markdown("""
        <div class="alert-medium">
            <h3 style="color: #ff9800; margin:0;">🟡 RISQUE MOYEN</h3>
            <p style="margin-top:0.5rem;"><strong>Probabilité d'inondation:</strong> 45%</p>
            <p><strong>Niveau prévu dans 48h:</strong> 8.15 m</p>
            <p><strong>Tendance:</strong> ↗️ Hausse progressive</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_reco:
        st.markdown("### 💡 Recommandations")
        reco_list = get_recommendations('Moyen')
        for reco in reco_list[:4]:
            st.markdown(f"- {reco}")
    
    st.markdown("---")
    
    # Graphique de tendance (simulé)
    st.markdown("### 📈 Évolution des 7 derniers jours")
    
    dates = pd.date_range(end=datetime.now(), periods=7, freq='D')
    cotes = [7.25, 7.32, 7.45, 7.58, 7.65, 7.75, 7.85]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=dates,
        y=cotes,
        mode='lines+markers',
        name='Cote mesurée',
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    ))
    
    # Seuils
    fig.add_hline(y=7.9, line_dash="dash", line_color="orange", 
                  annotation_text="Seuil d'alerte (7.9m)")
    fig.add_hline(y=8.3, line_dash="dash", line_color="red", 
                  annotation_text="Seuil critique (8.3m)")
    
    fig.update_layout(
        title="Cotes du fleuve Mono à Athiémé",
        xaxis_title="Date",
        yaxis_title="Cote (m)",
        hovermode='x unified',
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistiques rapides
    st.markdown("### 📊 Statistiques de la saison")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    
    with col_stat1:
        st.markdown("""
        <div class="metric-card">
            <h4>Jours d'inondation</h4>
            <h2>145 jours</h2>
            <p>2005-2024</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat2:
        st.markdown("""
        <div class="metric-card">
            <h4>Record historique</h4>
            <h2>8.88 m</h2>
            <p>Sept. 2007</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat3:
        st.markdown("""
        <div class="metric-card">
            <h4>Événements majeurs</h4>
            <h2>10 crues</h2>
            <p>Depuis 2005</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col_stat4:
        st.markdown("""
        <div class="metric-card">
            <h4>Précision modèle</h4>
            <h2>100%</h2>
            <p>Random Forest</p>
        </div>
        """, unsafe_allow_html=True)

# PAGE 2: FAIRE UNE PRÉDICTION
elif page == "🔮 Faire une prédiction":
    st.header("🔮 Prédiction d'Inondation")
    
    st.info("Entrez les données hydrométriques actuelles pour obtenir une prédiction à 24-48h.")
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        st.subheader("📊 Données hydrométriques")
        
        cote = st.number_input("Cote actuelle (m)", min_value=0.5, max_value=10.0, value=7.85, step=0.01)
        debit = st.number_input("Débit actuel (m³/s)", min_value=1.0, max_value=1000.0, value=520.0, step=1.0)
        
        var_24h = st.number_input("Variation 24h de la cote (m)", min_value=-2.0, max_value=2.0, value=0.15, step=0.01)
        var_48h = st.number_input("Variation 48h de la cote (m)", min_value=-2.0, max_value=2.0, value=0.28, step=0.01)
        
    with col_input2:
        st.subheader("🌧️ Données pluviométriques")
        
        pluie_24h = st.number_input("Pluie 24h (mm)", min_value=0.0, max_value=200.0, value=15.0, step=1.0)
        pluie_48h = st.number_input("Pluie 48h (mm)", min_value=0.0, max_value=400.0, value=28.0, step=1.0)
        pluie_7j = st.number_input("Pluie 7 jours (mm)", min_value=0.0, max_value=500.0, value=85.0, step=1.0)
        
        saison = st.selectbox("Saison", ["Saison des crues (Août-Oct)", "Hors saison des crues"])
    
    st.markdown("---")
    
    if st.button("🚀 Lancer la prédiction", type="primary", use_container_width=True):
        # Créer le dictionnaire de données
        data = {
            'Cote_m': cote,
            'Debit_m3s': debit,
            'Var_cote_24h': var_24h,
            'Var_cote_48h': var_48h,
            'Pluie_24h': pluie_24h,
            'Pluie_48h': pluie_48h,
            'Pluie_7j': pluie_7j,
            'Saison_crue': 1 if "crues" in saison else 0
        }
        
        # Faire la prédiction
        with st.spinner("Analyse en cours..."):
            results = predict_flood(data, models)
        
        st.success("✅ Prédiction terminée !")
        
        # Afficher les résultats
        col_res1, col_res2, col_res3 = st.columns(3)
        
        with col_res1:
            st.metric(
                label="Random Forest",
                value=f"{results['rf_proba']*100:.1f}%",
                delta="Probabilité d'inondation"
            )
        
        with col_res2:
            st.metric(
                label="Régression Logistique",
                value=f"{results['lr_proba']*100:.1f}%",
                delta="Probabilité d'inondation"
            )
        
        with col_res3:
            risk_color = get_risk_color(results['risk_level'])
            st.markdown(f"""
            <div style="background-color: {risk_color}20; padding: 1rem; border-radius: 0.5rem; border-left: 4px solid {risk_color};">
                <h4 style="margin:0;">Niveau de risque</h4>
                <h2 style="color: {risk_color}; margin:0.5rem 0;">🟡 {results['risk_level'].upper()}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Recommandations
        st.markdown("### 💡 Recommandations d'actions")
        
        recommendations = get_recommendations(results['risk_level'])
        for reco in recommendations:
            st.markdown(f"- {reco}")
        
        # Graphique de probabilité
        st.markdown("### 📊 Comparaison des modèles")
        
        fig = go.Figure(data=[
            go.Bar(name='Random Forest', x=['Probabilité'], y=[results['rf_proba']*100], marker_color='#1f77b4'),
            go.Bar(name='Régression Logistique', x=['Probabilité'], y=[results['lr_proba']*100], marker_color='#ff7f0e')
        ])
        
        fig.update_layout(
            title="Probabilité d'inondation (%) - Comparaison des modèles",
            yaxis_title="Probabilité (%)",
            barmode='group',
            height=300
        )
        
        st.plotly_chart(fig, use_container_width=True)

# PAGE 3: VISUALISATIONS
elif page == "📊 Visualisations":
    st.header("📊 Visualisations et Analyses")
    
    tab1, tab2, tab3 = st.tabs(["📈 Performance des modèles", "🎯 Importance des variables", "📅 Historique"])
    
    with tab1:
        st.subheader("Performance des modèles ML")
        
        col_perf1, col_perf2 = st.columns(2)
        
        with col_perf1:
            st.markdown("### Random Forest")
            metrics_rf = {
                'Accuracy': 100.0,
                'Precision': 100.0,
                'Recall': 100.0,
                'F1-Score': 100.0
            }
            
            for metric, value in metrics_rf.items():
                st.metric(metric, f"{value}%")
        
        with col_perf2:
            st.markdown("### Régression Logistique")
            metrics_lr = {
                'Accuracy': 99.79,
                'Precision': 90.62,
                'Recall': 100.0,
                'F1-Score': 95.08
            }
            
            for metric, value in metrics_lr.items():
                st.metric(metric, f"{value}%")
        
        # Graphique comparatif
        st.markdown("### 📊 Comparaison globale")
        
        metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
        rf_values = [100, 100, 100, 100]
        lr_values = [99.79, 90.62, 100, 95.08]
        
        fig = go.Figure(data=[
            go.Bar(name='Random Forest', x=metrics, y=rf_values, marker_color='#1f77b4'),
            go.Bar(name='Régression Logistique', x=metrics, y=lr_values, marker_color='#ff7f0e')
        ])
        
        fig.update_layout(
            title="Performance comparative des modèles (%)",
            yaxis_title="Score (%)",
            barmode='group',
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("🎯 Importance des variables (Random Forest)")
        
        # Top 10 variables importantes
        variables = [
            'Cote_m', 'Distance_seuil_critique', 'Distance_seuil_alerte',
            'Debit_m3s', 'Debit_ma_7j', 'Var_cote_48h', 'Cote_ma_7j',
            'Var_cote_24h', 'Taux_montee_m_par_h', 'Var_debit_24h'
        ]
        
        importance = [23.3, 23.2, 15.5, 13.4, 10.2, 4.8, 3.2, 2.5, 2.1, 1.8]
        
        fig = go.Figure(data=[
            go.Bar(x=importance, y=variables, orientation='h', marker_color='#1f77b4')
        ])
        
        fig.update_layout(
            title="Top 10 des variables les plus importantes",
            xaxis_title="Importance (%)",
            yaxis_title="Variable",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("💡 Les 3 variables les plus importantes (cote, distance aux seuils) représentent 62% de l'importance totale.")
    
    with tab3:
        st.subheader("📅 Historique des événements")
        
        # Tableau des événements majeurs
        st.markdown("### 🌊 Événements d'inondation majeurs (2005-2024)")
        
        events = pd.DataFrame({
            'Date': ['Sept 2007', 'Oct 2010', 'Sept 2013', 'Sept 2018', 'Sept 2019', 
                     'Oct 2020', 'Sept 2021', 'Sept 2022', 'Oct 2023', 'Sept 2024'],
            'Cote max (m)': [8.88, 8.55, 8.22, 8.45, 8.50, 8.12, 8.52, 8.67, 8.43, 8.35],
            'Durée (jours)': [12, 8, 6, 10, 14, 7, 11, 15, 9, 10],
            'Personnes affectées': ['65 000+', '45 000', '32 000', '42 000', '31 482', 
                                   '28 000', '38 500', '52 000', '35 000', '40 000']
        })
        
        st.dataframe(events, use_container_width=True, hide_index=True)
        
        # Graphique temporel
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=events['Date'],
            y=events['Cote max (m)'],
            mode='lines+markers',
            name='Cote maximale',
            line=dict(color='#d62728', width=3),
            marker=dict(size=10)
        ))
        
        fig.add_hline(y=7.9, line_dash="dash", line_color="orange", 
                      annotation_text="Seuil d'alerte")
        fig.add_hline(y=8.3, line_dash="dash", line_color="red", 
                      annotation_text="Seuil critique")
        
        fig.update_layout(
            title="Évolution des cotes maximales lors des événements majeurs",
            xaxis_title="Événement",
            yaxis_title="Cote maximale (m)",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)

# PAGE 4: À PROPOS
else:
    st.header("📚 À propos du système")
    
    col_about1, col_about2 = st.columns(2)
    
    with col_about1:
        st.markdown("""
        ### 🎯 Objectif
        
        Ce système d'alerte précoce utilise le **machine learning** pour prédire 
        les inondations du fleuve Mono à Athiémé avec **24 à 48 heures d'anticipation**.
        
        ### 🔬 Méthodologie
        
        - **Données**: 7 199 jours d'observations (2005-2024)
        - **Algorithmes**: Random Forest + Régression Logistique
        - **Variables**: 19 features (cote, débit, variations, précipitations)
        - **Performance**: 100% accuracy avec Random Forest
        
        ### 📊 Résultats clés
        
        - ✅ 145 jours d'inondation identifiés
        - ✅ 10 événements majeurs analysés
        - ✅ Validation rétrospective sur 3 événements récents
        - ✅ Système opérationnel à 3 niveaux de risque
        """)
    
    with col_about2:
        st.markdown("""
        ### 👥 Équipe
        
        **Étudiant chercheur**
        - Institut National de l'Eau (INE), Bénin
        
        **Encadrement académique**
        - Prof. VISSIN Expédit
        - Dr. Peter OUASSA
        
        ### 🤝 Partenaires
        
        - Direction Générale de l'Eau (DGEau)
        - Agence Nationale de Protection Civile (ANPC)
        - Météo-Bénin
        
        ### 📚 Référence
        
        Mémoire de licence en Gestion des Ressources en Eau
        Institut National de l'Eau (INE), Bénin, 2025
        
        ### 📧 Contact
        
        Pour plus d'informations sur ce système ou pour des collaborations:
        - 📍 Institut National de l'Eau, Bénin
        - 🌐 [Site web INE](http://www.ine.bj)
        """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🚀 Perspectives d'amélioration
    
    1. **Intégration données pluviométriques réelles** (CHIRPS, GPM)
    2. **Données barrage de Nangbéto** (débits amont)
    3. **Système multi-horizons** (12h, 24h, 48h, 72h)
    4. **Deep Learning LSTM** pour séries temporelles
    5. **Extension multi-sites** (tout le bassin du Mono)
    6. **Couplage imagerie satellite** (Sentinel-1, Landsat)
    7. **Application mobile** pour diffusion alertes
    """)
    
    st.success("💡 Ce système constitue une première étape vers un système d'alerte complet et opérationnel pour la commune d'Athiémé.")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 1rem;">
    <p>🌊 <strong>Système d'Alerte Précoce aux Inondations - Athiémé</strong></p>
    <p>Institut National de l'Eau (INE) | République du Bénin | 2025</p>
    <p>Développé dans le cadre d'un mémoire de licence en Gestion des Ressources en Eau</p>
</div>
""", unsafe_allow_html=True)
