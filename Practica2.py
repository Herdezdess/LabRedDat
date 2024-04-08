import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px
import seaborn as sns
sns.set()

st.set_page_config(page_title="Práctica 2: Predicción de COVID19", page_icon="🌍", layout="wide")
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
  #Convertirlo a dataframe
  #dataframe=pd.DataFrame(data[["Fecha","Casos por fecha de inicio de síntomas","Casos por fecha de toma de muestra","Casos por fecha de emisión de resultados"]])
  #Tomamos los datos
  #fecha=dataframe["Fecha"]
  #casos_sintomas=dataframe["Casos por fecha de inicio de síntomas"]
  #casos_muestra=dataframe["Casos por fecha de toma de muestra"]
  #casos_resultado=dataframe["Casos por fecha de emisión de resultados"]
  #Grafica de los tres casos
  
  
  # data.plot()
  #Grafica de 
  # data['Casos por fecha de inicio de síntomas'].plot()
  # data['Casos por fecha de toma de muestra'].plot()
  # data['Casos por fecha de emisión de resultados'].plot()
  
  fig, ax = plt.subplots(figsize=(10, 6))
  data['Casos por fecha de inicio de síntomas'].plot(label='Casos por fecha de inicio de síntomas')
  data['Casos por fecha de toma de muestra'].plot(label='Casos por fecha de toma de muestra')
  data['Casos por fecha de emisión de resultados'].plot(label='Casos por fecha de emisión de resultados')
  plt.xlabel("Fecha")
  plt.ylabel("Número de casos")
  plt.title("Casos de COVID-19 a lo largo del tiempo")
  plt.legend()
  st.pyplot(fig)

  

if selected == "Teoría":
  st.markdown("hola 2")
