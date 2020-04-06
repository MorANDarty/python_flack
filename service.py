from models import ToDoDB


class ToDoService:

    def __init__(self):
        self.db = ToDoDB()

    def create(self, params):
        return self.db.create(params['name'])

    def todo_is_done(self, todo_id):
        return self.db.todo_is_done(todo_id)

    def get_undone_todos(self):
        todos = self.db.get_undone_todos()
        string = "{"
        for index in range(0, len(todos) - 1):
            string += todos[index].to_json() + ','
        string += '}'
        return string
