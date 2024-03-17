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
    # Selección de cantidad de tiros
    m = st.slider('Seleccione la cantidad de tiros (m)', 0, 100, value=100)  # Crea un control deslizante para que el usuario seleccione la cantidad de tiros
    m_t = data.head(m)  # Selecciona las primeras 'm' filas de los datos
    # Gráfico de barras

    def binom(x,n,p):
        x = int(x)
        n = int(n)
            
        comb = math.comb(n,x)
        p_x = p**x
        q_nx = (1-p)**(n-x)
        return comb*p_x*q_nx

    binom = np.vectorize(binom)


    data = pd.read_csv('https://raw.githubusercontent.com/JARA99/F503-2024-public/main/Unidades/2-Distribuciones/Binomial-fichas.csv')
    print(f'data:\n{data}')

    data = data.loc[:m]

    counts_non_sort = data['GS'].value_counts()
    counts = pd.DataFrame(np.zeros(11))

    for row, value in counts_non_sort.items():
        counts.loc[row,0] = value

    print(f'counts:\n{counts}')
    print(f'index: {counts.index.values}')
    print(f'normalized counts: {list(counts[0]/m)}')


    fit, cov_mat = sco.curve_fit(binom,counts.index.values,counts[0]/m,[10,0.5],bounds=[(0,0),(np.inf,1)])

    print(f'Fit:\n{fit}\ncov_mat\n{cov_mat}')





    binomial_plot = px.line(x=counts.index.values, y=binom(counts.index.values,n,p), title="Lanzamiento de fichas")

    binomial_plot.add_bar(x=counts.index.values, y=counts[0]/m, name='Lanzamientos experimentales')

    binomial_plot.show()
    
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


