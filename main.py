import streamlit as st
import pandas as pd
import plotly.express as px
df = pd.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')
grafico01 = px.pie(df, names= 'Linguagem')
grafico02 = px.bar(df, color='Linguagem', x='Linguagem', y='Desenvolvedores')
st.title('Gráfico de Liguagens!')
st.plotly_chart(grafico01)
st.plotly_chart(grafico02)


st.dataframe(df)

Escolha  = st.selectbox('Qual a sua maneira de contato ideal:',['telefone','email','outros'])

st.write(Escolha)

botao = st.button('Pressione o Botão!')

st.write(botao)

linguagem = st.selectbox("Selecione a linguagem desejada!",df['Linguagem'].unique())

if st.button('Filtrar'):
    df.loc[df['Linguagem'] == linguagem]

