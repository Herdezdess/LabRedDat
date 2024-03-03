import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Parcial 1')

st.write('Laboratorio de reducción de datos')
st.write('Dessiré Zapeta Hernández')
st.write('202112959')

n = st.text_input('Valor de n')
st.write('El valor de n es ', n)

st.button("Reset", type="primary")
