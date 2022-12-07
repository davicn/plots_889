import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


url = 'https://raw.githubusercontent.com/albertsl/datasets/master/popularidad/temporal.csv'
df = pd.read_csv(url)

df1 = pd.read_csv('/c/Users/davi.nascimento/OneDrive - COMPASSO TECNOLOGIA LTDA/Documentos/Ada/turma_889/aula_streamlit/br.csv')

st.header('Trabalhando com Gráficos')

st.subheader('Line')
st.line_chart(
    data=df,
    x='Mes',
    width=900,
    height=400
)

st.subheader('Área')
st.area_chart(
    data=df,
    x='Mes'
)

st.subheader('Barra')
st.bar_chart(
    data=df,
    x='Mes'
)

st.subheader('Matplotlib')
a = [1,4,2,6,5,4,7]

fig1, ax = plt.subplots()
ax.plot(a)
st.pyplot(fig1)

st.subheader('Plotly')
fig2 = px.line(
    df,
    x='Mes',
    y='data science'
)

st.plotly_chart(fig2)

st.subheader('Map')

df1 = df1.loc[:,['lat','lng']]
df1.columns = ['lat','lon']

st.map(df1)



