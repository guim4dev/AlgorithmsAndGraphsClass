def maxTasks(tasks):
  if len(tasks) == 0: return 0, tasks
  tasks.sort(key = task_end) # ordenar por quem termina primeiro

  selected_tasks = tasks[0:1] # iniciar com o primeiro item da lista
  count = 1
  for task in tasks[1:]: 
    if task[0] >= selected_tasks[-1][1]:
      selected_tasks.append(task)
      count += 1
  return count, selected_tasks

def task_end(task):
  return task[1]

T = [(2, 5), (11, 15), (4, 9), (7, 10)]
print(maxTasks(T))