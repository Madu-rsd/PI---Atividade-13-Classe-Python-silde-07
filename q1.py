class Tarefa:
    tarefas = []
    def __init__(self, titulo, descricao):
        self.titulo = titulo
        self.descricao = descricao
        self.concluido = False
        Tarefa.tarefas.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.descricao}'
    
    @classmethod
    def listarTarefas(cls):
        for tarefa in cls.tarefas:
            print(tarefa)

    @classmethod
    def qtdTarefa(cls):
        return len(cls.tarefas)

tarefa1 = Tarefa('Criar metodo', 'como criar metodo')
tarefa2 = Tarefa('Criar classe', 'como criar classe')

Tarefa.listarTarefas()
print("Quantidade de tarefas:", Tarefa.qtdTarefa())