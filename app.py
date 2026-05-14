import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise de Dados de Veículos')

car_data = pd.read_csv('vehicles.csv')

st.write('Abaixo você pode ver os primeiros dados do arquivo:')
st.dataframe(car_data.head())

st.subheader('Visualizações por Botões')

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para o conjunto de dados')
    fig = px.scatter(car_data, x="odometer", y="price", title="Preço vs Quilometragem (Odometer)")
    st.plotly_chart(fig, use_container_width=True)


st.subheader('Visualizações por Caixas de Seleção')

build_histogram = st.checkbox('Exibir Histograma')
build_scatter = st.checkbox('Exibir Gráfico de Dispersão')

if build_histogram:
    st.write('Exibindo Histograma via Checkbox:')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Exibindo Gráfico de Dispersão via Checkbox:')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
