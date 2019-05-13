
#문제1번

print("(%d - %d * %d)/%d = %d" %(50,5,6,4,(50-5*6)/4) )


#문제2번

print(17%3)


#문제3번

print("이름 : 장한주 ", "전화번번호 : 010-9124-4770")


#문제4번

A = input("변수 지정")
print(A)


#문제5번

A = int(input("숫자 입력"))

if A%2 == 0:
    print("짝수")
else:
    print("홀수")


#문제6번

A = int(input("첫번째 숫자"))
B = int(input("두번째 숫자"))

if A > B:
    print(A)
else:
    print(B)
    
#문제7번

A = int(input("자격증 시험점수"))

if A >= 60:
    print("합격")
else:
    print("불합격")
