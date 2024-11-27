import tkinter as tk 

from coche import Coche
from coche import CocheElectrico
from coche import CocheCombustible

def siguienteCoche():

    if Coche.cont < len(listaCoches)-1:
        Coche.cont=Coche.cont + 1
    else:
        Coche.cont=0

    lblModeloData.config(text=listaCoches[Coche.cont].modelo)
    lblcvsData.config(text=listaCoches[Coche.cont].cvs)
    lblPrecioData.config(text=listaCoches[Coche.cont].precio)
    lblparMotorData.config(text=listaCoches[Coche.cont].parMotor)
    lblTraccionData.config(text=listaCoches[Coche.cont].traccion)
    lblCilindradaData.config(text=listaCoches[Coche.cont].cilindrada)
    lblKmsData.config(text=listaCoches[Coche.cont].kilometros)
    entSumarKms.delete(0, tk.END)
    
def actualizarkms():
    listaCoches[Coche.cont].actualizarkms(int(entSumarKms.get()))
    lblKmsData.config(text=listaCoches[Coche.cont].kilometros)



coche1=CocheCombustible("daciaDuster", 135, 19000, 240, "Delantera", "I3")
coche2=CocheCombustible("rangeRoverSV", 635, 237000, 800, "Total", "V8")
coche3=CocheCombustible("mercedesAMGGt63S", 639, 228443, 900, "Total", "V8")
coche4=CocheCombustible("renaultClio", 101, 17300, 170, "Delantera", "I3")
coche5=CocheCombustible("cupraFormentor", 333, 56090, 420, "Total", "I4")
coche6=CocheElectrico("teslaModelSPlaid", 1020, 107990, 1200, "Total", "Panasonic")
Coche.cont=0

listaCoches=[coche1, coche2, coche3, coche4, coche5, coche6]

window = tk.Tk()
window.title("Mi concesionario")
window.geometry("400x300")

lblTitulo=tk.Label(window, text="Concesionario San Alberto")
lblTitulo.pack()

frmInfoCoches=tk.Frame(window)
frmInfoCoches.pack()

lblModelo=tk.Label(frmInfoCoches, text="Modelo: ")
lblModelo.grid(column="1", row="1")
lblModeloData=tk.Label(frmInfoCoches, text=listaCoches[0].modelo)
lblModeloData.grid(column="2", row="1")

lblcvs=tk.Label(frmInfoCoches, text="Caballos: ")
lblcvs.grid(column="1", row="2")
lblcvsData=tk.Label(frmInfoCoches, text=listaCoches[0].cvs)
lblcvsData.grid(column="2", row="2")

lblprecio=tk.Label(frmInfoCoches, text="Precio: ")
lblprecio.grid(column="1", row="3")
lblPrecioData=tk.Label(frmInfoCoches, text=listaCoches[0].precio)
lblPrecioData.grid(column="2", row="3")

lblparMotor=tk.Label(frmInfoCoches, text="Par Motor: ")
lblparMotor.grid(column="1", row="4")
lblparMotorData=tk.Label(frmInfoCoches, text=listaCoches[0].parMotor)
lblparMotorData.grid(column="2", row="4")

lblTraccion=tk.Label(frmInfoCoches, text="Tracción: ")
lblTraccion.grid(column="1", row="5")
lblTraccionData=tk.Label(frmInfoCoches, text=listaCoches[0].traccion)
lblTraccionData.grid(column="2", row="5")

"""lblCilindrada=tk.Label(frmInfoCoches, text="Cilindrada: ")
lblCilindrada.grid(column="1", row="6")
lblCilindradaData=tk.Label(frmInfoCoches, text=listaCoches[0].cilindrada)
lblCilindradaData.grid(column="2", row="6")"""

lblKilometros=tk.Label(frmInfoCoches, text="Kiómetros:")
lblKilometros.grid(column="1", row="7")
lblKmsData = tk.Label(frmInfoCoches, text=listaCoches[0].kilometros)
lblKmsData.grid(column="2", row="7")

frmBotones=tk.Frame(window, padx=20, pady=20)
frmBotones.pack()

btnSumarKms = tk.Button(frmBotones, text="Añadir kms", command=actualizarkms)
entSumarKms = tk.Entry(frmBotones, width=10)
entSumarKms.insert(0, "0")
btnSumarKms.grid(column="1", row="2")
entSumarKms.grid(column="2", row="2")

btnSiguenteCoche=tk.Button(window, text=("Siguiente"), command=siguienteCoche)
btnSiguenteCoche.pack()



window.mainloop()