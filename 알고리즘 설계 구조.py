#순차구조
print("아침기상")
print("씻는다.")
print("학교에 등교한다.")


#조건구조
point_ = int(input("점수를 입력하세요 : "))

if point_ >= 90:
    print("합격")
else:
    print("불합격")


#반복구조
password_ = input("비밀번호를 입력하세요 : ")

while password_ != ["qwer1234", "asdf1234"]:#가장 햇갈리는
    print("비밀번호가 틀렸습니다. 다시 입력해 : ")
    password_ = input("비밀번호를 입력하세요 : ")

print("인증완료! 문의 열립니다.")
