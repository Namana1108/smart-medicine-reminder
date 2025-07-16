import requests

def send_sms(phone_number, message):
    response = requests.post('https://textbelt.com/text', {
        'phone': phone_number,
        'message': message,
        'key': 'textbelt',  # Free key
    })

    result = response.json()
    return result
