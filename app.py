from flask import Flask

#config
app = Flask(__name__)

#routes
@app.route("/")
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)