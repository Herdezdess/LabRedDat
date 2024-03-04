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
#posibles errores, si n no es entero, si n no es un numero
if  (isinstance(n, int)==false):
    st.write('n debe ser un número entero.')
elif (n.isdigit()==false):
    st.write('n debe ser un valor númerico')
else:
    st.write('El valor de n es ', n)


#Definimos los errores


p = st.number_input("Ingrese el valor deseado de p", value=None, placeholder="Type a number...")

if (p>1):
    st.write("P debe ser un número menor que 1")
elif (p.isdigit()==false):
    st.write('p debe ser un valor númerico')
else:
    st.write('El valor de n es ', p)



#Posibles errores de p




#Definimos la función binomial
def binomial(x,n,p):
    comb = math.comb(int(n),int(x))
    p_x = p**x
    p_nx = (1-p)**(n-x)
    return comb*p_x*p_nx 

#Hacemos una lista para la nuestra tabla
lista = np.arange(n+1)

#Definimos la primera fila de la tabla
data_table = pd.DataFrame({'x':lista})
#Ponelos la tabla con el valor probabilistico
data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p), axis=1)
st.write(data_table)

#Graficamos los datos de la tabla
binomial_plot, axis = plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C1')
binomial_plot.savefig('imagen.png')
#Le ponemos título al gráfico
st.title('Graficos binomiales')
st.pyplot(binomial_plot)














