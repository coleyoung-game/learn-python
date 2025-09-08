def add(a, b):
    return a + b

def sub(a, b): 
    return a-b

# import시 바로 실행 하게 됨.
# print(add(1, 4))
# print(sub(4, 2))

# __name__ 변수
# 직접 .py 파일을 실행할 땐 내부의 __name__ 변수엔 __main__값이 저장된다.
# 다른 파이썬 모듈에서 module_1을 import할 경우에는 __name__변수에 module_1이 저장된다.
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))