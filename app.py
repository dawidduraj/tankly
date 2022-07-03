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
    
    location = geocode(request.form.get("address"))
    type = request.form.get("type")
    radius = request.form.get("radius")

    if not location:
        return redirect("/error")
    
    stations = stationsearch(location,type,radius)

    return str(stations)

def geocode(search):
    GEOCODE_BASE_URL = "https://nominatim.openstreetmap.org/search?"
    parameters = {
        "format": "json",
        "q" : search
        }
    response = requests.get(GEOCODE_BASE_URL, params=parameters)
    #network error handling
    if not response.status_code == 200:
        return

    #no search results
    if len(response.json()) == 0:
        return
    
    #return first result
    return response.json()[0]
    
def stationsearch(location,type,radius):
    STATIONS_BASE_URL = "https://creativecommons.tankerkoenig.de/json/list.php?"
    API_KEY = "00000000-0000-0000-0000-000000000002"
    parameters = {
        "lat" : location["lat"],
        "lng" : location["lon"],
        "rad" : radius,
        "type" : type,
        "sort" : "price",
        "apikey" : API_KEY
    }
    response = requests.get(STATIONS_BASE_URL, params=parameters)
    if (not response.status_code == 200) or response.json()["ok"] == False:
        return
    return response.json()["stations"]
if __name__ == "__main__":
    app.run(debug=True)