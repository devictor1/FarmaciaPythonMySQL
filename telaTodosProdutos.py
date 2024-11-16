import mysql.connector
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def telaTodosProdutos():
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
           messagebox.showwarning("Atenção!", "Nenhum registro selecionado para.")
           return
        
        # Função para abrir a janela de edição
        edit_window = tk.Toplevel(todosProdutos_window)  # Criar nova janela
        edit_window.title("Editar Produto")  # Título da nova janela

        # Campos de entrada para edição
        entry_nome = tk.Entry(edit_window)
        entry_nome.grid(row=0, column=1, padx=10, pady=5)
        entry_quantidade = tk.Entry(edit_window)
        entry_quantidade.grid(row=1, column=1, padx=10, pady=5)
        entry_preco = tk.Entry(edit_window)
        entry_preco.grid(row=2, column=1, padx=10, pady=5)
        
        # Labels para os campos de entrada
        tk.Label(edit_window, text="Nome:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(edit_window, text="Quantidade:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(edit_window, text="Preço:").grid(row=2, column=0, sticky=tk.W)

        if selected_item:  # Se um item estiver selecionado, preencher os campos
            registro = tree.item(selected_item)['values']
            entry_nome.insert(0, registro[1])  # Produto
            entry_quantidade.insert(0, registro[2])  # Quantidade
            entry_preco.insert(0, registro[3])  # Preço


        def salvar():
            nome = entry_nome.get()  # coletar nome do usuário
            quantidade = entry_quantidade.get()  # coletar e-mail
            preco = entry_preco.get()  # coletar senha    
            conexao = conectar_bd()  # conectar com o Banco de Dados
            if conexao:
                cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
                if selected_item:  # Se um item estiver selecionado, atualizar
                    id_produto = tree.item(selected_item)['values'][0]  # coletar a ID do usuário escolhido
                    dados = (nome, quantidade, preco, id_produto)  # coletando os dados
                    cursor.execute("UPDATE produto SET nome = %s, quantidade = %s, preco = %s WHERE id = %s", dados)  # atualização
                    messagebox.showinfo("Sucesso!", "Registro atualizado com sucesso!")  # mensagem confirmando a alteração
                else:  # Caso contrário, inserir novo registro
                    dados = (nome, quantidade, preco)
                    cursor.execute("INSERT INTO produto (nome, quantidade, preco) VALUES (%s, %s, %s)", dados)  # inserção
                    messagebox.showinfo("Sucesso!", "Registro adicionado com sucesso!")  # mensagem confirmando a inserção
                conexao.commit()  # confirmação da edição
                conexao.close()  # fechamento da conexão
                carregarProdutos()  # recarregar a janela
                edit_window.destroy()  # Fechar a janela de edição
            
        # Função para voltar
        def voltar():
            edit_window.destroy()
            
        # Botão para voltar
        tk.Button(edit_window, text="Voltar", command=voltar).grid(row=4, column=1, pady=10)
            
        # Botão para salvar as alterações
        tk.Button(edit_window, text="Salvar", command=salvar).grid(row=4, column=1, pady=10)
        
    def addProd(selected_item=None):
                
        # Função para abrir a janela de criação
        addProd_window = tk.Toplevel(todosProdutos_window)  # Criar nova janela
        addProd_window.title("Editar Produto")  # Título da nova janela

        # Campos de entrada para edição
        entry_nome = tk.Entry(addProd_window)
        entry_nome.grid(row=0, column=1, padx=10, pady=5)
        entry_quantidade = tk.Entry(addProd_window)
        entry_quantidade.grid(row=1, column=1, padx=10, pady=5)
        entry_preco = tk.Entry(addProd_window)
        entry_preco.grid(row=2, column=1, padx=10, pady=5)
        
        # Labels para os campos de entrada
        tk.Label(addProd_window, text="Nome:").grid(row=0, column=0, sticky=tk.W)
        tk.Label(addProd_window, text="Quantidade:").grid(row=1, column=0, sticky=tk.W)
        tk.Label(addProd_window, text="Preço:").grid(row=2, column=0, sticky=tk.W)

        if selected_item:  # Se um item estiver selecionado, preencher os campos
            registro = tree.item(selected_item)['values']
            entry_nome.insert(0, registro[1])  # Produto
            entry_quantidade.insert(0, registro[2])  # Quantidade
            entry_preco.insert(0, registro[3])  # Preço


        def salvar():
            nome = entry_nome.get()  # coletar nome do usuário
            quantidade = entry_quantidade.get()  # coletar e-mail
            preco = entry_preco.get()  # coletar senha    
            conexao = conectar_bd()  # conectar com o Banco de Dados
            if conexao:
                cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
                if selected_item:  # Se um item estiver selecionado, atualizar
                    id_produto = tree.item(selected_item)['values'][0]  # coletar a ID do usuário escolhido
                    dados = (nome, quantidade, preco, id_produto)  # coletando os dados
                    cursor.execute("UPDATE produto SET nome = %s, quantidade = %s, preco = %s WHERE id = %s", dados)  # atualização
                    messagebox.showinfo("Sucesso!", "Registro atualizado com sucesso!")  # mensagem confirmando a alteração
                else:  # Caso contrário, inserir novo registro
                    dados = (nome, quantidade, preco)
                    cursor.execute("INSERT INTO produto (nome, quantidade, preco) VALUES (%s, %s, %s)", dados)  # inserção
                    messagebox.showinfo("Sucesso!", "Registro adicionado com sucesso!")  # mensagem confirmando a inserção
                conexao.commit()  # confirmação da edição
                conexao.close()  # fechamento da conexão
                carregarProdutos()  # recarregar a janela
                addProd_window.destroy()  # Fechar a janela de edição
            
        # Função para voltar
        def voltar():
            addProd_window.destroy()
            
        # Botão para voltar
        tk.Button(addProd_window, text="Voltar", command=voltar).grid(row=4, column=1, pady=10)
            
        # Botão para salvar as alterações
        tk.Button(addProd_window, text="Salvar", command=salvar).grid(row=4, column=1, pady=10)
        

    def excluir():
        selected_item = tree.selection()  # selecionar produto
        if not selected_item:  # Verifica se algum item está selecionado
            messagebox.showwarning("Atenção!", "Nenhum registro selecionado para excluir.")
            return
        id_produto = tree.item(selected_item)['values'][0]  # coletar a ID do usuário escolhido
        conexao = conectar_bd()  # conectar com o Banco de Dados
        if conexao:
            cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
            cursor.execute("DELETE FROM produto WHERE id = %s", (id_produto,))  # executando o script SQL
            conexao.commit()  # confirmação da edição
            conexao.close()  # fechamento da conexão
            tree.delete(selected_item)  # deletar o registro selecionado
            messagebox.showinfo("Sucesso!", "Registro excluído com sucesso!")  # mensagem confirmando a exclusão

    def carregarProdutos():
        tree.delete(*tree.get_children())  # limpa os registros mostrados anteriormente
        conexao = conectar_bd()  # conectar com o Banco de Dados
        if conexao:
            cursor = conexao.cursor()  # criar um cursor que executa os comandos MySQL
            cursor.execute("SELECT * FROM produto")  # execução do comando
            registros = cursor.fetchall()  # coletar todos os registros
            for registro in registros:
                tree.insert('', 'end', values=registro)
            conexao.close()  # fechar conexão

    # Criação da janela
    todosProdutos_window = tk.Tk()  # criação da janela
    todosProdutos_window.title("Cadastro de Produtos")  # título da janela

    # Criar a tabela de produtos
    columns = ("ID", "Nome", "Quantidade", "Preço")  # definindo as colunas
    tree = ttk.Treeview(todosProdutos_window, columns=columns, show="headings")  # criando a tabela com as colunas definidas
    for col in columns:  # criando as colunas
        tree.heading(col, text=col)  # definindo seus nomes
    tree.grid(row=0, column=0, columnspan=3)  # definindo a grid
    tree.bind('<<TreeviewSelect>>', selecionarRegistro)  # seleciona registro sempre que clica em um na grid

    # Botões de ação
    tk.Button(todosProdutos_window, text="Adicionar Produto", command=lambda: addProd()).grid(row=1, column=0, pady=5)
    tk.Button(todosProdutos_window, text="Excluir", command=excluir).grid(row=1, column=1, pady=5)
    tk.Button(todosProdutos_window, text="Editar", command=lambda: editar(selected_item=tree.selection())).grid(row=1, column=2, pady=5)

    # Carregar produtos ao iniciar a janela
    carregarProdutos()

    todosProdutos_window.mainloop()