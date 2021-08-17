from pymongo import MongoClient
import json


def get_client():
    CONNECTION_STRING = "mongodb+srv://Sam:2128506menemMENEM123@cluster0.7bhv1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    return MongoClient(CONNECTION_STRING)


def get_content(client):
    db = client["patrul_coords"]

    col = db["coords"]

    data = col.find_one()

    return data['content']


def form_json(data):
    with open('../routing/coords.json', 'w+') as file:
        file.write(json.dumps({'coords': eval(data)}))


if __name__ == "__main__":
    client = get_client()
    while True:
        try:
            coords = get_content(client)
            break
        except TypeError:
            continue
