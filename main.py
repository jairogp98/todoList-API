from app import init
import os

app = init()

@app.route('/')
def main():
    return "Hello World!"

if __name__ == '__main__':
    app.run(
        host=os.environ.get("FLASK_RUN_HOST"),
        port=os.environ.get("FLASK_RUN_PORT")
        )