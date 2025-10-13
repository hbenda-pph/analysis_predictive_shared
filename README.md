# Analysis Predictive Shared

## 📦 Módulo Compartido para Proyectos de Análisis Predictivo

Este repositorio contiene estilos, configuraciones y utilidades compartidas para todos los dashboards de Streamlit en proyectos de análisis predictivo.

## 🎯 Propósito

Centralizar estilos CSS y configuraciones para mantener consistencia visual y funcional entre todos los proyectos de análisis predictivo.

## 📁 Estructura

```
analysis_predictive_shared/
├── __init__.py              # Módulo principal
├── streamlit_config.py      # Estilos y configuraciones de Streamlit
└── README.md               # Este archivo
```

## 🚀 Uso

### En cualquier proyecto de Streamlit:

```python
import sys
import os

# Agregar shared al path
sys.path.append(os.path.join(os.path.dirname(__file__), '../analysis_predictive_shared'))

# Importar y aplicar estilos
from streamlit_config import apply_standard_styles

# Aplicar estilos estándar
apply_standard_styles()
```

### En Dockerfile:

```dockerfile
# Copiar módulo shared
COPY ../analysis_predictive_shared /app/analysis_predictive_shared

# Agregar al PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/app/analysis_predictive_shared"
```

## 📊 Funciones Disponibles

### `apply_standard_styles()`
Aplica estilos CSS estándar para dashboards:
- Títulos compactos y profesionales
- Espacios reducidos entre elementos
- Tabla con fuente legible
- Presentación científica y sobria

### `get_standard_colors()`
Retorna colores estándar para visualizaciones:
- Average Mix: Amarillo (#fff2cc)
- Monthly Values: Azul claro (#e8f4f8)
- Positive Variability: Verde (#d4edda)
- Negative Variability: Rojo (#f8d7da)

### `get_page_config()`
Retorna configuración estándar de página:
- Layout: wide
- Sidebar: expanded
- Icon: 📊

## 🔧 Proyectos que Usan Este Módulo

- `calls_historical_variability` - Análisis de variabilidad histórica
- `calls_analysis_dashboard` - Dashboard de análisis de llamadas
- `data_science_index` - Índice de ciencia de datos
- `data_science_admin` - Administración de ciencia de datos

## 📝 Mantenimiento

### Agregar Nuevo Estilo
1. Editar `streamlit_config.py`
2. Agregar función o modificar `apply_standard_styles()`
3. Commit y push
4. Todos los proyectos usan el nuevo estilo automáticamente

### Versionado
- **Versión actual**: 1.0.0
- **Cambios**: Documentados en commits de git

---

**Desarrollado por**: Platform Partners Team  
**Fecha**: Octubre 2025  
**Versión**: 1.0
