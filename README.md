# Analysis Predictive Shared
## 📦 Módulo Compartido para Proyectos de Análisis Predictivo

Este repositorio contiene estilos, configuraciones y utilidades compartidas para todos los dashboards de Streamlit en proyectos de análisis predictivo.

---

## 🎯 Propósito

Centralizar estilos CSS y configuraciones para mantener consistencia visual y funcional entre todos los proyectos de análisis predictivo.

---

## 📁 Estructura

```
analysis_predictive_shared/
├── __init__.py              # Módulo principal
├── streamlit_config.py      # Estilos y configuraciones de Streamlit
└── README.md               # Este archivo
```

---

## 🚀 Uso

### En cualquier proyecto de Streamlit:

```python
import sys
import os

# Agregar shared al path (intenta ambas rutas para dev y producción)
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../analysis_predictive_shared'))
    from streamlit_config import apply_standard_styles
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'analysis_predictive_shared'))
    from streamlit_config import apply_standard_styles

# Aplicar estilos estándar
apply_standard_styles()
```

### En build_deploy.sh:

```bash
# Copiar módulo shared al directorio actual antes del build
if [ -d "../analysis_predictive_shared" ]; then
    echo "📂 Copiando analysis_predictive_shared..."
    cp -r ../analysis_predictive_shared ./analysis_predictive_shared
    echo "✅ Módulo shared copiado"
fi

# Build
gcloud builds submit --tag ${IMAGE_TAG}

# Limpiar después del build
if [ -d "./analysis_predictive_shared" ]; then
    echo "🧹 Limpiando archivos temporales..."
    rm -rf ./analysis_predictive_shared
    echo "✅ Limpieza completada"
fi
```

### En .gitignore:

```gitignore
# Módulo shared copiado temporalmente (se copia durante build)
analysis_predictive_shared/
```

---

## 📊 Funciones Disponibles

### `apply_standard_styles()`

Aplica estilos CSS completos para dashboards profesionales:

#### **Títulos y Encabezados**
- h1: 1.8rem, peso 600
- h2: 1.5rem, peso 600
- h3: 1.3rem, peso 600
- h4: 1.1rem, peso 600
- Márgenes reducidos para presentación compacta

#### **Espaciado General**
- Padding contenedor: 1.5rem arriba, 1rem abajo
- Padding lateral: 2rem
- Espacios entre elementos: 0.5rem

#### **Tablas y DataFrames**
- Fuente: 11px para mejor legibilidad
- Headers con background #f0f2f6
- Padding optimizado: 8px headers, 6px celdas
- Bordes sutiles y profesionales

#### **Métricas (st.metric)**
- Valores grandes: 1.8rem, peso 600
- Labels: 0.9rem, peso 500
- Deltas: 0.85rem
- Background: #f8f9fa con borde
- Box-shadow sutil para profundidad
- Bordes redondeados

#### **Columnas**
- Padding entre columnas: 8px
- Distribución uniforme

#### **Botones**
- Width: 100%
- Border-radius: 6px
- Padding: 0.5rem 1rem
- Primary: #0066cc con hover #0052a3
- Peso fuente: 500

#### **Selectbox y Controles**
- Labels con peso 500
- Fuente: 0.95rem
- Margin bottom: 0.8rem

#### **Info Boxes (st.info, st.warning, etc.)**
- Padding: 0.75rem 1rem
- Border-radius: 6px
- Fuente: 0.9rem
- Margin bottom: 0.8rem

#### **Separadores (hr)**
- Margin: 0.8rem arriba y abajo
- Border sutil: 1px #e0e0e0

#### **Sidebar**
- Background: #f8f9fa
- Padding top: 1.5rem
- Fuentes reducidas para compactar

#### **Gráficos de Matplotlib**
- Margin bottom: 1rem
- Optimizado para visualización

#### **Tabs**
- Gap entre tabs: 8px
- Padding: 8px 16px
- Peso fuente: 500

#### **Expanders**
- Headers con peso 500
- Fuente: 1rem

#### **Spinners**
- Color: #0066cc

#### **Responsivo**
- Media query para móviles (<768px)
- Padding lateral: 1rem
- Métricas: 1.5rem

---

### `get_standard_colors()`

Retorna colores estándar para visualizaciones:

#### **Colores para Variabilidad**
```python
'average_mix': '#fff2cc'      # Amarillo
'monthly_values': '#e8f4f8'   # Azul claro
'positive_var': '#d4edda'     # Verde
'positive_text': '#155724'    # Verde oscuro
'negative_var': '#f8d7da'     # Rojo
'negative_text': '#721c24'    # Rojo oscuro
'neutral': '#f8f9fa'          # Gris
'company': '#f8f9fa'          # Gris para compañía
```

#### **Colores para Gráficos**
```python
'primary': '#0066cc'          # Azul principal
'secondary': '#6c757d'        # Gris
'success': '#28a745'          # Verde
'danger': '#dc3545'           # Rojo
'warning': '#ffc107'          # Amarillo
'info': '#17a2b8'             # Cian
```

#### **Colores para Inflection Points**
```python
'peak': '#90EE90'             # Verde claro para picos
'valley': '#FFB6C1'           # Rosa claro para valles
'peak_dark': '#155724'        # Verde oscuro
'valley_dark': '#721c24'      # Rojo oscuro
```

---

### `get_page_config()`

Retorna configuración estándar de página:

```python
{
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
    'page_icon': '📊'
}
```

---

## 🔧 Proyectos que Usan Este Módulo

1. **calls_historical_variability** - Análisis de variabilidad histórica
   - Tablas multi-compañía
   - Exportación a Google Sheets
   - Visualización de tendencias

2. **calls_analysis_dashboard** - Análisis de puntos de inflexión
   - Gráficos de matplotlib
   - Detección de picos y valles
   - Análisis estacional

3. **data_science_index** - Índice de ciencia de datos
   - Métricas de proyectos
   - Estado de dashboards

4. **data_science_admin** - Administración de ciencia de datos
   - Panel de control
   - Gestión de recursos

---

## 🎨 Características de Diseño

### **Filosofía de Diseño**
- **Científico y Sobrio**: Sin adornos innecesarios
- **Compacto**: Maximiza el espacio para datos
- **Profesional**: Colores y tipografía consistentes
- **Legible**: Tamaños de fuente optimizados
- **Responsive**: Funciona en diferentes dispositivos

### **Tipografía**
- **Fuente principal**: Sistema (Helvetica, Arial, sans-serif)
- **Pesos**: 400 (normal), 500 (medium), 600 (semibold)
- **Jerarquía clara**: h1 > h2 > h3 > h4 > body

### **Espaciado**
- **Consistente**: rem-based para escalabilidad
- **Reducido**: Más información visible sin scroll
- **Balanceado**: No muy apretado, no muy espaciado

### **Colores**
- **Paleta limitada**: Colores con propósito
- **Contraste**: WCAG AA compliant
- **Semántica**: Verde=positivo, Rojo=negativo, Azul=neutral

---

## 📝 Mantenimiento

### Agregar Nuevo Estilo

1. **Editar** `streamlit_config.py`
2. **Agregar** función o modificar `apply_standard_styles()`
3. **Documentar** en este README
4. **Commit y push**
5. **Todos los proyectos** usan el nuevo estilo automáticamente en próximo deploy

### Versionado

- **Versión actual**: 2.0.0
- **Changelog**:
  - **2.0.0**: Estilos completos para gráficos, métricas, columnas, info boxes (Oct 2025)
  - **1.0.0**: Estilos básicos para tablas y títulos (Sep 2025)

### Testing

Después de modificar estilos, probar en:
1. Dashboard con tablas (historical_variability)
2. Dashboard con gráficos (calls_analysis)
3. Móvil (responsive)
4. Diferentes navegadores

---

## 🚀 Deploy

Los proyectos que usan este módulo lo copian temporalmente durante el build:

```bash
# Durante build_deploy.sh:
# 1. Copia ../analysis_predictive_shared → ./analysis_predictive_shared
# 2. Docker incluye el módulo en la imagen
# 3. Limpia ./analysis_predictive_shared después del build
```

Esto asegura que:
- ✅ El módulo está disponible en producción (Docker)
- ✅ No se commitea en cada proyecto (está en .gitignore)
- ✅ Todos los proyectos usan la misma versión centralizada

---

## 💡 Tips de Uso

### Para Dashboards con Tablas
```python
apply_standard_styles()
# Los estilos de tabla se aplican automáticamente
```

### Para Dashboards con Gráficos
```python
apply_standard_styles()
# Los estilos de métricas, columnas y gráficos se aplican automáticamente
```

### Para Dashboards Mixtos
```python
apply_standard_styles()
# Todos los estilos están disponibles
```

### Uso de Colores Estándar
```python
from streamlit_config import get_standard_colors

colors = get_standard_colors()
# Usar en matplotlib, plotly, etc.
plt.plot(x, y, color=colors['primary'])
```

---

## 📞 Soporte

- **Repositorio**: `platform_partners/analysis_predictive/analysis_predictive_shared/`
- **Contacto**: Platform Partners Team
- **Documentación**: Este README + comentarios en código

---

**Desarrollado por**: Platform Partners Team  
**Fecha**: Octubre 2025  
**Versión**: 2.0.0  
**Estado**: Producción
