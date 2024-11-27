class Coche:
    def __init__(self, modelo, cvs, precio, parMotor, traccion):
        self.modelo=modelo
        self.cvs=cvs
        self.precio=precio
        self.parMotor=parMotor
        self.traccion=traccion
        self.kilometros=0
        

    def actualizarkms(self, kms):
        self.kilometros = self.kilometros + kms

    global cont


class CocheElectrico(Coche):
    def __init__(self, modelo, cvs, precio, parMotor, traccion, bateria):
        Coche.__init__(self, modelo, cvs, precio, parMotor, traccion)
        self.bateria=bateria

class CocheCombustible(Coche):
    def __init__(self, modelo, cvs, precio, parMotor, traccion, cilindrada):
        Coche.__init__(self, modelo, cvs, precio, parMotor, traccion)
        self.cilindrada=cilindrada

