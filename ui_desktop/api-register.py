import requests
import random
import string


def api_registration():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
    email = ("email={}@kluatr.ru".format(username))
    payload = "firstName=test" \
              "&lastName=testov" \
              "&{}" \
              "&password=111111" \
              "&cardNumber=1111111" \
              "&userMainRegisterForm=register" \
              "&formName=userMainRegister".format(str(email))

    url = "http://petrovich.efremov.dev.local/api/form"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)


api_registration()