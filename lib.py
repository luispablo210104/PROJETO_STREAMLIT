import pandas as pd

dicionario = {
    "Matricula": [1,2,3],
    "pessoas": ["Fulano", "Ciclano", "Deltrano"],
    'Notas': [8, 10, 8]
}
df = pd.DataFrame(dicionario)

filtro = df.loc[(df['Notas'] == 8) | (df['pessoas'] == "Fulano")]
print(filtro)
df = pd.DataFrame(dicionario)

filtro = df.loc[(df['Notas'] == 8) | (df['pessoas'] == "Fulano")]
print(filtro)



filtro = df.loc[(df['Curso'] == 'FullStack')]
idade = df.loc[(df['Idade'] >= 18) & (df["Idade"] <= 30)]
curso = df.loc[(df['Curso'] >= "Metaverso") | (df["Curso"] == "Desing")]
matricula = df.loc[df["Matricula"] == 3]
print(filtro)
print(idade)
print(curso)
print(matricula)