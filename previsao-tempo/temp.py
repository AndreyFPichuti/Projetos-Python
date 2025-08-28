import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

conn = sqlite3.connect('clima.db')
cursor = conn.cursor()

cursor.execute('SELECT cidade, temperatura, data_hora FROM historico ORDER BY id DESC LIMIT 10')
dados = cursor.fetchall()
conn.close()

if dados:
    cidades = [linha[0] for linha in dados]
    temperaturas = [linha[1] for linha in dados]
    datas = [linha[2] for linha in dados]

    plt.figure(figsize=(10,5))
    plt.plot(cidades, temperaturas, marker='o', linestyle='-', color='blue')
    plt.title("Últimas temperaturas registradas")
    plt.xlabel("Cidades")
    plt.ylabel("Temperatura (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print('Não há dados no histórico.')