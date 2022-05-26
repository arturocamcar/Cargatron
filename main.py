import pandas as pd
import streamlit as st
import functions as ft

st.set_page_config(layout='wide')

pagina = st.sidebar.selectbox('Pagina',('Home','Datos','Filtros'))

df = None

if pagina == 'Home':
    ft.home()
elif pagina =='Datos':
    df = ft.datos()
elif pagina =='Filtros':
    df = ft.filtros()






