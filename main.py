import requests
import json

TOKEN = "6839980250:AAEg_45T4eVGDAGtGzxAuUUl-P7tCQ2--1w"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}/"


# telegram bot
def make_request(method: str, params: dict = None):
    res = requests.get(f"{BASE_URL}{method}", params=params)
    return res.json()


def get_updates(offset: int = 0):
    return make_request("getUpdates", {"offset": offset})["result"]


def main():
    offset = 0
    while True:
        updates = get_updates(offset)
        for update in updates:
            offset = update["update_id"] + 1
            if update["message"]:
                text = update["message"]["text"]
                if text == "/start":
                    reply_keyboard = {
                        "keyboard": [
                                [
                                    {"text": "Contact"},
                                    {"text": "Photo"},
                                    {"text": "Location"}
                                ],
                        ],
                        "resize_keyboard": True
                    }
                    make_request(
                        "sendMessage",
                        {
                            "chat_id": update["message"]["chat"]["id"],
                            "text": "Assalomu alaykum, Info botga xush kelibsiz!",
                            "reply_markup": json.dumps(reply_keyboard)
                        },
                    )

                elif text == "/help":
                    make_request(
                        "sendMessage",
                        {
                             "chat_id": update["message"]["chat"]["id"],
                             "text": "Mavjud buyruqlar: \n/start - Botni ishga tushurish,\n /help - Botdan yordam olish,\n /location - Location yuborish,\n /photo - Rasm yuborish message bilan,\n /contact - Bog'lanish uchun contact"
                        }
                    )

                elif text == "/location" or text == "Location":
                    make_request(
                        "sendlocation?",
                        {
                             "chat_id": update["message"]["chat"]["id"],
                             "latitude": 41.27422,
                             "longitude": 69.19017
                        }
                    )

                elif text == "/photo" or text == "Photo":
                    send_media_group = [
                        {
                            "type": "photo",
                            "media": "https://i0.wp.com/picjumbo.com/wp-content/uploads/magical-spring-forest-scenery-during-morning-breeze-free-photo.jpg?w=600&quality=80"
                        },
                        {
                            "type": "photo",
                            "media": "https://cdn.pixabay.com/photo/2015/12/01/20/28/road-1072821_640.jpg",
                            "caption": "Nature photos"
                        },
                    ]
                    make_request(
                        "sendMediaGroup?",
                        {
                             "chat_id": update["message"]["chat"]["id"],
                             "media": json.dumps(send_media_group),
                        }
                    )

                elif text == "/contact" or text == "Contact":
                    make_request(
                        "sendMessage",
                        {
                            "chat_id": update["message"]['chat']['id'],
                            "text": "+998991234567 a'loqaga chiqish uchun kontakt"
                        }
                    )


if __name__ == "__main__":
  main()
