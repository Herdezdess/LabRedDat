import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from scipy.stats import linregress
import plotly.express as px
import seaborn as sns
import altair as alt
import math 
sns.set()

#Configuración de la página
st.set_page_config(page_title="Práctica 2: Predicción de COVID19", page_icon="🌍", layout="wide")


# Menú lateral
with st.sidebar:
  selected=option_menu(
    menu_title="Menú",
    options = ["Principal", "Teoría"],
    icons = ["house-heart-fill", "envelope-heart-fill"],
    menu_icon = "heart-eyes-fill",
    default_index = 0,
  )
if selected == "Principal":
  #título
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Predicción de COVID19</h1>", unsafe_allow_html=True)
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Gráficas desde el 13/03/2020 hasta el 1/05/2020</h1>", unsafe_allow_html=True)
  #lector del csv primera fecha
  data = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha_junio.csv', index_col=1, parse_dates=True)
  tab1, tab2, tab3, tab4 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])
  #Definimos la distribución de Poisson
  def f(x):
      return A * np.exp(-((x - u) / r) ** 2 / 2)
  
  with tab1:
    #hala los datos
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data1 = data['Casos por fecha de inicio de síntomas']
    data2 = data['Casos por fecha de toma de muestra']
    data3 = data['Casos por fecha de emisión de resultados']
    # Combinación de datos
    combined_data = pd.DataFrame({
      'Casos por fecha de inicio de síntomas': data1,
      'Casos por fecha de toma de muestra': data2,
      'Casos por fecha de emisión de resultados': data3
    })
    #muetsra el grafico
    st.scatter_chart(combined_data, size=20, use_container_width=True)
    
  with tab2:
    data1=data['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data1, color='#00129A', size=20, use_container_width=True)

    # Parámetros finales del ajuste que se obtuvieron en gnuplot
    A = 325.658
    u = 73.265
    r = 9.05745
    x_values = np.arange(len(data1))
    y_values = f(x_values)
    plt.plot(x_values, y_values, color='red', label='Ajuste de la función')
    st.pyplot()
    st.snow()

  
    # Datos
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

# Crear una figura y ejes
    fig, ax = plt.subplots(figsize=(8, 6))

# Graficar líneas
    ax.plot(x, y1, label='Sin(x)', color='blue')

# Graficar puntos
    ax.scatter(x, y2, label='Cos(x)', color='red')

# Configuración de la gráfica
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Gráfico de puntos y líneas')
    ax.legend()

# Mostrar la figura en Streamlit
    st.pyplot(fig)
    
  with tab3:
    data2=data['Casos por fecha de toma de muestra']
    st.scatter_chart(data2, color='#00A2E8', size=20, use_container_width=True)
  with tab4:
    data3=data['Casos por fecha de emisión de resultados']
    st.scatter_chart(data3, color='#7A1A82', size=20, use_container_width=True)

  #Lo mismo, pero para la segunda fecha
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Gráficas desde el 13/03/2020 hasta el 15/03/2021</h1>", unsafe_allow_html=True)
  sf = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha_marzo.csv', index_col=1, parse_dates=True)
  tab5, tab6, tab7, tab8 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])
  with tab5:
    #hala los datos
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data4 = sf['Casos por fecha de inicio de síntomas']
    data5 = sf['Casos por fecha de toma de muestra']
    data6 = sf['Casos por fecha de emisión de resultados']
    # Combinación de datos
    combined_data2 = pd.DataFrame({
      'Casos por fecha de inicio de síntomas': data4,
      'Casos por fecha de toma de muestra': data5,
      'Casos por fecha de emisión de resultados': data6
    })
    #muetsra el grafico
    st.scatter_chart(combined_data2, size=20, use_container_width=True)
  with tab6:
    data4=sf['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data4, color='#00129A', size=20, use_container_width=True)
  with tab7:
    data5=sf['Casos por fecha de toma de muestra']
    st.scatter_chart(data5, color='#00A2E8', size=20, use_container_width=True)
  with tab8:
    data6=sf['Casos por fecha de emisión de resultados']
    st.scatter_chart(data6, color='#7A1A82', size=20, use_container_width=True)

  #Lo mismo, pero para la tercera fecha
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Gráficas desde el 13/03/2020 hasta el 07/04/2024</h1>", unsafe_allow_html=True)
  tf = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha_todos.csv', index_col=1, parse_dates=True)
  tab9, tab10, tab11, tab12 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])
  with tab9:
    #hala los datos
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data7 = tf['Casos por fecha de inicio de síntomas']
    data8 = tf['Casos por fecha de toma de muestra']
    data9 = tf['Casos por fecha de emisión de resultados']
    # Combinación de datos
    combined_data3 = pd.DataFrame({
      'Casos por fecha de inicio de síntomas': data7,
      'Casos por fecha de toma de muestra': data8,
      'Casos por fecha de emisión de resultados': data9
    })
    #muetsra el grafico
    st.scatter_chart(combined_data3, size=20, use_container_width=True)
  with tab10:
    data7=tf['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data7, color='#00129A', size=20, use_container_width=True)
  with tab11:
    data8=tf['Casos por fecha de toma de muestra']
    st.scatter_chart(data8, color='#00A2E8', size=20, use_container_width=True)
  with tab12:
    data9=tf['Casos por fecha de emisión de resultados']
    st.scatter_chart(data9, color='#7A1A82', size=20, use_container_width=True)
    
  
    

  

if selected == "Teoría":
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>RESUMEN</h1>", unsafe_allow_html=True)
  st.markdown("""La pandemia del COVID-19 fué uno de los desafíos más grandes a los que la sociedad guatemalteca se ha enfrentado en la historia reciente. Esto no afectó solamente al sector de la salud, sino que fue un problema multifacético el cual afectó principalmente en las siguientes áreas:""")
  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>MARCO TEÓRICO</h1>", unsafe_allow_html=True)
  
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>CASO DE ESTUDIO</h1>", unsafe_allow_html=True)
  st.markdown("""Utilizando los registros de casos de COVID19 del ministerio de salud de la República de Guatemala se realizaron gráficas de los datos medidos en dos intervalos de tiempo diferentes. Cada uno de estos intervalos inicia el día en el que se registró el primer caso positivo de COVID-19 en Guatemala, es decir, el 13 de marzo de 2020. El primer intervalo toma los datos desde la anterior fecha hasta el 1 de junio de 2020. El segundo caso, toma aún más datos, siendo el 15 de marzo de 2021 la fecha límite para la toma de datos.""")
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>PROCEDIMIENTO EXPERIMENTAL</h1>", unsafe_allow_html=True)
  st.markdown("""Para esta práctica, se tomaron los dos casos de estudio mencionados anteriormente y se utilizó un ajuste hecho a partir de una distribución binomial. También fue necesario el uso de herramientas externas a Python como Gnuplot. Esto debido a que el ajuste realizado con Python se adapta solamente a los datos tomados y no realiza las predicciones deseadas, por lo cual se utilizó Gnuplot para poder obtener los valores para la distribución binomial y luego plotearla dentro de la gráfica con los datos recopilados. Este ajuste nos permitió dar una estimación de la fecha en la cual se dará el pico de casos positivos para COVID-19.""")
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #A2BDF1;'>DISCUSIÓN DE RESULTADOS</h1>", unsafe_allow_html=True)  
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>CONCLUSIONES</h1>", unsafe_allow_html=True)  
  st.divider()
  st.markdown("<h3 style='text-align: left; color: black;'>Referencias</h1>", unsafe_allow_html=True)
  st.markdown("""  
  **1.** Ministerio de Salud Pública y Asistencia Social. Situación de COVID19 en Guatemala. 
                  
  **2.**   
                
  **3.**   
    """)
  st.divider()
