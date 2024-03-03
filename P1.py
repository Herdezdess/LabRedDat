#librerias
from matplotlib import pyplot as plt
import numpy
import pandas
import math
import streamlit as st

#Datos personales
st.title('Parcial 1')
st.write('Laboratorio de reducción de datos')
st.write('Dessiré Zapeta Hernández')
st.write('202112959')

#Cajas de texto para que el usuario agregue los datos 
n = st.text_input('Ingrese el valor deseado de n, el número de caras', '1')
st.write('El valor de n es ', n)

p = st.text_input('Ingrese el valor deseado de p', '1/2')
st.write('El valor de p es ', p)

x = st.text_input('Ingrese el valor deseado de x', '10')
st.write('El valor de x es ', x)

#Definimos la función binomial
def binomial(x,n,p):
    comb = math.comb(n,x)
    p_x = p**x
    q = 1 - p
    q_nx = q**(n-x)
return comb*p_x*q_nx

lista = numpy.arange(n+1)
print(lista)

data_table = pandas.DataFrame({'x':lista})








