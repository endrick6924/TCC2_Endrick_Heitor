import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('luxury_cars.db')
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS carros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXT NOT NULL,
        ano INTEGER NOT NULL,
        cor TEXT,
        preco REAL NOT NULL,
        quilometragem INTEGER,
        status TEXT
    )
    ''')
    conexao.commit()
    conexao.close()

def cadastrar_carro(marca, modelo, ano, cor, preco, quilometragem, status):
    conexao = sqlite3.connect('luxury_cars.db')
    cursor = conexao.cursor()
    cursor.execute('''
    INSERT INTO carros (marca, modelo, ano, cor, preco, quilometragem, status)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (marca, modelo, ano, cor, preco, quilometragem, status))
    conexao.commit()
    conexao.close()

def listar_carros():
    conexao = sqlite3.connect('luxury_cars.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM carros')
    carros = cursor.fetchall()
    conexao.close()
    return carros

def atualizar_carro(id_carro, marca, modelo, ano, cor, preco, quilometragem, status):
    conexao = sqlite3.connect('luxury_cars.db')
    cursor = conexao.cursor()
    cursor.execute('''
    UPDATE carros
    SET marca = ?, modelo = ?, ano = ?, cor = ?, preco = ?, quilometragem = ?, status = ?
    WHERE id = ?
    ''', (marca, modelo, ano, cor, preco, quilometragem, status, id_carro))
    conexao.commit()
    conexao.close()

def excluir_carro(id_carro):
    conexao = sqlite3.connect('luxury_cars.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM carros WHERE id = ?', (id_carro,))
    conexao.commit()
    conexao.close()