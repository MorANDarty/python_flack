from flask import Flask
from flask import request

from service import ToDoService

app = Flask(__name__)


@app.route('/todo/create', methods=["POST"])
def create_todo():
    result = ToDoService().create(request.get_json())

    return result.to_json()


@app.route('todo/done/<todo_id>', methods=["PUT"])
def done_todo(todo_id):
    result = ToDoService().todo_is_done(todo_id)

    return result.to_json


@app.route('todo/undone', methods=["GET"])
def get_undone_todos():
    result = ToDoService().get_undone_todos()

    return result


if __name__ == '__main__':
    app.run()
