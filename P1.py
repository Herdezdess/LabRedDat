import streamlit as st
import plotly.express as px
import pandas as pd

st.title('Parcial 1')
st.write('Laboratorio de reducción de datos')
st.write('Dessiré Zapeta Hernández')
st.write('202112959')

n = st.text_input('Ingrese el valor deseado de n, el número de caras', '1')
st.write('El valor de n es ', n)

p = st.text_input('Ingrese el valor deseado de p', '1/2')
st.write('El valor de p es ', p)

x = st.text_input('Ingrese el valor deseado de x', '10')
st.write('El valor de x es ', x)




