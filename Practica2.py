import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
import plotly.express as px

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
  data = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha.csv')
  #Convertirlo a dataframe
  
  
  

  

if selected == "Teoría":
  st.markdown("hola 2")
