import tkinter as tk
from tkinter import ttk, messagebox
from functions import add_task, complete_task, remove_task, get_tasks

class TodoScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.tasks = []

        # Configuração da janela principal
        self.frame = ttk.Frame(root, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada de tarefa
        self.task_entry = ttk.Entry(self.frame, width=40, font=('Arial', 10))
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)

        # Botão "Adicionar"
        self.add_btn = ttk.Button(
            self.frame,
            text="Adicionar",
            command=self._add_task
        )
        self.add_btn.grid(row=0, column=1, padx=5, pady=5)

        # Lista de tarefas (Listbox)
        self.task_listbox = tk.Listbox(
            self.frame,
            width=50,
            height=15,
            font=('Arial', 10),
            selectbackground="#d9d9d9"
        )
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Botões "Concluir" e "Remover"
        self.complete_btn = ttk.Button(
            self.frame,
            text="Concluir",
            command=self._complete_task
        )
        self.complete_btn.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        self.remove_btn = ttk.Button(
            self.frame,
            text="Remover",
            command=self._remove_task
        )
        self.remove_btn.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

    def _add_task(self):
        """Adiciona uma nova tarefa."""
        task_text = self.task_entry.get()
        success, message = add_task(self.tasks, task_text)
        
        if success:
            self._update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", message)

    def _complete_task(self):
        """Marca a tarefa selecionada como concluída."""
        selected = self.task_listbox.curselection()
        if selected and complete_task(self.tasks, selected[0]):
            self._update_listbox()

    def _remove_task(self):
        """Remove a tarefa selecionada."""
        selected = self.task_listbox.curselection()
        if selected and remove_task(self.tasks, selected[0]):
            self._update_listbox()

    def _update_listbox(self):
        """Atualiza o Listbox com as tarefas."""
        self.task_listbox.delete(0, tk.END)
        
        for task in self.tasks:
            status = "✓" if task["done"] else "✗"
            task_text = f"[{status}] {task['task']}"
            
            # Insere a tarefa e aplica cor se estiver concluída
            idx = self.task_listbox.size()  # Obtém o índice do novo item
            self.task_listbox.insert(tk.END, task_text)
            if task["done"]:
                self.task_listbox.itemconfig(idx, {'fg': 'green'})