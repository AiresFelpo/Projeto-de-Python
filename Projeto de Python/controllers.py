import tkinter as tk
from models import Task, TaskManager
from views import TaskView

class TaskController:
    def __init__(self):
        self.task_manager = TaskManager()

    def adicionar_tarefa(self, descricao, prazo):
        tarefa = Task(descricao, prazo)
        self.task_manager.adicionar_tarefa(tarefa)

    def completar_tarefa(self, index):
        tarefas = self.task_manager.obter_tarefas()
        if 0 <= index < len(tarefas):
            tarefas[index].marcar_como_completa()

    def remover_tarefa(self, index):
        self.task_manager.remover_tarefa(index)

    def obter_tarefas(self):
        return self.task_manager.obter_tarefas()

    def run(self):
        root = tk.Tk()
        root.geometry("500x350")
        self.view = TaskView(root, self)
        self.view.update_task_list()
        root.mainloop()

if __name__ == "__main__":
    controller = TaskController()
    controller.run()
