import sqlite3
import requests
from datetime import datetime

API_KEY = "133cb52fe8b008bcec7338ee7a9f2303"  # Substitua pela sua chave real

# --- Criar banco e tabela ---
conn = sqlite3.connect("clima.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS historico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cidade TEXT,
    temperatura REAL,
    descricao TEXT,
    data_hora TEXT
)
""")
conn.commit()
conn.close()

# --- Função para salvar histórico ---
def salvar_historico(cidade, temperatura, descricao):
    conn = sqlite3.connect("clima.db")
    cursor = conn.cursor()
    data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO historico (cidade, temperatura, descricao, data_hora) VALUES (?, ?, ?, ?)",
        (cidade, temperatura, descricao, data_hora)
    )
    conn.commit()
    conn.close()

# --- Função para buscar clima ---
def buscar_clima(cidade):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            dados = resposta.json()
            temperatura = dados['main']['temp']
            descricao = dados['weather'][0]['description']
            print(f"Clima em {cidade}: {temperatura}°C, {descricao}")
            salvar_historico(cidade, temperatura, descricao)
        elif resposta.status_code == 401:
            print("Erro: Chave da API inválida. Verifique sua API_KEY.")
        elif resposta.status_code == 404:
            print("Erro: Cidade não encontrada. Verifique a grafia.")
        else:
            print(f"Erro {resposta.status_code}: {resposta.text}")
    except requests.exceptions.RequestException as e:
        print("Erro na requisição:", e)

# --- Execução principal ---
cidade = input("Digite o nome da cidade: ")
buscar_clima(cidade)
