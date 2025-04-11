def add_task(tasks, new_task):
    """Adiciona uma nova tarefa se ela não existir."""
    if not new_task.strip():
        return False, "Digite uma tarefa válida!"
    
    # Verifica se a tarefa já existe (ignorando maiúsculas e espaços)
    new_task_clean = new_task.strip().lower()
    for task in tasks:
        if task["task"].strip().lower() == new_task_clean:
            return False, "Esta tarefa já existe!"
    
    tasks.append({"task": new_task, "done": False})
    return True, "Tarefa adicionada!"

def complete_task(tasks, task_index):
    """Marca uma tarefa como concluída."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        return True
    return False

def remove_task(tasks, task_index):
    """Remove uma tarefa da lista."""
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        return True
    return False

def get_tasks(tasks):
    """Retorna a lista de tarefas formatadas."""
    return tasks