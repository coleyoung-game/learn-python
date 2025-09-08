"""
기본 문법을 숙지하기 위한 py 파일
"""


# 큰 따옴표 3개(줄바꿈)
#conversation = """hi my name is young 
#can i know your name? """
#print(conversation)
# 문자열 곱하기
#print("=" *50)
#print("My Program")
#print("=" *50)
# 문자열 슬라이싱(리스트 슬라이싱과 동일)
# 끝 번호에 해당하는 건 포함하지 않음
# 이상:미만
coolSyntax = "Life is too short, You need Python"
print(coolSyntax[0:4])
print(coolSyntax[5:7])
# 8번 인덱스부터 끝까지
print(coolSyntax[8:])
# 0부터 8번 인덱스까지
print(coolSyntax[:8])
# 전체
print(coolSyntax[:])
# 빼기 기호 사용 가능(뒤부터 시작)
print(coolSyntax[19:-7])

print("="*50)

# List 연산
a = [1, 2, 3]
b = [4, 5, 6]
# 합쳐진다[1, 2, 3, 4, 5, 6]
c = a + b
# 곱해진다 => [1, 2, 3, 1, 2, 3, 1, 2, 3]
d = a * 3
print(c)

print("="*50)
# Tuple
# 요소들을 ()로 둘러싼다
# 요솟값을 바꿀 수 없다
# dictionary key로 사용할 수 있음
# 처리 속도가 약간 더 빠름

# 함수가 여러 값을 반환할 때 사용하면 편리
# 함수 반환 값을 받는 단일 변수는 인덱스 접근이 가능하다.
# 보통은 언패킹 형식으로 받는다. -> 반환 값의 개수 만큼 변수를 선언한다.

# 생성 방법 
t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 괄호를 생략해도 됨
t5 = ('a', 'b', ('ab', 'cd'))

# Dictionary
# 생성
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
# Key는 Immutable Type이면 가능(튜플도 가능)
# Value엔 어떤 타입이든 넣을 수 있음(리스트 포함)
a = {'a': [1, 2, 3]}
# 쌍 추가
a[5] = 'b'

# get으로 value 값을 가져오면, 데이터가 없을 때 None으로 반환한다. -> 예외처리에 더 좋음
a.get('noke')
# 값이 없으면 '정보없음'이 반환 됨
test_result = a.get('noke', 'infomation not found.')
print(test_result)

print("="*50)
# Set(집합)
# 중복을 허용하지 않는다.
# 순서가 없다
# 인덱싱을 통해 요솟값을 얻을 수 없음

# 자료형에 참과 거짓이 존재 1, 0 / 'something' / ''

# python list 복사
a = [1, 2, 3]
# reference copy(참조 복사)
# 요소의 모든 주소를 참조
# ex) a = [1, 2 [1, 2]] -> 리스트 안에 있는 리스트의 주소도 참조 됨
b = a 
# shallow copy(얕은 복사)
# 새로운 리스트 객체를 생성
# 만약 리스트 안에 리스트가 있다면, 그 리스트의 참조 값은 Reference copy처리 된다.
b = a[:]
b = a.copy()
# deep copy(깊은 복사)
# copy 모듈의 deepcopy 함수 사용 해야 함
# 원본 리스트와 그 안에 있는 모든 요소들을 완전히 새로운 객체로 복사한다.

# 조건문
money = 2000
card = True
if money >= 3000 or card:
    print("You have to ride the taxi")
else:
    print("You have to walk")

# in 예약어
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("I'm rich boy")
else:
    print("i'm poor boy")

# 비교 연산자 연쇄 사용 가능
x = 5
1 < x < 10

# 조건부 표현식(삼항 연산자랑 비슷한듯)
score = 85
result = "accept" if score >= 60 else "fail"
print(result)

print("="*50)

# 반복문(while)

# while else문이 따로 존재한다.
while_count = 0
while while_count < 3:
    print(f"count: {while_count}")
    # 파이썬에선 후위 연산자가 없음(++, --)
    while_count += 1
else:
    print("end while")

print("="*50)

# 반복문(for)

# 전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# for문에 List안에 있는 tuple 적용
test_tuple = [(1, 2), (3, 4), (5, 6)]
for (first, last) in test_tuple:
    print(first+last)

# range 함수 활용
# range는 객체이다.

# for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end=" ")
    print('')

# list comprehension
list_nums = [1,2,3,4]
result = [num * 3 for num in list_nums]
print(result)

# for문도 else문을 추가할 수 있다.(정상적으로 종료됐을 때 수행하는 로직 구현 가능)

# enumerate 함수 활용
# 인덱스와 값을 함께 구하고 싶을 때 사용
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# zip 함수로 여러 리스트 순회(3개 까지 가능?)
names = ['hong', 'kim', 'lee']
scores = [85, 92, 78]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

print("="*50)

# 함수

# 여러 개의 입력 값을 받는 함수
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(add_many(1, 2, 3, 4, 5))

# 여러 개의 입력 값을 받는 함수 - 응용

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

print(add_mul('add', 1, 2, 3, 4, 5))
print(add_mul('mul', 1, 2, 3, 4, 5))

# 키워드 매개변수, **kwargs
# 매개변수들을 딕셔너리 형태로 받는다

def print_kwargs(**kwargs):
    print(kwargs)

#{'a': 1} 
print_kwargs(a=1)

# 키워드 매개변수, kwargs - 응용
def create_profile(**info):
    print("=== Profile Information ===")
    for key, value in info.items():
        print(f"{key}: {value}")

profile = create_profile(name='kim', age=30, job='programmer', hobby = 'reading a book')
#print(profile)

# 일반 매개변수, 가변 매개변수(*), 키워드 매개변수(**) 혼합 활용
def mixed_function(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수: {kwargs}")

mixed_function('홍길동', 1, 2, 3, age=25, citiy='서울')

# 리스트나 딕셔너리는 함수에서 변경 가능(레퍼런스 카피)