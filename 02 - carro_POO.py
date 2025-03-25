import time # essa biblioteca serve para dar pequenos intervalos durante a execução do código, para simular o processamento

# CRIAÇÃO DA CLASSE CARRO
class Carro:
    def __init__(self, modelo, ano, cor, combustível, ligado, velocidade):
        self.modelo = modelo # atribui o modelo do carro
        self.ano = ano # atribui o ano de fabricação do carro
        self.cor = cor # atribui a cor do carro
        self.ligado = ligado # indica se o carro está ligado ou não
        self.velocidade = velocidade # velocidade atual do carro
        self.combustível = combustível # indica a quantidade de combustível do carro
    
   # CRIAÇÃO DAS FUNÇÕES DA CLASSE CARRO
     
    def ligar(self): # AQUI VOCÊ LIGA O CARRO
        if not self.ligado:
            self.ligado = True
            print(f"(click)... {self.modelo} acaba de ser ligado!\n")
            time.sleep(2)
        else:
            print(f"(click)... {self.modelo} continua ligado!\n")
            time.sleep(2)
        
    def desligar(self): # AQUI VOCÊ DESLIGA O CARRO
        if self.ligado:
            self.ligado = False
            print(f"(click)... {self.modelo} acaba de desligar!\n")
            time.sleep(2)
        else:
            print(f"(click)... {self.modelo} continua desligado!\n")
            time.sleep(2)
             
    def acelerar(self): # AQUI VOCÊ ACELERA O CARRO EM 10 KM/H
        if self.ligado:
            if self.combustível > 0:
                if self.velocidade == 0:
                    self.velocidade += 10
                    self.combustível -= 5
                    print(f"(Vrum)... {self.modelo} acelerou 10 KM/H e começou a andar!\n")
                    time.sleep(2)
                else:
                    self.velocidade += 10
                    self.combustível -= 5
                    print(f"(Vrum... {self.modelo} acelerou 10 KM/H e agora está andando {self.velocidade} KM/H!)\n")
                    time.sleep(2)
            else:
                print(f"(Falha)... {self.modelo} está sem combustível para andar, reabasteça o veículo!\n")
                time.sleep(2)
        else:
            print(f"(Nada aconteceu)... {self.modelo} está desligado e não pode andar, ligue o veículo!\n")
            time.sleep(2)

        
    def frear(self): # AQUI VOCÊ REDUZ A VELOCIDADE DO CARRO EM 10 KM/H
        if self.ligado:
            if self.velocidade == 0:
                print(f"(Nada aconteceu)... {self.modelo} tentou desacelerar 10 KM/H, mas ele já está parado!\n")
                time.sleep(2)
            else:
                self.velocidade -= 10
                print(f"(Vrum... {self.modelo} desacelerou 10 KM/H e agora está andando {self.velocidade} KM/H!)\n")
                time.sleep(2)
                if self.velocidade == 0:
                    print(f"{self.modelo} agora está parado!\n")
                    time.sleep(2)
        else:
            print(f"(Nada aconteceu)... {self.modelo} está desligado e não pode frear!\n")
            time.sleep(2)
         
    def abastecer(self, quantidade): # AQUI VOCÊ ABASTECE O CARRO
        if self.combustível < 100:
            if (quantidade + self.combustível) <= 100:
                self.combustível += quantidade
                print(f"(Glup Glup)... {self.modelo} foi reabastecido e agora está com {self.combustível} L de combustível!\n")
                time.sleep(2)
            else:
                print(f"(OPS)... a quantidade desejada de combustível excede o limite de 100 L, escolha outra quantia!\n")
                time.sleep(2)
        else:
            print("(OPS)... o tanque do {self.modelo} já está cheio!")
                
    def buzinar(self): # AQUI VOCÊ FAZ O CARRO BUZINAR
        if self.ligado:
            print(f"(Beep Beep)... {self.modelo} buzinou!\n")
            time.sleep(2)
        else:
            print(f"(Nada aconteceu)... {self.modelo} está desligado e não pode buzinar, ligue o veículo!\n")
            time.sleep(2)
         
    def status(self):    
        print(f"Status do veículo:\n"
             f"Modelo = {self.modelo}\n"
             f"Ano = {self.ano}\n"
             f"Cor = {self.cor}\n"
             f"Combustível = {self.combustível} litros\n"
             f"Velocidade atual = {self.velocidade} KM/H\n"
             f"Carro Ligado = {self.ligado}\n")
        time.sleep(2)
        
        
# CRIAÇÃO DOS CARRROS
car1 = Carro("Toyota", 2008, "Vermelho", 100, False, 0)


# CHAMANDO AS FUNÇÕES
car1.ligar()
car1.acelerar()
car1.acelerar()
car1.abastecer(10)
car1.frear()
car1.status()
        
# INDICANDO O FIM DO CÓDIGO
print("Fim do código!")