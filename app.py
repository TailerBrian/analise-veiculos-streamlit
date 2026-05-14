import streamlit as st
import pandas as pd

st.header('Análise de Dados de Veículos')

df = pd.read_csv('vehicles.csv')

st.write('Abaixo pode ver os primeiros dados do ficheiro:')
st.dataframe(df.head())