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
    - Tabla con fuente legible
    - Presentación científica y sobria
    """
    st.markdown("""
    <style>
        /* Reducir tamaño de títulos */
        h1 {
            font-size: 1.8rem !important;
            margin-bottom: 0.5rem !important;
            margin-top: 0.8rem !important;
        }
        h2 {
            font-size: 1.5rem !important;
            margin-bottom: 0.4rem !important;
            margin-top: 0.6rem !important;
        }
        h3 {
            font-size: 1.3rem !important;
            margin-bottom: 0.4rem !important;
            margin-top: 0.6rem !important;
        }
        
        /* Reducir espacios en blanco */
        .block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1rem !important;
        }
        
        /* Reducir espacios entre elementos */
        .element-container {
            margin-bottom: 0.5rem !important;
        }
        
        /* Tabla más compacta */
        .stDataFrame {
            font-size: 11px;
        }
        
        /* Captions más pequeños */
        .stCaption {
            font-size: 11px;
            margin-bottom: 0.3rem !important;
        }
        
        /* Reducir espacios en sidebar */
        .css-1d391kg {
            padding-top: 1.5rem !important;
        }
        
        /* Reducir espacios en selectbox */
        .stSelectbox {
            margin-bottom: 0.8rem !important;
        }
        
        /* Reducir espacios en botones */
        .stButton {
            margin-bottom: 0.5rem !important;
        }
        
        /* Reducir separadores */
        hr {
            margin-top: 0.5rem !important;
            margin-bottom: 0.5rem !important;
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
        'average_mix': '#fff2cc',      # Amarillo
        'monthly_values': '#e8f4f8',   # Azul claro
        'positive_var': '#d4edda',     # Verde
        'positive_text': '#155724',    # Verde oscuro
        'negative_var': '#f8d7da',     # Rojo
        'negative_text': '#721c24',    # Rojo oscuro
        'neutral': '#f8f9fa',          # Gris
        'company': '#f8f9fa'           # Gris para compañía
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
