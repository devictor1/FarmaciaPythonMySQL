import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import *

def conectar_bd():
    return mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='farmaciaflamingo'
)

# Criação da janela de registros de credenciais

def telaRegistro():

        # Funções de placeholder
        # Placeholder para Email
        def focusInEmail(event):
            # Função para esconder o placeholder quando o campo de entrada está em foco
            if entry_email.get() == 'exemplo@dominio.com':
                entry_email.delete(0, tk.END)  # Limpa o campo
                entry_email.config(fg='black')  # Restaura a cor do texto
        def focusOutEmail(event):
            # Função para mostrar o placeholder quando o campo de entrada está vazio
            if entry_email.get() == '':
                entry_email.insert(0, 'exemplo@dominio.com') # placeholder
                entry_email.config(fg='grey') # Cor do texto do placeholder

        # Placeholder para Nome
        def focusInNome(event):
        # Função para esconder o placeholder quando o campo de entrada está em foco
            if entry_nome.get() == 'Nome Sobrenome': # se estiver com o placeholder 
                entry_nome.delete(0, tk.END)  # Limpa o campo
                entry_nome.config(fg='black')  # Restaura a cor do texto
        def focusOutNome(event):
            #Função para mostrar o placeholder quando o campo de entrada está vazio
            if entry_nome.get() == '': # se estiver vazio
                entry_nome.insert(0, 'Nome Sobrenome') # placeholder
                entry_nome.config(fg='grey') # Cor do texto do placeholder

        # Placeholder para Usuario
        def focusInUsuario(event):
            # Função para esconder o placeholder quando o campo de entrada está em foco
            if entry_usuario.get() == 'iniciaisAAAAMMDD':
                entry_usuario.delete(0, tk.END)  # Limpa o campo
                entry_usuario.config(fg='black')  # Restaura a cor do texto
        def focusOutUsuario(event):
            # Função para mostrar o placeholder quando o campo de entrada está vazio
            if entry_usuario.get() == '':
                entry_usuario.insert(0, 'iniciaisAAAAMMDD') # placeholder
                entry_usuario.config(fg='grey') # Cor do texto do placeholder

        # Placeholder para Email
        def focusInSenha(event):
            if entry_senha.get() == 'Senha de até 30 caracteres':
                entry_senha.delete(0, tk.END)  # Limpa o campo
                entry_senha.config(fg='black')  # Restaura a cor do texto

        def focusOutSenha(event):
            if entry_senha.get() == '':
                entry_senha.insert(0, 'Senha de até 30 caracteres')  # placeholder
                entry_senha.config(fg='grey')  # Cor do texto do placeholder

        def limparCampos():
            entry_usuario.delete(0, tk.END) # limpar campo de usuario
            entry_nome.delete(0, tk.END) # limpar campo de nome
            entry_email.delete(0, tk.END) # limpar campo de email
            entry_senha.delete(0, tk.END) # limpar campo de senha

        def voltarTela():
            registro_window.destroy()  # Fecha a janela de recuperação

        def registrar():
        # Preparando os campos de entrada
            usuario = entry_usuario.get() # recebe o usuario
            nome = entry_nome.get() # recebe o nome
            email = entry_email.get() # recebe o email
            senha =  entry_senha.get() # recebe a senha
            conexao = conectar_bd()
            cursor = conexao.cursor()
            dados = (usuario, nome, email, senha)
            cursor.execute("INSERT INTO usuario (usuario, nome, email, senha) VALUES (%s,%s,%s,%s)", dados)
            conexao.commit()
            conexao.close()
            if dados:
                messagebox.showinfo("Sucesso", "Registro realizado com sucesso!")
                limparCampos()
            else:
                messagebox.showinfo("Falha!", "Registro não realizado!!")
                limparCampos()

        registro_window = tk.Tk() # criação da janela
        registro_window.title("Novo Funcionário") # título da janela
        registro_window.geometry("400x300")

        tk.Label(registro_window, text="Nome").grid(row=0, column=1) # label para nome
        entry_nome = tk.Entry(registro_window, width=30) # campo de entrada
        entry_nome.grid(row=0, column=2) # localização do campo de entrada
        entry_nome.bind('<FocusIn>', focusInNome) # função para quando o campo é focado
        entry_nome.bind('<FocusOut>', focusOutNome) # função para quando o campo perde o foco
        entry_nome.insert(0, 'Nome Sobrenome') # placeholder
        entry_nome.config(fg='grey') # cor do placeholder

        tk.Label(registro_window, text="Usuario").grid(row=1, column=1)  # label para usuario
        entry_usuario = tk.Entry(registro_window, width=30) # campo de entrada
        entry_usuario.grid(row=1, column=2) # localização do campo de entrada
        entry_usuario.bind('<FocusIn>', focusInUsuario) # função para quando o campo é focado
        entry_usuario.bind('<FocusOut>', focusOutUsuario) # função para quando o campo perde o foco
        entry_usuario.insert(0, 'iniciaisAAAAMMDD') # placeholder
        entry_usuario.config(fg='grey') # cor do placeholder

        tk.Label(registro_window, text="E-mail").grid(row=2, column=1) # label para e-mail
        entry_email = tk.Entry(registro_window, width=30) # campo de entrada
        entry_email.grid(row=2, column=2) # localização do campo de entrada
        entry_email.bind('<FocusIn>', focusInEmail) # função para quando o campo é focado
        entry_email.bind('<FocusOut>', focusOutEmail) # função para quando o campo perde o foco
        entry_email.insert(0, 'exemplo@dominio.com') # placeholder
        entry_email.config(fg='grey') # cor do placeholder

        tk.Label(registro_window, text="Senha").grid(row=3, column=1) # label para senha
        entry_senha = tk.Entry(registro_window, width=30) # campo de entrada
        entry_senha.grid(row=3, column=2) # localização do campo de entrada
        entry_senha.bind('<FocusIn>', focusInSenha) # função para quando o campo é focado
        entry_senha.bind('<FocusOut>', focusOutSenha) # função para quando o campo perde o foco
        entry_senha.insert(0, 'Senha de até 30 caracteres') # placeholder
        entry_senha.config(fg='grey') # cor do placeholder

        tk.Button(registro_window, text="Voltar", command=voltarTela).grid(row=5, column=0, pady=10)
        tk.Button(registro_window, text="Cadastrar", command=registrar).grid(row=5, column=1, pady=10)

        registro_window.mainloop()