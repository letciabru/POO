class Cachorro:
    def __init__(self, nome, raca, comidas, acordado, feliz, energia): #para o init funcionar, lembre-se sempre de colocar 2 underlines antes e dois depois
        self.nome = nome
        self.raça = raca
        self.comidas = comidas
        self.acordado = acordado
        self.feliz = feliz
        self.energia = energia

    def acordar(self):
        if not self.acordado:
            self.acordado = True
            print(f"{self.nome} acaba de acordar... suas energias foram restauradas!")
        else:
            print(f"Bom dia! {self.nome} já está acordado!")

    def dormir (self):
        if self.acordado:
            self.acordado = False
            print(f"Bom sono! {self.nome} acaba de dormir!")
            self.energia = 100
        else:
            print(f"{self.nome} já está dormindo!")

    def comer (self):
        if self.acordado:
            self.comidas -= 1
            print(f"(Sons de comida)... {self.nome} comeu e agora tem {self.comidas} restantes!")
            if not self.feliz:
                self.feliz = True
                print(f"{self.nome} ficou feliz após comer!")
            else:
                print(f"{self.nome} continua feliz!")
        else:
            print(f"{self.nome} não pode comer por estar dormindo")

    def brincar(self):
        if self.acordado:
            if self.energia >= 20:
                if not self.feliz:
                    self.feliz = True
                    self.energia -= 20
                    print(f"(sons de folhas)... {self.nome} brincou no quintal e agora está feliz!")
                else:
                    self.energia -= 20
                    print(f"(sons de folhas)... {self.nome} brincou no quintal, ele continua feliz!")
            else:
                print(f"{self.nome} está cansado demais para brincar! (Coloque ele para dormir pra restaurar sua energia)")
        else:
            print(f"{self.nome} não pode brincar por estar dormindo!")

    def latir(self):
        if self.acordado:
            print(f"{self.nome} latiu: Au! Au!")
        else:
            print(f"{self.nome} não pode latir por estar dormindo!")

    def ignorar(self):
        if self.acordado:
            if self.feliz:
                self.feliz = False
                print(f"Você ignorou {self.nome}, agora ele está triste!")
            else:
                print(f"Você ignorou {self.nome}, ele continua triste!")
        else:
                print(f"Você ignorou {self.nome}, mas ele nem reparou por estar dormindo!")
            
            
dog1 = Cachorro("Humpt Dumpt", "Pincher", 5, True, False, 100)
dog2 = Cachorro("Garfield", "Golden", 8, True, True, 100)

dog1.brincar()
dog1.brincar()
dog1.brincar()
dog1.brincar()
dog1.brincar()
dog1.brincar()
dog1.dormir()
dog1.acordar()