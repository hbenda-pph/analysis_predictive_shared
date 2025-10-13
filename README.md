# Analysis Predictive Shared
## 📦 Módulo Simple y Compartido

Estilos CSS simples y convenciones unificadas para todos los dashboards de análisis predictivo.

---

## 🎯 Filosofía: Simple y Unificado

**Un solo estilo por elemento. Todos los proyectos usan lo mismo.**

- ✅ **h2**: Título principal del dashboard (1.75rem)
- ✅ **h3**: Secciones principales (1.3rem)
- ✅ **h4**: Subsecciones (1.1rem)
- ✅ Estilos básicos para tablas, métricas, botones

**NO hay variantes.** Todos los dashboards siguen las mismas convenciones.

---

## 🚀 Uso

### En cualquier dashboard:

```python
import sys
import os

# Agregar shared al path
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '../analysis_predictive_shared'))
    from streamlit_config import apply_standard_styles
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'analysis_predictive_shared'))
    from streamlit_config import apply_standard_styles

# Configuración de página
st.set_page_config(
    page_title="Mi Dashboard",
    page_icon="📊",
    layout="wide"
)

# APLICAR ESTILOS (inmediatamente después de set_page_config)
apply_standard_styles()

# Título principal (h2 - SIEMPRE)
st.markdown("## Mi Dashboard")

# Sección (h3)
st.markdown("### Análisis Principal")

# Subsección (h4)
st.markdown("#### Detalles")
```

---

## 📊 Convenciones Obligatorias

### Títulos

```python
# ✅ CORRECTO - Título principal con h2
st.markdown("## Título del Dashboard")

# ❌ INCORRECTO - No usar st.title() o h1
st.title("Título del Dashboard")  # NO

# ✅ CORRECTO - Sección con h3
st.markdown("### Sección Principal")

# ✅ CORRECTO - Subsección con h4
st.markdown("#### Subsección")
```

### Estilos Aplicados

| Elemento | Tamaño | Peso | Uso |
|----------|--------|------|-----|
| h2 | 1.75rem | 600 | Título principal del dashboard |
| h3 | 1.3rem | 600 | Secciones principales |
| h4 | 1.1rem | 600 | Subsecciones |
| Tablas | 11px | - | Todas las tablas |
| Métricas | 1.8rem | 600 | st.metric() |

---

## 🔧 Deploy

### En build_deploy.sh:

```bash
# Copiar módulo shared
if [ -d "../analysis_predictive_shared" ]; then
    cp -r ../analysis_predictive_shared ./analysis_predictive_shared
fi

# Build
gcloud builds submit --tag ${IMAGE_TAG}

# Limpiar
if [ -d "./analysis_predictive_shared" ]; then
    rm -rf ./analysis_predictive_shared
fi
```

### En .gitignore:

```gitignore
# Módulo shared copiado temporalmente
analysis_predictive_shared/
```

---

## 📝 Mantenimiento

### Principio: Mantenerlo Simple

- ✅ Un solo estilo por elemento
- ✅ Cambios afectan a TODOS los dashboards
- ✅ No agregar variantes o casos especiales
- ❌ No complicar con selectores CSS específicos
- ❌ No agregar estilos por proyecto individual

### Agregar Nuevo Estilo

1. **¿Es realmente necesario?** - Si solo un proyecto lo necesita, va en ese proyecto, no aquí
2. **Editar** `streamlit_config.py`
3. **Documentar** en este README
4. **Commit y push**
5. **Probar** en TODOS los dashboards

---

## 📦 Proyectos que Usan Este Módulo

Todos siguen las mismas convenciones:

1. **calls_historical_variability**
   - Título: `## Historical Variability Analyzer`
   - Secciones: h3

2. **calls_analysis_dashboard**
   - Título: `## ServiceTitan - Inflection Points Analysis`
   - Secciones: h3

3. **data_science_index**
   - Título: `## Data Science Index`
   - Secciones: h3

---

## 🎨 Funciones Disponibles

### `apply_standard_styles()`

Aplica todos los estilos compartidos. **Llamar una vez** después de `st.set_page_config()`.

### `get_standard_colors()`

Retorna colores estándar:

```python
colors = get_standard_colors()
# colors['primary'] = '#0066cc'
# colors['success'] = '#28a745'
# colors['danger'] = '#dc3545'
# colors['peak'] = '#90EE90'
# colors['valley'] = '#FFB6C1'
```

### `get_page_config()`

Retorna configuración estándar:

```python
config = get_page_config()
# config['layout'] = 'wide'
# config['page_icon'] = '📊'
```

---

## ✅ Checklist para Nuevos Dashboards

Cuando crees un nuevo dashboard:

- [ ] Importar `apply_standard_styles()`
- [ ] Llamar después de `st.set_page_config()`
- [ ] Usar `## Título` para el título principal (h2)
- [ ] Usar `### Sección` para secciones (h3)
- [ ] Usar `#### Subsección` para subsecciones (h4)
- [ ] Agregar copia de shared en `build_deploy.sh`
- [ ] Agregar `analysis_predictive_shared/` en `.gitignore`

---

## 🔍 Testing

Después de modificar estilos, verificar en:
- [ ] Dashboard con tablas
- [ ] Dashboard con gráficos
- [ ] Sidebar con controles
- [ ] Métricas (st.metric)
- [ ] Responsive (móvil)

---

**Desarrollado por**: Platform Partners Team  
**Fecha**: Octubre 2025  
**Versión**: 2.1.0 (Simplificado)  
**Mantra**: Simple, Unificado, Mantenible
