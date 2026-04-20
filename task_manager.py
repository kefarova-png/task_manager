import json


class TaskManager:
    def __init__(self):  #  Инициализация пустого списка задач
        self.tasks = []


    def add_task(self, description: str):  #  Добавление новой задачи с описанием и начальным статусом False
        task = {'description': description, 'completed': False}  #  Каждая задача -- список словарей.
        self.tasks.append(task)


    def complete_task(self, index: int):  #  Отметка задачи как выполненной по индексу
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print(f"Ошибка: задача с индексом {index} не существует.")


    def remove_task(self, index: int):  #  Удаление задачи по индексу
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print(f"Ошибка: задача с индексом {index} не существует.")


    def save_to_json(self, filename: str):  #  Сохранение текущего списка задач в JSON-файл
        with open(filename, 'w') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)


    def load_from_json(self, filename: str):  #  Загрузка задач из JSON-файла
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            print(f"Файл {filename} не найден. Текущий список задач остается пустым.")
        except json.JSONDecodeError:
            print(f"Ошибка чтения файла {filename}: неверный формат JSON.")


    def list_tasks(self):  #  Метод для вывода всех задач

        if not self.tasks:
            print("Список задач пуст.")
            return
        for idx, task in enumerate(self.tasks):
            status = '✓' if task['completed'] else '✗'
            print(f"{idx}. [{status}] {task['description']}")