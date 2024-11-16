import mysql.connector
import tkinter as tk
from tkinter import messagebox

def conectar_bd():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='root',
        database='farmaciaflamingo'
    )



def telaRecuperarSenha():
    # Placeholder para Usuario
    def focusInUsuario(event):
        if entry_usuario.get() == 'iniciaisAAAAMMDD':
            entry_usuario.delete(0, tk.END)
            entry_usuario.config(fg='black')

    def focusOutUsuario(event):
        if entry_usuario.get() == '':
            entry_usuario.insert(0, 'iniciaisAAAAMMDD')
            entry_usuario.config(fg='grey')

    # Placeholder para Email
    def focusInEmail(event):
        if entry_email.get() == 'exemplo@dominio.com':
            entry_email.delete(0, tk.END)
            entry_email.config(fg='black')

    def focusOutEmail(event):
        if entry_email.get() == '':
            entry_email.insert(0, 'exemplo@dominio.com')
            entry_email.config(fg='grey')

    def recuperarSenha():
        usuario = entry_usuario.get()
        email = entry_email.get()
        conexao = conectar_bd()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND email = %s", (usuario, email))
        resultado = cursor.fetchone()
        if resultado:
            cursor.execute("SELECT senha FROM usuario WHERE usuario = %s AND email = %s", (usuario, email))
            senha = cursor.fetchone()
            messagebox.showinfo("Sucesso!", f"Sua senha é: {senha[0]}")
            conexao.close()
            recovery_window.destroy()  # Fecha a janela de recuperação
        else:
            messagebox.showerror("Erro", "Usuário ou email não encontrado!")
            
            
    def voltarTela():
        recovery_window.destroy() # Fecha a janela de recuperação

    recovery_window = tk.Tk()
    recovery_window.title("Recuperar Senha")
    recovery_window.geometry("400x300")
    tk.Label(recovery_window, text="Recupere sua senha!", font="Helvetica").grid(row=0, column=2)

    tk.Label(recovery_window, text="Seu usuário:").grid(row=6, column=1)
    entry_usuario = tk.Entry(recovery_window, width=30)
    entry_usuario.grid(row=6, column=2)
    entry_usuario.bind('<FocusIn>', focusInUsuario)
    entry_usuario.bind('<FocusOut>', focusOutUsuario)
    entry_usuario.insert(0, 'iniciaisAAAAMMDD')
    entry_usuario.config(fg='grey')

    tk.Label(recovery_window, text="Seu e-mail:").grid(row=7, column=1)
    entry_email = tk.Entry(recovery_window, width=30)
    entry_email.grid(row=7, column=2)
    entry_email.bind('<FocusIn>', focusInEmail)
    entry_email.bind('<FocusOut>', focusOutEmail)
    entry_email.insert(0, 'exemplo@dominio.com')
    entry_email.config(fg='grey')

    tk.Button(recovery_window, text="Voltar", command=voltarTela).grid(row=9, column=1, pady=10)
    tk.Button(recovery_window, text="Recuperar", command=recuperarSenha).grid(row=9, column=2, pady=10)

    recovery_window.mainloop()