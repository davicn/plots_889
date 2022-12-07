
import streamlit as st
import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import plotly.express as px


url = 'https://raw.githubusercontent.com/albertsl/datasets/master/popularidad/temporal.csv'
df = pd.read_csv(url)

with st.sidebar:
    option = st.radio(
        "Selecione o tipo de gráfico",
        ("Line", "Área", "Barra")
    )
    

st.header('Dados')

if option=='Line':
    st.subheader('Line')
    st.line_chart(
        data=df,
        x='Mes',
    )

elif option=='Área':
    st.subheader('Área')
    st.area_chart(
        data=df,
        x='Mes'
    )
    
elif option=='Barra':
    st.subheader('Barra')
    st.bar_chart(
        data=df,
        x='Mes'
    )
