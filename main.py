import streamlit as st
import pandas as pd

st.header('Olá,Mundos!')

st.write('''
''')

df = pd.read_csv('https://raw.githubusercontent.com/hermeson883/data_science_workshop/main/linguagens.csv')

st.dataframe(df)

Escolha  = st.selectbox('Qual a sua maneira de contato ideal:',['telefone','email','outros'])

st.write(Escolha)

botao = st.button('Pressione o Botão!')

st.write(botao)

linguagem = st.selectbox("Selecione a linguagem desejada!",df['Linguagem'].unique())

if st.button('Filtrar'):
    df.loc[df['Linguagem'] == linguagem]

