import os
from Model.todo_model import ToDoModel
from View.todo_view import ToDoView
from Controller.todo_controller import ToDoController

if __name__ == "__main__":
    dateipfad = os.path.join(".", "todo_list.txt")
    model = ToDoModel(dateipfad)
    view = ToDoView()
    controller = ToDoController(model, view)
    controller.start()