import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


url = 'https://raw.githubusercontent.com/albertsl/datasets/master/popularidad/temporal.csv'
df = pd.read_csv(url)

st.header('Trabalhando com Widgets')


st.subheader('Button')
result = st.button("Clique")

if result==True:
    st.write('Clicou')
else:
    st.write('Ainda não Clicou')

st.subheader('selectbox')
option = st.selectbox(
    'Selecione a coluna',
    df.columns)

st.subheader('multiselect')
options = st.multiselect(
    'Selecione as colunas',
    df.columns
)


ops = st.radio(
    'Selecione as colunas',
    df.columns

)

st.write('Opção: ',ops)
aux = df.loc[:,options]
# st.write('You selected:', option)

st.dataframe(aux)

try:
    st.subheader('Line')
    st.line_chart(
        data=aux,
        x='Mes'
    )
except:
    st.write('Não vai plotar')


