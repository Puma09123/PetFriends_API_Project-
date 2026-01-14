import requests
from settings import BASE_URL, AUTH_KEY


def get_pets_list(filter=""):
    headers = {
        "Authorization": AUTH_KEY
    }
    params = {"filter": filter}
    response = requests.get(f"{BASE_URL}/api/pets", headers=headers, params=params)
    return response


def add_new_pet(name, animal_type, age, pet_photo):
    headers = {
        "Authorization": AUTH_KEY
    }
    data = {
        "name": name,
        "animal_type": animal_type,
        "age": age
    }
    files = {
        "pet_photo": open(pet_photo, "rb")
    }
    response = requests.post(
        f"{BASE_URL}/api/pets",
        headers=headers,
        data=data,
        files=files
    )
    return response
