class Transporte:
    def __init__(self, carro=None, moto=None, bicicleta=None):
        self.carro = carro
        self.moto = moto
        self.bicicleta = bicicleta

    def mover(self):
        if self.carro:
            print(f"o {self.carro} está se movendo rápido demais.")
        if self.moto:
            print(f"a {self.moto} está prestes a quebrar.")
        if self.bicicleta:
            print(f"a {self.bicicleta} está rápida, pois está trocando a marcha.")

if __name__ == "__main__":
    transporte = Transporte(carro="carro", moto="moto", bicicleta="bicicleta")
    transporte.mover()

    carro = Transporte(carro="carro")
    moto = Transporte(moto="moto")
    bicicleta = Transporte(bicicleta="bicicleta")

    carro.mover()
    moto.mover()
    bicicleta.mover()