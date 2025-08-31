import pandas as pd

df = pd.read_csv('livros.csv')

print("Média:", df['Preco'].mean())
print("Mediana:", df['Preco'].median())
print("Mínimo:", df['Preco'].min())
print("Máximo:", df['Preco'].max())
print("Desvio padrão:", df['Preco'].std())

print('Top 10 livros mais caros: ')
print(df.sort_values(by='Preco', ascending=False).head(10))

print('\nTop 10 livros mais baratos: ')
print(df.sort_values(by='Preco', ascending=True).head(10))
