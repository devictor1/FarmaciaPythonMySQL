import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
  
    # Criação da janela de cadastro
def telaMenu():
    from telaTodosUsuarios import telaTodosUsuarios
    from telaTodosProdutos import telaTodosProdutos
    
    def voltarTela():
        menu_window.destroy() # Fecha a janela de recuperação
        
    menu_window = tk.Tk() # criação da janela
    menu_window.title("Menu Principal") # título da janela
    menu_window.geometry("400x400")
    
   
    tk.Button(menu_window, text="Ver todos os usuarios", command=telaTodosUsuarios).grid(row=2, column=2,) # criação do botão de mostrar todos e sua localização na grid
    tk.Button(menu_window, text="Ver todos os produtos", command=telaTodosProdutos).grid(row=3, column=2,) # criação do botão de edição e sua localização na grid
    tk.Button(menu_window, text="Voltar", command=voltarTela).grid(row=6, column=2,) # criação do botão de exclusão e sua localização na grid
    
    menu_window.mainloop()