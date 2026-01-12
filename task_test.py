import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'

def test_post():
    new_task = {
        'title': 'Nova tarefa',
        'description': 'Descrição nova tarefa'
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task)
    assert response.status_code == 200

    response_json = response.json()
    assert "Status" in response_json
    assert "id" in response_json


def test_get():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200

    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    task_id = 1
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200

    task = response.json()
    assert task["id"] == task_id


def test_put():
    task_id = 1
    update = {
        "completed": False,
        "description": "Nova descrição",
        "title": "Tarefa atualizada"
    }

    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update)
    assert response.status_code == 200

    response_json = response.json()
    assert response_json['completed'] == update['completed']
    assert response_json['description'] == update['description']
    assert response_json['title'] == update['title']


def test_delete():
    task_id = 1

    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200

    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 404
