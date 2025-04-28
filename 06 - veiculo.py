class Veiculo:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("seu veículo acaba de ligar!")

    def acelerar(self):
        print("seu veículo está acelerando!")

        
class Carro(Veiculo):
    def ligar(self):
        print(f"seu {self.modelo} acaba de ligar!")
    def acelerar(self):
        print("vruuuummm")
    def frear(self):
        print("diminuindo a velocidade")
    def empinar(self):
        print("ronco ronco")
    
 
class Moto(Veiculo):
    def ligar(self):
        print(f"seu {self.modelo} acaba de ligar!")
    def acelerar(self):
        print("randandannnn")   

carro1 = Carro("BMW série 3", 2025)
carro1.ligar()
carro1.acelerar()

moto1 = Moto("BMW S1000RR", 2009)
moto1.ligar()
moto1.acelerar()
moto1.empinar()
