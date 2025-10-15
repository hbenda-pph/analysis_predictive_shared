"""
Streamlit Configuration
=======================

Estilos compartidos simples y mantenibles para todos los dashboards.

Uso:
    from streamlit_config import apply_standard_styles
    apply_standard_styles()
    
Convenciones:
    - h2: Título principal del dashboard
    - h3: Secciones principales
    - h4: Subsecciones
"""

import streamlit as st


def apply_standard_styles():
    """
    Aplica estilos CSS estándar simples para todos los dashboards.
    
    Convenciones unificadas:
    - Todos los dashboards usan h2 para el título principal
    - Todos los dashboards usan h3 para secciones
    - Todos los dashboards usan h4 para subsecciones
    """
    st.markdown("""
    <style>
        /* ============================================
           FUENTE IBM PLEX (Científica y profesional)
           Para revertir: Comentar esta sección completa
           ============================================ */
        @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap');
        
        /* Aplicar fuente a todo el dashboard */
        html, body, [class*="css"], * {
            font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
        }
        
        /* Fuente monoespaciada para números y datos */
        .stDataFrame, 
        [data-testid="stMetricValue"],
        .stDataFrame td,
        code {
            font-family: 'IBM Plex Mono', 'Consolas', monospace !important;
            font-variant-numeric: tabular-nums !important;
        }
        
        /* ============================================
           TÍTULOS - Convención unificada
           ============================================ */
        /* h2: TÍTULO PRINCIPAL del dashboard */
        h2 {
            font-size: 1.75rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.5rem !important;
            margin-top: 0.75rem !important;
            padding: 0.5rem 0px !important;
        }
        
        /* h3: SECCIONES principales */
        h3 {
            font-size: 1.3rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.4rem !important;
            margin-top: 0.6rem !important;
            padding: 0.4rem 0px !important;
        }
        
        /* h4: SUBSECCIONES */
        h4 {
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            margin-bottom: 0.3rem !important;
            margin-top: 0.5rem !important;
            padding: 0.3rem 0px !important;
        }
        
        /* ============================================
           ESPACIADO GENERAL Y FONDO
           ============================================ */
        /* Fondo gris suave tipo paper científico */
        .main {
            background-color: #fafafa !important;
        }
        
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            background-color: #fafafa !important;
        }
        
        .element-container {
            margin-bottom: 0.5rem !important;
        }
        
        /* ============================================
           TABLAS
           ============================================ */
        .stDataFrame {
            font-size: 11px !important;
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
           MÉTRICAS
           ============================================ */
        [data-testid="stMetricValue"] {
            font-size: 1.8rem !important;
            font-weight: 600 !important;
        }
        
        [data-testid="stMetricLabel"] {
            font-size: 0.9rem !important;
            font-weight: 500 !important;
        }
        
        div[data-testid="metric-container"] {
            background-color: #f8f9fa !important;
            border: 1px solid #e0e0e0 !important;
            padding: 12px 16px !important;
            border-radius: 6px !important;
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
        .stButton > button {
            width: 100% !important;
            border-radius: 6px !important;
            font-weight: 500 !important;
            padding: 0.5rem 1rem !important;
        }
        
        /* ============================================
           CONTROLES (selectbox, radio, etc.)
           ============================================ */
        .stSelectbox label,
        .stRadio label,
        .stCheckbox label {
            font-weight: 500 !important;
            font-size: 0.95rem !important;
        }
        
        /* ============================================
           INFO BOXES
           ============================================ */
        .stAlert {
            padding: 0.75rem 1rem !important;
            margin-bottom: 0.8rem !important;
            border-radius: 6px !important;
            font-size: 0.9rem !important;
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
    </style>
    """, unsafe_allow_html=True)


def get_standard_colors():
    """
    Colores estándar para visualizaciones.
    
    Returns:
        dict: Diccionario con colores estándar
    """
    return {
        # Colores básicos
        'primary': '#0066cc',
        'secondary': '#6c757d',
        'success': '#28a745',
        'danger': '#dc3545',
        'warning': '#ffc107',
        'info': '#17a2b8',
        
        # Para tablas de variabilidad
        'positive': '#d4edda',
        'negative': '#f8d7da',
        'neutral': '#f8f9fa',
        
        # Para inflection points
        'peak': '#90EE90',
        'valley': '#FFB6C1'
    }


def get_page_config():
    """
    Configuración estándar de página.
    
    Returns:
        dict: Configuración para st.set_page_config()
    """
    return {
        'layout': 'wide',
        'initial_sidebar_state': 'expanded',
        'page_icon': '📊'
    }
