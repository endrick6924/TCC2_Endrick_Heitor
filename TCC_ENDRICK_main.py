import tkinter as tk
from tkinter import ttk, messagebox
import database

def listar():
    for item in tabela.get_children():
        tabela.delete(item)
    carros = database.listar_carros()
    for carro in carros:
        tabela.insert("", tk.END, values=(carro[0], carro[1], carro[2], carro[3], carro[5], carro[7]))

def limpar_campos():
    for entry in entradas.values():
        entry.delete(0, tk.END)
    tabela.selection_remove(tabela.selection())

def cadastrar():
    dados = [entry.get().strip() for entry in entradas.values()]
    
    if not dados[0] or not dados[1] or not dados[2] or not dados[4]:
        messagebox.showerror("Erro", "Marca, Modelo, Ano e Preço são obrigatórios.")
        return

    try:
        ano = int(dados[2])
        preco = float(dados[4].replace(",", "."))
        quilometragem = int(dados[5]) if dados[5] else 0
    except ValueError:
        messagebox.showerror("Erro", "Ano e Quilometragem devem ser números inteiros, e Preço deve ser um número válido.")
        return

    database.cadastrar_carro(dados[0], dados[1], ano, dados[3], preco, quilometragem, dados[6])
    limpar_campos()
    listar()

def selecionar(event):
    item_selecionado = tabela.selection()
    if not item_selecionado:
        return
    dados = tabela.item(item_selecionado[0], 'values')
    
    entradas['marca'].delete(0, tk.END)
    entradas['marca'].insert(0, dados[1])
    entradas['modelo'].delete(0, tk.END)
    entradas['modelo'].insert(0, dados[2])
    entradas['ano'].delete(0, tk.END)
    entradas['ano'].insert(0, dados[3])
    entradas['preco'].delete(0, tk.END)
    entradas['preco'].insert(0, dados[4])

def atualizar():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Selecione um carro para atualizar.")
        return
    id_carro = tabela.item(item_selecionado[0], 'values')[0]
    dados = [entry.get().strip() for entry in entradas.values()]
    
    if not dados[0] or not dados[1] or not dados[2] or not dados[4]:
        messagebox.showerror("Erro", "Marca, Modelo, Ano e Preço são obrigatórios.")
        return

    try:
        ano = int(dados[2])
        preco = float(dados[4].replace(",", "."))
        quilometragem = int(dados[5]) if dados[5] else 0
    except ValueError:
        messagebox.showerror("Erro", "Ano e Quilometragem devem ser números inteiros, e Preço deve ser um número válido.")
        return

    database.atualizar_carro(id_carro, dados[0], dados[1], ano, dados[3], preco, quilometragem, dados[6])
    limpar_campos()
    listar()

def excluir():
    item_selecionado = tabela.selection()
    if not item_selecionado:
        messagebox.showerror("Erro", "Selecione um carro para excluir.")
        return
    id_carro = tabela.item(item_selecionado[0], 'values')[0]
    database.excluir_carro(id_carro)
    limpar_campos()
    listar()

janela = tk.Tk()
janela.title("Luxury Cars - Sistema de Estoque")
janela.geometry("800x600")

entradas = {}

campos = [
    ("marca", "Marca:"),
    ("modelo", "Modelo:"),
    ("ano", "Ano:"),
    ("cor", "Cor:"),
    ("preco", "Preço (R$):"),
    ("quilometragem", "Quilometragem (km):"),
    ("status", "Status (Novo/Seminovo):")
]

for i, (chave, label_text) in enumerate(campos):
    tk.Label(janela, text=label_text).grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = tk.Entry(janela, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    entradas[chave] = entry

frame_botoes = tk.Frame(janela)
frame_botoes.grid(row=len(campos), column=0, columnspan=2, pady=15)

tk.Button(frame_botoes, text="Cadastrar", command=cadastrar).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Atualizar", command=atualizar).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Excluir", command=excluir).pack(side=tk.LEFT, padx=5)
tk.Button(frame_botoes, text="Limpar Campos", command=limpar_campos).pack(side=tk.LEFT, padx=5)

colunas = ("ID", "Marca", "Modelo", "Ano", "Preço", "Status")
tabela = ttk.Treeview(janela, columns=colunas, show="headings", height=8)

tabela.heading("ID", text="ID")
tabela.heading("Marca", text="Marca")
tabela.heading("Modelo", text="Modelo")
tabela.heading("Ano", text="Ano")
tabela.heading("Preço", text="Preço")
tabela.heading("Status", text="Status")

tabela.column("ID", width=40, anchor=tk.CENTER)
tabela.column("Marca", width=120, anchor=tk.W)
tabela.column("Modelo", width=150, anchor=tk.W)
tabela.column("Ano", width=60, anchor=tk.CENTER)
tabela.column("Preço", width=100, anchor=tk.E)
tabela.column("Status", width=100, anchor=tk.CENTER)

tabela.grid(row=len(campos)+1, column=0, columnspan=2, padx=10, pady=10)

tabela.bind("<<TreeviewSelect>>", selecionar)

database.criar_tabela()
listar()

janela.mainloop()