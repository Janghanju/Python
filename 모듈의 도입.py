#egoing을 a에 모듈화하고 그 이름을 z로 약속한다.
from egoing import a as z
#k8805를 모듈화하고 그 이름을 k로 약속한다.
import k8805 as k
#z로 약속한 egoing이란 모듈의 a의 값을 출력한다.
print(z())
#k로 약속한 모듈 k8805의 a를 출력한다.
print(k.a())
