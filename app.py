"""
╔══════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                      ║
║           🌊 SYSTÈME D'ALERTE PRÉCOCE AUX INONDATIONS - ATHIÉMÉ 🌊                   ║
║                                                                                      ║
║                     Plateforme Intelligente de Prédiction                            ║
║                        Basée sur le Machine Learning                                 ║
║                                                                                      ║
║   Auteur: BOSSOU Kossèni Affoladé Roméo                                             ║
║   Encadrement: Prof. VISSIN Expédit | Dr. Pierre OUASSA                             ║
║   Institution: Institut National de l'Eau (INE), Bénin                              ║
║   Année académique: 2024-2025                                                        ║
║                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import joblib
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION DE LA PAGE
# ═══════════════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="🌊 SAP Inondations Athiémé",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════════════════
# CSS PROFESSIONNEL - DESIGN PREMIUM
# ═══════════════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
/* ═══════════════════════════════════════════════════════════════════════════
   IMPORTATION DES POLICES PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ═══════════════════════════════════════════════════════════════════════════
   VARIABLES CSS - PALETTE DE COULEURS
   ═══════════════════════════════════════════════════════════════════════════ */
:root {
    /* Couleurs principales */
    --primary-900: #0a1628;
    --primary-800: #0d2137;
    --primary-700: #0f2d4a;
    --primary-600: #14405f;
    --primary-500: #1a5276;
    --primary-400: #2980b9;
    --primary-300: #5dade2;
    --primary-200: #85c1e9;
    --primary-100: #d4e6f1;
    
    /* Accents */
    --accent-cyan: #00d4ff;
    --accent-gold: #ffd700;
    --accent-emerald: #00d9a5;
    
    /* États */
    --danger-dark: #922b21;
    --danger: #e74c3c;
    --danger-light: #f5b7b1;
    --warning-dark: #9a7d0a;
    --warning: #f39c12;
    --warning-light: #f9e79f;
    --success-dark: #1e8449;
    --success: #27ae60;
    --success-light: #abebc6;
    
    /* Neutres */
    --neutral-900: #1a1a2e;
    --neutral-800: #16213e;
    --neutral-700: #2c3e50;
    --neutral-600: #34495e;
    --neutral-500: #5d6d7e;
    --neutral-400: #85929e;
    --neutral-300: #aab7b8;
    --neutral-200: #d5dbdb;
    --neutral-100: #ecf0f1;
    --neutral-50: #f8f9fa;
    
    /* Effets */
    --shadow-sm: 0 2px 8px rgba(0,0,0,0.08);
    --shadow-md: 0 4px 20px rgba(0,0,0,0.12);
    --shadow-lg: 0 8px 40px rgba(0,0,0,0.16);
    --shadow-glow-cyan: 0 0 30px rgba(0,212,255,0.3);
    --shadow-glow-danger: 0 0 30px rgba(231,76,60,0.4);
    --shadow-glow-warning: 0 0 30px rgba(243,156,18,0.4);
    --shadow-glow-success: 0 0 30px rgba(39,174,96,0.4);
    
    /* Transitions */
    --transition-fast: 0.15s ease;
    --transition-normal: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 0.5s cubic-bezier(0.4, 0, 0.2, 1);
    
    /* Rayons */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;
    --radius-full: 9999px;
}

/* ═══════════════════════════════════════════════════════════════════════════
   STYLES GLOBAUX
   ═══════════════════════════════════════════════════════════════════════════ */
.stApp {
    background: linear-gradient(135deg, var(--primary-900) 0%, var(--neutral-800) 50%, var(--primary-800) 100%);
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* Masquer éléments Streamlit */
#MainMenu, footer, header {visibility: hidden;}
.stDeployButton {display: none;}

/* ═══════════════════════════════════════════════════════════════════════════
   HEADER HERO PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.hero-section {
    background: linear-gradient(135deg, 
        rgba(10,22,40,0.95) 0%, 
        rgba(26,82,118,0.9) 50%, 
        rgba(41,128,185,0.85) 100%);
    border-radius: var(--radius-xl);
    padding: 3rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    border: 1px solid rgba(0,212,255,0.2);
    box-shadow: var(--shadow-lg), var(--shadow-glow-cyan);
}

.hero-section::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 30% 30%, rgba(0,212,255,0.1) 0%, transparent 50%),
                radial-gradient(circle at 70% 70%, rgba(0,217,165,0.08) 0%, transparent 50%);
    animation: heroGlow 15s ease-in-out infinite;
}

@keyframes heroGlow {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    33% { transform: translate(2%, 2%) rotate(1deg); }
    66% { transform: translate(-1%, 1%) rotate(-1deg); }
}

.hero-section::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, 
        var(--accent-cyan), 
        var(--accent-emerald), 
        var(--accent-gold), 
        var(--accent-cyan));
    background-size: 300% 100%;
    animation: shimmerLine 4s linear infinite;
}

@keyframes shimmerLine {
    0% { background-position: 100% 0; }
    100% { background-position: -100% 0; }
}

.hero-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.8rem;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, var(--accent-cyan) 50%, var(--accent-emerald) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
    position: relative;
    z-index: 1;
    text-shadow: 0 0 40px rgba(0,212,255,0.3);
}

.hero-subtitle {
    font-size: 1.3rem;
    color: var(--neutral-200);
    font-weight: 400;
    margin-bottom: 1rem;
    position: relative;
    z-index: 1;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0,212,255,0.15);
    border: 1px solid rgba(0,212,255,0.3);
    padding: 0.5rem 1rem;
    border-radius: var(--radius-full);
    font-size: 0.85rem;
    color: var(--accent-cyan);
    font-weight: 500;
    position: relative;
    z-index: 1;
}

/* ═══════════════════════════════════════════════════════════════════════════
   CARTES MÉTRIQUES PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.metric-card {
    background: linear-gradient(145deg, 
        rgba(255,255,255,0.08) 0%, 
        rgba(255,255,255,0.02) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    border: 1px solid rgba(255,255,255,0.1);
    position: relative;
    overflow: hidden;
    transition: var(--transition-normal);
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(0,212,255,0.3);
    box-shadow: var(--shadow-lg), var(--shadow-glow-cyan);
}

.metric-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--metric-gradient, linear-gradient(90deg, var(--accent-cyan), var(--accent-emerald)));
}

.metric-icon {
    width: 56px;
    height: 56px;
    border-radius: var(--radius-md);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8rem;
    margin-bottom: 1rem;
    background: var(--metric-bg, rgba(0,212,255,0.15));
}

.metric-label {
    font-size: 0.85rem;
    color: var(--neutral-400);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.metric-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 2.4rem;
    font-weight: 700;
    color: #ffffff;
    line-height: 1.1;
}

.metric-unit {
    font-size: 1rem;
    color: var(--neutral-400);
    font-weight: 400;
    margin-left: 0.25rem;
}

.metric-change {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    font-size: 0.85rem;
    font-weight: 600;
    margin-top: 0.5rem;
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-full);
}

.metric-change.positive {
    background: rgba(39,174,96,0.15);
    color: var(--success);
}

.metric-change.negative {
    background: rgba(231,76,60,0.15);
    color: var(--danger);
}

/* ═══════════════════════════════════════════════════════════════════════════
   CARTES D'ALERTE PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.alert-card {
    border-radius: var(--radius-xl);
    padding: 2rem;
    position: relative;
    overflow: hidden;
    border: 2px solid transparent;
    transition: var(--transition-normal);
}

.alert-card.danger {
    background: linear-gradient(145deg, 
        rgba(231,76,60,0.2) 0%, 
        rgba(146,43,33,0.15) 100%);
    border-color: var(--danger);
    box-shadow: var(--shadow-glow-danger);
}

.alert-card.warning {
    background: linear-gradient(145deg, 
        rgba(243,156,18,0.2) 0%, 
        rgba(154,125,10,0.15) 100%);
    border-color: var(--warning);
    box-shadow: var(--shadow-glow-warning);
}

.alert-card.success {
    background: linear-gradient(145deg, 
        rgba(39,174,96,0.2) 0%, 
        rgba(30,132,73,0.15) 100%);
    border-color: var(--success);
    box-shadow: var(--shadow-glow-success);
}

.alert-icon-container {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
    position: relative;
}

.alert-card.danger .alert-icon-container {
    background: linear-gradient(145deg, var(--danger), var(--danger-dark));
    animation: pulseGlow 2s ease-in-out infinite;
}

.alert-card.warning .alert-icon-container {
    background: linear-gradient(145deg, var(--warning), var(--warning-dark));
}

.alert-card.success .alert-icon-container {
    background: linear-gradient(145deg, var(--success), var(--success-dark));
}

@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 0 0 rgba(231,76,60,0.4); }
    50% { box-shadow: 0 0 0 20px rgba(231,76,60,0); }
}

.alert-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.alert-card.danger .alert-title { color: var(--danger-light); }
.alert-card.warning .alert-title { color: var(--warning-light); }
.alert-card.success .alert-title { color: var(--success-light); }

.alert-description {
    font-size: 1.1rem;
    color: rgba(255,255,255,0.8);
    line-height: 1.6;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PROBABILITÉ - JAUGE CIRCULAIRE
   ═══════════════════════════════════════════════════════════════════════════ */
.probability-container {
    text-align: center;
    padding: 2rem;
}

.probability-gauge {
    position: relative;
    width: 200px;
    height: 200px;
    margin: 0 auto 1.5rem;
}

.probability-value {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: 'Space Grotesk', sans-serif;
    font-size: 3rem;
    font-weight: 700;
}

.probability-label {
    font-size: 1rem;
    color: var(--neutral-400);
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* ═══════════════════════════════════════════════════════════════════════════
   GLASSMORPHISM PANELS
   ═══════════════════════════════════════════════════════════════════════════ */
.glass-panel {
    background: linear-gradient(145deg, 
        rgba(255,255,255,0.07) 0%, 
        rgba(255,255,255,0.02) 100%);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-radius: var(--radius-xl);
    border: 1px solid rgba(255,255,255,0.1);
    padding: 2rem;
    margin-bottom: 1.5rem;
}

.glass-panel-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

.glass-panel-icon {
    width: 48px;
    height: 48px;
    border-radius: var(--radius-md);
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
}

.glass-panel-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.4rem;
    font-weight: 600;
    color: #ffffff;
}

.glass-panel-subtitle {
    font-size: 0.9rem;
    color: var(--neutral-400);
}

/* ═══════════════════════════════════════════════════════════════════════════
   SIDEBAR PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, 
        var(--primary-900) 0%, 
        var(--neutral-800) 100%);
    border-right: 1px solid rgba(0,212,255,0.2);
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stNumberInput label,
section[data-testid="stSidebar"] .stSlider label {
    color: var(--neutral-200) !important;
    font-weight: 500;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

section[data-testid="stSidebar"] .stSelectbox > div > div,
section[data-testid="stSidebar"] .stNumberInput > div > div > input {
    background: rgba(255,255,255,0.08) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: var(--radius-md) !important;
    color: #ffffff !important;
}

section[data-testid="stSidebar"] .stSelectbox > div > div:hover,
section[data-testid="stSidebar"] .stNumberInput > div > div > input:hover {
    border-color: var(--accent-cyan) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   BOUTONS PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, var(--primary-500) 0%, var(--primary-600) 100%) !important;
    color: #ffffff !important;
    border: 1px solid rgba(0,212,255,0.3) !important;
    border-radius: var(--radius-md) !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1px !important;
    transition: var(--transition-normal) !important;
    box-shadow: var(--shadow-md) !important;
}

.stButton > button:hover {
    background: linear-gradient(135deg, var(--primary-400) 0%, var(--primary-500) 100%) !important;
    border-color: var(--accent-cyan) !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--shadow-lg), var(--shadow-glow-cyan) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* Bouton principal d'analyse */
.analyze-button > button {
    background: linear-gradient(135deg, var(--accent-cyan) 0%, var(--accent-emerald) 100%) !important;
    color: var(--primary-900) !important;
    font-size: 1.1rem !important;
    padding: 1rem 3rem !important;
    width: 100%;
}

.analyze-button > button:hover {
    background: linear-gradient(135deg, #33ddff 0%, #33e6b8 100%) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   TABS PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(255,255,255,0.05);
    border-radius: var(--radius-lg);
    padding: 0.5rem;
    gap: 0.5rem;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: var(--radius-md) !important;
    color: var(--neutral-400) !important;
    font-weight: 500 !important;
    padding: 0.75rem 1.5rem !important;
    transition: var(--transition-fast) !important;
}

.stTabs [data-baseweb="tab"]:hover {
    color: #ffffff !important;
    background: rgba(255,255,255,0.08) !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, var(--primary-500), var(--primary-600)) !important;
    color: #ffffff !important;
}

.stTabs [data-baseweb="tab-highlight"] {
    display: none !important;
}

.stTabs [data-baseweb="tab-border"] {
    display: none !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   INPUTS PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.stNumberInput > div > div > input,
.stTextInput > div > div > input,
.stSelectbox > div > div {
    background: rgba(255,255,255,0.08) !important;
    border: 2px solid rgba(255,255,255,0.12) !important;
    border-radius: var(--radius-md) !important;
    color: #ffffff !important;
    font-size: 1rem !important;
    padding: 0.75rem 1rem !important;
    transition: var(--transition-fast) !important;
}

.stNumberInput > div > div > input:focus,
.stTextInput > div > div > input:focus,
.stSelectbox > div > div:focus-within {
    border-color: var(--accent-cyan) !important;
    box-shadow: 0 0 0 3px rgba(0,212,255,0.15) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   TABLES PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.stDataFrame {
    background: rgba(255,255,255,0.05) !important;
    border-radius: var(--radius-lg) !important;
    overflow: hidden !important;
}

.stDataFrame [data-testid="stDataFrameResizable"] {
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: var(--radius-lg) !important;
}

/* ═══════════════════════════════════════════════════════════════════════════
   RECOMMENDATIONS PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.reco-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem 1.25rem;
    background: rgba(255,255,255,0.05);
    border-radius: var(--radius-md);
    margin-bottom: 0.75rem;
    border-left: 4px solid var(--accent-cyan);
    transition: var(--transition-fast);
}

.reco-item:hover {
    background: rgba(255,255,255,0.08);
    transform: translateX(4px);
}

.reco-number {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.9rem;
    color: var(--primary-900);
    flex-shrink: 0;
}

.reco-text {
    color: var(--neutral-200);
    font-size: 0.95rem;
    line-height: 1.5;
}

/* ═══════════════════════════════════════════════════════════════════════════
   FOOTER PREMIUM
   ═══════════════════════════════════════════════════════════════════════════ */
.footer-section {
    background: linear-gradient(135deg, 
        rgba(10,22,40,0.95) 0%, 
        rgba(22,33,62,0.95) 100%);
    border-radius: var(--radius-xl);
    padding: 2rem;
    margin-top: 3rem;
    border: 1px solid rgba(0,212,255,0.2);
    text-align: center;
}

.footer-logo {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    background: linear-gradient(135deg, var(--accent-cyan), var(--accent-emerald));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 1rem;
}

.footer-info {
    color: var(--neutral-400);
    font-size: 0.9rem;
    line-height: 1.8;
}

.footer-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(0,212,255,0.1);
    padding: 0.5rem 1rem;
    border-radius: var(--radius-full);
    font-size: 0.85rem;
    color: var(--accent-cyan);
    margin-top: 1rem;
}

/* ═══════════════════════════════════════════════════════════════════════════
   ANIMATIONS
   ═══════════════════════════════════════════════════════════════════════════ */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.animate-fade-in {
    animation: fadeInUp 0.6s ease-out forwards;
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

/* ═══════════════════════════════════════════════════════════════════════════
   RESPONSIVE
   ═══════════════════════════════════════════════════════════════════════════ */
@media (max-width: 768px) {
    .hero-title {
        font-size: 1.8rem;
    }
    
    .hero-subtitle {
        font-size: 1rem;
    }
    
    .metric-value {
        font-size: 1.8rem;
    }
    
    .glass-panel {
        padding: 1.25rem;
    }
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# CHARGEMENT DES MODÈLES ET DONNÉES
# ═══════════════════════════════════════════════════════════════════════════════
@st.cache_resource
def load_models():
    """Charge les modèles ML entraînés"""
    rf_model = joblib.load('random_forest_model.pkl')
    lr_model = joblib.load('logistic_regression_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return rf_model, lr_model, scaler

@st.cache_data
def load_data():
    """Charge les données historiques"""
    df = pd.read_csv('dataset_athieme_features_2005_2024.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Chargement
rf_model, lr_model, scaler = load_models()
df_hist = load_data()

# ═══════════════════════════════════════════════════════════════════════════════
# CONSTANTES ET CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════
SEUIL_ALERTE = 7.9
SEUIL_CRITIQUE = 8.3
FEATURES = [
    'Cote_m', 'Debit_m3s', 'Var_cote_24h', 'Var_cote_48h', 'Var_cote_7j',
    'Var_debit_24h', 'Var_debit_48h', 'Taux_montee_m_par_h',
    'Distance_seuil_alerte', 'Distance_seuil_critique',
    'Cote_ma_7j', 'Debit_ma_7j',
    'Pluie_24h', 'Pluie_48h', 'Pluie_72h', 'Pluie_7j', 'Pluie_14j',
    'Jour_annee', 'Saison_crue'
]

# ═══════════════════════════════════════════════════════════════════════════════
# FONCTIONS UTILITAIRES
# ═══════════════════════════════════════════════════════════════════════════════

def prepare_features(cote, debit, var_24h, var_48h, pluie_24h, pluie_48h, pluie_72h, pluie_7j, pluie_14j):
    """Prépare le vecteur de features pour la prédiction"""
    
    # Calculs dérivés
    var_7j = var_24h * 3  # Approximation
    var_debit_24h = var_24h * 50  # Approximation basée sur relation cote-débit
    var_debit_48h = var_48h * 50
    taux_montee = var_24h / 24
    distance_alerte = SEUIL_ALERTE - cote
    distance_critique = SEUIL_CRITIQUE - cote
    cote_ma_7j = cote - (var_24h * 3)  # Approximation
    debit_ma_7j = debit * 0.95
    jour_annee = datetime.now().timetuple().tm_yday
    mois = datetime.now().month
    saison_crue = 1 if mois in [8, 9, 10] else 0
    
    features = np.array([[
        cote, debit, var_24h, var_48h, var_7j,
        var_debit_24h, var_debit_48h, taux_montee,
        distance_alerte, distance_critique,
        cote_ma_7j, debit_ma_7j,
        pluie_24h, pluie_48h, pluie_72h, pluie_7j, pluie_14j,
        jour_annee, saison_crue
    ]])
    
    return features

def get_risk_level(probability):
    """Détermine le niveau de risque"""
    if probability >= 0.70:
        return "ÉLEVÉ", "danger"
    elif probability >= 0.30:
        return "MOYEN", "warning"
    else:
        return "FAIBLE", "success"

def get_recommendations(risk_level, probability, cote):
    """Génère les recommandations selon le risque"""
    
    if risk_level == "ÉLEVÉ":
        return [
            "🚨 ÉVACUATION PRÉVENTIVE des zones inondables à déclencher immédiatement",
            "📞 Alerter l'ANPC et les autorités locales pour activation du plan ORSEC",
            "📢 Diffuser l'alerte rouge via tous les canaux (radio, SMS, crieurs publics)",
            "🏥 Pré-positionner les équipes de secours et moyens médicaux d'urgence",
            "🚗 Organiser le transport des personnes vulnérables vers les sites d'hébergement",
            "💧 Sécuriser les points d'eau potable et stocks alimentaires d'urgence"
        ]
    elif risk_level == "MOYEN":
        return [
            "⚠️ Activer la cellule de veille 24h/24 avec suivi horaire des niveaux",
            "📋 Préparer les plans d'évacuation et identifier les itinéraires",
            "📦 Constituer les kits d'urgence et vérifier les stocks de secours",
            "📞 Informer les populations riveraines du risque et des consignes",
            "🏠 Protéger les biens et documents importants en hauteur",
            "📡 Maintenir la communication avec les services météorologiques"
        ]
    else:
        return [
            "✅ Surveillance de routine - lecture quotidienne des niveaux",
            "📊 Mise à jour des données hydrométriques dans le système",
            "🔧 Vérification du bon fonctionnement des équipements de mesure",
            "📝 Sensibilisation continue des populations aux risques d'inondation"
        ]

# ═══════════════════════════════════════════════════════════════════════════════
# FONCTION: CRÉATION DES GRAPHIQUES PLOTLY
# ═══════════════════════════════════════════════════════════════════════════════

def create_gauge_chart(probability, risk_level, risk_class):
    """Crée une jauge de probabilité élégante"""
    
    colors = {
        'danger': '#e74c3c',
        'warning': '#f39c12', 
        'success': '#27ae60'
    }
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=probability * 100,
        number={'suffix': '%', 'font': {'size': 48, 'color': '#ffffff', 'family': 'Space Grotesk'}},
        gauge={
            'axis': {
                'range': [0, 100],
                'tickwidth': 2,
                'tickcolor': '#ffffff',
                'tickfont': {'color': '#aab7b8', 'size': 12}
            },
            'bar': {'color': colors[risk_class], 'thickness': 0.8},
            'bgcolor': 'rgba(255,255,255,0.05)',
            'borderwidth': 2,
            'bordercolor': 'rgba(255,255,255,0.2)',
            'steps': [
                {'range': [0, 30], 'color': 'rgba(39,174,96,0.15)'},
                {'range': [30, 70], 'color': 'rgba(243,156,18,0.15)'},
                {'range': [70, 100], 'color': 'rgba(231,76,60,0.15)'}
            ],
            'threshold': {
                'line': {'color': '#ffffff', 'width': 3},
                'thickness': 0.8,
                'value': probability * 100
            }
        },
        title={
            'text': f"<b>Risque {risk_level}</b><br><span style='font-size:14px;color:#aab7b8'>Probabilité d'inondation (24-48h)</span>",
            'font': {'size': 20, 'color': '#ffffff', 'family': 'Space Grotesk'}
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=350,
        margin=dict(l=30, r=30, t=80, b=30),
        font={'family': 'Plus Jakarta Sans'}
    )
    
    return fig

def create_historical_chart(df, days=30):
    """Crée le graphique d'évolution historique"""
    
    df_recent = df.tail(days).copy()
    
    fig = go.Figure()
    
    # Zone de danger (rouge)
    fig.add_hrect(
        y0=SEUIL_CRITIQUE, y1=df_recent['Cote_m'].max() + 0.5,
        fillcolor='rgba(231,76,60,0.1)',
        line_width=0,
        annotation_text="Zone critique", annotation_position="top right",
        annotation=dict(font_size=11, font_color='#e74c3c')
    )
    
    # Zone d'alerte (orange)
    fig.add_hrect(
        y0=SEUIL_ALERTE, y1=SEUIL_CRITIQUE,
        fillcolor='rgba(243,156,18,0.1)',
        line_width=0,
        annotation_text="Zone d'alerte", annotation_position="top right",
        annotation=dict(font_size=11, font_color='#f39c12')
    )
    
    # Ligne des cotes
    fig.add_trace(go.Scatter(
        x=df_recent['Date'],
        y=df_recent['Cote_m'],
        mode='lines+markers',
        name='Niveau du fleuve',
        line=dict(color='#00d4ff', width=3, shape='spline'),
        marker=dict(size=6, color='#00d4ff', line=dict(color='#ffffff', width=1)),
        fill='tozeroy',
        fillcolor='rgba(0,212,255,0.1)',
        hovertemplate='<b>Date:</b> %{x|%d/%m/%Y}<br><b>Cote:</b> %{y:.2f} m<extra></extra>'
    ))
    
    # Seuil d'alerte
    fig.add_hline(
        y=SEUIL_ALERTE,
        line_dash="dash",
        line_color='#f39c12',
        line_width=2,
        annotation_text=f"Seuil d'alerte ({SEUIL_ALERTE}m)",
        annotation_position="bottom left",
        annotation=dict(font_size=12, font_color='#f39c12', bgcolor='rgba(0,0,0,0.5)')
    )
    
    # Seuil critique
    fig.add_hline(
        y=SEUIL_CRITIQUE,
        line_dash="dash",
        line_color='#e74c3c',
        line_width=2,
        annotation_text=f"Seuil critique ({SEUIL_CRITIQUE}m)",
        annotation_position="bottom left",
        annotation=dict(font_size=12, font_color='#e74c3c', bgcolor='rgba(0,0,0,0.5)')
    )
    
    fig.update_layout(
        title=dict(
            text=f'<b>📈 Évolution du niveau du fleuve Mono</b><br><span style="font-size:13px;color:#aab7b8">Derniers {days} jours de mesures à la station d\'Athiémé</span>',
            font=dict(size=18, color='#ffffff', family='Space Grotesk'),
            x=0
        ),
        xaxis=dict(
            title='Date',
            gridcolor='rgba(255,255,255,0.05)',
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff')
        ),
        yaxis=dict(
            title='Cote (mètres)',
            gridcolor='rgba(255,255,255,0.05)',
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff'),
            range=[0, max(df_recent['Cote_m'].max() + 0.5, SEUIL_CRITIQUE + 0.5)]
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(l=60, r=30, t=100, b=60),
        hovermode='x unified',
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='right',
            x=1,
            font=dict(color='#ffffff')
        )
    )
    
    return fig

def create_model_comparison_chart():
    """Crée le graphique de comparaison des modèles"""
    
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    rf_values = [100, 100, 100, 100]
    lr_values = [99.58, 82.86, 100, 90.62]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Random Forest',
        x=metrics,
        y=rf_values,
        marker=dict(
            color='#00d4ff',
            line=dict(color='#00d4ff', width=2),
            pattern=dict(shape='')
        ),
        text=[f'{v}%' for v in rf_values],
        textposition='outside',
        textfont=dict(color='#00d4ff', size=14, family='Space Grotesk')
    ))
    
    fig.add_trace(go.Bar(
        name='Régression Logistique',
        x=metrics,
        y=lr_values,
        marker=dict(
            color='#00d9a5',
            line=dict(color='#00d9a5', width=2)
        ),
        text=[f'{v:.1f}%' for v in lr_values],
        textposition='outside',
        textfont=dict(color='#00d9a5', size=14, family='Space Grotesk')
    ))
    
    fig.update_layout(
        title=dict(
            text='<b>🏆 Comparaison des Performances</b><br><span style="font-size:13px;color:#aab7b8">Métriques d\'évaluation sur l\'ensemble de test (1 439 observations)</span>',
            font=dict(size=18, color='#ffffff', family='Space Grotesk'),
            x=0
        ),
        barmode='group',
        xaxis=dict(
            tickfont=dict(color='#ffffff', size=13),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        yaxis=dict(
            title='Score (%)',
            range=[0, 115],
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff'),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=60, r=30, t=100, b=60),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            font=dict(color='#ffffff', size=12)
        ),
        bargap=0.15,
        bargroupgap=0.1
    )
    
    return fig

def create_feature_importance_chart():
    """Crée le graphique d'importance des variables"""
    
    features_names = [
        'Distance seuil critique', 'Cote (m)', 'Distance seuil alerte',
        'Débit (m³/s)', 'Moyenne mobile débit 7j', 'Moyenne mobile cote 7j',
        'Pluie cumul 7j', 'Pluie 72h', 'Saison des crues', 'Pluie 14j'
    ]
    importance = [23.22, 22.96, 15.43, 13.86, 10.08, 4.57, 2.64, 1.90, 1.89, 1.86]
    
    colors = px.colors.sequential.Tealgrn[::-1][:len(features_names)]
    
    fig = go.Figure(go.Bar(
        x=importance,
        y=features_names,
        orientation='h',
        marker=dict(
            color=importance,
            colorscale='Tealgrn',
            line=dict(color='rgba(255,255,255,0.3)', width=1)
        ),
        text=[f'{v:.1f}%' for v in importance],
        textposition='outside',
        textfont=dict(color='#ffffff', size=12)
    ))
    
    fig.update_layout(
        title=dict(
            text='<b>🎯 Importance des Variables Prédictives</b><br><span style="font-size:13px;color:#aab7b8">Contribution relative dans le modèle Random Forest</span>',
            font=dict(size=18, color='#ffffff', family='Space Grotesk'),
            x=0
        ),
        xaxis=dict(
            title='Importance relative (%)',
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff'),
            gridcolor='rgba(255,255,255,0.05)',
            range=[0, 30]
        ),
        yaxis=dict(
            tickfont=dict(color='#ffffff', size=11),
            autorange='reversed'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=450,
        margin=dict(l=180, r=60, t=100, b=60)
    )
    
    return fig

def create_seasonal_chart(df):
    """Crée le graphique de saisonnalité"""
    
    monthly_avg = df.groupby('Mois')['Cote_m'].agg(['mean', 'max']).reset_index()
    month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct', 'Nov', 'Déc']
    monthly_avg['Mois_nom'] = [month_names[i-1] for i in monthly_avg['Mois']]
    
    colors = ['#00d4ff' if m not in [8, 9, 10] else '#e74c3c' for m in monthly_avg['Mois']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=monthly_avg['Mois_nom'],
        y=monthly_avg['mean'],
        name='Cote moyenne',
        marker=dict(color=colors, line=dict(color='rgba(255,255,255,0.3)', width=1)),
        text=[f'{v:.2f}m' for v in monthly_avg['mean']],
        textposition='outside',
        textfont=dict(size=10, color='#aab7b8')
    ))
    
    fig.add_trace(go.Scatter(
        x=monthly_avg['Mois_nom'],
        y=monthly_avg['max'],
        name='Cote maximale',
        mode='lines+markers',
        line=dict(color='#ffd700', width=3),
        marker=dict(size=10, color='#ffd700', line=dict(color='#ffffff', width=2))
    ))
    
    fig.add_hline(
        y=SEUIL_ALERTE,
        line_dash="dash",
        line_color='#f39c12',
        annotation_text="Seuil d'alerte",
        annotation_position="bottom right"
    )
    
    fig.update_layout(
        title=dict(
            text='<b>📅 Saisonnalité des Niveaux du Fleuve</b><br><span style="font-size:13px;color:#aab7b8">Moyennes mensuelles sur la période 2005-2024 | Rouge = Saison des crues</span>',
            font=dict(size=18, color='#ffffff', family='Space Grotesk'),
            x=0
        ),
        xaxis=dict(
            tickfont=dict(color='#ffffff', size=12),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        yaxis=dict(
            title='Cote (mètres)',
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff'),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=60, r=30, t=100, b=60),
        legend=dict(
            orientation='h',
            yanchor='bottom',
            y=1.02,
            xanchor='center',
            x=0.5,
            font=dict(color='#ffffff')
        ),
        barmode='group'
    )
    
    return fig

def create_flood_events_chart(df):
    """Crée le graphique des événements d'inondation"""
    
    events = [
        {'date': '2007-09', 'cote': 8.88, 'label': 'Sept 2007'},
        {'date': '2010-10', 'cote': 8.55, 'label': 'Oct 2010'},
        {'date': '2013-09', 'cote': 8.22, 'label': 'Sept 2013'},
        {'date': '2018-09', 'cote': 8.45, 'label': 'Sept 2018'},
        {'date': '2019-09', 'cote': 8.50, 'label': 'Sept 2019'},
        {'date': '2021-09', 'cote': 8.52, 'label': 'Sept 2021'},
        {'date': '2022-09', 'cote': 8.67, 'label': 'Sept 2022'},
        {'date': '2023-10', 'cote': 8.43, 'label': 'Oct 2023'}
    ]
    
    events_df = pd.DataFrame(events)
    colors = ['#e74c3c' if c > 8.5 else '#f39c12' for c in events_df['cote']]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=events_df['label'],
        y=events_df['cote'],
        marker=dict(
            color=colors,
            line=dict(color='rgba(255,255,255,0.3)', width=2)
        ),
        text=[f'{v:.2f}m' for v in events_df['cote']],
        textposition='outside',
        textfont=dict(color='#ffffff', size=12, family='Space Grotesk')
    ))
    
    fig.add_hline(y=SEUIL_ALERTE, line_dash="dash", line_color='#f39c12', line_width=2)
    fig.add_hline(y=SEUIL_CRITIQUE, line_dash="dash", line_color='#e74c3c', line_width=2)
    
    # Annotation du record
    fig.add_annotation(
        x='Sept 2007',
        y=8.88,
        text='🏆 Record historique',
        showarrow=True,
        arrowhead=2,
        arrowcolor='#ffd700',
        font=dict(color='#ffd700', size=12),
        ax=0,
        ay=-40
    )
    
    fig.update_layout(
        title=dict(
            text='<b>🌊 Événements d\'Inondation Majeurs</b><br><span style="font-size:13px;color:#aab7b8">Cotes maximales atteintes lors des crues historiques (2005-2024)</span>',
            font=dict(size=18, color='#ffffff', family='Space Grotesk'),
            x=0
        ),
        xaxis=dict(
            tickfont=dict(color='#ffffff', size=11),
            tickangle=-45,
            gridcolor='rgba(255,255,255,0.05)'
        ),
        yaxis=dict(
            title='Cote maximale (mètres)',
            range=[7.5, 9.5],
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff'),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=400,
        margin=dict(l=60, r=30, t=100, b=80)
    )
    
    return fig

# ═══════════════════════════════════════════════════════════════════════════════
# INTERFACE PRINCIPALE
# ═══════════════════════════════════════════════════════════════════════════════

# Header Hero
st.markdown("""
<div class="hero-section">
    <div class="hero-badge">
        <span>🎓</span>
        <span>Mémoire de Licence Professionnelle • INE Bénin • 2025</span>
    </div>
    <h1 class="hero-title">🌊 Système d'Alerte Précoce aux Inondations</h1>
    <p class="hero-subtitle">Plateforme Intelligente de Prédiction par Machine Learning — Station d'Athiémé, Fleuve Mono</p>
    <div style="display: flex; gap: 1rem; flex-wrap: wrap; margin-top: 1.5rem; position: relative; z-index: 1;">
        <div class="hero-badge">
            <span>📊</span>
            <span>7 199 observations</span>
        </div>
        <div class="hero-badge">
            <span>🎯</span>
            <span>100% Accuracy (Random Forest)</span>
        </div>
        <div class="hero-badge">
            <span>⏱️</span>
            <span>Prédiction 24-48h</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# SIDEBAR - PARAMÈTRES DE PRÉDICTION
# ═══════════════════════════════════════════════════════════════════════════════

with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1.5rem 0; border-bottom: 1px solid rgba(255,255,255,0.1); margin-bottom: 1.5rem;">
        <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌊</div>
        <div style="font-family: 'Space Grotesk', sans-serif; font-size: 1.2rem; font-weight: 700; color: #00d4ff;">
            SAP Athiémé
        </div>
        <div style="font-size: 0.8rem; color: #aab7b8;">v2.0 • Machine Learning</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Paramètres Hydrométriques")
    
    # Date de l'analyse
    date_analyse = st.date_input(
        "📅 Date de l'analyse",
        value=datetime.now(),
        help="Date des mesures à analyser"
    )
    
    st.markdown("---")
    
    # Mesures principales
    st.markdown("#### 💧 Mesures du jour")
    
    cote_actuelle = st.number_input(
        "Cote actuelle (m)",
        min_value=0.0,
        max_value=12.0,
        value=6.5,
        step=0.01,
        format="%.2f",
        help="Niveau d'eau mesuré au limnimètre"
    )
    
    debit_actuel = st.number_input(
        "Débit actuel (m³/s)",
        min_value=0.0,
        max_value=1000.0,
        value=250.0,
        step=1.0,
        format="%.1f",
        help="Débit calculé à partir de la courbe de tarage"
    )
    
    st.markdown("---")
    
    st.markdown("#### 📈 Variations observées")
    
    var_cote_24h = st.number_input(
        "Variation 24h (m)",
        min_value=-3.0,
        max_value=3.0,
        value=0.15,
        step=0.01,
        format="%.2f",
        help="Différence de cote avec hier"
    )
    
    var_cote_48h = st.number_input(
        "Variation 48h (m)",
        min_value=-5.0,
        max_value=5.0,
        value=0.28,
        step=0.01,
        format="%.2f",
        help="Différence de cote avec avant-hier"
    )
    
    st.markdown("---")
    
    st.markdown("#### 🌧️ Précipitations")
    
    pluie_24h = st.number_input(
        "Pluie dernières 24h (mm)",
        min_value=0.0,
        max_value=200.0,
        value=15.0,
        step=0.5,
        help="Cumul pluviométrique des dernières 24 heures"
    )
    
    pluie_48h = st.number_input(
        "Pluie dernières 48h (mm)",
        min_value=0.0,
        max_value=300.0,
        value=28.0,
        step=0.5
    )
    
    pluie_72h = st.number_input(
        "Pluie dernières 72h (mm)",
        min_value=0.0,
        max_value=400.0,
        value=42.0,
        step=0.5
    )
    
    pluie_7j = st.number_input(
        "Pluie derniers 7 jours (mm)",
        min_value=0.0,
        max_value=500.0,
        value=85.0,
        step=1.0
    )
    
    pluie_14j = st.number_input(
        "Pluie derniers 14 jours (mm)",
        min_value=0.0,
        max_value=700.0,
        value=145.0,
        step=1.0
    )
    
    st.markdown("---")
    
    st.markdown("#### ⚙️ Options")
    
    modele_choisi = st.selectbox(
        "Modèle de prédiction",
        ["Random Forest (recommandé)", "Régression Logistique", "Moyenne des deux"],
        help="Sélectionnez le modèle à utiliser pour la prédiction"
    )
    
    st.markdown("---")
    
    # Bouton d'analyse
    st.markdown('<div class="analyze-button">', unsafe_allow_html=True)
    analyze_button = st.button("🔍 ANALYSER LE RISQUE", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# ONGLETS PRINCIPAUX
# ═══════════════════════════════════════════════════════════════════════════════

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🎯 Prédiction", 
    "📊 Dashboard", 
    "🏆 Performances", 
    "📈 Analyse Historique",
    "📖 Documentation"
])

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 1: PRÉDICTION
# ═══════════════════════════════════════════════════════════════════════════════

with tab1:
    
    if analyze_button:
        # Préparation des features
        features = prepare_features(
            cote_actuelle, debit_actuel, var_cote_24h, var_cote_48h,
            pluie_24h, pluie_48h, pluie_72h, pluie_7j, pluie_14j
        )
        
        # Normalisation
        features_scaled = scaler.transform(features)
        
        # Prédictions
        rf_proba = rf_model.predict_proba(features_scaled)[0][1]
        lr_proba = lr_model.predict_proba(features_scaled)[0][1]
        
        # Sélection du modèle
        if "Random Forest" in modele_choisi:
            probability = rf_proba
        elif "Régression" in modele_choisi:
            probability = lr_proba
        else:
            probability = (rf_proba + lr_proba) / 2
        
        risk_level, risk_class = get_risk_level(probability)
        recommendations = get_recommendations(risk_level, probability, cote_actuelle)
        
        # Affichage des résultats
        col1, col2 = st.columns([1, 1])
        
        with col1:
            # Carte d'alerte
            alert_icons = {'danger': '🚨', 'warning': '⚠️', 'success': '✅'}
            alert_titles = {'danger': 'ALERTE CRITIQUE', 'warning': 'VIGILANCE RENFORCÉE', 'success': 'SITUATION NORMALE'}
            alert_descriptions = {
                'danger': 'Probabilité très élevée d\'inondation dans les 24-48 heures. Actions immédiates requises.',
                'warning': 'Risque modéré d\'inondation. Surveillance renforcée et préparation recommandées.',
                'success': 'Risque faible d\'inondation. Maintien de la surveillance de routine.'
            }
            
            st.markdown(f"""
            <div class="alert-card {risk_class}">
                <div class="alert-icon-container">
                    {alert_icons[risk_class]}
                </div>
                <h2 class="alert-title">{alert_titles[risk_class]}</h2>
                <p class="alert-description">{alert_descriptions[risk_class]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Jauge de probabilité
            st.plotly_chart(create_gauge_chart(probability, risk_level, risk_class), use_container_width=True)
        
        with col2:
            # Métriques détaillées
            st.markdown("""
            <div class="glass-panel">
                <div class="glass-panel-header">
                    <div class="glass-panel-icon">📊</div>
                    <div>
                        <div class="glass-panel-title">Analyse Détaillée</div>
                        <div class="glass-panel-subtitle">Paramètres de la prédiction</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Métriques en grille
            m1, m2 = st.columns(2)
            with m1:
                st.metric("Cote actuelle", f"{cote_actuelle:.2f} m", f"{var_cote_24h:+.2f} m/24h")
                st.metric("Débit", f"{debit_actuel:.0f} m³/s")
                st.metric("Random Forest", f"{rf_proba*100:.1f}%")
            with m2:
                st.metric("Distance seuil alerte", f"{SEUIL_ALERTE - cote_actuelle:.2f} m")
                st.metric("Pluie 7 jours", f"{pluie_7j:.0f} mm")
                st.metric("Rég. Logistique", f"{lr_proba*100:.1f}%")
            
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Recommandations
        st.markdown("""
        <div class="glass-panel">
            <div class="glass-panel-header">
                <div class="glass-panel-icon">📋</div>
                <div>
                    <div class="glass-panel-title">Recommandations Opérationnelles</div>
                    <div class="glass-panel-subtitle">Actions à entreprendre selon le niveau de risque</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        reco_html = ""
        for i, reco in enumerate(recommendations, 1):
            reco_html += f"""
            <div class="reco-item">
                <div class="reco-number">{i}</div>
                <div class="reco-text">{reco}</div>
            </div>
            """
        st.markdown(reco_html, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
    else:
        # État initial - instructions
        st.markdown("""
        <div class="glass-panel" style="text-align: center; padding: 4rem 2rem;">
            <div style="font-size: 4rem; margin-bottom: 1.5rem;">🎯</div>
            <h2 style="color: #ffffff; font-family: 'Space Grotesk', sans-serif; margin-bottom: 1rem;">
                Prêt pour l'Analyse
            </h2>
            <p style="color: #aab7b8; font-size: 1.1rem; max-width: 500px; margin: 0 auto 2rem;">
                Entrez les paramètres hydrométriques dans le panneau latéral, puis cliquez sur 
                <strong style="color: #00d4ff;">ANALYSER LE RISQUE</strong> pour obtenir une prédiction.
            </p>
            <div style="display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                <div style="text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">💧</div>
                    <div style="color: #aab7b8; font-size: 0.9rem;">Cote & Débit</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📈</div>
                    <div style="color: #aab7b8; font-size: 0.9rem;">Variations</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🌧️</div>
                    <div style="color: #aab7b8; font-size: 0.9rem;">Précipitations</div>
                </div>
                <div style="text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🤖</div>
                    <div style="color: #aab7b8; font-size: 0.9rem;">Prédiction ML</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 2: DASHBOARD
# ═══════════════════════════════════════════════════════════════════════════════

with tab2:
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card" style="--metric-gradient: linear-gradient(90deg, #00d4ff, #00d9a5);">
            <div class="metric-icon" style="--metric-bg: rgba(0,212,255,0.15);">📊</div>
            <div class="metric-label">Observations</div>
            <div class="metric-value">7 199<span class="metric-unit">jours</span></div>
            <div class="metric-change positive">↑ 2005-2024</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card" style="--metric-gradient: linear-gradient(90deg, #e74c3c, #c0392b);">
            <div class="metric-icon" style="--metric-bg: rgba(231,76,60,0.15);">🌊</div>
            <div class="metric-label">Inondations</div>
            <div class="metric-value">145<span class="metric-unit">jours</span></div>
            <div class="metric-change negative">2.01% du total</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="--metric-gradient: linear-gradient(90deg, #f39c12, #e67e22);">
            <div class="metric-icon" style="--metric-bg: rgba(243,156,18,0.15);">📏</div>
            <div class="metric-label">Record historique</div>
            <div class="metric-value">8.88<span class="metric-unit">m</span></div>
            <div class="metric-change negative">Sept 2007</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-card" style="--metric-gradient: linear-gradient(90deg, #27ae60, #1e8449);">
            <div class="metric-icon" style="--metric-bg: rgba(39,174,96,0.15);">🎯</div>
            <div class="metric-label">Accuracy RF</div>
            <div class="metric-value">100<span class="metric-unit">%</span></div>
            <div class="metric-change positive">Performance parfaite</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_historical_chart(df_hist, 60), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_seasonal_chart(df_hist), use_container_width=True)
    
    # Statistiques détaillées
    st.markdown("""
    <div class="glass-panel">
        <div class="glass-panel-header">
            <div class="glass-panel-icon">📈</div>
            <div>
                <div class="glass-panel-title">Statistiques du Dataset</div>
                <div class="glass-panel-subtitle">Analyse descriptive des variables principales (2005-2024)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    stats_df = df_hist[['Cote_m', 'Debit_m3s', 'Pluie_24h', 'Pluie_7j']].describe().T
    stats_df.columns = ['Nb obs.', 'Moyenne', 'Écart-type', 'Min', '25%', 'Médiane', '75%', 'Max']
    stats_df.index = ['Cote (m)', 'Débit (m³/s)', 'Pluie 24h (mm)', 'Pluie 7j (mm)']
    
    st.dataframe(
        stats_df.style.format("{:.2f}").background_gradient(cmap='Blues', subset=['Moyenne', 'Max']),
        use_container_width=True
    )
    
    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 3: PERFORMANCES
# ═══════════════════════════════════════════════════════════════════════════════

with tab3:
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(create_model_comparison_chart(), use_container_width=True)
    
    with col2:
        st.plotly_chart(create_feature_importance_chart(), use_container_width=True)
    
    # Matrices de confusion
    st.markdown("""
    <div class="glass-panel">
        <div class="glass-panel-header">
            <div class="glass-panel-icon">📊</div>
            <div>
                <div class="glass-panel-title">Matrices de Confusion</div>
                <div class="glass-panel-subtitle">Répartition des prédictions sur l'ensemble de test (1 439 observations)</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Matrice RF
        cm_rf = np.array([[1410, 0], [0, 29]])
        fig_cm_rf = go.Figure(data=go.Heatmap(
            z=cm_rf,
            x=['Prédit Normal', 'Prédit Inondation'],
            y=['Réel Normal', 'Réel Inondation'],
            colorscale='Blues',
            showscale=False,
            text=cm_rf,
            texttemplate='%{text}',
            textfont=dict(size=20, color='white')
        ))
        fig_cm_rf.update_layout(
            title=dict(text='<b>Random Forest</b><br><span style="color:#aab7b8;font-size:12px">0 erreur • Performance parfaite</span>', font=dict(color='white', size=16)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=80, r=30, t=80, b=60),
            xaxis=dict(tickfont=dict(color='white'), side='bottom'),
            yaxis=dict(tickfont=dict(color='white'), autorange='reversed')
        )
        st.plotly_chart(fig_cm_rf, use_container_width=True)
    
    with col2:
        # Matrice LR
        cm_lr = np.array([[1404, 6], [0, 29]])
        fig_cm_lr = go.Figure(data=go.Heatmap(
            z=cm_lr,
            x=['Prédit Normal', 'Prédit Inondation'],
            y=['Réel Normal', 'Réel Inondation'],
            colorscale='Oranges',
            showscale=False,
            text=cm_lr,
            texttemplate='%{text}',
            textfont=dict(size=20, color='white')
        ))
        fig_cm_lr.update_layout(
            title=dict(text='<b>Régression Logistique</b><br><span style="color:#aab7b8;font-size:12px">6 faux positifs • Recall 100%</span>', font=dict(color='white', size=16)),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=300,
            margin=dict(l=80, r=30, t=80, b=60),
            xaxis=dict(tickfont=dict(color='white'), side='bottom'),
            yaxis=dict(tickfont=dict(color='white'), autorange='reversed')
        )
        st.plotly_chart(fig_cm_lr, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Tableau récapitulatif
    st.markdown("""
    <div class="glass-panel">
        <div class="glass-panel-header">
            <div class="glass-panel-icon">🏆</div>
            <div>
                <div class="glass-panel-title">Récapitulatif des Performances</div>
                <div class="glass-panel-subtitle">Comparaison détaillée des deux algorithmes</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    perf_data = {
        'Métrique': ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'ROC-AUC', 'Faux Positifs', 'Faux Négatifs'],
        'Random Forest': ['100.00%', '100.00%', '100.00%', '100.00%', '1.0000', '0', '0'],
        'Régression Logistique': ['99.58%', '82.86%', '100.00%', '90.62%', '1.0000', '6', '0'],
        'Interprétation': [
            'Taux global de bonnes prédictions',
            'Fiabilité des alertes émises',
            'Détection de toutes les inondations',
            'Équilibre precision/recall',
            'Capacité de discrimination',
            'Alertes inutiles',
            'Inondations manquées (critique)'
        ]
    }
    
    perf_df = pd.DataFrame(perf_data)
    st.dataframe(perf_df, use_container_width=True, hide_index=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 4: ANALYSE HISTORIQUE
# ═══════════════════════════════════════════════════════════════════════════════

with tab4:
    
    st.plotly_chart(create_flood_events_chart(df_hist), use_container_width=True)
    
    # Distribution des inondations par année
    st.markdown("""
    <div class="glass-panel">
        <div class="glass-panel-header">
            <div class="glass-panel-icon">📅</div>
            <div>
                <div class="glass-panel-title">Distribution des Inondations par Année</div>
                <div class="glass-panel-subtitle">Nombre de jours avec cote ≥ 7,9 m par année</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    yearly_floods = df_hist.groupby('Annee')['Inondation'].sum().reset_index()
    yearly_floods.columns = ['Année', 'Jours d\'inondation']
    
    fig_yearly = go.Figure()
    
    fig_yearly.add_trace(go.Bar(
        x=yearly_floods['Année'],
        y=yearly_floods['Jours d\'inondation'],
        marker=dict(
            color=yearly_floods['Jours d\'inondation'],
            colorscale='Reds',
            line=dict(color='rgba(255,255,255,0.3)', width=1)
        ),
        text=yearly_floods['Jours d\'inondation'],
        textposition='outside',
        textfont=dict(color='#ffffff', size=11)
    ))
    
    fig_yearly.update_layout(
        xaxis=dict(
            title='Année',
            tickmode='linear',
            tickfont=dict(color='#ffffff'),
            titlefont=dict(color='#ffffff'),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        yaxis=dict(
            title='Nombre de jours',
            tickfont=dict(color='#aab7b8'),
            titlefont=dict(color='#ffffff'),
            gridcolor='rgba(255,255,255,0.05)'
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=350,
        margin=dict(l=60, r=30, t=30, b=60)
    )
    
    st.plotly_chart(fig_yearly, use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Tableau des événements majeurs
    st.markdown("""
    <div class="glass-panel">
        <div class="glass-panel-header">
            <div class="glass-panel-icon">🌊</div>
            <div>
                <div class="glass-panel-title">Événements d'Inondation Majeurs</div>
                <div class="glass-panel-subtitle">Crues historiques avec cote maximale > 8,0 m</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    events_table = pd.DataFrame({
        'Période': ['Sept 2007', 'Oct 2010', 'Sept 2013', 'Sept 2018', 'Sept 2019', 'Sept 2021', 'Sept 2022', 'Oct 2023'],
        'Cote max (m)': [8.88, 8.55, 8.22, 8.45, 8.50, 8.52, 8.67, 8.43],
        'Durée (jours)': [25, 15, 11, 20, 6, 7, 20, 19],
        'Niveau': ['🔴 Critique', '🔴 Critique', '🟠 Alerte', '🔴 Critique', '🔴 Critique', '🔴 Critique', '🔴 Critique', '🔴 Critique']
    })
    
    st.dataframe(events_table, use_container_width=True, hide_index=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# TAB 5: DOCUMENTATION
# ═══════════════════════════════════════════════════════════════════════════════

with tab5:
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="glass-panel">
            <div class="glass-panel-header">
                <div class="glass-panel-icon">🎯</div>
                <div>
                    <div class="glass-panel-title">Objectif du Système</div>
                    <div class="glass-panel-subtitle">Finalité et portée du projet</div>
                </div>
            </div>
            <p style="color: #d5dbdb; line-height: 1.8;">
                Ce système d'alerte précoce vise à <strong style="color: #00d4ff;">prédire les inondations 
                du fleuve Mono à Athiémé</strong> avec 24 à 48 heures d'anticipation, permettant aux 
                autorités et populations de prendre les mesures préventives nécessaires.
            </p>
            <br>
            <p style="color: #d5dbdb; line-height: 1.8;">
                Le système utilise des algorithmes de <strong style="color: #00d9a5;">Machine Learning</strong> 
                entraînés sur 20 ans de données hydrométriques pour identifier les patterns précurseurs 
                d'inondations.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-panel">
            <div class="glass-panel-header">
                <div class="glass-panel-icon">📊</div>
                <div>
                    <div class="glass-panel-title">Données Utilisées</div>
                    <div class="glass-panel-subtitle">Sources et caractéristiques</div>
                </div>
            </div>
            <ul style="color: #d5dbdb; line-height: 2;">
                <li><strong>Source:</strong> Direction Générale de l'Eau (DGEau), Bénin</li>
                <li><strong>Période:</strong> 1er janvier 2005 au 16 septembre 2024</li>
                <li><strong>Observations:</strong> 7 199 jours de mesures continues</li>
                <li><strong>Variables:</strong> 19 features prédictives</li>
                <li><strong>Cible:</strong> Inondation (cote ≥ 7,9 m)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="glass-panel">
            <div class="glass-panel-header">
                <div class="glass-panel-icon">🤖</div>
                <div>
                    <div class="glass-panel-title">Méthodologie ML</div>
                    <div class="glass-panel-subtitle">Approche technique</div>
                </div>
            </div>
            <ul style="color: #d5dbdb; line-height: 2;">
                <li><strong>Algorithmes:</strong> Random Forest, Régression Logistique</li>
                <li><strong>Division:</strong> 80% entraînement / 20% test</li>
                <li><strong>Équilibrage:</strong> SMOTE pour classes déséquilibrées</li>
                <li><strong>Normalisation:</strong> StandardScaler</li>
                <li><strong>Optimisation:</strong> Grid Search avec CV 5-fold</li>
                <li><strong>Validation:</strong> Test sur événements historiques</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-panel">
            <div class="glass-panel-header">
                <div class="glass-panel-icon">👥</div>
                <div>
                    <div class="glass-panel-title">Équipe du Projet</div>
                    <div class="glass-panel-subtitle">Encadrement académique</div>
                </div>
            </div>
            <p style="color: #d5dbdb; line-height: 2;">
                <strong style="color: #00d4ff;">Auteur:</strong><br>
                BOSSOU Kossèni Affoladé Roméo<br><br>
                <strong style="color: #00d4ff;">Encadrement:</strong><br>
                Prof. VISSIN Expédit (Directeur)<br>
                Dr. Pierre OUASSA (Co-encadrant)<br><br>
                <strong style="color: #00d4ff;">Institution:</strong><br>
                Institut National de l'Eau (INE)<br>
                Université d'Abomey-Calavi, Bénin
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Partenaires
    st.markdown("""
    <div class="glass-panel">
        <div class="glass-panel-header">
            <div class="glass-panel-icon">🤝</div>
            <div>
                <div class="glass-panel-title">Partenaires Institutionnels</div>
                <div class="glass-panel-subtitle">Organismes impliqués dans la gestion du risque inondation</div>
            </div>
        </div>
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 2rem; margin-top: 1rem;">
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🏛️</div>
                <div style="color: #ffffff; font-weight: 600;">DGEau</div>
                <div style="color: #aab7b8; font-size: 0.85rem;">Direction Générale de l'Eau</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🚨</div>
                <div style="color: #ffffff; font-weight: 600;">ANPC</div>
                <div style="color: #aab7b8; font-size: 0.85rem;">Agence Nationale de Protection Civile</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🌤️</div>
                <div style="color: #ffffff; font-weight: 600;">Météo-Bénin</div>
                <div style="color: #aab7b8; font-size: 0.85rem;">Service Météorologique National</div>
            </div>
            <div style="text-align: center;">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎓</div>
                <div style="color: #ffffff; font-weight: 600;">INE/UAC</div>
                <div style="color: #aab7b8; font-size: 0.85rem;">Institut National de l'Eau</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════════════════════

st.markdown("""
<div class="footer-section">
    <div class="footer-logo">🌊 SAP Athiémé</div>
    <div class="footer-info">
        Système d'Alerte Précoce aux Inondations du Fleuve Mono<br>
        Mémoire de Licence Professionnelle • Filière GCREC<br>
        Institut National de l'Eau (INE) • Université d'Abomey-Calavi<br><br>
        <strong>Auteur:</strong> BOSSOU Kossèni Affoladé Roméo<br>
        <strong>Encadrement:</strong> Prof. VISSIN Expédit • Dr. Pierre OUASSA
    </div>
    <div class="footer-badge">
        <span>🎓</span>
        <span>Année académique 2024-2025</span>
    </div>
</div>
""", unsafe_allow_html=True)
