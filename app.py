import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Vehiculos entre 2018 y 2019')

st.write('Informe Financiero')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos    
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir grafico de dispersion') # crear un botón

if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de dispersion')
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)