"""
Streamlit Configuration
=======================

Estilos y configuraciones compartidas para dashboards de Streamlit
en proyectos de análisis predictivo.

Uso:
    from streamlit_config import apply_standard_styles
    apply_standard_styles()
"""

import streamlit as st


def apply_standard_styles():
    """
    Aplica estilos CSS estándar para dashboards de análisis predictivo.
    
    Características:
    - Títulos compactos y profesionales
    - Espacios reducidos entre elementos
    - Tablas con fuente legible
    - Métricas compactas
    - Gráficos optimizados
    - Presentación científica y sobria
    """
    st.markdown("""
    <style>
        /* ============================================
           TÍTULOS Y ENCABEZADOS
           ============================================ */
        h1 {
            font-size: 1.8rem !important;
            margin-bottom: 0.5rem !important;
            margin-top: 0.8rem !important;
            font-weight: 600 !important;
        }
        h2 {
            font-size: 1.5rem !important;
            margin-bottom: 0.4rem !important;
            margin-top: 0.6rem !important;
            font-weight: 600 !important;
        }
        h3 {
            font-size: 1.3rem !important;
            margin-bottom: 0.4rem !important;
            margin-top: 0.6rem !important;
            font-weight: 600 !important;
        }
        h4 {
            font-size: 1.1rem !important;
            margin-bottom: 0.3rem !important;
            margin-top: 0.5rem !important;
            font-weight: 600 !important;
        }
        
        /* ============================================
           ESPACIADO GENERAL
           ============================================ */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        
        .element-container {
            margin-bottom: 0.5rem !important;
        }
        
        /* ============================================
           TABLAS Y DATAFRAMES
           ============================================ */
        .stDataFrame {
            font-size: 11px !important;
        }
        
        .stDataFrame table {
            width: 100% !important;
        }
        
        .stDataFrame th {
            background-color: #f0f2f6 !important;
            font-weight: 600 !important;
            padding: 8px !important;
        }
        
        .stDataFrame td {
            padding: 6px 8px !important;
        }
        
        /* ============================================
           MÉTRICAS (st.metric)
           ============================================ */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            font-weight: 600 !important;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
            font-weight: 500 !important;
            color: #31333F !important;
        }
        
        [data-testid="stMetricDelta"] {
            font-size: 0.85rem !important;
        }
        
        div[data-testid="metric-container"] {
            background-color: #f8f9fa !important;
            border: 1px solid #e0e0e0 !important;
            padding: 12px 16px !important;
            border-radius: 6px !important;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
        }
        
        /* ============================================
           COLUMNAS
           ============================================ */
        div[data-testid="column"] {
            padding: 0 8px !important;
        }
        
        /* ============================================
           BOTONES
           ============================================ */
        .stButton {
            margin-bottom: 0.5rem !important;
        }
        
        .stButton > button {
            width: 100% !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
            padding: 0.5rem 1rem !important;
        }
        
        .stButton > button[kind="primary"] {
            background-color: #0066cc !important;
            border-color: #0066cc !important;
        }
        
        .stButton > button[kind="primary"]:hover {
            background-color: #0052a3 !important;
            border-color: #0052a3 !important;
        }
        
        /* ============================================
           SELECTBOX Y CONTROLES
           ============================================ */
        .stSelectbox {
            margin-bottom: 0.8rem !important;
        }
        
        .stSelectbox label {
            font-weight: 500 !important;
            font-size: 0.95rem !important;
        }
        
        .stRadio {
            margin-bottom: 0.8rem !important;
        }
        
        .stCheckbox {
            margin-bottom: 0.5rem !important;
        }
        
        /* ============================================
           CAPTIONS Y TEXTOS PEQUEÑOS
           ============================================ */
        .stCaption {
            font-size: 0.85rem !important;
            margin-bottom: 0.3rem !important;
            color: #6c757d !important;
        }
        
        /* ============================================
           INFO BOXES (info, warning, success, error)
           ============================================ */
        .stAlert {
            padding: 0.75rem 1rem !important;
            margin-bottom: 0.8rem !important;
            border-radius: 6px !important;
            font-size: 0.9rem !important;
        }
        
        div[data-testid="stAlert"] {
            padding: 0.75rem 1rem !important;
        }
        
        /* ============================================
           SEPARADORES
           ============================================ */
        hr {
            margin-top: 0.8rem !important;
            margin-bottom: 0.8rem !important;
            border: none !important;
            border-top: 1px solid #e0e0e0 !important;
        }
        
        /* ============================================
           SIDEBAR
           ============================================ */
        section[data-testid="stSidebar"] {
            background-color: #f8f9fa !important;
        }
        
        section[data-testid="stSidebar"] > div {
            padding-top: 1.5rem !important;
        }
        
        section[data-testid="stSidebar"] .stSelectbox label {
            font-size: 0.9rem !important;
        }
        
        /* ============================================
           GRÁFICOS DE MATPLOTLIB
           ============================================ */
        .stPlotlyChart, .stPyplot {
            margin-bottom: 1rem !important;
        }
        
        /* Reducir espacio alrededor de gráficos */
        div[data-testid="stImage"] {
            margin-bottom: 0.5rem !important;
        }
        
        /* ============================================
           TABS
           ============================================ */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px !important;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 8px 16px !important;
            font-weight: 500 !important;
        }
        
        /* ============================================
           EXPANDERS
           ============================================ */
        .streamlit-expanderHeader {
            font-weight: 500 !important;
            font-size: 1rem !important;
        }
        
        /* ============================================
           SPINNERS Y LOADING
           ============================================ */
        .stSpinner > div {
            border-color: #0066cc !important;
        }
        
        /* ============================================
           AJUSTES RESPONSIVOS
           ============================================ */
        @media (max-width: 768px) {
            .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
            
            [data-testid="stMetricValue"] {
                font-size: 1.5rem !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)


def get_standard_colors():
    """
    Retorna los colores estándar para visualizaciones.
    
    Returns:
        dict: Diccionario con colores estándar
    """
    return {
        # Colores para variabilidad
        'average_mix': '#fff2cc',      # Amarillo
        'monthly_values': '#e8f4f8',   # Azul claro
        'positive_var': '#d4edda',     # Verde
        'positive_text': '#155724',    # Verde oscuro
        'negative_var': '#f8d7da',     # Rojo
        'negative_text': '#721c24',    # Rojo oscuro
        'neutral': '#f8f9fa',          # Gris
        'company': '#f8f9fa',          # Gris para compañía
        
        # Colores para gráficos
        'primary': '#0066cc',          # Azul principal
        'secondary': '#6c757d',        # Gris
        'success': '#28a745',          # Verde
        'danger': '#dc3545',           # Rojo
        'warning': '#ffc107',          # Amarillo
        'info': '#17a2b8',             # Cian
        
        # Colores para inflection points
        'peak': '#90EE90',             # Verde claro para picos
        'valley': '#FFB6C1',           # Rosa claro para valles
        'peak_dark': '#155724',        # Verde oscuro
        'valley_dark': '#721c24'       # Rojo oscuro
    }


def get_page_config():
    """
    Retorna la configuración estándar de página para Streamlit.
    
    Returns:
        dict: Diccionario con configuración de página
    """
    return {
        'layout': 'wide',
        'initial_sidebar_state': 'expanded',
        'page_icon': '📊'
    }
