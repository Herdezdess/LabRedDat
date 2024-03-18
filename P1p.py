import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import plotly.express as px

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
    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Distribución Binomial: Lanzamiento de monedas</h1>", unsafe_allow_html=True)
    data = pd.read_csv('https://raw.githubusercontent.com/JARA99/F503-2024-public/main/Unidades/2-Distribuciones/Binomial-fichas.csv')
    print(data)
    m = st.slider('Seleccione la cantidad de tiros (m)', 0, 100, value=100)
    m_t = data.head(m + 1)
    grafica = px.histogram(m_t, 'DF')
    st.plotly_chart(grafica)
    st.divider()
    st.table(m_t)

if selected == "Teoria":
    #Los tipos de cuadros, morado palido y azul pálido
    estilo_cuadro = """
    <style>
    .cuadro-morado {
        padding: 20px;
        background-color: #F4E8FF; 
        border-radius: 10px;
    }
    </style>
    """

    estilo_cuadro_azul = """
    <style>
    .cuadro-azul {
        padding: 20px;
        background-color: #D4EEF0; 
        border-radius: 10px;
    }
    </style>
    """
    #se agregan a streamlit
    st.markdown(estilo_cuadro, unsafe_allow_html=True)
    st.markdown(estilo_cuadro_azul, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Resumen</h1>", unsafe_allow_html=True) 
    st.divider()

    st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Objetivos</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="cuadro-morado">
        <p>▶ Obtener de forma experimental la cantidad de caras al lanzar diez monedas del mismo valor. </p>
        <p>▶ Realizar un histograma con los datos obtenidos usando Python y mostrarlos en una app de Streamlit.</p>
        <p>▶ Ajustar los valores obtenidos en el histograma y mostrarlos en la app.</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Teoria de la Distribución Binomial</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class= "cuadro-azul">
        <p>La distribución binomial es un modelo probabilístico discreto que describe el número de éxitos en una serie de ensayos secuenciales independientes, donde cada uno tiene siempre la misma probabilidad de éxito. Este modelo es utilizado con mucha frecuencia en experimentos donde se obtengan resultados binarios, es decir, si el resultado se puede categorizar como Éxito o Fracaso.</p>
        <p>Para definir a la distribución binomial, se requieren dos parámetros. El primero de ellos es el <strong>número total de intentos (n)</strong> y la <strong>probabilidad de éxito de cada ensayo (p)</strong>. Agregado a esto, regularmente se utiliza el símbolo X para denotar una variable que cuenta el número de éxitos en n cantidad de ensayos.</p>
        <p>La fórmula para calcular la probabilidad de exactamente k éxitos en n ensayos, con una probabilidad de éxito p, es:</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(r''' P(x = k) = \binom{n}{k} p^{k} (1-p)^{n-k} ''')
    st.markdown("""
    <div class= "cuadro-azul">
        <p>Donde:</p>
        <ul>
            <li>(n k) es el coeficiente binomial.</li>
            <li>p es la probabilidad de éxito en un solo ensayo.</li>
            <li>(1 - p) es la probabilidad de fracaso en un solo ensayo.</li>
            <li>k es el número de éxitos en n ensayos.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.divider()

    
    st.markdown("""Para definir a la distribución binomial, se requieren dos parámetros. El primero de ellos es el **número total de intentos (n)** y la **probabilidad de exito de cada ensayo (p)**. Agregado a esto, regularmente se utiliza el simbolo X para denotar una variable que cuenta el número de éxitos en n cantidad de ensayos. """)
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
    
    st.markdown("""
    <div class="cuadro-morado">
        <p>En esta práctica, cada pareja lanzó un grupo de 10 monedas un total de 100 veces para poder observar la tendencia de las monedas a caer en el lado de la cara. Tras recopilar todos los datos, estos fueron ingresados en un archivo CSV para su análisis posterior. Lo primero que se realizó fue un histograma que muestra la forma en que se distribuyó una cierta cantidad m de tiros de las monedas, donde la m puede ser elegida por el usuario. Añadido a lo anterior, se realizó un ajuste a los datos que se muestran en el histograma. Dicho ajuste fue hecho a partir de una función binomial. Por último, se muestran los valores obtenidos a partir del ajuste, los valores obtenidos en los conteos de monedas y la desviación estándar de todos estos datos.</p>
        <p>En el caso donde se utilizaron los datos de toda la clase, se realizó un proceso muy similar al caso anterior, con la diferencia de que en este histograma no se puede variar la m, por lo cual se muestra la información de todos los datos obtenidos. De igual manera, se presenta el ajuste binomial, los valores del ajuste, los valores de conteo medio de caras y su desviación estándar.</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("<h2 style='text-align: left; color: #A2BDF1;'>Análisis de Resultados</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class= "cuadro-azul">
        <p>▶ Al variar el número de veces que se lanzan las monedas la gráfica de barras cambia, notamos que mientras mayor es este número más se parece a lo teóricamente esperado.</p>
        <p>▶ Se utilizaron monedas de diez centavos, sin embargo un lado de la moneda no es simétrico respecto al otro, lo cual podría alterar nuestra toma de datos.</p>
    </div>
    """, unsafe_allow_html=True) 
    st.divider()
    st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Conclusiones</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div class="cuadro-morado">
        <p>▶ En nuestra gráfica podemos observar que el valor que más se repite es el cinco, este es el valor promedio de los datos tomados. Lo que concuerda con la teoría, ya que es el caso más probable.</p>
        <p>▶ Nuestros datos han sido aterados de forma mínima por las condiciones en la toma de datos (el peso de las monedas, el suelo, aire, entre otros.), esto se ve reflejado en la comparación de estos datos con los valores teóricos esperados. Los valores experimentales son similares a los valores teóricos, podemos decir entonces que no se cometieron errores significativos en la toma de datos.</p>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    st.markdown("<h3 style='text-align: left; color: black;'>Referencias</h1>", unsafe_allow_html=True)
    st.markdown("""  
    **1.** Johnson, N.L., Kotz, S., & Kemp, A.W. (1992). "Univariate Discrete Distributions". John Wiley and Sons.  
                  
    **2.** Devore, J.L. (2011). "Probability and Statistics for Engineering and the Sciences". Cengage Learning.  
                
    **3.** Wackerly, D., Mendenhall III, W., & Scheaffer, R.L. (2008). "Mathematical Statistics with Applications". Cengage Learning.  
    """)
    st.divider()

