
# Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

# Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
    def verificar_saldo(self):
        return self.__saldo, self.mensagem_personalizada()
    
# Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo:
    def mensagem_personalizada(self):
        if self.__saldo < 10:
            return self.__saldo, "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.__saldo >= 50:
            return self.__saldo, "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return self.__saldo, "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        
# Classe UsuarioTelefone:
class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano

# Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo(self):
        _, mensagem = self.plano.verificar_saldo()
        return mensagem
       
# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input("Digite seu nome: ")
nome_plano = input("Digite o nome do plano: ")
saldo_inicial = float(input("Digite o saldo inicial: "))

 # Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
saldo_usuario, mensagem_usuario = usuario.verificar_saldo()  
print(mensagem_usuario)