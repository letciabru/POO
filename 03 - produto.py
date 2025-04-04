class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.quantidade = quantidade
        
    def get_nome(self):
        return self.__nome
    
    def get_preco(self):
        return self.__preco
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
        
    def set_preco(self, novo_preco):
        if novo_preco > 0:
            self.__preco = novo_preco
        else:
            print("Preço Inválido!")
        
# Criação dos produtos  
objeto1 = Produto("Mouse gamer", 60, 3)

# Chamando as funções
print("----Obtendo o nome e preço do produto----")
print(f"Nome: {objeto1.get_nome()}")
print(f"Preço: R$ {objeto1.get_preco()}")

print("\n----Modificando as informações do produto----")
NovoNome = input("Digite o novo nome para o produto: ")
NovoPreco = float(input("Novo preço para o produto: "))
objeto1.set_nome(NovoNome)
objeto1.set_preco(NovoPreco)

print("\n----Obtendo o nome e preço atualizados----")
print(f"Nome: {objeto1.get_nome()}")
print(f"Preço: R$ {objeto1.get_preco()}")
