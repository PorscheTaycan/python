#240111

#튜플
#괄호가 없는 튜플
#만들면
#return 으로 반환 받는 형태로 튜플이 많이 쓰임
def xxx():
    return

tp = 10,20,30,40
print(tp)

a,b = 10, 20
print(a)
print(b)
a,b = b,a
print(a)
print(b)


#람다 lambda 표현
#함수의 표현법 중 하나
def xxxx(): #사용자 함수를 정의만 함
    print("xxxx함수가 호출되었다.")


#호출 부분은 따로 존재
xxxx()


def call(func):
    for i in range(10):
        func()

def print_hello():
    print('안녕하세요')

call(print_hello) #콜백 함수 사용 방법
#콜백 함수 : 함수의 매개변수에 사용되는 함수
#콜백함수 : 함수 ()이 아니라 함수의 명 전달

def play(func):
    for i in range(10):
        func()

def a ():
    print('a')
def b ():
    print('b')
def c ():
    print('c')

play(a)


#filter함수
#map함수
#함수를 매개변수로 사용하는 대표적인 함수들
#map(함수, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트 구성
#filter(함수명, 리스트) : 리스트의 요소를 함수에 넣고 리턴된 값이 True인 것으로 새로운 리스트 구성


def power(item): #item-> 매개변수
    return item * item
def under_3(item):
    return item < 3

list_input_a = [1,2,3,4,5]
output = map(power, list_input_a)
print("#map() 함수의 실행결과")
print("map(power, list):", output)
print("map(power, list):", list(output))
print()

output_b = filter(under_3, list_input_a)
print("#filter() 함수의 실행 결과")
print("filter(under_3, list):", output_b)
print("filter(under_3, list): ", list(output_b))


#filter object와 map object는 제너레이터라고 한다.
#메모리 절약을 위해서 제너레이터 object형태로 반환이 온다.
#제너레이터 내부 값을 조회하려면 list로 형 변환



#일반 함수 (사용자 정의 def)
#재귀 함수 :
# 1. 탈출 조건이 있어야 함
# 2. 문제 해결 방법이 동일

#콜백 함수


#람다 : 코드 중간에 정의와 호출을 하는 방법
#def를 사용하지 않는다. (정의 단계가 없다.)
#함수를 간단하게 선언하는 방법


a = map(lambda x: x * x, [1,2,3,4,5])
print(a)
print(list(a))

#람다 사용 장점 : 미리 선언되지 않은 함수를 코드 중간에 선언 가능
#람다 사용 단점 : 간단한 return 방식의 함수 구상만 가능\


#파일 처리
#파일 관련 처리 내장 함수

#파일 열기 함수 open
#파일 읽기 함수 read
#파일 쓰기 함수 write
#파일 닫기 함수 close


#open()
#파일 오픈 함수의 매개변수
#1. 파일 경로 : 파일경로는 문자열로 처리
#2. 파일 오픈 모드
#   2-1. 오픈 모드 w : write모드(새로쓰기)
#   2-2. 오픈 모드 a : append모드(이어쓰기)
#   2-3. 오픈 모드 r : read모드(읽기)


file= open("basic.txt", 'w') #파일이 생성이 된다. 왼쪽에 새로 만들기 모드임
file .write('hello python')
file .write('hello python')
file .write('hello python')
file .write('hello python')
file .write('hello python')
file .write('hello python')
file .write('hello python')
file .write('hello python')


file.close() # 파일을 열면 항상 닫아줘야 한다.
#파일이 중복으로 열리면 생기는 문제 방지 하기 위해서 닫아줘야 한다.



#with 방식으로 파일을 여는 방법
with open('basic.txt', 'w') as f: # 얘는 close 안 해도 됨. 이유가 들여쓰기 되어있어서 할 일 끝나면 알아서 닫힘
    # #그리고 위에 작성한 것이 다 날라가는데 w 모드가 되어있어서 새로 만들기가 적용 됨
    f.write('hello ')
    f.write('hello ')
    f.write('hello ')
    f.write('hello ')


#with open() as f : 방식으로 파일을 오픈하면 close를 생략 가능


#텍스트 읽기
#read()
with open('basic.txt', 'r') as f1:
    contents = f1.read()
print(contents)

#텍스트 한 줄씩 읽기
#데이터를 구조적으로 표현하는 형식 CSV, JSON, XML
#ex) CSV
#이름, 키, 몸무게
#A, 170, 70
#B, 160, 60

#CSV파일은 한 줄에 하나의 데이터
#쉼표로 데이터 구분
#첫 줄은 데이터의 헤어 ( 헤더는 데이터가 무엇을 나타내는지 )



import random

hanguls = list('가나다라마바사아자차카타파하')

with open('info.csv', 'w') as file:
    file.write("{}, {}, {}\n".format('이름', '체중', '신장'))
    for i in range(1000):

        name = random.choice(hanguls) + random.choice(hanguls)
        w = random.randrange(40, 100)
        h = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, w, h))


with open('info.txt', 'r') as file:
    for line in file:
        (n, w, h) = line.strip().split(", ")

        if (not n) or (not w) or (not h):
            continue
        bmi = int(w) / ((int(h) / 100) ** 2)
        result = ''
        if 25 <= bmi:
            result = '과체중'
        elif 19.5 <= bmi:
            result = '정상 체중'
        else:
            result = '저체중'

        print('\n'.join(['이름 : {}', '몸무게 : {}', '키 : {}', 'BMI : {}', '결과 : {}']).format(n, w, h, bmi, result))
        print()

def Hanoi_Top(circle, x, y, z ):
    global count
    if circle == 1:
        count += 1
        print(x,'-> ', y)
        return


    else:
        Hanoi_Top(circle-1, x, z, y)
        #A C B #가장 아래를 제외한 모든 원판 내려놓기
        print(x,'->',y) #최하단 원판 옮기기 : 1회
        count+=1
        Hanoi_Top(circle-1, z, y, x)
        #C B A #가장 아래 원판 제외한 내려놓은 원판을
        #가장 아래원판의 위에 올리기
    Hanoi_Top(circle-1, 'z', 'y', 'x')

def move (n):
    return (2**n) -1

i = int(input('원판의 개수를 입력해주세요 ' ))
Hanoi_Top(i, 'x', 'y', 'z')
print(f'이동횟수는 {count}회 입니다.')
