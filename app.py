import requests
from flask import Flask, redirect, render_template, request

#constants
STATIONS_BASE_URL = "https://creativecommons.tankerkoenig.de/json/list.php?"
API_KEY = "df905214-1612-2644-13c6-0d734ed17fd7"
GEOCODE_BASE_URL = "https://nominatim.openstreetmap.org/search?"

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
    sort = request.form.get("sort")

    if not location:
        return render_template("index.html", error=True)
    
    stations = stationsearch(location,type,radius,sort)

    print(location)
    return render_template("search.html",address=location["address"],stations=stations,radius=radius,type=type,sort=sort)

def geocode(search):
    parameters = {
        "format": "json",
        "addressdetails": "1",
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
    
def stationsearch(location,type,radius,sort):
    parameters = {
        "lat" : location["lat"],
        "lng" : location["lon"],
        "rad" : radius,
        "type" : type,
        "sort" : sort,
        "apikey" : API_KEY
    }
    response = requests.get(STATIONS_BASE_URL, params=parameters)
    if (not response.status_code == 200) or response.json()["ok"] == False:
        return
    return response.json()["stations"]

# on 404 redirect to index
@app.errorhandler(404)
def page_not_found(e):
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=False)