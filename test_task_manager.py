import pytest  #  Библиотека для тестирования
from task_manager import TaskManager  #  Импорт тестируемого класса TaskManager из файла task_manager.py
#  при использовании pytest, писать строки для запуска функций не нужно


def test_add_and_complete_task():
    tm = TaskManager()  #  Создаем новый экземпляр TaskManager
    tm.add_task("Пример задачи")  #  В список tm добавляем новую задачу с описанием "Пример задачи"
    assert len(tm.tasks) == 1  #  Проверяем, что в списке задач -- одна задача
    assert tm.tasks[0]['completed'] is False  #  Проверяем невыполненность этой задачи № 0
    tm.complete_task(0)  #  Помечаем эту задачу № 0 (индекс 0) как выполненную
    assert tm.tasks[0]['completed'] is True  #  Проверяем выполненность этой задачи № 0


def test_remove_task():
    tm = TaskManager()  #  Создаем новый экземпляр TaskManager
    tm.add_task("Задача 1")  #  В список tm добавляем новую задачу с описанием "Задача 1"
    tm.add_task("Задача 2")  #  В список tm добавляем новую задачу с описанием "Задача 2"
    tm.remove_task(0)  #  Удаляем задачу № 0 (индекс 0)
    assert len(tm.tasks) == 1  #  Проверяем, что в списке задач осталась одна задача
    assert tm.tasks[0]['description'] != "Задача 1"  #  Проверяем, что удалилась именно "Задача 1"
    assert tm.tasks[0]['description'] == "Задача 2"  #  Проверяем, что "Задача 2" не удалилась


def test_save_load_json(tmp_path):
    tm = TaskManager()  #  Создаем новый экземпляр TaskManager
    tm.add_task("Задача для сохранения")  #  Добавляем новую задачу с описанием "Задача для сохранения"
    tm.complete_task(0)  #   Помечаем задачу выполненной
    filename = tmp_path / "tasks.json"  #  Пишем сюда
    tm.save_to_json(str(filename))  #  Сохраняем задачи в файл в формате json
    tm2 = TaskManager()  #  Создаем новый экземпляр
    tm2.load_from_json(str(filename))  #  и загружаем данные из файла
    assert len(tm2.tasks) == 1  #  Проверяем, что в загруженном списке задач одна задача
    assert tm2.tasks[0]['description'] == "Задача для сохранения"  #  именно с описанием "Задача для сохранения"
    assert tm2.tasks[0]['completed'] is True  #  и со статусом выполненная