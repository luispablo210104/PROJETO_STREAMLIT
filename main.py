import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')
grafico01 = px.pie(df, names= 'Linguagem')
grafico02 = px.bar(df, color='Linguagem', x='Linguagem', y='Desenvolvedores')
st.title('Gráfico de Liguagens!')
st.plotly_chart(grafico01)
st.plotly_chart(grafico02)
