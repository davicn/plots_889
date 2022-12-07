import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('iris.csv')

st.header('Trabalhando com dados')

st.subheader('Dataframe')
st.dataframe(data=df)

st.subheader('Table')
st.table(data=df.head())

st.subheader('Json')
d = [{
    "nome": "Davi",
    "notas": [4.5, 7, 10],
    "aprovado":True
}, {
    "nome": "Davi",
    "notas": [4.5, 7, 10],
    "aprovado":True
}]
st.json(body=d)

st.subheader('Metric')
st.metric(
    label="Minha métrica",
    value=80,
    delta="100%"
)
