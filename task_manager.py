import json


class TaskManager:
    def __init__(self) -> None:  #  Инициализация пустого списка задач
        self.tasks = []


    def add_task(self, description: str) -> None:  #  Добавление новой задачи с описанием и начальным статусом False
        task = {'description': description, 'completed': False}  #  Каждая задача -- список словарей.
        self.tasks.append(task)
        print(f"Задача '{description}' успешно добавлена.")  #  Сообщение об успешном добавлении


    def complete_task(self, index: int) -> None:  #  Отметка задачи как выполненной по индексу
        if index in range(0, len(self.tasks)):
            if self.tasks[index]['completed'] is False:
                self.tasks[index]['completed'] = True
                print(f"Задача с индексом {index} успешно отмечена как выполненная.")
                return
            print(f"Ошибка: задача с индексом {index} уже выполнена.")
        else:
            print(f"Ошибка: задача с индексом {index} не существует.")


    def remove_task(self, index: int) -> None:  #  Удаление задачи по индексу
        if index in range(0, len(self.tasks)):
            removed_task = self.tasks.pop(index)  #  Сохраняем удаляемую задачу, чтобы вывести ее описание после удаления
            print(f"Задача '{removed_task['description']}' успешно удалена.")
        else:
            print(f"Ошибка: задача с индексом {index} не существует.")


    def save_to_json(self, filename: str) -> None:  #  Сохранение текущего списка задач в JSON-файл
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.tasks, file, ensure_ascii=False, indent=4)
            print(f"Список задач успешно сохранен в файл '{filename}'.")
        except Exception as error:
            print(f"При сохранении файла произошла ошибка: {error}")


    def load_from_json(self, filename: str) -> None:  #  Загрузка задач из JSON-файла
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.tasks = json.load(file)
            print(f"Задачи успешно загружены из файла '{filename}'.")
        except FileNotFoundError:
            print(f"Файл '{filename}' не найден. Текущий список задач остается пустым.")
        except json.JSONDecodeError:
            print(f"Ошибка чтения файла '{filename}': неверный формат JSON.")
        except Exception as error:
            print(f"Произошла неизвестная ошибка: {error}")


    def list_tasks(self) -> None:  #  Метод для вывода всех задач
        if not self.tasks:
            print("Список задач пуст.")
            return
        for index, task in enumerate(self.tasks):
            status = '✓' if task['completed'] else '✗'
            print(f"{index}. [{status}] {task['description']}")