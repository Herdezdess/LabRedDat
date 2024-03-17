import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
from scipy.stats import binom
from scipy.optimize import curve_fit

# Definir la función binomial_distribution fuera del bloque if

#Nombre e ícono de la pestaña
st.set_page_config(page_title="Practica 1: Distribución Binomial", page_icon="🌍", layout="wide")
with st.sidebar:
    selected=option_menu(
        menu_title="Menú",
        options = ["Principal", "Teoria"],
        icons = ["house-heart-fill", "envelope-heart-fill"],
        menu_icon = "heart-eyes-fill",
        default_index = 0,
    )

if selected == "Principal":
    # Título
    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Distribución Binomial: Lanzamiento de monedas</h1>", unsafe_allow_html=True)
    # Lectura de datos
    data = pd.read_csv('https://raw.githubusercontent.com/JARA99/F503-2024-public/main/Unidades/2-Distribuciones/Binomial-fichas.csv')
    # Selección de cantidad de tiros
    m = st.slider('Seleccione la cantidad de tiros (m)', 0, 100, value=100)  # Crea un control deslizante para que el usuario seleccione la cantidad de tiros
    m_t = data.head(m)  # Selecciona las primeras 'm' filas de los datos
    # Gráfico de barras
    grafica = px.histogram(m_t, 'DF')  # Crea un gráfico de barras utilizando Plotly Express con los datos de 'm_t'
    st.plotly_chart(grafica)  # Muestra el gráfico de barras en la aplicación
    # Ajuste de distribución binomial
    x_values = np.arange(0, max(m_t['DF']) + 1)  # Crea un rango de valores de 0 a la máxima cantidad de tiros
    n = len(m_t['DF'])  # Obtiene el tamaño de la muestra
    p_fit = np.mean(m_t['DF']) / max(m_t['DF'])  # Calcula la probabilidad de éxito para el ajuste binomial
    binomial_fit = binom.pmf(x_values, n, p_fit)  # Calcula la función de masa de probabilidad (PMF) de la distribución binomial
    # Gráfico de ajuste
    st.markdown("<h2 style='text-align: center; color: #A2BDF1;'>Ajuste de Distribución Binomial</h2>", unsafe_allow_html=True)  # Título del ajuste
    st.line_chart(list(zip(x_values, binomial_fit)))  # Muestra un gráfico de línea con el ajuste de la distribución binomial
    # Tabla de datos
    st.table(m_t)  # Muestra una tabla con los datos de los tiros de monedas seleccionados por el usuario
    st.divider()



if selected == "Teoria":
    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Teoria de la Distribución Binomial</h1>", unsafe_allow_html=True)  

    st.markdown("""La distribución binomial es modelo probabilistico discreto. Este describe el número de éxitos en una serie de ensayos secuenciales independientes, donde cada uno tiene siempre la misma probabilidad de exito. Este modelo es utilizado con mucha frecuencia en experimentos donde se obtengan resultados binarios, es decir, si el resultado se puede categorizar como Éxito o Fracaso.""")
    st.markdown("""Para definir a la distribución binomial, se requieren dos parametros. El primero de ellos es el **número total de intentos (n)** y la **probabilidad de exito de cada ensayo (p)**. Agregado a esto, regularmente se utiliza el simbolo X para denotar una variable que cuenta el número de éxitos en n cantidad de ensayos. """)
    st.markdown("""La fórmula para calcular la probabilidad de exactamente k éxitos en n ensayos, con una probabilidad de éxito p, es:""")

    st.latex(r''' P(x = k) = \binom{n}{k} p^{k} (1-p)^{n-k} ''')

    st.markdown("""Donde:  
    ▶ (n k) es el coeficiente binomial.  
    ▶ p es la probabilidad de éxito en un solo ensayo.  
    ▶ (1 - p) es la probabilidad de fracaso en un solo ensayo.  
    ▶ k es el número de exitos en n ensayos.
    """)
    st.divider()
    st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Acerca de esta practica</h1>", unsafe_allow_html=True)  
    st.markdown("""En esta practica, cada pareja, lanzó un grupo de 10 monedas un total de 100 veces para poder observar la tendencia de las monedas a caer en el lado de la cara. Tras recopilar todos los datos, estos fueron ingresados en un archivo csv para su analisis posterior. Lo primero que se realizó fue un histograma que muestra la fomra en que se distribuyó una cierta cantidad m de tiros de las monedas, donde la m puede ser elegida por el usuario. Añadido a lo anterior, se realizó un ajuste a los datos que se muestran en el histograma. Dicho ajuste fue hecho a paritr de un función binomial. Por último, se muestran los valores obtenidos a partir del ajuste, los valores obtenidos en los conteos de monedas y la desviación estandar de todos estos datos. """)  
    st.markdown("""En el caso donde se utilizaron los datos de toda la clase, se realizó un proceso muy similar al caso anterior, con la diferencia que en este histograma no se puede varias la m, por lo cual se muestra la información de todos los datos obtenidos. De igual manera se presenta el ajuste binomial, los valores del ajuste, los valores de ocnteo medio de caras y su desviación estandar. """)
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


