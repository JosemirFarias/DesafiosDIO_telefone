# class UsuarioTelefone com os atributos nome, numero e plano
class UsuarioTelefone():
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# conseito de encapsulamento, onde os produtos serão encapsulados dentro da classe
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, valor):
        self.__numero = valor

    @property
    def plano(self):
        return self.__plano
    
    @plano.setter
    def plano(self, valor):
        self.__plano = valor

# método __str__ para retornar a mensagem de sucesso       
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."

# input para receber os dados do usuário       
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número do usuário: ")
plano = input("Digite o plano do usuário: ")

# instanciando a classe UsuarioTelefone
usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)
