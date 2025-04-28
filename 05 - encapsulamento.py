class ContaBancaria:
    def _init_(self, titular, saldo):
        self.titular = titular #público
        self.__saldo = saldo #privado

    def despositar(self, valor):
        self.__saldo += valor

    def get_saldo(self):
        return self.__saldo
    def set_saldo(self,valor):
        if valor >=0:
            self.__saldo = valor
        else:
            print("Valor invalido")

conta = ContaBancaria('Emyloca',900000000000000000000)
print(conta.get_saldo()) 
conta.set_saldo(900000000000000000000)
print(conta.get_saldo())
