from datetime import datetime

class Task:
    def __init__(self, descricao, prazo=None):
        self.descricao = descricao
        self.completa = False
        self.prazo = prazo

    def marcar_como_completa(self):
        self.completa = True

class TaskManager:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, index):
        if 0 <= index < len(self.tarefas):
            del self.tarefas[index]

    def obter_tarefas(self):
        return self.tarefas
