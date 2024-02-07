#268p 1번
numbers = [1,2,3,4,1,2,3,1,4,1,2,3] #숫자 리스트 선언
count = {} # 숫자별 개수 저장하기 위한 빈 딕셔너리 선언
for number in numbers: #숫자를 하나씩 꺼내서
    if number not in count: #딕셔너리에 해당 숫자 키가 없다면
        count[number] = 0 #해당 숫자 키에 0 할당
    count[number] +=1 #해당 숫자 키 카운트를 1 올림
print("{}에서\n 사용된 숫자의 종류는 {}개입니다.\n 참고 : {}".format(numbers,len(count), count)) # 출력

#2번
#각 요소마다 몇 개 있는지 카운트하는 문제

DNA = input("염기 서열을 입력해주세요 : ")
count = {
    "a" : 0,
    "t" : 0,
    "g" : 0,
    "c" : 0,
    "s" : 0,
    "x" : 0
}
for i in DNA: #74~77까지는 1번 문제와 동일
    count[i] += 1
for key in count: # 출력 방식만 1번 문제와 다름
    print("{}의 개수 :{}.".format(key, count[key]))

#3번
DNA = "ctacaatgtcagtatacccattgcattagccgg"
for i in range(0, len(DNA), 3):  #0부터 str의 길이까지 3스텝
    sliced = DNA[i:i+3] #for문 첫 바퀴의 경우 i = 0, 0~3까지 슬라이싱
    if len(sliced) == 3: #슬라이싱 한 결과가 len값 3이면 출력
        print(sliced)

#4번
#중첩된 리스트를 1차원으로 평탄화하는 문제, 모든 중첩을 제거
l = [1, 2, [3, 4], 5, [6, 7], [8, 9]]
res = [] #평탄화 된 리스트를 담기 위한 빈 리스트 선언
for i in l: #원본 리스트에서 요소 하나씩 반복
    if type(i)==list: #i를 통해 꺼낸 요소의 타입이 리스트라면
        for j in i: #list를 다시 반복문으로 j를 통해 요소 하나씩
            res.append(j) #꺼낸 j요소를 res 리스트에 append
    else: #i를 통해 꺼낸 요소의 타입이 리스트가 아닌 경우
        res.append(i) # 바로 res에 추가
print(res) #출력


listb = [1,2,3,4]
x = len(listb)
print(x)

#함수 function, mehtod

#함수의 호출 = 함수의 사용 = call = ( )
#함수의 매개변수, 재료를 넣는다. ( )안에
#함수의 리턴 = 함수의 반환 = 함수의 결과 -> 있을 수도 있고, 없을 수도 있다.


#함수의 기본 형태
#def 키워드를 사용한다.

def myfunc(): #함수의 정의
    print("함수실행문1") #함수 내부 실행문
    print("함수실행문2")
    print("함수실행문3")
    print("함수실행문4")

myfunc() #함수의 호출
print(myfunc)
dict={"a" : 1}
print(myfunc)
print(dict.keys())
#매개변수 : 함수의 정의 측면에서 용이
#매개변수 : 함수에서 요구하는 재료 변수


def myfunc2(mV, nV):
    print(mV)
    print(nV)
    print(id(mV+nV))
    print(locals(), "local2")
    locals()['xx'] = 10
    print(locals(), "local3")
myfunc2(128, 129)
#print(m) 함수의 매개변수는 함수 내에서만 유효하다.

print(locals(), "4")

#parameter : 매개변수 ( 함수의 호출에서 전달한 값을 정의에서 받는 변수 )
#argument : 전달인자 ( 재료 )-> 128, 129 ( 함수 호출 시점에서 함수의 정의로 전달하는 값 )

#가변 매개변수 *
#가변 매개변수 뒤에는 일반 매개변수가 올 수 없다.
#가변 매개변수는 하나만 사용 가능

def myfunc3(a, b, *c):
    print(a,b,c)

myfunc3(1,2,3)

def print_n_times(n, *values):
    #n번 반복합니다.
    for i in range(n):
        #valuse는 리스트처럼 활용합니다.
        for value in values:
            print(value)
        #단순한 줄바꿈
        print()
#함수를 호출합니다.
print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")

#기본 매개변수
#매개변수 = 값 형태
#기본 매개변수는 기본 값을 가짐
#따라서 안 써도 되고 써도 되고
#default 값이 있음
print("첫 번째 줄",123,3,3,5,3, sep=" ", end= '\n', flush=False)
print("두 번째 줄")


def print_n_times(value, n=2):
    #n번 반복합니다.
    for i in range(n):
        print(value)

#함수를 호출합니다.
print_n_times("안녕하세요")


#함수를 정의합니다.
def return_test():
    print("A위치입니다.")
    return
    print("B위치입니다.")

#함수를 호출합니다.
return_test()


a = "hello"
print(a.replace('h', '!'))
print(a.upper)
print(a.strip())

b = [1,2]
print(b.append(3)) #None이 나오는 것 : return이 없는것
print(b)

def rt():
    print(1)
    return 100
    print(2)
rt()
print(rt())

#return은 함수 내에 작성 가능
#함수 내에서 return 키워드가 읽히면 함수를 탈출한다.
#return 뒤에 작성된 value를 들고 탈출함.
#return 뒤에 value가 없으면 None을 반환


#함수를 선언합니다.
def sum_all(start, end):
    #변수를 선언합니다.
    output = 0
    #반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1):
        output += i
    #리턴합니다.
    return output

#함수를 호출합니다.
print("0 to 100 : ", sum_all(0, 100))
print("0 to 1000 : ", sum_all(0, 1000))
print("50 to 100 : ", sum_all(50, 100))
print("500 to 1000 : ", sum_all(500, 1000))


#함수를 선언합니다.
def sum_all (start=0, end= 100, step = 1):
    #변수를 선언합니다.
    output = 0
    #반복문을 돌려 숫자를 더합니다.
    for i in range(start, end + 1, step):
        output += i
        #리턴합니다.
        return output

#함수를 호출합니다.
print("A.", sum_all(0, 100, 10))
print("B.", sum_all(end = 100))
print("C.", sum_all(end = 100, step = 2))
