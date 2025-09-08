from ast import IsNot
import module_1
# 모듈 이름, 모듈 함수
from module_1 import add
# 다중으로 불러올 수 있음
from module_1 import add, sub
# 모든 함수를 불러옴
from module_1 import *

#import module_2

result = add(3,4)
print(result)
result = sub(5,2)
print(result)


# 다른 디렉터리에 있는 모듈 가져오기.
import sys
# 해당 구문을 실행하면 저장 된다. (다시 실행할 땐 실행하면 안될듯)
sys.path.append("D:\Project\python\learn-python-git\learn_python\modules")
print(sys.path)
# 추가한 경로에 있는 module_2.py를 불러온다.
import module_2
result = module_2.add(3,4)

print(result)

