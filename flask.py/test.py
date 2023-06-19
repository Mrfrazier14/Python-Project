from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! This is a test for HTML home page <h1>HELLO</h1>"

def user(name):
    return f"Hello {name}!"

if __name__ == '__main__':
    app.run()
