from flask import Flask, redirect, render_template, request

#config
app = Flask(__name__)

#routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods = ['POST', 'GET'])
def search():
    if request.method == "GET":
        return redirect("/")
    return request.form.get("address")

if __name__ == "__main__":
    app.run(debug=True)