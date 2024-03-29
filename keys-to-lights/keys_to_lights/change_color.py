import requests

import keys_to_lights

headers = {
    "Authorization": "Bearer " + keys_to_lights.idontknow.HOME_ASSISTANT_TOKEN,
    "content-type": "application/json",
}



def change_color(r, g, b):

    data = {
        "entity_id": "light.h6110_10f3",
        "rgb_color": [r, g, b]
        # "transition": 20
    }

    requests.post(keys_to_lights.idontknow.HOME_ASSISTANT_URL, json=data, headers=headers)

if __name__ == "__main__":

    change_color(0, 255, 0)
    change_color(0, 60, 255)