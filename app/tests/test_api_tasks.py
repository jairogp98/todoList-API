import json
def test_task_post(client, jwt_token):
    """
        GIVEN a json payload with data
        WHEN wants to create a new task
        THEN validate if task could be created or exists
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {jwt_token}'
    }
    payload = {
        "title": "test",
        "description": "This is a testing task",
        "user_id": 4,
        "expiration_date": "2023-01-01",
        "status": "Stand-by",
        "priority": "ASAP",
        "active": True
    }

    response = client.post(("/api/tasks/"), data=json.dumps(payload), headers=headers)
    assert response.status_code == 200

def test_task_get_by_user(client, jwt_token):
    """
        GIVEN an user ID
        WHEN the EP get called
        THEN get all the tasks associate to that user
    """

    headers = {
        'Authorization': f'Bearer {jwt_token}',
    }

    response = client.get(("/api/tasks/4"), headers=headers)
    assert response.status_code == 200

def test_task_put(client, jwt_token):
    """
        GIVEN a json payload with data
        WHEN wants to create a new task
        THEN validate if task could be created or exists
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {jwt_token}'
    }
    payload = {
        "id": 3,
        "title": "Test update",
        "description": "This is a modification of the previous task",
        "expiration_date": "2023-01-01",
        "status": "Doing",
        "priority": "ASAP"
    }

    response = client.put(("/api/tasks/"), data=json.dumps(payload), headers=headers)
    assert response.status_code == 200