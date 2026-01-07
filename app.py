from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

# CRUD - Create, Read, Update, Delete

tasks = []
id_control = 1

@app.route("/tasks", methods=["POST"])
def create_task():
    global id_control
    data = request.get_json()
    new_task = Task(id=id_control,
                    title=data["title"],
                    description=data.get("description", ""),
                    completed=bool(data.get("completed", False))
)

    id_control += 1

    # Pegar nova tarefa e adicionar na lista tasks
    tasks.append(new_task)
    print(tasks)
    return jsonify({"Status": "Success"}), 200

@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks] # Cria uma lista vazia task list, Pega uma tarefa por vez da lista tasks, Converte a tarefa em dicionário, Coloca dentro da lista task_list

    output = {
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)
@app.route("/tasks/<int:id>", methods=["GET"])
def get_id(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"status": "service not found" }), 404

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    if task == None:
        return jsonify({"status": "service not found"}), 404
    
    data = request.get_json()
    task.title = data["title"]
    task.description = data["description"]
    task.completed = data["completed"]
    return jsonify({"message": "Tarefa atualizada com sucesso"}), 200

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    if task == None:
        return jsonify({'status': 'service not found'}), 404
    tasks.delete(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})




if __name__ == "__main__":
    app.run(debug=True)