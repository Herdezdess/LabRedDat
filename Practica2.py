import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from scipy.stats import linregress
import plotly.express as px
import seaborn as sns
import altair as alt
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
  #lector del csv
  data = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha.csv', index_col=1, parse_dates=True)

  tab1, tab2, tab3, tab4 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])

  with tab1:
    #jala los datos
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
    st.scatter_chart(combined_data, size=20 use_container_width=True)
    
  with tab2:
    
    data1=data['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data1, color='#00129A', size=20, use_container_width=True)
    

  with tab3:
   
    data2=data['Casos por fecha de toma de muestra']
    st.scatter_chart(data2, color='#00A2E8', size=20, use_container_width=True)

  with tab4:

    data3=data['Casos por fecha de emisión de resultados']
    st.scatter_chart(data3, color='#7A1A82', size=20, use_container_width=True)
    
  
    

  

if selected == "Teoría":
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>RESUMEN</h1>", unsafe_allow_html=True)
  st.markdown("""En Guatemala los datos de contagios de COVID19 han sido registrados en diversas páginas, esto es útil en la predicción de ciertos fenómenos como la tendencia de los datos.""")
  st.markdown("""Usando """)
  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>MARCO TEÓRICO</h1>", unsafe_allow_html=True)
  
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>CASO DE ESTUDIO</h1>", unsafe_allow_html=True)
  st.markdown("""Utilizando los registros de casos de COVID19 del ministerio de salud de la República de Guatemala se realizaron gráficas de los datos disponibles desde el 1 de junio de 2020 hasta el 15 de marzo de 2021.""")
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>PROCEDIMIENTO EXPERIMENTAL</h1>", unsafe_allow_html=True)
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
