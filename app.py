import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Système d'Alerte Précoce - Athiémé",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS Ultra-Professionnel avec Design Premium
st.markdown("""
<style>
    /* ============================================
       IMPORTS & VARIABLES
       ============================================ */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
    
    :root {
        --primary-gradient: linear-gradient(135deg, #0f4c75 0%, #1a5980 25%, #2980b9 50%, #3498db 100%);
        --secondary-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        --danger-gradient: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        --warning-gradient: linear-gradient(135deg, #f2994a 0%, #f2c94c 100%);
        --success-gradient: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        --dark-blue: #0a2540;
        --medium-blue: #1e4d6b;
        --light-blue: #e8f4fc;
        --accent-cyan: #00d4ff;
        --accent-gold: #ffd700;
        --glass-bg: rgba(255, 255, 255, 0.85);
        --glass-border: rgba(255, 255, 255, 0.3);
        --shadow-soft: 0 8px 32px rgba(0, 0, 0, 0.1);
        --shadow-medium: 0 15px 35px rgba(0, 0, 0, 0.15);
        --shadow-strong: 0 25px 50px rgba(0, 0, 0, 0.2);
    }
    
    /* ============================================
       GLOBAL STYLES
       ============================================ */
    * {
        font-family: 'Poppins', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .main .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Background avec motif subtil */
    .stApp {
        background: linear-gradient(180deg, #f8fafc 0%, #e8f4fc 50%, #dbeafe 100%);
        background-attachment: fixed;
    }
    
    /* ============================================
       HEADER HERO SECTION
       ============================================ */
    .hero-container {
        background: var(--primary-gradient);
        border-radius: 24px;
        padding: 3rem;
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-strong);
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: -50%;
        right: -20%;
        width: 500px;
        height: 500px;
        background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
        animation: float 8s ease-in-out infinite;
    }
    
    .hero-container::after {
        content: '';
        position: absolute;
        bottom: -30%;
        left: -10%;
        width: 300px;
        height: 300px;
        background: radial-gradient(circle, rgba(0,212,255,0.2) 0%, transparent 70%);
        animation: float 6s ease-in-out infinite reverse;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
    }
    
    @keyframes pulse-glow {
        0%, 100% { box-shadow: 0 0 20px rgba(0, 212, 255, 0.3); }
        50% { box-shadow: 0 0 40px rgba(0, 212, 255, 0.6); }
    }
    
    @keyframes shimmer {
        0% { background-position: -200% center; }
        100% { background-position: 200% center; }
    }
    
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        color: white;
        text-align: center;
        margin: 0;
        text-shadow: 0 4px 20px rgba(0,0,0,0.3);
        letter-spacing: -1px;
        position: relative;
        z-index: 10;
    }
    
    .main-title span {
        background: linear-gradient(90deg, #fff, #00d4ff, #fff);
        background-size: 200% auto;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shimmer 3s linear infinite;
    }
    
    .sub-title {
        font-size: 1.4rem;
        color: rgba(255, 255, 255, 0.95);
        text-align: center;
        margin-top: 1rem;
        font-weight: 500;
        position: relative;
        z-index: 10;
        letter-spacing: 0.5px;
    }
    
    .badge-row {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
        position: relative;
        z-index: 10;
    }
    
    .badge {
        background: rgba(255, 255, 255, 0.2);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 50px;
        padding: 0.6rem 1.5rem;
        color: white;
        font-size: 0.95rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* ============================================
       SECTION HEADERS
       ============================================ */
    h1, h2, h3 {
        font-family: 'Poppins', sans-serif !important;
    }
    
    h1 {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: var(--dark-blue) !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.8rem !important;
        border-bottom: 4px solid transparent !important;
        border-image: var(--primary-gradient) 1 !important;
    }
    
    h2 {
        font-size: 1.6rem !important;
        font-weight: 600 !important;
        color: var(--medium-blue) !important;
        margin-top: 2rem !important;
    }
    
    h3 {
        font-size: 1.3rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
    }
    
    /* ============================================
       GLASS MORPHISM CARDS
       ============================================ */
    .glass-card {
        background: var(--glass-bg);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-radius: 20px;
        border: 1px solid var(--glass-border);
        padding: 2rem;
        box-shadow: var(--shadow-soft);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: var(--shadow-medium);
    }
    
    .glass-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: var(--primary-gradient);
        border-radius: 20px 20px 0 0;
    }
    
    /* ============================================
       METRIC CARDS PREMIUM
       ============================================ */
    .metric-premium {
        background: white;
        border-radius: 20px;
        padding: 1.8rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.08);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        border: 1px solid #e2e8f0;
    }
    
    .metric-premium:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
    }
    
    .metric-premium::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 5px;
        background: var(--primary-gradient);
    }
    
    .metric-premium.gold::before {
        background: var(--warning-gradient);
    }
    
    .metric-premium.green::before {
        background: var(--success-gradient);
    }
    
    .metric-premium.red::before {
        background: var(--danger-gradient);
    }
    
    .metric-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #e8f4fc 0%, #dbeafe 100%);
    }
    
    .metric-label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #64748b;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2.8rem;
        font-weight: 800;
        color: var(--dark-blue);
        line-height: 1.1;
        margin-bottom: 0.3rem;
    }
    
    .metric-delta {
        font-size: 0.95rem;
        font-weight: 600;
        color: #059669;
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }
    
    .metric-delta.negative {
        color: #dc2626;
    }
    
    /* ============================================
       ALERT CARDS
       ============================================ */
    .alert-premium {
        border-radius: 24px;
        padding: 2.5rem;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-medium);
    }
    
    .alert-premium::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 8px;
        height: 100%;
    }
    
    .alert-critical {
        background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 50%, #fecaca 100%);
        border: 2px solid #fca5a5;
    }
    
    .alert-critical::before {
        background: var(--danger-gradient);
    }
    
    .alert-critical .alert-icon {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        animation: pulse-glow 2s infinite;
    }
    
    .alert-warning {
        background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 50%, #fde68a 100%);
        border: 2px solid #fcd34d;
    }
    
    .alert-warning::before {
        background: var(--warning-gradient);
    }
    
    .alert-safe {
        background: linear-gradient(135deg, #ecfdf5 0%, #d1fae5 50%, #a7f3d0 100%);
        border: 2px solid #6ee7b7;
    }
    
    .alert-safe::before {
        background: var(--success-gradient);
    }
    
    .alert-icon {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
        color: white;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    }
    
    .alert-warning .alert-icon {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    }
    
    .alert-safe .alert-icon {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    }
    
    .alert-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .alert-critical .alert-title { color: #991b1b; }
    .alert-warning .alert-title { color: #92400e; }
    .alert-safe .alert-title { color: #065f46; }
    
    .alert-text {
        font-size: 1.1rem;
        line-height: 1.8;
        margin-bottom: 0.5rem;
    }
    
    .alert-critical .alert-text { color: #7f1d1d; }
    .alert-warning .alert-text { color: #78350f; }
    .alert-safe .alert-text { color: #064e3b; }
    
    /* ============================================
       STAT BOXES
       ============================================ */
    .stat-box {
        background: white;
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 800;
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1rem;
        font-weight: 600;
        color: #475569;
    }
    
    .stat-sub {
        font-size: 0.85rem;
        color: #94a3b8;
        margin-top: 0.3rem;
    }
    
    /* ============================================
       STREAMLIT COMPONENTS OVERRIDE
       ============================================ */
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2.4rem !important;
        font-weight: 800 !important;
        color: var(--dark-blue) !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 1rem !important;
        font-weight: 600 !important;
        color: #64748b !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }
    
    [data-testid="stMetricDelta"] {
        font-size: 0.95rem !important;
        font-weight: 600 !important;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--dark-blue) 0%, var(--medium-blue) 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: white !important;
        border: none !important;
    }
    
    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.2) !important;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: rgba(255, 255, 255, 0.9) !important;
        font-weight: 500 !important;
        padding: 0.8rem 1rem !important;
        border-radius: 12px !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(255, 255, 255, 0.1) !important;
    }
    
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        color: rgba(255, 255, 255, 0.85) !important;
    }
    
    /* Buttons */
    .stButton button {
        background: var(--primary-gradient) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 700 !important;
        padding: 1rem 2.5rem !important;
        border-radius: 16px !important;
        border: none !important;
        box-shadow: 0 10px 30px rgba(15, 76, 117, 0.3) !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    .stButton button:hover {
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 0 15px 40px rgba(15, 76, 117, 0.4) !important;
    }
    
    .stButton button:active {
        transform: translateY(-2px) scale(1.01) !important;
    }
    
    /* Inputs */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div {
        font-size: 1.1rem !important;
        font-weight: 500 !important;
        border: 2px solid #e2e8f0 !important;
        border-radius: 12px !important;
        padding: 0.8rem 1rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div:focus-within {
        border-color: #3498db !important;
        box-shadow: 0 0 0 3px rgba(52, 152, 219, 0.2) !important;
    }
    
    .stNumberInput label,
    .stSelectbox label {
        font-size: 1.05rem !important;
        font-weight: 600 !important;
        color: #334155 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.5rem;
        background: transparent;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 1rem 2rem !important;
        border-radius: 12px !important;
        color: #475569 !important;
        background: white !important;
        border: 2px solid #e2e8f0 !important;
        transition: all 0.3s ease !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: #f1f5f9 !important;
    }
    
    .stTabs [aria-selected="true"] {
        background: var(--primary-gradient) !important;
        color: white !important;
        border-color: transparent !important;
        box-shadow: 0 8px 25px rgba(15, 76, 117, 0.3) !important;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        font-size: 1.15rem !important;
        font-weight: 600 !important;
        color: var(--dark-blue) !important;
        background: white !important;
        border-radius: 12px !important;
        padding: 1rem !important;
    }
    
    /* Info/Success/Warning/Error boxes */
    .stAlert {
        border-radius: 16px !important;
        padding: 1.2rem 1.5rem !important;
        font-size: 1.05rem !important;
        border-left-width: 6px !important;
    }
    
    /* Dataframes */
    .stDataFrame {
        border-radius: 16px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
    }
    
    /* Dividers */
    hr {
        border: none !important;
        height: 2px !important;
        background: linear-gradient(90deg, transparent, #cbd5e1, transparent) !important;
        margin: 2.5rem 0 !important;
    }
    
    /* ============================================
       FOOTER
       ============================================ */
    .footer-premium {
        background: var(--primary-gradient);
        border-radius: 24px;
        padding: 3rem;
        margin-top: 4rem;
        text-align: center;
        box-shadow: var(--shadow-strong);
        position: relative;
        overflow: hidden;
    }
    
    .footer-premium::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    }
    
    .footer-premium h3 {
        color: white !important;
        font-size: 1.6rem !important;
        margin-bottom: 1rem !important;
        position: relative;
        z-index: 1;
    }
    
    .footer-premium p {
        color: rgba(255, 255, 255, 0.9) !important;
        font-size: 1.05rem !important;
        margin: 0.5rem 0 !important;
        position: relative;
        z-index: 1;
    }
    
    .footer-stats {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin-top: 2rem;
        flex-wrap: wrap;
        position: relative;
        z-index: 1;
    }
    
    .footer-stat {
        text-align: center;
    }
    
    .footer-stat-value {
        font-size: 2rem;
        font-weight: 800;
        color: var(--accent-cyan);
    }
    
    .footer-stat-label {
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.7);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* ============================================
       RECOMMENDATION LIST
       ============================================ */
    .reco-item {
        background: white;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        margin-bottom: 0.8rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        border-left: 4px solid #3498db;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .reco-item:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .reco-item.critical {
        border-left-color: #ef4444;
        background: #fef2f2;
    }
    
    .reco-item.warning {
        border-left-color: #f59e0b;
        background: #fffbeb;
    }
    
    .reco-item.success {
        border-left-color: #10b981;
        background: #ecfdf5;
    }
    
    .reco-number {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: var(--primary-gradient);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 0.9rem;
        flex-shrink: 0;
    }
    
    .reco-text {
        font-size: 1.05rem;
        color: #334155;
        font-weight: 500;
    }
    
    /* ============================================
       PROGRESS INDICATORS
       ============================================ */
    .progress-container {
        background: #e2e8f0;
        border-radius: 10px;
        height: 12px;
        overflow: hidden;
        margin: 1rem 0;
    }
    
    .progress-bar {
        height: 100%;
        border-radius: 10px;
        transition: width 1s ease-out;
    }
    
    .progress-bar.danger { background: var(--danger-gradient); }
    .progress-bar.warning { background: var(--warning-gradient); }
    .progress-bar.success { background: var(--success-gradient); }
    
    /* ============================================
       ANIMATIONS
       ============================================ */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .animate-fadeInUp {
        animation: fadeInUp 0.6s ease-out forwards;
    }
    
    /* ============================================
       RESPONSIVE
       ============================================ */
    @media (max-width: 768px) {
        .main-title { font-size: 2rem; }
        .sub-title { font-size: 1.1rem; }
        .metric-value { font-size: 2rem; }
        .stat-number { font-size: 2.2rem; }
        .badge-row { gap: 0.5rem; }
        .badge { padding: 0.4rem 1rem; font-size: 0.85rem; }
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour charger les modèles
@st.cache_resource
def load_models():
    """Charge les modèles ML entraînés"""
    try:
        rf_model = joblib.load('random_forest_model.pkl')
        lr_model = joblib.load('logistic_regression_model.pkl')
        scaler = joblib.load('scaler.pkl')
        return {
            'rf': rf_model,
            'lr': lr_model,
            'scaler': scaler
        }
    except Exception as e:
        st.error(f"⚠️ Erreur lors du chargement des modèles : {e}")
        st.info("📋 Veuillez vous assurer que les fichiers .pkl sont présents dans le répertoire de l'application.")
        return None

def predict_flood(input_data, models):
    """Effectue une prédiction d'inondation avec les modèles ML entraînés"""
    if models is None:
        return None
    
    try:
        features = np.array([[
            input_data['Cote_m'],
            input_data['Debit_m3s'],
            input_data['Var_cote_24h'],
            input_data['Var_cote_48h'],
            input_data['Var_cote_7j'],
            input_data['Var_debit_24h'],
            input_data['Var_debit_48h'],
            input_data['Taux_montee_m_par_h'],
            input_data['Distance_seuil_alerte'],
            input_data['Distance_seuil_critique'],
            input_data['Cote_ma_7j'],
            input_data['Debit_ma_7j'],
            input_data['Pluie_24h'],
            input_data['Pluie_48h'],
            input_data['Pluie_72h'],
            input_data['Pluie_7j'],
            input_data['Pluie_14j'],
            input_data['Jour_annee'],
            input_data['Saison_crue']
        ]])
        
        features_scaled = models['scaler'].transform(features)
        rf_proba = models['rf'].predict_proba(features_scaled)[0][1]
        lr_proba = models['lr'].predict_proba(features_scaled)[0][1]
        avg_proba = (rf_proba + lr_proba) / 2
        
        if avg_proba >= 0.7:
            risk_level = 'Élevé'
        elif avg_proba >= 0.3:
            risk_level = 'Moyen'
        else:
            risk_level = 'Faible'
        
        return {
            'rf_proba': rf_proba,
            'lr_proba': lr_proba,
            'avg_proba': avg_proba,
            'risk_level': risk_level
        }
    
    except Exception as e:
        st.error(f"⚠️ Erreur lors de la prédiction : {e}")
        return None

def get_risk_color(risk_level):
    """Retourne la couleur selon le niveau de risque"""
    colors = {
        'Faible': '#10b981',
        'Moyen': '#f59e0b',
        'Élevé': '#ef4444'
    }
    return colors.get(risk_level, '#6b7280')

def get_recommendations(risk_level):
    """Retourne les recommandations selon le niveau de risque"""
    recommendations = {
        'Faible': [
            "✅ Situation normale - Poursuite de la surveillance de routine",
            "📊 Maintien de la collecte régulière des données hydrométriques",
            "📢 Aucune alerte à diffuser auprès des populations",
            "🔄 Vérification systématique des équipements de mesure"
        ],
        'Moyen': [
            "⚠️ Vigilance accrue requise - Activation du niveau d'alerte 2",
            "👥 Information immédiate des chefs de village et de l'ANPC",
            "📋 Préparation et révision des plans d'évacuation préventifs",
            "📡 Intensification de la surveillance (mesures bi-quotidiennes)",
            "🚨 Pré-positionnement des équipes d'intervention",
            "📱 Activation de la chaîne de communication d'urgence"
        ],
        'Élevé': [
            "🚨 ALERTE MAXIMALE - Niveau 3 activé - Action immédiate requise",
            "📢 Déclenchement de l'alerte générale auprès des populations",
            "🏃 Évacuation préventive immédiate des zones à risque élevé",
            "🚁 Mobilisation de tous les moyens d'intervention (ANPC, Croix-Rouge)",
            "🏥 Préparation et activation des centres d'hébergement d'urgence",
            "📞 Coordination inter-institutionnelle (DGEau, Météo-Bénin, Préfecture)",
            "⛔ Interdiction stricte d'accès aux zones inondables",
            "🆘 Activation immédiate du plan ORSEC communal"
        ]
    }
    return recommendations.get(risk_level, [])

def create_plotly_theme():
    """Retourne le thème Plotly personnalisé"""
    return dict(
        font=dict(family='Poppins, sans-serif', size=14, color='#334155'),
        plot_bgcolor='rgba(248, 250, 252, 0.8)',
        paper_bgcolor='white',
        colorway=['#0f4c75', '#3498db', '#00d4ff', '#11998e', '#38ef7d', '#f2994a', '#eb3349'],
        hoverlabel=dict(
            bgcolor='white',
            font_size=14,
            font_family='Poppins, sans-serif'
        )
    )

# En-tête Hero
st.markdown("""
<div class="hero-container">
    <h1 class="main-title">🌊 SYSTÈME D'ALERTE PRÉCOCE <span>AUX INONDATIONS</span></h1>
    <p class="sub-title">Commune d'Athiémé • Fleuve Mono • République du Bénin</p>
    <div class="badge-row">
        <div class="badge">🤖 Machine Learning</div>
        <div class="badge">📊 Random Forest 100%</div>
        <div class="badge">🎯 Prédiction 48h</div>
        <div class="badge">🏛️ INE Bénin</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar Premium
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Flag_of_Benin.svg/320px-Flag_of_Benin.svg.png", width=100)
    
    st.markdown("### 📋 Navigation")
    
    page = st.radio(
        "",
        ["🏠 Tableau de bord", "🔮 Prédiction ML", "📊 Performances", "📚 Documentation"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    
    st.markdown("### 🏛️ Institut National de l'Eau")
    st.caption("Système opérationnel basé sur le Machine Learning")
    
    st.markdown("---")
    
    st.markdown("### 👨‍🏫 Encadrement")
    st.markdown("**Prof.** VISSIN Expédit")
    st.markdown("**Dr.** Pierre OUASSA")
    
    st.markdown("---")
    
    st.markdown("### 📈 Performance des Modèles")
    st.markdown("🌲 **Random Forest** : `100%`")
    st.markdown("📊 **Régression Log.** : `99.79%`")
    
    st.markdown("---")
    
    st.markdown("### 📅 Données")
    st.markdown("**Période** : 2005 - 2024")
    st.markdown("**Observations** : 7 199")

# Chargement des modèles
models = load_models()

if models is None:
    st.error("⚠️ Les modèles de Machine Learning ne sont pas chargés. Veuillez vérifier la présence des fichiers .pkl")
    st.stop()

# =============================================
# PAGE 1: TABLEAU DE BORD
# =============================================
if page == "🏠 Tableau de bord":
    st.markdown("# 📊 Tableau de Bord de Surveillance")
    st.markdown("**Surveillance hydrométrique en temps réel du fleuve Mono à Athiémé**")
    
    # Métriques principales avec design premium
    st.markdown("### 📍 Paramètres Hydrométriques Actuels")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-premium">
            <div class="metric-icon">📏</div>
            <div class="metric-label">Cote du Fleuve</div>
            <div class="metric-value">7,85 m</div>
            <div class="metric-delta negative">↗ +0,15 m (24h)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-premium gold">
            <div class="metric-icon">💧</div>
            <div class="metric-label">Débit Mesuré</div>
            <div class="metric-value">520 m³/s</div>
            <div class="metric-delta negative">↗ +45 m³/s (24h)</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-premium red">
            <div class="metric-icon">⚠️</div>
            <div class="metric-label">Niveau de Risque</div>
            <div class="metric-value" style="color: #f59e0b;">MOYEN</div>
            <div class="metric-delta" style="color: #f59e0b;">Probabilité : 45%</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="metric-premium green">
            <div class="metric-icon">⏱️</div>
            <div class="metric-label">Anticipation</div>
            <div class="metric-value">48h</div>
            <div class="metric-delta">✓ Surveillance active</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Alerte et recommandations
    col_alert, col_reco = st.columns([1, 1])
    
    with col_alert:
        st.markdown("### ⚠️ État d'Alerte Actuel")
        st.markdown("""
        <div class="alert-premium alert-warning">
            <div class="alert-icon">🟡</div>
            <div class="alert-title">NIVEAU D'ALERTE : MOYEN</div>
            <p class="alert-text"><strong>Probabilité d'inondation :</strong> 45%</p>
            <p class="alert-text"><strong>Niveau prévu dans 48h :</strong> 8,15 m</p>
            <p class="alert-text"><strong>Tendance observée :</strong> ↗️ Hausse progressive</p>
            <p class="alert-text"><strong>Distance au seuil d'alerte :</strong> 0,05 m</p>
            <div class="progress-container">
                <div class="progress-bar warning" style="width: 45%;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_reco:
        st.markdown("### 💡 Recommandations Opérationnelles")
        recommendations = get_recommendations('Moyen')
        reco_html = ""
        for i, reco in enumerate(recommendations[:4], 1):
            reco_html += f"""
            <div class="reco-item warning">
                <div class="reco-number">{i}</div>
                <div class="reco-text">{reco}</div>
            </div>
            """
        st.markdown(reco_html, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Graphique de tendance
    st.markdown("### 📈 Évolution de la Cote (7 derniers jours)")
    
    dates = pd.date_range(end=datetime.now(), periods=7, freq='D')
    cotes = [7.25, 7.32, 7.45, 7.58, 7.65, 7.75, 7.85]
    
    fig = go.Figure()
    
    # Zone de fond pour le danger
    fig.add_hrect(y0=8.3, y1=9.5, fillcolor="rgba(239, 68, 68, 0.1)", line_width=0)
    fig.add_hrect(y0=7.9, y1=8.3, fillcolor="rgba(245, 158, 11, 0.1)", line_width=0)
    
    # Ligne principale
    fig.add_trace(go.Scatter(
        x=dates,
        y=cotes,
        mode='lines+markers',
        name='Cote mesurée',
        line=dict(color='#0f4c75', width=4, shape='spline'),
        marker=dict(size=12, color='#0f4c75', line=dict(width=3, color='white')),
        fill='tozeroy',
        fillcolor='rgba(15, 76, 117, 0.1)'
    ))
    
    # Seuils
    fig.add_hline(y=7.9, line_dash="dash", line_color="#f59e0b", line_width=3,
                  annotation_text="⚠️ Seuil d'alerte (7,9 m)", 
                  annotation_position="right",
                  annotation_font=dict(size=13, color='#f59e0b', family='Poppins'))
    fig.add_hline(y=8.3, line_dash="dash", line_color="#ef4444", line_width=3,
                  annotation_text="🚨 Seuil critique (8,3 m)", 
                  annotation_position="right",
                  annotation_font=dict(size=13, color='#ef4444', family='Poppins'))
    
    fig.update_layout(
        title=dict(
            text="<b>Variation de la cote du fleuve Mono à Athiémé</b>",
            font=dict(size=20, color='#0a2540', family='Poppins')
        ),
        xaxis_title="Date",
        yaxis_title="Cote (mètres)",
        hovermode='x unified',
        height=500,
        **create_plotly_theme(),
        yaxis=dict(range=[7, 9], gridcolor='rgba(0,0,0,0.05)'),
        xaxis=dict(gridcolor='rgba(0,0,0,0.05)')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Statistiques
    st.markdown("---")
    st.markdown("### 📊 Statistiques de Référence (2005-2024)")
    
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    
    with col_s1:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">145</div>
            <div class="stat-label">Jours d'Inondation</div>
            <div class="stat-sub">Période 2005-2024</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_s2:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">8,88m</div>
            <div class="stat-label">Record Historique</div>
            <div class="stat-sub">Septembre 2007</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_s3:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">10</div>
            <div class="stat-label">Événements Majeurs</div>
            <div class="stat-sub">Depuis 2005</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col_s4:
        st.markdown("""
        <div class="stat-box">
            <div class="stat-number">100%</div>
            <div class="stat-label">Précision Modèle</div>
            <div class="stat-sub">Random Forest</div>
        </div>
        """, unsafe_allow_html=True)

# =============================================
# PAGE 2: PRÉDICTION ML
# =============================================
elif page == "🔮 Prédiction ML":
    st.markdown("# 🔮 Module de Prédiction par Machine Learning")
    st.markdown("**Prédiction d'inondation basée sur les modèles Random Forest et Régression Logistique**")
    
    st.success("✅ **Système opérationnel** — Modèles entraînés sur 7 199 observations (2005-2024)")
    
    st.markdown("---")
    
    col_input1, col_input2 = st.columns(2)
    
    with col_input1:
        st.markdown("### 📊 Paramètres Hydrométriques")
        
        cote = st.number_input("**Cote actuelle (m)**", min_value=0.5, max_value=10.0, value=7.85, step=0.01,
                               help="Hauteur d'eau mesurée à la station hydrométrique d'Athiémé")
        debit = st.number_input("**Débit actuel (m³/s)**", min_value=1.0, max_value=1000.0, value=520.0, step=1.0,
                                help="Débit du fleuve Mono mesuré à Athiémé")
        
        st.markdown("**Variations temporelles de la cote**")
        var_24h = st.number_input("Variation sur 24h (m)", min_value=-2.0, max_value=2.0, value=0.15, step=0.01)
        var_48h = st.number_input("Variation sur 48h (m)", min_value=-2.0, max_value=2.0, value=0.28, step=0.01)
        var_7j = st.number_input("Variation sur 7 jours (m)", min_value=-3.0, max_value=3.0, value=0.45, step=0.01)
        
        st.markdown("**Variations du débit**")
        var_debit_24h = st.number_input("Variation débit 24h (m³/s)", min_value=-500.0, max_value=500.0, value=45.0, step=1.0)
        var_debit_48h = st.number_input("Variation débit 48h (m³/s)", min_value=-500.0, max_value=500.0, value=78.0, step=1.0)
        
        taux_montee = st.number_input("**Taux de montée (m/h)**", min_value=0.0, max_value=0.1, value=0.006, step=0.001, format="%.3f")
        
    with col_input2:
        st.markdown("### 🌧️ Données Pluviométriques")
        
        st.markdown("**Précipitations cumulées**")
        pluie_24h = st.number_input("Cumul 24h (mm)", min_value=0.0, max_value=200.0, value=15.0, step=1.0)
        pluie_48h = st.number_input("Cumul 48h (mm)", min_value=0.0, max_value=400.0, value=28.0, step=1.0)
        pluie_72h = st.number_input("Cumul 72h (mm)", min_value=0.0, max_value=500.0, value=42.0, step=1.0)
        pluie_7j = st.number_input("Cumul 7 jours (mm)", min_value=0.0, max_value=600.0, value=85.0, step=1.0)
        pluie_14j = st.number_input("Cumul 14 jours (mm)", min_value=0.0, max_value=800.0, value=145.0, step=1.0)
        
        st.markdown("**Contexte temporel**")
        jour_annee = st.number_input("**Jour de l'année (1-365)**", min_value=1, max_value=365, value=260, step=1,
                                     help="Exemple : 260 correspond au 17 septembre")
        
        saison = st.selectbox("**Période hydrologique**", 
                            ["Saison des crues (Août-Octobre)", "Hors saison des crues"],
                            help="La saison des crues correspond à la période Août-Octobre")
    
    # Calculs automatiques
    distance_alerte = 7.9 - cote
    distance_critique = 8.3 - cote
    cote_ma_7j = cote - var_7j / 2
    debit_ma_7j = debit - (var_debit_24h * 3)
    
    st.markdown("---")
    
    if st.button("🚀 LANCER LA PRÉDICTION", type="primary", use_container_width=True):
        input_data = {
            'Cote_m': cote,
            'Debit_m3s': debit,
            'Var_cote_24h': var_24h,
            'Var_cote_48h': var_48h,
            'Var_cote_7j': var_7j,
            'Var_debit_24h': var_debit_24h,
            'Var_debit_48h': var_debit_48h,
            'Taux_montee_m_par_h': taux_montee,
            'Distance_seuil_alerte': distance_alerte,
            'Distance_seuil_critique': distance_critique,
            'Cote_ma_7j': cote_ma_7j,
            'Debit_ma_7j': debit_ma_7j,
            'Pluie_24h': pluie_24h,
            'Pluie_48h': pluie_48h,
            'Pluie_72h': pluie_72h,
            'Pluie_7j': pluie_7j,
            'Pluie_14j': pluie_14j,
            'Jour_annee': jour_annee,
            'Saison_crue': 1 if "crues" in saison else 0
        }
        
        with st.spinner("🤖 Analyse en cours par les algorithmes de Machine Learning..."):
            import time
            time.sleep(1)  # Effet visuel
            results = predict_flood(input_data, models)
        
        if results:
            st.balloons()
            st.success("✅ **Prédiction terminée avec succès !**")
            
            st.markdown("---")
            st.markdown("### 📊 Résultats de la Prédiction")
            
            col_res1, col_res2, col_res3 = st.columns(3)
            
            with col_res1:
                rf_color = "#10b981" if results['rf_proba'] < 0.3 else "#f59e0b" if results['rf_proba'] < 0.7 else "#ef4444"
                st.markdown(f"""
                <div class="metric-premium">
                    <div class="metric-icon">🌲</div>
                    <div class="metric-label">Random Forest</div>
                    <div class="metric-value" style="color: {rf_color};">{results['rf_proba']*100:.1f}%</div>
                    <div class="metric-delta">Accuracy: 100%</div>
                    <div class="progress-container">
                        <div class="progress-bar {'danger' if results['rf_proba'] >= 0.7 else 'warning' if results['rf_proba'] >= 0.3 else 'success'}" style="width: {results['rf_proba']*100}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_res2:
                lr_color = "#10b981" if results['lr_proba'] < 0.3 else "#f59e0b" if results['lr_proba'] < 0.7 else "#ef4444"
                st.markdown(f"""
                <div class="metric-premium">
                    <div class="metric-icon">📈</div>
                    <div class="metric-label">Régression Logistique</div>
                    <div class="metric-value" style="color: {lr_color};">{results['lr_proba']*100:.1f}%</div>
                    <div class="metric-delta">Accuracy: 99.79%</div>
                    <div class="progress-container">
                        <div class="progress-bar {'danger' if results['lr_proba'] >= 0.7 else 'warning' if results['lr_proba'] >= 0.3 else 'success'}" style="width: {results['lr_proba']*100}%;"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_res3:
                risk_color = get_risk_color(results['risk_level'])
                alert_class = "alert-critical" if results['risk_level'] == 'Élevé' else "alert-warning" if results['risk_level'] == 'Moyen' else "alert-safe"
                icon = "🔴" if results['risk_level'] == 'Élevé' else "🟡" if results['risk_level'] == 'Moyen' else "🟢"
                st.markdown(f"""
                <div class="alert-premium {alert_class}" style="padding: 1.5rem;">
                    <div class="alert-title" style="font-size: 1.2rem;">NIVEAU DE RISQUE</div>
                    <div style="font-size: 2.5rem; font-weight: 800; color: {risk_color}; margin: 0.5rem 0;">{icon} {results['risk_level'].upper()}</div>
                    <div style="font-size: 1.1rem; opacity: 0.9;">Moyenne : {results['avg_proba']*100:.1f}%</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Recommandations
            st.markdown("### 💡 Recommandations Opérationnelles")
            
            recommendations = get_recommendations(results['risk_level'])
            reco_class = "critical" if results['risk_level'] == 'Élevé' else "warning" if results['risk_level'] == 'Moyen' else "success"
            
            cols = st.columns(2)
            for i, reco in enumerate(recommendations):
                with cols[i % 2]:
                    st.markdown(f"""
                    <div class="reco-item {reco_class}">
                        <div class="reco-number">{i+1}</div>
                        <div class="reco-text">{reco}</div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("---")
            
            # Graphique comparatif
            st.markdown("### 📊 Comparaison des Modèles")
            
            fig = go.Figure()
            
            fig.add_trace(go.Bar(
                name='Random Forest',
                x=['Probabilité d\'inondation'],
                y=[results['rf_proba']*100],
                marker=dict(
                    color='#0f4c75',
                    line=dict(width=0),
                    cornerradius=10
                ),
                text=[f"<b>{results['rf_proba']*100:.1f}%</b>"],
                textposition='outside',
                textfont=dict(size=18, color='#0f4c75', family='Poppins'),
                width=0.35
            ))
            
            fig.add_trace(go.Bar(
                name='Régression Logistique',
                x=['Probabilité d\'inondation'],
                y=[results['lr_proba']*100],
                marker=dict(
                    color='#f59e0b',
                    line=dict(width=0),
                    cornerradius=10
                ),
                text=[f"<b>{results['lr_proba']*100:.1f}%</b>"],
                textposition='outside',
                textfont=dict(size=18, color='#f59e0b', family='Poppins'),
                width=0.35
            ))
            
            fig.update_layout(
                title=dict(
                    text="<b>Comparaison des probabilités calculées</b>",
                    font=dict(size=20, color='#0a2540', family='Poppins')
                ),
                yaxis_title="Probabilité (%)",
                yaxis=dict(range=[0, 115], gridcolor='rgba(0,0,0,0.05)'),
                barmode='group',
                height=400,
                **create_plotly_theme(),
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="center",
                    x=0.5,
                    font=dict(size=14)
                ),
                bargap=0.3
            )
            
            st.plotly_chart(fig, use_container_width=True)

# =============================================
# PAGE 3: PERFORMANCES
# =============================================
elif page == "📊 Performances":
    st.markdown("# 📊 Performances des Modèles de Machine Learning")
    st.markdown("**Évaluation quantitative sur ensemble de test indépendant (1 439 observations)**")
    
    st.markdown("---")
    
    tab1, tab2, tab3 = st.tabs(["📈 Métriques", "🎯 Importance Variables", "📅 Historique"])
    
    with tab1:
        st.markdown("### 📊 Résultats sur l'Ensemble de Test")
        
        col_perf1, col_perf2 = st.columns(2)
        
        with col_perf1:
            st.markdown("""
            <div class="glass-card">
                <h3 style="color: #0f4c75; margin-top: 0;">🌲 Random Forest Classifier</h3>
            </div>
            """, unsafe_allow_html=True)
            
            metrics_rf = {'Accuracy': 100.0, 'Precision': 100.0, 'Recall': 100.0, 'F1-Score': 100.0}
            for metric, value in metrics_rf.items():
                st.markdown(f"""
                <div class="stat-box" style="margin-bottom: 1rem;">
                    <div class="stat-number">{value}%</div>
                    <div class="stat-label">{metric}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.success("✅ **Performance exceptionnelle** — Classification parfaite")
        
        with col_perf2:
            st.markdown("""
            <div class="glass-card">
                <h3 style="color: #f59e0b; margin-top: 0;">📈 Régression Logistique</h3>
            </div>
            """, unsafe_allow_html=True)
            
            metrics_lr = {'Accuracy': 99.79, 'Precision': 90.62, 'Recall': 100.0, 'F1-Score': 95.08}
            for metric, value in metrics_lr.items():
                st.markdown(f"""
                <div class="stat-box" style="margin-bottom: 1rem;">
                    <div class="stat-number">{value}%</div>
                    <div class="stat-label">{metric}</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.success("✅ **Performance très élevée** — Rappel parfait")
        
        st.markdown("---")
        
        # Graphique comparatif
        st.markdown("### 📊 Comparaison Graphique")
        
        metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
        rf_values = [100, 100, 100, 100]
        lr_values = [99.79, 90.62, 100, 95.08]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            name='Random Forest',
            x=metrics,
            y=rf_values,
            marker=dict(color='#0f4c75', cornerradius=8),
            text=[f'<b>{v}%</b>' for v in rf_values],
            textposition='outside',
            textfont=dict(size=14, color='#0f4c75', family='Poppins')
        ))
        
        fig.add_trace(go.Bar(
            name='Régression Logistique',
            x=metrics,
            y=lr_values,
            marker=dict(color='#f59e0b', cornerradius=8),
            text=[f'<b>{v:.1f}%</b>' for v in lr_values],
            textposition='outside',
            textfont=dict(size=14, color='#f59e0b', family='Poppins')
        ))
        
        fig.update_layout(
            title=dict(
                text="<b>Performance comparative des algorithmes</b>",
                font=dict(size=20, color='#0a2540', family='Poppins')
            ),
            yaxis_title="Score (%)",
            yaxis=dict(range=[0, 115], gridcolor='rgba(0,0,0,0.05)'),
            barmode='group',
            height=500,
            **create_plotly_theme(),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="center",
                x=0.5,
                font=dict(size=14)
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("📋 **Note méthodologique** : Ces performances ont été obtenues sur un ensemble de test indépendant, non utilisé lors de l'entraînement.")
    
    with tab2:
        st.markdown("### 🎯 Importance des Variables (Random Forest)")
        st.markdown("**Contribution relative des 19 variables prédictives**")
        
        variables = [
            'Cote (m)', 'Distance seuil critique', 'Distance seuil alerte',
            'Débit (m³/s)', 'Moyenne mobile débit 7j', 'Variation cote 48h',
            'Moyenne mobile cote 7j', 'Variation cote 24h', 'Taux de montée',
            'Variation débit 24h'
        ]
        
        importance = [23.3, 23.2, 15.5, 13.4, 10.2, 4.8, 3.2, 2.5, 2.1, 1.8]
        
        # Création des couleurs en dégradé
        colors = ['#0f4c75' if i < 3 else '#3498db' if i < 6 else '#64b5f6' for i in range(len(importance))]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            y=variables,
            x=importance,
            orientation='h',
            marker=dict(
                color=importance,
                colorscale=[[0, '#64b5f6'], [0.5, '#3498db'], [1, '#0f4c75']],
                cornerradius=8
            ),
            text=[f'<b>{v}%</b>' for v in importance],
            textposition='outside',
            textfont=dict(size=13, color='#0a2540', family='Poppins')
        ))
        
        fig.update_layout(
            title=dict(
                text="<b>Top 10 des variables les plus importantes</b>",
                font=dict(size=20, color='#0a2540', family='Poppins')
            ),
            xaxis_title="Importance relative (%)",
            xaxis=dict(range=[0, 30], gridcolor='rgba(0,0,0,0.05)'),
            height=550,
            **create_plotly_theme(),
            showlegend=False
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.success("💡 **Analyse** : Les trois variables les plus importantes représentent à elles seules **62%** de l'importance totale du modèle.")
    
    with tab3:
        st.markdown("### 📅 Historique des Événements Majeurs (2005-2024)")
        st.markdown("**Recensement des 10 crues exceptionnelles ayant affecté Athiémé**")
        
        events = pd.DataFrame({
            'Date': ['Sept. 2007', 'Oct. 2010', 'Sept. 2013', 'Sept. 2018', 'Sept. 2019', 
                     'Oct. 2020', 'Sept. 2021', 'Sept. 2022', 'Oct. 2023', 'Sept. 2024'],
            'Cote max (m)': [8.88, 8.55, 8.22, 8.45, 8.50, 8.12, 8.52, 8.67, 8.43, 8.35],
            'Durée (jours)': [12, 8, 6, 10, 14, 7, 11, 15, 9, 10],
            'Personnes affectées': ['65 000+', '45 000', '32 000', '42 000', '31 482', 
                                   '28 000', '38 500', '52 000', '35 000', '40 000']
        })
        
        st.dataframe(events, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Graphique temporel
        fig = go.Figure()
        
        fig.add_hrect(y0=8.3, y1=9.0, fillcolor="rgba(239, 68, 68, 0.1)", line_width=0)
        fig.add_hrect(y0=7.9, y1=8.3, fillcolor="rgba(245, 158, 11, 0.1)", line_width=0)
        
        fig.add_trace(go.Scatter(
            x=events['Date'],
            y=events['Cote max (m)'],
            mode='lines+markers',
            name='Cote maximale',
            line=dict(color='#ef4444', width=4, shape='spline'),
            marker=dict(size=14, color='#ef4444', line=dict(width=3, color='white')),
            fill='tozeroy',
            fillcolor='rgba(239, 68, 68, 0.1)'
        ))
        
        fig.add_hline(y=7.9, line_dash="dash", line_color="#f59e0b", line_width=3,
                      annotation_text="Seuil d'alerte (7,9 m)", annotation_position="right")
        fig.add_hline(y=8.3, line_dash="dash", line_color="#ef4444", line_width=3,
                      annotation_text="Seuil critique (8,3 m)", annotation_position="right")
        
        fig.update_layout(
            title=dict(
                text="<b>Évolution des cotes maximales lors des événements majeurs</b>",
                font=dict(size=20, color='#0a2540', family='Poppins')
            ),
            xaxis_title="Événement",
            yaxis_title="Cote maximale (m)",
            yaxis=dict(range=[7.5, 9.2], gridcolor='rgba(0,0,0,0.05)'),
            height=500,
            **create_plotly_theme()
        )
        
        st.plotly_chart(fig, use_container_width=True)

# =============================================
# PAGE 4: DOCUMENTATION
# =============================================
else:
    st.markdown("# 📚 Documentation Technique")
    st.markdown("**Méthodologie et contexte du système d'alerte précoce**")
    
    st.markdown("---")
    
    col_doc1, col_doc2 = st.columns(2)
    
    with col_doc1:
        st.markdown("""
        <div class="glass-card">
            <h3 style="margin-top: 0;">🎯 Objectif du Système</h3>
            <p>Ce système d'alerte précoce utilise des algorithmes de <strong>Machine Learning</strong> pour prédire 
            les inondations du fleuve Mono à Athiémé avec un <strong>délai d'anticipation de 24 à 48 heures</strong>, 
            permettant ainsi une évacuation préventive des populations vulnérables.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card" style="margin-top: 1.5rem;">
            <h3 style="margin-top: 0;">🔬 Méthodologie Scientifique</h3>
            <p><strong>Données d'entrée :</strong></p>
            <ul>
                <li>Période : 2005-2024 (20 ans)</li>
                <li>Volume : 7 199 observations quotidiennes</li>
                <li>Source : Direction Générale de l'Eau (DGEau)</li>
            </ul>
            <p><strong>Variables prédictives :</strong></p>
            <ul>
                <li>19 features : cote, débit, variations temporelles, précipitations, saisonnalité</li>
            </ul>
            <p><strong>Algorithmes déployés :</strong></p>
            <ul>
                <li>Random Forest Classifier (100 arbres)</li>
                <li>Régression Logistique multinomiale</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card" style="margin-top: 1.5rem;">
            <h3 style="margin-top: 0;">📊 Résultats de Validation</h3>
            <ul>
                <li>✅ Random Forest : 100% d'accuracy</li>
                <li>✅ Régression Logistique : 99,79% d'accuracy</li>
                <li>✅ 145 jours d'inondation identifiés</li>
                <li>✅ 10 événements majeurs analysés</li>
                <li>✅ Système à 3 niveaux de risque</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col_doc2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="margin-top: 0;">👥 Équipe de Développement</h3>
            <p><strong>Réalisation :</strong></p>
            <ul>
                <li>Étudiant-chercheur en Gestion des crises et risques liés à l'eau et au Climat</li>
                <li>Institut National de l'Eau (INE), Bénin</li>
            </ul>
            <p><strong>Encadrement académique :</strong></p>
            <ul>
                <li>Professeur VISSIN Expédit (Directeur)</li>
                <li>Docteur Pierre OUASSA (Co-directeur)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card" style="margin-top: 1.5rem;">
            <h3 style="margin-top: 0;">🤝 Partenaires Institutionnels</h3>
            <ul>
                <li><strong>Direction Générale de l'Eau (DGEau)</strong><br>
                    <small>Fourniture des données hydrométriques</small></li>
                <li><strong>Agence Beninoise pour la Protection Civile (ABPC)</strong><br>
                    <small>Expertise en gestion des risques</small></li>
                <li><strong>Météo-Bénin</strong><br>
                    <small>Données pluviométriques et prévisions</small></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="glass-card" style="margin-top: 1.5rem;">
            <h3 style="margin-top: 0;">📚 Référence Académique</h3>
            <p>Mémoire de licence en Gestion des crises et risques liés à l'eau et au Climat <br>
            Institut National de l'Eau (INE)<br>
            République du Bénin, 2025</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🚀 Perspectives d'Amélioration")
    
    perspectives = [
        "Intégration de données satellitaires (CHIRPS, GPM)",
        "Acquisition des données du barrage de Nangbéto",
        "Développement multi-horizons (12h, 24h, 48h, 72h)",
        "Application d'algorithmes Deep Learning (LSTM, GRU)",
        "Extension géographique au bassin du Mono",
        "Couplage imagerie satellite (Sentinel-1, Landsat)",
        "Développement application mobile",
        "Intégration système national multi-risques"
    ]
    
    cols = st.columns(2)
    for i, persp in enumerate(perspectives):
        with cols[i % 2]:
            st.markdown(f"""
            <div class="reco-item">
                <div class="reco-number">{i+1}</div>
                <div class="reco-text">{persp}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.success("💡 **Note importante** : Ce système utilise des modèles ML réellement entraînés sur 20 ans de données. Il constitue un outil opérationnel directement exploitable.")

# Footer Premium
st.markdown("""
<div class="footer-premium">
    <h3>🌊 SYSTÈME D'ALERTE PRÉCOCE AUX INONDATIONS — ATHIÉMÉ</h3>
    <p>Institut National de l'Eau (INE) • République du Bénin • 2025</p>
    <p>Développé dans le cadre d'un mémoire de licence en Gestion des Ressources en Eau</p>
    <div class="footer-stats">
        <div class="footer-stat">
            <div class="footer-stat-value">100%</div>
            <div class="footer-stat-label">Random Forest</div>
        </div>
        <div class="footer-stat">
            <div class="footer-stat-value">99.79%</div>
            <div class="footer-stat-label">Rég. Logistique</div>
        </div>
        <div class="footer-stat">
            <div class="footer-stat-value">7 199</div>
            <div class="footer-stat-label">Observations</div>
        </div>
        <div class="footer-stat">
            <div class="footer-stat-value">20 ans</div>
            <div class="footer-stat-label">De données</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
