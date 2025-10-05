from flask import Flask, request, jsonify # Importação flask
from models.task import Task

app = Flask(__name__)

# Rotas
# @app.route("/")
# def hello_world():
#     return "Hello World!"

# @app.route("/about")
# def about():
#     return "Sobre"

tasks = []
task_id_control = 1
# CRUD
@app.route("/tasks", methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data.get("title"), description=data.get("description"))
    task_id_control += 1
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})

@app.route("/tasks", methods=['GET'])
def get_tasks():
    # task_list = []
    # for task in tasks:
    #     task_list.append(task.to_dict())
    # outra forma
    task_list = [task.to_dict() for task in tasks]

    output = {
        "tasks" : task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task_by_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify({"task": t.to_dict()})
    return jsonify({"message": "Não foi possível encontrar a tarefa!"}), 404

@app.route('/user/<username>')
def show_user(username):
    return jsonify({"username": username})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Não foi possível encontrar a tarefa!"}), 404
    
    data = request.get_json()
    task.title = data.get('title')
    task.description = data.get('description')
    task.completed = data.get('completed')

    return jsonify({"message": "Tarefa atualizada com sucesso!"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    
    if not tasks:
        return jsonify({"message":"Não foi possível encontrar a tarefa!"}), 404
    
    tasks.remove(task)
    return jsonify({"message":"Tarefa removida com sucesso!"})



# Executando 
if __name__ == "__main__":
    app.run(debug=True)