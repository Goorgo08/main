import streamlit as st

st.set_page_config(
    page_title="Jorge | Data Science Hub",
    page_icon="🧭",
    layout="wide"
)

st.title("🚀 Mis Proyectos de Data Science")
st.markdown("Bienvenido/a a mi colección de aplicaciones interactivas. Selecciona el proyecto al que deseas acceder:")

st.write("")

col1, col2 = st.columns(2, gap="large")

with col1:
    with st.container(border=True):
        st.subheader("🏃 Maratón de Boston 2017")
        st.caption("Analítica Deportiva & Modelado Predictivo")
        
        st.markdown("""
        **¿Qué incluye este proyecto?**
        - **20 Retos Técnicos:** Análisis exploratorio de datos sobre más de 26.000 corredores (distribución por edad, género, ritmo de carrera, origen geográfico y detección de *outliers*).
        - **5 Hallazgos Clave:** Estudio en profundidad del efecto "muro", gestión de energía en carrera y consistencia de ritmo.
        - **Simulador de Meta:** Modelo de regresión lineal para predecir el tiempo final del corredor a partir de sus pasos por el 5K, 10K y media maratón.
        """)
        
        st.link_button(
            "Abrir Maratón de Boston ↗",
            "https://proyecto-media-maraton.streamlit.app/",
            type="primary",
            use_container_width=True
        )

with col2:
    with st.container(border=True):
        st.subheader("🏦 Credit Approval & Pricing Portal")
        st.caption("Fintech, Credit Scoring & Simulación Financiera")
        
        st.markdown("""
        **¿Qué incluye este proyecto?**
        - **Benchmark de Modelos:** Comparativa de rendimiento entre *Random Forest Optimizado* y *Regresión Logística* (métricas de Recall y F2-Score ponderando el coste del impago).
        - **Evaluación de Elegibilidad:** Scoring en tiempo real del solicitante en función de datos sociodemográficos, empleo, ingresos y garantías.
        - **Pricing & Rentabilidad:** Simulador financiero (método francés) ajustado por riesgo acumulado y cálculo del beneficio esperado para el banco.
        """)
        
        st.link_button(
            "Abrir Simulador de Crédito ↗",
            "https://credit-approval-app.streamlit.app/",
            type="primary",
            use_container_width=True
        )

st.write("")
st.divider()
st.caption("Desarrollado con Python & Streamlit.")