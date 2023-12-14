from mailtm import Email
from TempMail import TempMail, Inbox


def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])


def get_tmail_v1():
    test = Email()
    print("\nDomain: " + test.domain)

    test.register()
    print("\nEmail Adress: " + str(test.address))

    test.start(listener)
    print("\nWaiting for new emails...")


def get_tmail_v2():
    import requests

    url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/delete/id/%7Bmail_id%7D/"

    headers = {
        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
        "X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())


if __name__ == '__main__':
    get_tmail_v2()
