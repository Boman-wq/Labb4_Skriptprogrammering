
import json, random, requests
from random import randrange

url = "http://127.0.0.1:5000/json"
randescription = ["Sunny", "Cloudy", "Rainy"]
data = {"sensor" : "s-65",
    "location" : "Borlänge",
    "temperature" : randrange(10, 26),
    "description" : random.choice(randescription)}

datadump = json.dumps(data)

eksde = requests.post("http://127.0.0.1:5000/json", json=data)

print(eksde.text)