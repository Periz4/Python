import tkinter as tk 

class Coche:
    def __init__(self, modelo, cvs, precio, parMotor, traccion, cilindrada):
        self.modelo=modelo
        self.cvs=cvs
        self.precio=precio
        self.parMotor=parMotor
        self.traccion=traccion
        self.cilindrada=cilindrada


cohce1=Coche("daciaDuster", 135, 19000, 240, "delantera", "I3")


window = tk.Tk()
window.title("Mi concesionario")
window.geometry("400x300")

lblTitulo=tk.Label(window, text="Concesionario San Alberto")
lblTitulo.pack()

class Coche:
    modelo=str







window.mainloop()