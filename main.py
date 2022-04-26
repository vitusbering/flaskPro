import json
import os.path
from flask import Flask, request

app = Flask(__name__)

cars = [
    {
        "id": 1,
        "brand": "Nissan",
        "model": "X-Trail",
        "year": 2019,
        "color": "blue"
    }, {
        "id": 2,
        "brand": "Toyota",
        "model": "Camry",
        "year": 2019,
        "color": "black"
    }
]


fileName = "cars.json"


@app.route("/cars/<int:car_id>")
def get_id_cars(car_id: int):
    return [car for car in cars if car["id"] == car_id][0]


def save_json(data):
    with open(fileName, "w") as file:
        line = json.dumps(data, indent=4)
        file.write(line)


@app.route("/cars/")
def get_all_cars():
    global cars
    if not os.path.exists(fileName):
        save_json(cars)
    if os.path.exists(fileName):
        with open(fileName, "r") as file:
            cars = json.load(file)
    return json.dumps(cars)


@app.route("/cars/", methods=["POST"])
def create_cars():
    data = request.get_json()
    cars.append(data)
    save_json(cars)
    # print(data)
    return data

