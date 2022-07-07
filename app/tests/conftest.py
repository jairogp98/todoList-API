import pytest
from app import init
from ..database.models.users import Users
from flask_jwt_extended import create_access_token

@pytest.fixture()
def client():
    app = init()
    client = app.test_client()
    ctx = app.test_request_context()
    ctx.push()

    yield client

    ctx.pop()

@pytest.fixture
def jwt_token(user):
    return user.encode_access_token()

@pytest.fixture
def user():
    user = Users.query.filter_by(email = "test@test.com").first()
    return user
