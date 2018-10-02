import requests
import random
import string


# def api_registration():
#     username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))
#     email = ("email={}@kluatr.ru".format(username))
#     payload = "firstName=test" \
#               "&lastName=testov" \
#               "&{}" \
#               "&password=111111" \
#               "&cardNumber=1111111" \
#               "&userMainRegisterForm=register" \
#               "&formName=userMainRegister".format(str(email))
#
#     url = "http://petrovich.efremov.dev.local/api/form"
#
#     headers = {
#         'content-type': "application/x-www-form-urlencoded",
#         'cache-control': "no-cache",
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(response.text)
#
#
# api_registration()


# def api_registration():
#     payload = "cardNumber=8787878" \
#               "&method=addAndGetFullCart"
#
#     url = "https://tver.petrovich.ru/api/pet/v001/user/card"
#
#     headers = {
#         'content-type': "application/x-www-form-urlencoded",
#         'cache-control': "no-cache",
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(response.text)
#
#
# while True:
#     api_registration()

def petlocal():
    payload = "PAGE_PARAMS[ELEMENT_ID]=143465" \
              "&AJAX_CALL=Y="\
              "&vote=Y" \
              "&vote_id_no=143445" \
              "&rating_no=0" \

    url = "http://petlocal.ru/bitrix/components/askaron/askaron.ibvote.iblock.vote/component.php"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)