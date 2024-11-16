import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def telaTodosUsuarios():
    def conectar_bd():
        try:
            return mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='root',
                database='farmaciaflamingo'
            )
        except mysql.connector.Error as err:
            messagebox.showerror("Erro de Conexão", f"Erro: {err}")
            return None

    def selecionarRegistro(event):
        selected_item = tree.selection()  # Selecionar o registro
        

    def editar(selected_item=None):
        if not selected_item:  # Verifica se algum item está selecionado
           messagebox.showwarning("Atenção!", "Nenhum registro selecionado para editar.")
           return
        # Função para abrir a janela de edição
        edit_window = tk.Toplevel(todosUsuarios_window)  # Criar nova janela
        edit_window.title("Editar Usuario")  # Título da nova janela

        # Campos de entrada para edição
        entry_usuario = tk.Entry(edit_window)
        entry_usuario.grid(row=0, column=1, padx=10, pady=5)
        entry_nome = tk.Entry(edit_window)
        entry_nome.grid(row=1, column=1, padx=10, pady=5)
        entry_email = tk.Entry(edit_window)
        entry_email.grid(row=2, column=1, padx=10, pady=5)
        
        # Labels para os campos de entrada
        tk.Label(edit_window, text="Usuário:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(edit_window, text="Nome:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(edit_window, text="E-mail:").grid(row=2, column=0, sticky=tk.W)

        if selected_item:  # Se um item estiver selecionado, preencher os campos
            registro = tree.item(selected_item)['values']
            entry_usuario.insert(0, registro[1]) # Usuario
            entry_nome.insert(0, registro[2]) # Nome
            entry_email.insert(0, registro[3]) # E-mail


        def salvar():
            usuario = entry_usuario.get().strip()  # coletar usuário
            nome = entry_nome.get().strip()  # coletar nome
            email = entry_email.get().strip()  # coletar email

            # Verificar se os campos estão vazios
            if not usuario or not nome or not email:
                messagebox.showwarning("Atenção!", "Todos os campos devem ser preenchidos.")
                return

            conexao = conectar_bd()  # conectar com o Banco de Dados
            if conexao:
                cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
                try:
                    if selected_item:  # Se um item estiver selecionado, atualizar
                        id_usuario = tree.item(selected_item)['values'][0]  # coletar a ID do usuário escolhido
                        dados = (usuario, nome, email, id_usuario)  # coletando os dados
                        cursor.execute("UPDATE usuario SET usuario = %s, nome = %s, email = %s WHERE id = %s", dados)  # atualização
                        messagebox.showinfo("Sucesso!", "Registro atualizado com sucesso!")  # mensagem confirmando a alteração
                    else:  # Caso contrário, inserir novo registro
                        dados = (usuario, nome, email)
                        cursor.execute("INSERT INTO usuario (usuario, nome, email) VALUES (%s, %s, %s)", dados)  # inserção
                        messagebox.showinfo("Sucesso!", "Registro adicionado com sucesso!")  # mensagem confirmando a inserção
                    
                    conexao.commit()  # confirmação da edição
                except mysql.connector.Error as err:
                    messagebox.showerror("Erro", f"Erro ao salvar: {err}")
                finally:
                    conexao.close()  # fechamento da conexão
                    carregarUsuarios()  # recarregar a janela
                    edit_window.destroy()  # Fechar a janela de edição
            
        # Função para voltar
        def voltar():
            edit_window.destroy()
        
        # Botão para voltar
        tk.Button(edit_window, text="Voltar", command=voltar).grid(row=4, column=0, pady=5)  
            
        # Botão para salvar as alterações
        tk.Button(edit_window, text="Salvar", command=salvar).grid(row=4, column=1, pady=5)
        
    def addUser(selected_item=None):
        # Função para abrir a janela de edição
        addUser_window = tk.Toplevel(todosUsuarios_window)  # Criar nova janela
        addUser_window.title("Adicionar Usuário")  # Título da nova janela

        # Campos de entrada para adição
        entry_usuario = tk.Entry(addUser_window)
        entry_usuario.grid(row=0, column=1, padx=10, pady=5)
        entry_nome = tk.Entry(addUser_window)
        entry_nome.grid(row=1, column=1, padx=10, pady=5)
        entry_email = tk.Entry(addUser_window)
        entry_email.grid(row=2, column=1, padx=10, pady=5)
        entry_senha = tk.Entry(addUser_window)
        entry_senha.grid(row=3, column=1, padx=10, pady=5)
        
        # Labels para os campos de entrada
        tk.Label(addUser_window, text="Usuário:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(addUser_window, text="Nome:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(addUser_window, text="E-mail:").grid(row=2, column=0, sticky=tk.W)
        tk.Label(addUser_window, text="Senha:").grid(row=3, column=0, sticky=tk.W)
        

        if selected_item:  # Se um item estiver selecionado, preencher os campos
            registro = tree.item(selected_item)['values']
            entry_usuario.insert(0, registro[1]) # Usuario
            entry_nome.insert(0, registro[2]) # Nome
            entry_email.insert(0, registro[3]) # E-mail
            entry_senha.insert(0, registro[4])

        def salvar():
            usuario = entry_usuario.get().strip() # coletar usuário
            nome = entry_nome.get().strip() # coletar nome
            email = entry_email.get().strip() # coletar email
            senha = entry_senha.get().strip() # coletar senha

            # Verificar se os campos estão vazios
            if not usuario or not nome or not email or not senha:
                messagebox.showwarning("Atenção!", "Todos os campos devem ser preenchidos.")
                return

            conexao = conectar_bd()  # conectar com o Banco de Dados
            if conexao:
                cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
                try:
                    if selected_item:  # Se um item estiver selecionado, atualizar
                        id_usuario = tree.item(selected_item)['values'][0]  # coletar a ID do usuário escolhido
                        dados = (usuario, nome, email, senha, id_usuario)  # coletando os dados
                        cursor.execute("UPDATE usuario SET usuario = %s, nome = %s, email = %s, senha = %s WHERE id = %s", dados)  # atualização
                        messagebox.showinfo("Sucesso!", "Registro atualizado com sucesso!")  # mensagem confirmando a alteração
                    else:  # Caso contrário, inserir novo registro
                        dados = (usuario, nome, email, senha)
                        cursor.execute("INSERT INTO usuario (usuario, nome, email, senha) VALUES (%s, %s, %s, %s)", dados)  # inserção
                        messagebox.showinfo("Sucesso!", "Registro adicionado com sucesso!")  # mensagem confirmando a inserção
                    
                    conexao.commit()  # confirmação da edição
                except mysql.connector.Error as err:
                    messagebox.showerror("Erro", f"Erro ao salvar: {err}")
                finally:
                    conexao.close()  # fechamento da conexão
                    carregarUsuarios()  # recarregar a janela
                    addUser_window.destroy()  # Fechar a janela de edição
            
        # Função para voltar
        def voltar():
            addUser_window.destroy()
        
        # Botão para voltar
        tk.Button(addUser_window, text="Voltar", command=voltar).grid(row=4, column=0, pady=5)  
            
        # Botão para salvar as alterações
        tk.Button(addUser_window, text="Salvar", command=salvar).grid(row=4, column=1, pady=5)

    def excluir():
        selected_item = tree.selection()  # selecionar Usuario
        if not selected_item:  # Verifica se algum item está selecionado
            messagebox.showwarning("Atenção!", "Nenhum registro selecionado para excluir.")
            return
        id_usuario = tree.item(selected_item)['values'][0]  # coletar a ID do usuário escolhido
        conexao = conectar_bd()  # conectar com o Banco de Dados
        if conexao:
            cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
            cursor.execute("DELETE FROM usuario WHERE id = %s", (id_usuario,))  # executando o script SQL
            conexao.commit()  # confirmação da edição
            conexao.close()  # fechamento da conexão
            tree.delete(selected_item)  # deletar o registro selecionado
            messagebox.showinfo("Sucesso!", "Registro excluído com sucesso!")  # mensagem confirmando a exclusão

    def carregarUsuarios():
        tree.delete(*tree.get_children())  # limpa os registros mostrados anteriormente
        conexao = conectar_bd()  # conectar com o Banco de Dados
        if conexao:
            cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
            cursor.execute("SELECT * FROM usuario")  # execução do comando
            registros = cursor.fetchall()  # coletar todos os registros
            for registro in registros:
                tree.insert('', 'end', values=registro)
            conexao.close()  # fechar conexão

    # Criação da janela
    todosUsuarios_window = tk.Tk()  # criação da janela
    todosUsuarios_window.title("Cadastro de Usuarios")  # título da janela

    # Criar a tabela de Usuarios
    columns = ("ID", "Usuario", "Nome", "E-mail")  # definindo as colunas
    tree = ttk.Treeview(todosUsuarios_window, columns=columns, show="headings")  # criando a tabela com as colunas definidas
    for col in columns:  # criando as colunas
        tree.heading(col, text=col)  # definindo seus usuarios
    tree.grid(row=0, column=0, columnspan=3)  # definindo a grid
    tree.bind('<<TreeviewSelect>>', selecionarRegistro)  # seleciona registro sempre que clica em um na grid

    # Botões de ação
    tk.Button(todosUsuarios_window, text="Adicionar Usuario", command=lambda: addUser()).grid(row=1, column=0, pady=5)
    tk.Button(todosUsuarios_window, text="Excluir", command=excluir).grid(row=1, column=1, pady=5)
    tk.Button(todosUsuarios_window, text="Editar", command=lambda: editar(selected_item=tree.selection())).grid(row=1, column=2, pady=5)

    # Carregar Usuarios ao iniciar a janela
    carregarUsuarios()

    todosUsuarios_window.mainloop()