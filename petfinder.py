"""Methods regarding Petfinder API"""

import os
import requests

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

GET_TOKEN_URL = "https://api.petfinder.com/v2/oauth2/token"

RANDOM_PET_URL = "https://api.petfinder.com/v2/animals?limit=100"



def get_oauth_token():
    """TODO: """

    resp = requests.post(GET_TOKEN_URL,
        data = {"grant_type": "client_credentials",
                "client_id": PETFINDER_API_KEY,
                "client_secret": PETFINDER_SECRET_KEY}
    )

    token = resp.json()
    return token["access_token"]


def get_random_pet(auth_token):

    resp = requests.get(RANDOM_PET_URL, headers = {"Authorization": f"Bearer" })
