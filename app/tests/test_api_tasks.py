import json
def test_task_post(client, jwt_token):
    """
        GIVEN a json payload with data
        WHEN wants to create a new task
        THEN create the task
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

    response = client.get(("/api/tasks/byUser/4"), headers=headers)
    assert response.status_code == 200

def test_task_put(client, jwt_token):
    """
        GIVEN a json payload with data
        WHEN wants to update an existing task
        THEN update the task or the task doesn't exist
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

def test_task_patch(client, jwt_token):
    """
        GIVEN a task ID
        WHEN wants to delete the task
        THEN deactivate the specified task
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {jwt_token}'
    }

    response = client.patch(("/api/tasks/byTask/5"), headers=headers)
    assert response.status_code == 200

def test_task_get_by_id(client, jwt_token):
    """
        GIVEN a task ID
        WHEN the EP get called
        THEN get the data of that specific task
    """

    headers = {
        'Authorization': f'Bearer {jwt_token}',
    }

    response = client.get(("/api/tasks/byTask/4"), headers=headers)
    assert response.status_code == 200

def test_task_get_expired_tasks(client, jwt_token):
    """
        GIVEN a user ID
        WHEN the EP get called
        THEN get the expired o to expire tasks
    """

    headers = {
        'Authorization': f'Bearer {jwt_token}',
    }

    response = client.get(("/api/tasks/validity/4"), headers=headers)
    assert response.status_code == 200