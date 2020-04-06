class ToDoModel:

    def __init__(self, name, todo_id, is_done):
        self.name = name
        self.todo_id = todo_id
        self.is_done = is_done

    def to_json(self):
        return {'{name:' + self.name + ', id:' + self.todo_id + ', is_done:' + self.is_done + '}'}


class ToDoDB:
    def __init__(self):
        self.todos = []

    def create(self, name, todo_id, is_done):
        todo = ToDoModel(name, todo_id, is_done)
        self.todos.append(todo)
        return todo

    def todo_is_done(self, todo_id):
        todo = self.todos[todo_id]
        self.todos[todo_id] = ToDoModel(todo.name, todo_id, True)
        return self.todos[todo_id]

    def get_undone_todos(self):
        todos = []
        for index in range(0, len(self.todos) - 1):
            if not self.todos[index].is_done:
                todos.append(self.todos[index])
        return todos
