import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

globos = st.button('lanzar los globos')

if globos:
    st.balloons()

#st.set_page_config(page_title ='App Arturo',page_icon =':shark:')
#st.set_page_config(page_title='App de Arturo', page_icon= '🧊')

st.sidebar.image('../1-Numpy/img/numpy.png')
st.sidebar.image('https://imagenes.t13.cl/images/original/2018/01/1515518836-perro.jpg')

#st.stop() #deja de ejecutar todo lo de abajo

col1, col2, col3, col4 = st. columns(4)

with col1:
    st.markdown('# Lorem ipsum')
with col2: 
    st.markdown('# Dolor')
with col3:
    st.markdown('# Sit amet')
with col4:
    st.markdown('# Probando')


df = pd.read_csv('red_recarga_acceso_publico _2021.csv', sep=';')

distrito = st.text_input ('Introduce un distrito')


lista_distritos = df ['DISTRITO'].unique()
distrito2 = st.selectbox ('Elige un distrito', lista_distritos)

st.dataframe(df[df['DISTRITO']== distrito2])

st.write('Hola mundo')



df = df[['DISTRITO', 'DIRECCION']]


st.dataframe(df)

st.metric('Temperatura', 19,4)

df = px.data.tips()
fig = px.histogram(df, x="total_bill")
#fig.show()

#Plotly
st.plotly_chart(fig)

boton = st.button('Haz click')

if boton:
    st.writen('Heclicado')
else:
    st.write('No he clicado')

st.markdown ('Como te encuentras hoy?')

humor = st.radio('Humos',('Contento','Triste', 'Enfadado'))

if humor == 'Contento':
    st.write('¡Que bien!')
elif humor == 'Triste':
    st.write ('¡Tomate un cafe!')
else:
    st.write ('¡Tomate una tila!')