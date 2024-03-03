import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Parcial 1')

st.write('Laboratorio de reducción de datos')
st.write('Dessiré Zapeta Hernández')
st.write('202112959')

n = st.text_input('Ingrese el valor deseado de n')
st.write('El valor de n es ', n)

n = st.number_input('Ingrese el valor deseado de p')
st.write('El valor de n es', n)

p = st.text_input('Ingrese el valor deseado de p')
st.write('El valor de n es ', p)

st.button("Reset", type="primary")
