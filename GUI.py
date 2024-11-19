import tkinter as tk 
#creamos ventana principal con tk
window = tk.Tk()
window.title("Título")
window.geometry("400x300")

def funcionSaludar():
    lblTexto.config(text="Hola " + entNombre.get())

def funcionDespedir():
    lblDesp.config(text="Adiós " + entNombre.get())

lblTitiulo=tk.Label(window, text="primer programa")
lblTitiulo.pack(pady=40)

LblNombre=tk.Label(window, text="introduce tu nombre")
LblNombre.pack()

entNombre=tk.Entry(window)
entNombre.pack()

BtnSaludo=tk.Button(window, text="NO ME PULSES", command=funcionSaludar)
BtnSaludo.pack()

lblTexto=tk.Label(window, text="")
lblTexto.pack()

BtnBye=tk.Button(window, text="QUE NO ME PULSES", command=funcionDespedir)
BtnBye.pack()

lblDesp=tk.Label(window, text="")
lblDesp.pack()

#Hace que no se cierre el programa y esté siempre en ejecución
window.mainloop()