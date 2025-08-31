import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('livros.csv')

# Definindo faixa de preços

faixas = [0, 15, 25, 40, 50, df['Preco'].max()]
labels = ['0-15', '15-25', '25-40', '40-50', '50+']

df['Faixa'] = pd.cut(df['Preco'], bins=faixas, labels=labels, include_lowest=True)

contagem = df['Faixa'].value_counts().sort_index()

grafico = contagem.plot(kind='bar', color='skyblue')
plt.xlabel('Faixa de Preço')
plt.ylabel('Quantidade de Livros')
plt.title('Distribuição de Preço dos Livros')


# Adicionando o número exato de livros correspondente em cada faixa

for i, v in enumerate(contagem):
    grafico.text(i, v + 0.5, str(v), ha='center', va='bottom')

plt.show()

# Agora, livros mais caros

top_livros = df.sort_values(by='Preco', ascending=False).head(10)

top_livros.plot(kind='barh', x='Titulo', y='Preco', color='salmon', legend=False)
plt.xlabel('Preço')
plt.ylabel('Título do Livro')
plt.title('Top 10 livros mais caros')
plt.show()