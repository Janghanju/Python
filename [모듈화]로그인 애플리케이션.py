import 모듈3_auth
input_id = input("아이디를 입력해주세요. \n")

if 모듈3_auth.login(input_id):
    print("Hello, "+input_id)
else:
    print("Who are you?")
