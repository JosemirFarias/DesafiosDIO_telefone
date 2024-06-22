# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

# Crie um método fazer_chamada para permitir que um usuário faça uma chamada telefônica:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        
# Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano':
    def custo_chamada(self, duracao):
        return self.plano.custo_chamada(duracao)

# Verifique se o saldo do plano é suficiente para a chamada.
    def verificar_saldo(self):
        return self.plano.saldo

# Se o saldo for suficiente, deduz o custo da chamada do saldo do plano.
    def deduzir_saldo(self, custo):
        self.plano.deduzir_saldo(custo)

# E retorne uma mensagem de sucesso com o destinatário e o saldo restante após a chamada:
    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if custo > self.plano.saldo:
            return f"Saldo insuficiente para fazer a chamada."
        else:
            self.plano.deduzir_saldo(custo)
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}"
# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

# Crie um método para verificar_saldo e retorne o saldo atual:
    def verificar_saldo(self):
        return self.saldo

# Crie um método custo_chamada para calcular o custo de uma chamada supondo o custo de $0.10 por minuto:
    def custo_chamada(self, duracao):
        return duracao * 0.10

# Crie um método deduzir_saldo para deduz o valor do saldo do plano:
    def deduzir_saldo(self, custo):
        self.saldo -= custo

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input("Digite o nome do usuário: ")
numero = input("Digite o número do usuário: ")
saldo_inicial = float(input("Digite o saldo inicial do usuário: "))

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input("Digite o número do destinatário: ")
duracao = int(input("Digite a duração da chamada em minutos: "))

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))