import requests
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
    
    #geocoding request
    BASE_URL = "https://nominatim.openstreetmap.org/search?"
    parameters = {
        "format": "json",
        "q" : request.form.get("address")
        }
    response = requests.get(BASE_URL, params=parameters)
    print(response.content)
    return f"{response.status_code}"

if __name__ == "__main__":
    app.run(debug=True)