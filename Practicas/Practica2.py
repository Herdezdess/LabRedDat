import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from scipy.stats import linregress
import plotly.express as px
import seaborn as sns
import altair as alt
import math 
sns.set()

#Configuración de la página
st.set_page_config(page_title="Práctica 2: Predicción de COVID19", page_icon="🌍", layout="wide")

#diseño css y animación de los covichus
custom_css = """
<style>
/* Bordes laterales */
.stApp {
    border-left: 200px solid #D7C7F7; /* Color del borde izquierdo */
    border-right: 200px solid #D7C7F7; /* Color del borde derecho */
}

/* Animación de covis cayendo */
@keyframes falling {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(100vh); }
}

/* Estilo para los covis */
.falling-emoji {
    position: fixed;
    animation: falling 7s linear infinite;
    font-size: 2em;
}

/* posición covichus */
#emoji1 { left: 50px; }
#emoji2 { left: 150px; }
#emoji3 { right: 50px; }
#emoji4 { right: 150px; }
</style>
"""

# Se agrega el diseño CSS a streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# Los covichus cayendo
st.markdown('<div class="falling-emoji" id="emoji1">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">🦠</div>', unsafe_allow_html=True)

st.markdown('<div class="falling-emoji" id="emoji1">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">🦠</div>', unsafe_allow_html=True)

st.markdown('<div class="falling-emoji" id="emoji1">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">🦠</div>', unsafe_allow_html=True)

st.markdown('<div class="falling-emoji" id="emoji1">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji2">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji3">🦠</div>', unsafe_allow_html=True)
st.markdown('<div class="falling-emoji" id="emoji4">🦠</div>', unsafe_allow_html=True)







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
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>Predicción de COVID19</h1>", unsafe_allow_html=True)
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Gráficas desde el 13/03/2020 hasta el 1/05/2020</h1>", unsafe_allow_html=True)
  #lector del csv primera fecha
  data = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha_junio.csv', index_col=1, parse_dates=True)
  tab1, tab2, tab3, tab4 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])
  #Definimos la distribución de Poisson
  def f(x):
      return A * np.exp(-((x - u) / r) ** 2 / 2)
  
  with tab1:
    #hala los datos
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data1 = data['Casos por fecha de inicio de síntomas']
    data2 = data['Casos por fecha de toma de muestra']
    data3 = data['Casos por fecha de emisión de resultados']
    # Combinación de datos
    combined_data = pd.DataFrame({
      'Casos por fecha de inicio de síntomas': data1,
      'Casos por fecha de toma de muestra': data2,
      'Casos por fecha de emisión de resultados': data3
    })
    #muetsra el grafico
    st.scatter_chart(combined_data, size=20, use_container_width=True)

    A = 630.658
    u = 73.265
    r = 9.05745
    x_values = np.arange(100)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab2:
    
    data1=data['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data1, color='#00129A', size=20, use_container_width=True)
    #obtener los valores de x de la gráfica anterior
    x = data.index.tolist()

    # Parámetros finales del ajuste que se obtuvieron en gnuplot
    A = 470.658
    u = 73.265
    r = 9.05745
    x_values = np.arange(100)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    st.snow()


    
  with tab3:
    data2=data['Casos por fecha de toma de muestra']
    st.scatter_chart(data2, color='#00A2E8', size=20, use_container_width=True)

    A = 638.658
    u = 73.265
    r = 9.05745
    x_values = np.arange(100)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab4:
    data3=data['Casos por fecha de emisión de resultados']
    st.scatter_chart(data3, color='#7A1A82', size=20, use_container_width=True)

    A = 423.658
    u = 72.265
    r = 9.05745
    x_values = np.arange(100)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)

  #Lo mismo, pero para la segunda fecha
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Gráficas desde el 13/03/2020 hasta el 15/03/2021</h1>", unsafe_allow_html=True)
  sf = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha_marzo.csv', index_col=1, parse_dates=True)
  tab5, tab6, tab7, tab8 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])
  with tab5:
    #hala los datos
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data4 = sf['Casos por fecha de inicio de síntomas']
    data5 = sf['Casos por fecha de toma de muestra']
    data6 = sf['Casos por fecha de emisión de resultados']
    # Combinación de datos
    combined_data2 = pd.DataFrame({
      'Casos por fecha de inicio de síntomas': data4,
      'Casos por fecha de toma de muestra': data5,
      'Casos por fecha de emisión de resultados': data6
    })
    #muetsra el grafico
    st.scatter_chart(combined_data2, size=20, use_container_width=True)

    A = 1000.2614
    u = 390.7638
    r = 25.8805
    x_values = np.arange(500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab6:
    data4=sf['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data4, color='#00129A', size=20, use_container_width=True)
    
    A = 1915.516
    u = 965.7638
    r = 25.8805
    x_values = np.arange(500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab7:
    data5=sf['Casos por fecha de toma de muestra']
    st.scatter_chart(data5, color='#00A2E8', size=20, use_container_width=True)

    A = 1992.6
    u = 395.638
    r = 25.8805
    x_values = np.arange(500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab8:
    data6=sf['Casos por fecha de emisión de resultados']
    st.scatter_chart(data6, color='#7A1A82', size=20, use_container_width=True)

    A = 950.2614
    u = 388.01
    r = 25.8805
    x_values = np.arange(500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)

  #Lo mismo, pero para la tercera fecha
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Gráficas desde el 13/03/2020 hasta el 07/04/2024</h1>", unsafe_allow_html=True)
  tf = pd.read_csv('https://raw.githubusercontent.com/Herdezdess/LabRedDat/main/confirmados_fecha_todos.csv', index_col=1, parse_dates=True)
  tab9, tab10, tab11, tab12 = st.tabs(["Casos a lo largo del tiempo", "Casos por fecha de inicio de síntomas", "Casos por fecha de toma de muestra", "Casos por fecha de emisión de resultados"])
  with tab9:
    #hala los datos
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data7 = tf['Casos por fecha de inicio de síntomas']
    data8 = tf['Casos por fecha de toma de muestra']
    data9 = tf['Casos por fecha de emisión de resultados']
    # Combinación de datos
    combined_data3 = pd.DataFrame({
      'Casos por fecha de inicio de síntomas': data7,
      'Casos por fecha de toma de muestra': data8,
      'Casos por fecha de emisión de resultados': data9
    })
    #muetsra el grafico
    st.scatter_chart(combined_data3, size=20, use_container_width=True)
    
    A = 354.251
    u = 1425.638
    r = 25.8805
    x_values = np.arange(1500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
  with tab10:
    data7=tf['Casos por fecha de inicio de síntomas']
    st.scatter_chart(data7, color='#00129A', size=20, use_container_width=True)

    A = 108.243
    u = 1422.7638
    r = 25.8805
    x_values = np.arange(1500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab11:
    data8=tf['Casos por fecha de toma de muestra']
    st.scatter_chart(data8, color='#00A2E8', size=20, use_container_width=True)

    A = 295.42
    u = 1422.638
    r = 25.8805
    x_values = np.arange(1500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  with tab12:
    data9=tf['Casos por fecha de emisión de resultados']
    st.scatter_chart(data9, color='#7A1A82', size=20, use_container_width=True)

    A = 521.25
    u = 1430.01
    r = 25.8805
    x_values = np.arange(1500)
    y_values = A * np.exp(-((x_values - u) / r)**2 / 2)
    df = pd.DataFrame({'y': y_values})
    st.line_chart(df)
    
  
    

  
if selected == "Teoría":
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>RESUMEN</h1>", unsafe_allow_html=True)
  st.markdown("""La pandemia del COVID-19 fué uno de los desafíos más grandes a los que la sociedad guatemalteca se ha enfrentado en la historia reciente. Esto no afectó solamente al sector de la salud, sino que fue un problema multifacético el cual afectó principalmente en las siguientes áreas:""")
  st.markdown("""  
    ▶ **Impacto económico y social:** Las medidas de contención tuvieron un impacto significativo en la economía guatemalteca, especialmente en sectore como el turismo, la agricultura y la manufactura. Además, muchos guatemaltecos enfrentaron dificultades económicas debido a la pérdida de empleos y la reducción de ingresos. 
    
    ▶ **Presión sobre el sistema de salud:** El sistema de salud guatemalteco enfrentó desafíos significativos debido al aumento de casos de COVID-19. La falta de recursos, equipos de protección personal y capacidad hospitalaria adecuada se convirtieron en preocupaciones importantes durante los picos de la pandemia. 
    
    ▶ **Desafíos sociales y desigualdades:** La pandemia destacó y exacerbó las desigualdades sociales existentes en Guatemala. Grupos vulnerables, como comunidades indígenas y personas de bajos recursos enfrentaron dificultades adicionales debido a la falta de acceso a servicios de salud adecuados y a condiciones de vida precarias.
    """)
  st.markdown("""La pandemia tuvo un fuerte impacto en cada uno de los puntos vitales de la sociedad en Guatemala. Es por ello que su estudio a lo largo del tiempo es importante. Este laboratorio pretende realizar un estudio posterior para determinar si es posible realizar predicciones acertadas a partir de una cantidas limitada de datos obtenidos durante los ciertos periodos de la pandemia.""")
  st.divider()
  st.markdown("<h1 style='text-align: center; color: #A2BDF1;'>MARCO TEÓRICO</h1>", unsafe_allow_html=True)
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>Distribución binomial</h1>", unsafe_allow_html=True)
  st.markdown("""Este modelo matemático nos da la probabilidad de obtener una cantidad k de casos exitosos en una cantidad de ensayos n. Cada uno de estos intentos tiene una probabilidad de éxito p. La expresión para la distribución binomial es:""")
  st.latex(r''' P(x = k) = \binom{n}{k} p^{k} (1-p)^{n-k} ''')
  st.markdown("""Todo esto permite que la distribución binomial sea utilizada para el estudio del comportamiento de algún fenómeno, proceso u objeto de estudio. Esto quiere decir que nos permite hacer predicciones a partir de un grupo de datos medidos para tener una idea de cómo evolucionará el objeto o fenómeno de estudio, lo cual da cabida a aplicaciones como:""")
  st.markdown("""
    ▶ **Procesos Bernoulli:** La distribución binomial es adecuada para modelar experimentos con dos resultados posibles, como lanzamientos de monedas, pruebas de éxito/fallo, entre otros.
    
    ▶ **Predicciones en investigación y ciencias sociales:** Se utiliza para predecir el número de respuestas afirmativas o negativas en encuestas, votaciones, estudios de mercado, entre otros.
    
    ▶ **Control de calidad:** Permite predecir la cantidad de productos defectuosos en una muestra tomada de una producción de masa.
    
    ▶ **Finanzas:** En la valoración de opciones financieras, la distribución binomial es utilizada para modelar el comportamiento de los precios de las acciones.
    """)
  st.markdown("""A pesar de que la distribución binomial puede llegar a ser de mucha ayuda a la hora de realizar predicciones hay que tomar en cuenta que esta misma tiene ciertas consideraciones y limitaciones a tomar en cuenta.""")
  st.markdown("""
    ▶ La distribución binomial asume que los ensayos son independientes y que la probabilidad de éxito es constante en cada ensayo. Si estas condiciones no se cumplen, otros modelos probabilísticos pueden ser más apropiados.
    
    ▶ En casos donde el número de ensayos (n) es grande, la distribución binomial se aproxima a la distribución normal mediante el teorema del límite central, lo que facilita los cálculos y las interpretaciones.
    """)
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>CASO DE ESTUDIO</h1>", unsafe_allow_html=True)
  st.markdown("""Utilizando los registros de casos de COVID19 del Ministerio de Salud de la República de Guatemala se realizaron gráficas de los datos medidos en dos intervalos de tiempo diferentes. Cada uno de estos intervalos inicia el día en el que se registró el primer caso positivo de COVID19 en Guatemala, es decir, el 13 de marzo de 2020. El primer intervalo toma los datos desde la anterior fecha hasta el 1 de junio de 2020. El segundo caso toma aún más datos, siendo el 15 de marzo de 2021 la fecha límite para la toma de datos. Por último se agregó un tercer rango de fechas, con fecha límite el 7 de abril de 2024.""")
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>PROCEDIMIENTO EXPERIMENTAL</h1>", unsafe_allow_html=True)
  st.markdown("""Para esta práctica, se tomaron los casos de estudio mencionados anteriormente y se utilizó un ajuste hecho a partir de una distribución binomial. También fue necesario el uso de herramientas externas a Python como Gnuplot. Esto debdo a que el ajuste realizado con Python se adapta solamente a los datos tomados y no realiza las predicciones deseadas, por lo cual se utilizó Gnuplot para poder obtener los valores para la disribución binomial y luego plotearla dentro de la gráfica con los datos recopilados. Este ajuste nos permitió dar una estimación de la fecha en la cual se dará el pico de casos positivos para COVID19.""")
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #A2BDF1;'>DISCUSIÓN DE RESULTADOS</h1>", unsafe_allow_html=True)  
  st.markdown("""
    ▶  Durante la realización de los fit correspondientes, se cambiarón los rangos de fechas. Para la segunda gráfica tomamos las fechas desde el 31 de enero del 2021 hasta el 15 de marzo del 2021 y para la tercera gráfica tomamos las fechas desde el 7 de enero del 2024 hasta el 7 de abril del 2024. 
    
    ▶  Lo anterior fue realizado así debido que dichas gráficas ya contienen picos u olas, por lo que estas ya no se comportan como una binomial y no se puede realizar el ajuste en todo el rango de fechas. El nuevo rango de fechas fue elegido de forma que tome todas las fechas de una "ola" para que se comporte como una binomial.
    
    ▶ De la primer gráfica desde la última fecha que tenemos los casos disminuirán. De la segunda vemos que tendremos en promedio (esto se puede ver en la gráfica "Casos a lo largo del tiempo") un valor de 1000 casos para el día 395 (corresponde al 12/04/2021). De la tercera gráfica obtenemos un valor máximo (promedio) de 352 casos por día para el día 1424 (corresponde al 4/02/24). Estos datos corresponden a los picos de las últimas olas.
    
    """)
  st.divider()
  st.markdown("<h2 style='text-align: left; color: #D3BEF1;'>CONCLUSIONES</h1>", unsafe_allow_html=True)  
  st.markdown("""
    ▶ La primera gráfica nos ayuda a ver el comportamiento de los casos de COVID19 a lo largo del tiempo, además de eso, podemos hacer una predicción de lo que pasará; del fit podemos ver que ya obtuvimos un pico en los casos, estos seguirán en disminución.
    
    ▶ El fit de la segunda nos da una predicción de la enfermedad; este nos dice que tendremos un aumento de casos, y para aproximadamente el 12 de abril de 2021 alcanzar el pico de la ola, siendo este aproximadamente 1000 casos. 
    
    ▶ En el fit de la tercera gráfica podemos ver que ya se alcanzó el pico de la ola y los casos estarán en disminución.

    """)
  st.divider()
  st.markdown("<h3 style='text-align: left; color: black;'>Referencias</h1>", unsafe_allow_html=True)
  st.markdown("""  
  **1.** Ministerio de Salud Pública y Asistencia Social. Situación de COVID19 en Guatemala. 
                  
  **2.**   
                
  **3.**   
    """)
  st.divider()
