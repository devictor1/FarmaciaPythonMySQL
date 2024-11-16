import mysql.connector
from ttkbootstrap import Style
from ttkbootstrap.constants import *
from ttkbootstrap import Label, Entry, Button
from tkinter import messagebox
from telaRecuperarSenha import telaRecuperarSenha
from telaRegistro import telaRegistro
from telaMenu import telaMenu

def conectar_bd():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='farmaciaflamingo'
    )

def telaLogin():
    def limparCampos():
        entry_usuario.delete(0, END)  # limpar campo de usuario
        entry_senha.delete(0, END)  # limpar campo de senha

    def validarLogin():
        usuario = entry_usuario.get()
        senha = entry_senha.get()
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND senha = %s", (usuario, senha))  # Seleciona o usuario
        resultado = cursor.fetchone()  # pega somente um usuario
        if resultado:
            messagebox.showinfo("Sucesso!", "Login realizado com sucesso!")
            conexao.close()
            login_window.destroy()
            telaMenu()
        else:
            messagebox.showerror("Erro", "Usuario ou senha não encontrado!")
            conexao.close()
            limparCampos()

    # Placeholder para Usuario
    def focusInUsuario(event):
        if entry_usuario.get() == 'iniciaisAAAAMMDD':
            entry_usuario.delete(0, END)  # Limpa o campo

    def focusOutUsuario(event):
        if entry_usuario.get() == '':
            entry_usuario.insert(0, 'iniciaisAAAAMMDD')  # placeholder

    # Placeholder para Senha
    def focusInSenha(event):
        if entry_senha.get() == 'Senha de até 30 caracteres':
            entry_senha.delete(0, END)  # Limpa o campo

    def focusOutSenha(event):
        if entry_senha.get() == '':
            entry_senha.insert(0, 'Senha de até 30 caracteres')  # placeholder

    # Initialize the TTK Bootstrap window
    login_window = Style().master  
    login_window.geometry("400x300")
    login_window.title("Login")  # Título da janela

    Label(login_window, text="Farmácia Flamingo", font="Helvetica", bootstyle="info").grid(row=0, column=2, pady=10)

    Label(login_window, text="Usuario").grid(row=1, column=1)  # label para usuario
    entry_usuario = Entry(login_window, width=30)  # campo de entrada
    entry_usuario.grid(row=1, column=2)  # localização do campo de entrada
    entry_usuario.bind('<FocusIn>', focusInUsuario)  # função para quando o campo é focado
    entry_usuario.bind('<FocusOut>', focusOutUsuario)  # função para quando o campo perde o foco
    entry_usuario.insert(0, 'iniciaisAAAAMMDD')  # placeholder
    
    Label(login_window, text="Senha").grid(row=2, column=1)  # label para senha
    entry_senha = Entry(login_window, show='*', width=30)  # campo de entrada
    entry_senha.grid(row=2, column=2)  # localização do campo de entrada
    entry_senha.bind('<FocusIn>', focusInSenha)  # função para quando o campo é focado
    entry_senha.bind('<FocusOut>', focusOutSenha)  # função para quando o campo perde o foco
    entry_senha.insert(0, 'Senha de até 30 caracteres')  # placeholder

    Button(login_window, text="Registrar", command=telaRegistro, bootstyle="success").grid(row=3, column=1, pady=10)
    Button(login_window, text="Esqueci minha senha", command=telaRecuperarSenha, bootstyle="warning").grid(row=3, column=2, pady=10)
    Button(login_window, text="Entrar", command=validarLogin, bootstyle="primary").grid(row=3, column=3, pady=10)

    login_window.mainloop()  # inicia a janela de login