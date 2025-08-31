import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

for i in range(1,51):
    url = f'https://books.toscrape.com/catalogue/page-{i}.html'

    response = requests.get(url)
    arquivo_existe = os.path.exists('livros.csv')

    with open('livros.csv', mode='a', encoding='utf-8') as file:

        if not arquivo_existe:
            file.write('Titulo,Preco\n')

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            # Pegando todos os produtos

            livros = soup.find_all('article', class_='product_pod')

            for livro in livros:
                titulo = livro.h3.a['title']
                preco = livro.find('p', class_='price_color').text
                valor = float(preco.replace('Â£', '').strip())
                
                data = f'"{titulo}",{valor}\n'

                file.write(data)
        else:
            print('Erro ao acessar o site: ', response.status_code)
        
