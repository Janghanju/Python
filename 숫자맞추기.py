#조건문사용
#변수 dap지정
#랜덤문 randomint()
#반복문 while XXXX(True, false 둘중하나로 지정) :, break(True지정시 정답값이면 멈춤)
#반복문2 for 변수 range(시작값,최대값)
#값 입력문 input()
import random

dap=random.randint(1,10000)

while True :
    
    x= input("1 ~ 10000까지의 숫자를 맞춰보세요: ")
    g= int(x)

    if dap == g:
       print("정답입니다.")
       break
    if dap < g:
       print("정답보다 큰 값입니다.")
    if dap > g:
       print("정답보다 작은 값입니다.")

print("게임 끝")
