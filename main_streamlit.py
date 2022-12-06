import streamlit as st
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt 
# import plotly.express as px

url = 'https://raw.githubusercontent.com/albertsl/datasets/master/popularidad/temporal.csv'

df = pd.read_csv(url)


with st.sidebar:
    st.header('Escolha sua visualização')
    option = st.radio("Tipo de plot", ('Line', 'Area','Bar', 'Pie'))

st.header('Dados')
st.dataframe(df.head())

if option=='Line':
    st.subheader('Plot Line')
    st.line_chart(data=df,
            x='Mes')
elif option=='Area':
    st.subheader('Plot Area')
    st.area_chart(data=df,
            x='Mes')

elif option=='Bar':
    st.subheader('Plot Bar')
    st.bar_chart(data=df,
            x='Mes')

# elif option=='Pie':
#     x = ['a','b','c','d','e','f']
#     y = [45,67,32,20,23,78]

#     fig = px.pie(
#         df,
#         values='data science',
#         names='categorical',
#         # title='Pizza Frango com Catupiry',
#         # color_discrete_sequence= px.colors.sequential.Oranges
#     )
#     st.plotly_chart(fig)
