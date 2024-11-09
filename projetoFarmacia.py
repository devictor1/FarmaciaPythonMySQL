import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

def conectar_bd():
    return mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='root',
    database='farmaciaflamingo'
)

# Criação da janela de login
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
            # Função para esconder o placeholder quando o campo de entrada está em foco
            if entry_email.get() == 'Senha de até 30 caracteres':
                entry_email.delete(0, tk.END)  # Limpa o campo
                entry_email.config(fg='black')  # Restaura a cor do texto
        def focusOutSenha(event):
            # Função para mostrar o placeholder quando o campo de entrada está vazio
            if entry_email.get() == '':
                entry_email.insert(0, 'Senha de até 30 caracteres') # placeholder
                entry_email.config(fg='grey') # Cor do texto do placeholder

        def limparCampos():
            entry_usuario.delete(0, tk.END) # limpar campo de usuario
            entry_nome.delete(0, tk.END) # limpar campo de nome
            entry_email.delete(0, tk.END) # limpar campo de email
            entry_senha.delete(0, tk.END) # limpar campo de senha

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
            messagebox.showinfo("Sucesso!", "Cadastro realizado com sucesso!")
            limparCampos()

        registro_window = tk.Tk() # criação da janela
        registro_window.title("Farmácia") # título da janela

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

        tk.Button(registro_window, text="Voltar").grid(row=5, column=0, pady=10)
        tk.Button(registro_window, text="Cadastrar", command=registrar).grid(row=5, column=1, pady=10)

        registro_window.mainloop()



def abrir_tela_login():
    def limparCampos():
            entry_usuario.delete(0, tk.END) # limpar campo de usuario
            entry_senha.delete(0, tk.END) # limpar campo de senha

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
            abrir_tela_cadastro()
        else:
            messagebox.showerror("Erro", "Usuario ou senha não encontrado!")
            conexao.close()
            limparCampos()

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
        # Função para esconder o placeholder quando o campo de entrada está em foco
        if entry_senha.get() == 'Senha de até 30 caracteres':
            entry_senha.delete(0, tk.END)  # Limpa o campo
            entry_senha.config(fg='black')  # Restaura a cor do texto
    def focusOutSenha(event):
        # Função para mostrar o placeholder quando o campo de entrada está vazio
        if entry_senha.get() == '':
            entry_senha.insert(0, 'Senha de até 30 caracteres') # placeholder
            entry_senha.config(fg='grey') # Cor do texto do placeholder

    login_window = tk.Tk()
    login_window.geometry("300x300")
    tk.Label(login_window, text="Login Farmácia Flamingo", font="Helvetica").grid(row=0, column=2)
      # Campo para inserir o usuário
    tk.Label(login_window, text="Usuario").grid(row=6, column=1)  # label para usuario
    entry_usuario = tk.Entry(login_window, width=30) # campo de entrada
    entry_usuario.grid(row=6, column=2) # localização do campo de entrada
    entry_usuario.bind('<FocusIn>', focusInUsuario) # função para quando o campo é focado
    entry_usuario.bind('<FocusOut>', focusOutUsuario) # função para quando o campo perde o foco
    entry_usuario.insert(0, 'iniciaisAAAAMMDD') # placeholder
    entry_usuario.config(fg='grey') # cor do placeholder
      # Campo para inserir a senha
    tk.Label(login_window, text="Senha").grid(row=7, column=1)  # label para usuario
    entry_senha = tk.Entry(login_window, width=30) # campo de entrada
    entry_senha.grid(row=7, column=2) # localização do campo de entrada
    entry_senha.bind('<FocusIn>', focusInSenha) # função para quando o campo é focado
    entry_senha.bind('<FocusOut>', focusOutSenha) # função para quando o campo perde o foco
    entry_senha.insert(0, 'Senha de até 30 caracteres') # placeholder
    entry_senha.config(fg='grey') # cor do placeholder

    tk.Button(login_window, text="Registrar", command=telaRegistro).grid(row=9, column=1, pady=10)
    tk.Button(login_window, text="Esqueci minha senha", command=telaRecuperarSenha).grid(row=9, column=2, pady=10)
    tk.Button(login_window, text="Entrar", command=validarLogin).grid(row=9, column=3, pady=10)

    login_window.title("Login") # Título da janela
    login_window.mainloop() # inicia a janela de login

def telaRecuperarSenha():
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
        def recuperarSenha():
            usuario = entry_usuario.get()
            email = entry_email.get()
            conexao = conectar_bd()
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND email = %s", (usuario, email)) # Seleciona o usuario
            resultado = cursor.fetchone() # pega somente um usuario
            if resultado:
                cursor.execute("SELECT senha FROM usuario WHERE usuario = %s AND email = %s", (usuario, email))
                senha = cursor.fetchone()
                messagebox.showinfo("Sucesso!", senha)
                conexao.close()
                recovery_window.destroy()
                abrir_tela_login()
            else:
                messagebox.showerror("Erro", "Usuario ou email não encontrado!")
                conexao.close()

        recovery_window = tk.Tk()
        recovery_window.title("Recuperar Senha")
        recovery_window.geometry("300x300")
        tk.Label(recovery_window, text="Recupere sua senha!", font="Helvetica").grid(row=0, column=2)

        tk.Label(recovery_window, text="Seu usuário:").grid(row=6, column=1)  # label para usuario
        entry_usuario = tk.Entry(recovery_window, width=30) # campo de entrada
        entry_usuario.grid(row=6, column=2) # localização do campo de entrada
        entry_usuario.bind('<FocusIn>', focusInUsuario) # função para quando o campo é focado
        entry_usuario.bind('<FocusOut>', focusOutUsuario) # função para quando o campo perde o foco
        entry_usuario.insert(0, 'iniciaisAAAAMMDD') # placeholder
        entry_usuario.config(fg='grey') # cor do placeholder

        tk.Label(recovery_window, text="Seu e-mail:").grid(row=7, column=1)  # label para usuario
        entry_email = tk.Entry(recovery_window, width=30) # campo de entrada
        entry_email.grid(row=7, column=2) # localização do campo de entrada
        entry_email.bind('<FocusIn>', focusInEmail) # função para quando o campo é focado
        entry_email.bind('<FocusOut>', focusOutEmail) # função para quando o campo perde o foco
        entry_email.insert(0, 'exemplo@dominio.com') # placeholder
        entry_email.config(fg='grey') # cor do placeholder

        tk.Button(recovery_window, text="Recuperar", command=recuperarSenha).grid(row=9, column=2, pady=10)

        recovery_window.mainloop()
    


    # Criação da janela de cadastro
def abrir_tela_cadastro():
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

    # Placeholder para Senha
    def focusInSenha(event):
        # Função para esconder o placeholder quando o campo de entrada está em foco
        if entry_senha.get() == 'Senha de até 30 caracteres':
            entry_senha.delete(0, tk.END)  # Limpa o campo
            entry_senha.config(fg='black')  # Restaura a cor do texto
    def focusOutSenha(event):
        # Função para mostrar o placeholder quando o campo de entrada está vazio
        if entry_senha.get() == '':
            entry_senha.insert(0, 'Senha de até 30 caracteres') # placeholder
            entry_senha.config(fg='grey') # Cor do texto do placeholder

    def cadastrar():
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
        messagebox.showinfo("Sucesso!", "Cadastro realizado com sucesso!")
        limparCampos()

        # Função para mostrar todos os registros
    def mostrar_todos():
        tree.delete(*tree.get_children()) # limpa os registros mostrados anteriormente
        conexao = conectar_bd() # conectar com o Banco de Dados
        cursor = conexao.cursor() # criar um cursor que executa os comandos MySQL
        cursor.execute("select * from usuario") # execução do comando
        registros = cursor.fetchall() # coletar todos os registros
        for registro in registros:
            tree.insert('', 'end', values=registro)
        conexao.close() # fechar conexão
        
        # Função para selecionar registros
    def selecionar_registro(event):
        print(f"Registro selecionado")  # Debug
        selected_item = tree.selection()  # Selecionar o registro
        if selected_item:  # Verifica se algum item está selecionado
            registro = tree.item(selected_item)['values']  # Coletar os valores do registro
            entry_usuario.delete(0, tk.END)
            entry_usuario.insert(0, registro[1])  # Usuario
            entry_nome.delete(0, tk.END)
            entry_nome.insert(0, registro[2])  # Nome
            entry_email.delete(0, tk.END)
            entry_email.insert(0, registro[3])  # E-mail
            entry_senha.delete(0, tk.END)
            entry_senha.insert(0, registro[4])  # Senha

        # Função para editar registros
    def editar():
        selected_item = tree.selection() # selecionar usuario
        if not selected_item:  # Verifica se algum item está selecionado
            messagebox.showwarning("Atenção!", "Nenhum registro selecionado para editar.")
            return
        id_usuario = tree.item(selected_item)['values'][0] # coletar a ID do usuário escolhido
        usuario = entry_usuario.get() # coletar login do usuario
        nome = entry_nome.get() # coletar nome do usuário
        email = entry_email.get() # coletar e-mail
        senha =  entry_senha.get() # coletar senha    
        conexao =  conectar_bd() # conectar com o Banco de Dados
        cursor = conexao.cursor() # criar um cursor que executa os comandos MySQL
        dados = (usuario, nome, email, senha, id_usuario) # coletando os dados
        cursor.execute("UPDATE usuario SET usuario = %s, nome = %s, email = %s, senha = %s WHERE id = %s", dados) # criação do botão e sua localização
        conexao.commit() # confirmação da edição
        conexao.close() # fechamento da conexão
        messagebox.showinfo("Sucesso!","Registro atualizado com sucesso!") # mensagem confirmando a alteração
        limparCampos() # chamando função que limpa os campos de entrada usados
        mostrar_todos()

        # Função para excluir registros
    def excluir():
        selected_item = tree.selection()[0] # selecionar usuario
        id_usuario = tree.item(selected_item)['values'][0] # coletar a ID do usuário escolhido
        conexao = conectar_bd() # conectar com o Banco de Dados
        cursor = conexao.cursor() # criar um cursor que executa os comandos MySQL
        cursor.execute("DELETE FROM usuario WHERE id = %s", (id_usuario,)) # executando o script SQL
        conexao.commit() # confirmação da edição
        conexao.close() # fechamento da conexão
        tree.delete(selected_item) # deletar o registro selecionado
        messagebox.showinfo("Sucesso!","Registro excluido com sucesso!") # mensagem confirmando a exclusão
        limparCampos() # chamando função que limpa os campos de entrada usados

        # Função para limpar os campos de entrada
    def limparCampos():
        entry_usuario.delete(0, tk.END) # limpar campo de usuario
        entry_nome.delete(0, tk.END) # limpar campo de nome
        entry_email.delete(0, tk.END) # limpar campo de email
        entry_senha.delete(0, tk.END) # limpar campo de senha
        focusOutEmail()
        focusOutNome()
        focusOutSenha()
        focusOutUsuario()

    cadastro_window = tk.Tk() # criação da janela
    cadastro_window.title("Farmácia") # título da janela

    tk.Label(cadastro_window, text="Nome").grid(row=0, column=1) # label para nome
    entry_nome = tk.Entry(cadastro_window, width=30) # campo de entrada
    entry_nome.grid(row=0, column=2) # localização do campo de entrada
    entry_nome.bind('<FocusIn>', focusInNome) # função para quando o campo é focado
    entry_nome.bind('<FocusOut>', focusOutNome) # função para quando o campo perde o foco
    entry_nome.insert(0, 'Nome Sobrenome') # placeholder
    entry_nome.config(fg='grey') # cor do placeholder

    tk.Label(cadastro_window, text="Usuario").grid(row=1, column=1)  # label para usuario
    entry_usuario = tk.Entry(cadastro_window, width=30) # campo de entrada
    entry_usuario.grid(row=1, column=2) # localização do campo de entrada
    entry_usuario.bind('<FocusIn>', focusInUsuario) # função para quando o campo é focado
    entry_usuario.bind('<FocusOut>', focusOutUsuario) # função para quando o campo perde o foco
    entry_usuario.insert(0, 'iniciaisAAAAMMDD') # placeholder
    entry_usuario.config(fg='grey') # cor do placeholder

    tk.Label(cadastro_window, text="E-mail").grid(row=2, column=1) # label para e-mail
    entry_email = tk.Entry(cadastro_window, width=30) # campo de entrada
    entry_email.grid(row=2, column=2) # localização do campo de entrada
    entry_email.bind('<FocusIn>', focusInEmail) # função para quando o campo é focado
    entry_email.bind('<FocusOut>', focusOutEmail) # função para quando o campo perde o foco
    entry_email.insert(0, 'exemplo@dominio.com') # placeholder
    entry_email.config(fg='grey') # cor do placeholder

    tk.Label(cadastro_window, text="Senha").grid(row=3, column=1) # label para senha
    entry_senha = tk.Entry(cadastro_window, width=30) # campo de entrada
    entry_senha.grid(row=3, column=2) # localização do campo de entrada
    entry_senha.bind('<FocusIn>', focusInSenha) # função para quando o campo é focado
    entry_senha.bind('<FocusOut>', focusOutSenha) # função para quando o campo perde o foco
    entry_senha.insert(0, 'Senha de até 30 caracteres') # placeholder
    entry_senha.config(fg='grey') # cor do placeholder
    
    # Botões para realizar as ações
    tk.Button(cadastro_window, text="Limpar Campos", command=limparCampos).grid(row=4, column=2, pady=10) # criação do botão para limpar os inputs
    tk.Button(cadastro_window, text="Cadastrar", command=cadastrar).grid(row=5, column=0, pady=10) # criação do botão de cadastro e sua localização na grid
    tk.Button(cadastro_window, text="Mostrar Todos", command=mostrar_todos).grid(row=5, column=1, pady=10) # criação do botão de mostrar todos e sua localização na grid
    tk.Button(cadastro_window, text="Editar", command=editar).grid(row=5, column=2, pady=10) # criação do botão de edição e sua localização na grid
    tk.Button(cadastro_window, text="Excluir", command=excluir).grid(row=5, column=3, pady=10) # criação do botão de exclusão e sua localização na grid

    # Criar a tabela de usuários
    columns = ("ID", "Nome", "Data de Nascimento", "E-mail", "Telefone") # definindo as colunas
    tree = ttk.Treeview(cadastro_window, columns=columns, show="headings") # criando a tabela com as colunas definidas
    for col in columns: # criando as colunas
        tree.heading(col, text=col) # definindo seus nomes
    tree.grid(row=6, column=0, columnspan=4) # definindo a grid
    tree.bind('<<TreeviewSelect>>', selecionar_registro) # seleciona registro sempre que clica em um na grid
    
    cadastro_window.mainloop() # iniciando a janela DE CADASTRO

abrir_tela_login()