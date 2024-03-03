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


def binomial(x,n,p):
    comb = math.comb(n,x)
    p_x = p**x
    u_p = (1 - p)**(n-x)
return comb*p_x*u_p

lista = numpy.arange(n+1)
print(lista)

data_table = pandas.DataFrame({'x':lista})

data_table['Pb'] = data_table.apply(lambda row: binomial(row['x'],n,p,q), axis=1)
print(data_table)


binomial_plot, axis = plt.subplots()
axis.bar(data_table['x'],data_table['Pb'])
axis.plot(data_table['x'],data_table['Pb'],color='C1')

binomial_plot.savefig('imagen.png')

st.title('Graficos binomiales')
st.pyplot(binomial_plot)


