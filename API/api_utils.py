import json


def get_json(data):
    informations = dict()

    for info in data:
        informations[info[0]] = {
            "capital": info[1],
            "population": info[2],
            "density": info[3],
            "surface": info[4],
            "language": info[5],
            "timezone": info[6],
            "regime": info[7],
            "currency": info[7],
        }
    return json.dumps(informations)
