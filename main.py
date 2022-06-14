from app import init
import os
from app.database.db import db

app = init()

@app.route('/')
def main():
    return "Hello World!"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host=os.environ.get("FLASK_RUN_HOST"),
        port=os.environ.get("FLASK_RUN_PORT")
        )