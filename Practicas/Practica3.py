import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from scipy.stats import linregress
from scipy.stats import chi2_contingency
import plotly.express as px
import seaborn as sns
import altair as alt
import math 
sns.set()

#Configuración de la página
st.set_page_config(page_title="Práctica 3: Decaimiento de Cesio-137", page_icon="☢️", layout="wide")

#diseño css y animación de los covichus
custom_css = """
<style>
/* Bordes laterales */
.stApp {
    border-left: 200px solid #D7C7F7; /* Color del borde izquierdo */
    border-right: 200px solid #D7C7F7; /* Color del borde derecho */
}

/* Animación del simbolo de radioactivo cayendo */
@keyframes falling {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(100vh); }
}

/* Estilo para los cuidado peligro */
.falling-emoji {
    position: fixed;
    animation: falling 7s linear infinite;
    font-size: 3em;
}

/* posición cuidado peligro */
#emoji1 { left: 30px; }
#emoji2 { left: 120px; }
#emoji3 { right: 30px; }
#emoji4 { right: 120px; }
</style>
"""

# Se agrega el diseño CSS a streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# Aquí se agregan los simbolos de CUIDADO PELIGRO 
st.markdown('<div class="falling-emoji" id="emoji1">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">☣</div>', unsafe_allow_html=True)

st.markdown('<div class="falling-emoji" id="emoji1">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">☣</div>', unsafe_allow_html=True)

st.markdown('<div class="falling-emoji" id="emoji1">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">☣</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">☣</div>', unsafe_allow_html=True)








# Menú lateral
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
  st.markdown("<h1 style='text-align: center; color: #A2BDF1; text-shadow: 3px 3px #BEFBB3;'>- Decaimiento de Cesio-137 -</h1>", unsafe_allow_html=True)
  #st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Mediciones en el aire</h1>", unsafe_allow_html=True)
    

#Definir fórmula del fit para el aire
def fit(x):
    A=63.5733
    u=2.18871
    r=1.59884
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit = np.vectorize(fit)

# Datos aire
data = pd.read_csv('https://raw.githubusercontent.com/Fabricio-mencos/LabRedDat/main/Practicas/Practica3/datos1.csv')
df = pd.DataFrame(data)
value_range = np.arange(-3,df['Aire'].max()+1)
count = df['Aire'].value_counts().reindex(value_range, fill_value=0).reset_index()
print(count)

plot_fit = px.line(x=value_range, y=fit(value_range))
plot_fit.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit.add_bar(x=count['Aire'], y=count['count'])
st.plotly_chart(plot_fit)

prom1=np.mean(data['Aire'])
desv1= np.std(data['Aire'])
promedio1 = round(prom1, 3)
desviacion1 = round(desv1, 3)
st.write('Promedio de los datos:', promedio1)
st.write('Desviación Estándar de los datos:', desviacion1)



#st.divider()
st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Mediciones con el Cesio-137</h1>", unsafe_allow_html=True)

# Definir fórmula del fit para el cesio
def fit2(x):
    A=25.382
    u=439.84
    r=19.6525
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit2 = np.vectorize(fit2)

# Datos cesio
print(df['Cesio'].min())
value_range2 = np.arange(df['Cesio'].min(),df['Cesio'].max()+1)
count2 = df['Cesio'].value_counts().reindex(value_range2, fill_value=0).reset_index()
print(count2)
print(value_range2)

group = np.arange(350, 505, 5)
cesio_cut = df.groupby(pd.cut(df['Cesio'], group))['Cesio'].count()
print(cesio_cut)
data_c = pd.read_csv('https://raw.githubusercontent.com/Fabricio-mencos/LabRedDat/main/Practicas/Practica3/Cesio.csv')
dfd = pd.DataFrame(data_c)

plot_fit2 = px.line(x=group, y=fit2(group))
plot_fit2.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit2.add_bar(x=group, y=dfd['count'])
st.plotly_chart(plot_fit2)

def f(x):
    return (25.382) * np.exp(-((x - 439.84) / 19.6525) ** 2 / 2)
f_esp=np.array([f(x) for x in df])
f_obs, _ = np.historigram(datos, bins='auto')
chi2 = np.sum((f_esp - f_obs)**2/f_esp)
g_lib = len(f_obs) - 1
p = 1 - chi2.cdf(chi2, g_lib)
st.write('Valor de Chi Cuadrado', chi2)
st.write('Grados de libertad', g_lib)
st.write('Valor asociado a la prueba de Chi cuadrado', p)





st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Datos de la prueba de Chi Cuadrado</h1>", unsafe_allow_html=True)
tabla_contingencia = pd.crosstab(index=data['Aire'], columns=data['Cesio'])
chi2, p, _, _ = chi2_contingency(tabla_contingencia)
chit2= round(chi2, 3)
pt2 = round(p,3)
st.write('Valor de Chi-Cuadrado:', chit2)
st.write('Valor asociado a la prueba de Chi-Cuadrado:', pt2)
#chi2 es el valor de la chi-cuadrado calculado y p es el p valor asociado a la prueba de chi-cuadrado.

    
  
if selected == "Teoría":
  st.divider()
  st.markdown("*USAC-ECFM. Laboratorio de reducción de datos.*")
  st.markdown("*Práctica 3. Decaimiento del Cesio-137*")
  st.markdown("*Mencos Calva, Allan Fabricio. 202106009,*")
  st.markdown("*Zapeta Hernández, Alejandra Dessiré. 202112959.*")
  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1; text-shadow: 3px 3px #BEFBB3;'>--- RESUMEN ---</h1>", unsafe_allow_html=True)
  st.markdown('<div style="text-align: justify;">Esta práctica pretende analizar el decaimiento del cesio-137 y compararlo con los decaimientos medidos en el aire sin utilizar ningún tipo de material radioactivo. Posteriormente se hará un ajuste a partir de una distribución Gaussiana y una distribución de Poisson para poder determinar cual de estas se adapte mejor a cada uno de los casos. Finalmente, para analizar la relación entre cada uno de los ajustes realizados, se hará la prueba de Chi cuadrada.</div>', unsafe_allow_html=True)


  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1; text-shadow: 3px 3px #BEFBB3;'>--- Marco Teórico---</h1>", unsafe_allow_html=True)
  st.markdown("<h3 style='text-align: left; color: #5E67DC; text-shadow: 3px 3px #BEFBB3;'>Cesio-137 [Cs]</h3>", unsafe_allow_html=True)
  st.markdown("""
    El cesio es el elemento número 55 de la tabla periódica y tiene un peso atómico de 132.9u. A simple vista, este elemento es de color plateado blanquesino que puede llegar a ser flexible y blando. Aunque este metal se vuelve líquido cerca de la temperatura ambiente. El cesio-137 es la forma radiactiva más común del cesio, el cual es producido mediante fisión nuclear para utilizarse en dispositivos médicos y también se obtiene como subproducto de la fisión nuclear dentro de los reactores nucleares o pruebas de armas nucleares.
              
    El cesio-137 es capaz de emitir partículas beta y rayos gamma. Su vida media es de 30.17 años y se mueve con muchísima facilidad con el aire, pero también se disuelve con mucha facilidad al pasar por agua. Cuando el cesio-137 se usa en pequeñas cantidades, puede ser utilizado para calibrar contadores Geiger-Muller. Si la cantidad de cesio-137 aumenta, este puede ser usado para: 
    """)
  st.markdown("""  
    ▶ Dispositivos de radioterapia médica para el tratamiento del cáncer.

    
    ▶ Manómetros industriales que detectan el flujo de líquido a través de tuberías.

    
    ▶ Otros dispositivos industriales que miden el espesor de materiales como papel o láminas de metal.
    """)
  
  st.markdown("<h3 style='text-align: left; color: #5E67DC; text-shadow: 3px 3px #BEFBB3;'>Contador Geiger-Muller</h3>", unsafe_allow_html=True)
  st.markdown("""
    El contador Geiger es utilizado para detectar la radiación ionizante, es decir que puede medir la cantidad de radiación alfa, beta, gamma, fotones, rayos X. Este es llamado Geiger-Muller porque fue desarrollado en 1928 por los físicos alemanes Hans Geiger y Walter Muller. Hoy en día suele utilizarse mucho para determinar la peligrosidad de diferentes materiales y puede dar mediciones inmediatas o puede programarse para que mida la radiación en un determinado periodo de tiempo
              
    Los detectores Geiger-Muller funcionan con un principio muy simple: Dentro del detector hay un gas noble y cuando las partículas entran al detector, estas reaccionan con ese gas noble. Cuando se da esta interacción, el gas cambia sus propiedades habituales y crea una conductividad. Todo esto hace que la radiación pueda medirse a partir de la frecuencia del flujo de la corriente que se genera. Algunos contadores también son capaces de medir rayos X, pero eso dependerá exclusivamente del contador pues existen de diferentes calidades que podrán proporcionar mayor precisión a la hora de realizar las mediciones.
    """)
  
  st.markdown("<h3 style='text-align: left; color: #5E67DC; text-shadow: 3px 3px #BEFBB3;'>Distribución de Poisson</h3>", unsafe_allow_html=True)
  st.markdown(""" 
    Fue desarrollada por Siméon Denis Poisson en 1838. Esta distribución, de variable discreta, tiene una enorme importancia en el área de la modelización de fenómenos en los cuales el interés reside en determinar el número de hechos de cierto tipo que se pueden producir en un intervalo de tiempo donde estos hechos tiene una probabilidad muy baja de suceder o son muy raros. 
              
    La expresión matemática para esta función de probabilidad está dada por: 
    """) 
  st.latex(r''' P(X=k) = \frac{\lambda ^k\cdot e^{-\lambda }}{k!} ''')
  st.markdown("donde lambda es llamado el parámetro de probabilidad, k es el número de ocasiones en las que queremos obtener determinado suceso y e es el número de Euler. ")
  st.markdown("<h3 style='text-align: left; color: #5E67DC; text-shadow: 3px 3px #BEFBB3;'>Prueba de Chi cuadrada</h3>", unsafe_allow_html=True)
  st.markdown("""
    La prueba del chi cuadrado (o prueba chi-cuadrado) es una técnica estadística utilizada para evaluar relaciones entre variables categóricas. Se basa en la comparación entre datos observados y datos esperados para determinar si las diferencias entre ellos son estadísticamente significativas. Hay dos tipos principales de pruebas del chi cuadrado:
          
    ▶ La prueba de independencia
          
    ▶Prueba de bondad de ajuste
              
    En general, el resultado de la prueba del chi cuadrado es un valor (el "estadístico chi cuadrado") que describe la magnitud de la diferencia entre los valores observados y esperados. El valor p (probabilidad) asociado con este estadístico nos ayuda a determinar si la diferencia es significativa. Si el valor p es pequeño (por ejemplo, menos de 0.05), puedes rechazar la hipótesis nula, lo que indica que hay una asociación significativa entre las variables (o que la distribución observada no se ajusta a la esperada).

    """)
  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1; text-shadow: 3px 3px #BEFBB3;'>-- Análisis de resultados--</h1>", unsafe_allow_html=True)
  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1; text-shadow: 3px 3px #BEFBB3;'>--- Conclusiones---</h1>", unsafe_allow_html=True)








  st.divider()
  st.markdown("<h3 style='text-align: left; color: black;'>Referencias</h1>", unsafe_allow_html=True)
  st.markdown("""  
  **1.**  Radionuclide Basics: Cesium-137 | US EPA. (2024, 5 febrero). US EPA. https://www.epa.gov/radiation/radionuclide-basics-cesium-137
          
  **2.**   Instrumentación, P. I. S. (2024, 27 abril). Contador Geiger | PCE Instruments. https://www.pce-instruments.com/espanol/instrumento-medida/medidor/contador-geiger-kat_163206.htm
                
  **3.**   colaboradores de Wikipedia. (2024, 8 abril). Distribución de poisson. Wikipedia, la Enciclopedia Libre. https://es.wikipedia.org/wiki/Distribuci%C3%B3n_de_Poisson

    """)
  st.divider()

  
  st.markdown('<div style="text-align: justify;> <div>', unsafe_allow_html=True)
  st.markdown('<div style="text-align: justify;> <div>', unsafe_allow_html=True)
  st.markdown('<div style="text-align: justify;> <div>', unsafe_allow_html=True)
