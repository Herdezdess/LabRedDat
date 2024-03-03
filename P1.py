#Librerias
import math 

import numpy as np
import pandas as pd
import streamlit as st

#Datos personales
st.title('Parcial 1')
st.write('Laboratorio de reducción de datos')
st.write('Dessiré Zapeta Hernández')
st.write('202112959')

#Le pedimos al usuario que ingrese los datos necesarios
n = st.text_input('Ingrese el valor deseado de n, el número intentos', '1')
st.write('El valor de n es ', n)
p = st.text_input('Ingrese el valor deseado de p, la probabilidad de obtener el caso deseado', '1/2')
st.write('El valor de p es ', p)

#Definimos la función binomial


#Hacemos una lista

lista = np.arange(n + 1)
st.write(lista)














