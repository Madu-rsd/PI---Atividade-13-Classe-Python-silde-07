class Pessoa:
    pessoas = []

    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'

    @classmethod
    def listarPessoas(cls):
        for pessoa in cls.pessoas:
            print(pessoa)

    # método de instância
    def aniversario(self):
        self.idade += 1


pessoa1 = Pessoa('Anny', 17, 'Estudante')
pessoa2 = Pessoa('Katiane', 38, 'Professora')

Pessoa.listarPessoas()

print("\nDepois do aniversário:\n")

pessoa1.aniversario()

Pessoa.listarPessoas()