import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Práctica 2: Predicción de COVID19", page icon="🌍", layout="wide")
with st.sidebar:
  selected=option_menu(
    menu_title="Menú",
    options = ["Principal", "Teoría"],
    icons = ["house-heart-fill", "envelope-heart_fill"],
    menu_icon = "heart-eyes-fill",
    default_index = 0,
  )
if selected == "Principal":
  st.markdown("hola")

if selected == "Teoría":
  st.markdown("hola 2")
