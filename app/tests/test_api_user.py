import json
def test_user_get(client, jwt_token):
    """
        GIVEN the EP of get users
        WHEN the EP get called
        THEN get all the users registered in db
    """

    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }

    response = client.get(("/api/users/"), headers=headers)
    assert response.status_code == 200

def test_user_get_by_id(client, jwt_token):
    """
        GIVEN an user ID
        WHEN the EP get called
        THEN get the user requested by ID
    """

    headers = {
        'Authorization': f'Bearer {jwt_token}',
    }

    response = client.get(("/api/users/4"), headers=headers)
    assert response.status_code == 200

def test_user_post(client):
    """
        GIVEN a json payload with data
        WHEN wants to create a new user
        THEN validate if user could be created or exists
    """
    headers = {
        'Content-Type': 'application/json'
    }
    payload={
        "name": "Test",
        "lastname": "Test",
        "email": "test@test.com",
        "password": "test",
        "active" : 1
    }

    response = client.post(("/api/users/"), data=json.dumps(payload), headers=headers)
    assert response.status_code == 200 or response.status_code == 406

def test_user_deactivate(client, jwt_token):
    """
        GIVEN an user ID
        WHEN the EP get called
        THEN update the active status of the user
    """

    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }

    response = client.patch(("/api/users/deactivate/1"), headers=headers)
    assert response.status_code == 200

def test_user_put(client, jwt_token):
    """
        GIVEN a json payload with data
        WHEN wants to update an existing user
        THEN validate if user could be updated
    """
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {jwt_token}'
    }
    payload={
        "id": 3,
        "name": "Jairo",
        "lastname": "Gomez",
        "email": "gomezjairo@blabla.com"
    }

    response = client.put(("/api/users/"), data=json.dumps(payload), headers=headers)
    assert response.status_code == 200