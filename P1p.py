import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from scipy.stats import binom

# Establecer la configuración de la página
st.set_page_config(page_title="Práctica 1: Distribución Binomial", page_icon="🌍", layout="wide")

# Función para ajustar la distribución binomial a los datos
def fit_binomial(data):
    p = data.mean().mean() / len(data.columns)
    n = len(data.columns)
    x = np.arange(0, n + 1)
    y = binom.pmf(x, n, p)
    return x, y

# Principal
if st.sidebar.selectbox("Menú", ["Principal", "Teoría"]) == "Principal":
    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Distribución Binomial: Lanzamiento de monedas</h1>", unsafe_allow_html=True)
    data = pd.read_csv('https://raw.githubusercontent.com/JARA99/F503-2024-public/main/Unidades/2-Distribuciones/Binomial-fichas.csv')
    m = st.slider('Seleccione la cantidad de tiros (m)', 0, 100, value=100)
    m_t = data.head(m)
    grafica = px.histogram(m_t, 'DF')

    # Ajuste de la distribución binomial
    x_fit, y_fit = fit_binomial(m_t)

    # Graficar el histograma y la distribución binomial ajustada
    fig = px.histogram(m_t, 'DF')
    fig.add_scatter(x=x_fit, y=y_fit, mode='lines', name='Ajuste Binomial')
    st.plotly_chart(fig)

    # Mostrar la tabla de datos
    st.divider()
    st.table(m_t)

elif st.sidebar.selectbox("Menú", ["Principal", "Teoría"]) == "Teoría":
    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Teoría de la Distribución Binomial</h1>", unsafe_allow_html=True)  

    st.markdown("""La distribución binomial es un modelo probabilístico discreto que describe el número de éxitos en una serie de ensayos independientes, donde cada uno tiene la misma probabilidad de éxito.""")
    st.markdown("""La fórmula para calcular la probabilidad de exactamente k éxitos en n ensayos, con una probabilidad de éxito p, es:""")

    st.latex(r''' P(x = k) = \binom{n}{k} p^{k} (1-p)^{n-k} ''')

    st.markdown("""Donde:  
    ▶ (n k) es el coeficiente binomial.  
    ▶ p es la probabilidad de éxito en un solo ensayo.  
    ▶ (1 - p) es la probabilidad de fracaso en un solo ensayo.  
    ▶ k es el número de éxitos en n ensayos.
    """)
    st.divider()
    st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Acerca de esta práctica</h1>", unsafe_allow_html=True)  
    st.markdown("""En esta práctica, se lanzaron 10 monedas un total de 100 veces para observar la tendencia de las monedas a caer en el lado de la cara. Luego de recopilar los datos, se realizó un histograma que muestra la distribución de una cierta cantidad m de tiros de las monedas. Además, se ajustó una función binomial a los datos y se graficó junto con el histograma.""")  
    st.divider()
    st.markdown("<h2 style='text-align: left; color: #A2BDF1;'>Análisis de Resultados</h1>", unsafe_allow_html=True)  
    st.divider()
    st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Conclusiones</h1>", unsafe_allow_html=True)  
    st.divider()
    st.markdown("<h3 style='text-align: left; color: black;'>Referencias</h1>", unsafe_allow_html=True)
    st.markdown("""  
    **1.** Johnson, N.L., Kotz, S., & Kemp, A.W. (1992). "Univariate Discrete Distributions". John Wiley and Sons.  
                  
    **2.** Devore, J.L. (2011). "Probability and Statistics for Engineering and the Sciences". Cengage Learning.  
                
    **3.** Wackerly, D., Mendenhall III, W., & Scheaffer, R.L. (2008). "Mathematical Statistics with Applications". Cengage Learning.  
    """)

    st.divider()
