#Librerias
from matplotlib import pyplot as plt
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
n = st.number_input("Ingrese el valor deseado de n", value=None, placeholder="Type a number...")
st.write('El valor de n es ', n)
p = st.number_input("Ingrese el valor deseado de p", value=None, placeholder="Type a number...")
st.write('El valor de p es ', p)

#Definimos la función binomial
def binomial(x,n,p):
    comb = math.comb(int(n),int(x))
    p_x = p**x
    p_nx = (1-p)**(n-x)
    return comb*p_x*p_nx 

#Hacemos una lista para la nuestra tabla
lista = np.arange(n+1)
st.write(lista)

#Definimos la primera fila de la tabla
data_table = pd.DataFrame({'x':lista})
#Ponelos la 
data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p), axis=1)
st.write(data_table)


binomial_plot, axis = plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C1')
binomial_plot.savefig('imagen.png')

st.title('Graficos binomiales')
st.pyplot(binomial_plot)














