import requests

def huidige_temperatuur():

    url = "https://api.open-meteo.com/v1/forecast?latitude=52.0908&longitude=5.1222&hourly=temperature_2m&current=temperature_2m"

    response = requests.get(url)

    data = response.json()

    temperatuur = data["current"]["temperature_2m"]

    return temperatuur








