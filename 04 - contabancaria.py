# Criando a classe ContaBancaria
class ContaBancaria:
    def __init__(self, titular, saldo, limite): # atributos da classe banco
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        
# Criando as funções da classe
    def depositar(self, valor): # função para depositar dinheiro
        if valor > 0:
            self.__saldo += valor
            print(f"R$ {valor} foram depositadosna conta de {self.__titular}!")
        else:
            print("Valor inválido para depósito!!!")
            
    def sacar(self, valor): # função para sacar dinheiro do saldo ou do limite
        if valor <= self.__saldo and valor > 0:
            self.__saldo -= valor
            print(f"R$ {valor} foram retirados do saldo de {self.__titular}!")
        elif (valor > self.__saldo and valor > 0) and (valor <= self.__limite):
            self.__limite -= valor
            print(f"Saldo insuficiente... R$ {valor} foram retirados do limite de {self.__titular}!")
        else:
            print(f"Saldo e limite insuficientes!!!")
            
    def get_saldo(self): # função para ver o saldo atual
        print(f"Saldo atual da conta de {self.__titular}: R$ {self.__saldo}")
        
    def set_limite(self, novo_limite): #função para alterar o limite da conta
        self.__limite = novo_limite
        print(f"O limite da conta de {self.__titular} foi atualizado para R$ {self.__limite}")
        
# Criando as contas
conta1 = ContaBancaria("Logan", 500, 700)

# Chamando as funções
conta1.get_saldo()
conta1.depositar(200)
conta1.sacar(300)
conta1.get_saldo()
conta1.set_limite(900)
conta1.sacar(800)
conta1.get_saldo()
