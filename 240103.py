#< 프로그램 오류 4가지 >
#sytaxerror : 문법 오류가 있는 상태
#type error : 문자 + 숫자 데이터 형태 문제
#index error : "helle"[10] => index out of range
#value error : 변환 불가능 한 값 변환 시도
#                1. 숫자가 아닌 것을 숫자로 변환하려 할 때
#                2. 소수점이 있는 문자열을 int로 변환하려 할 때

print(int(input("입력하세요: ")))

#숫자를 입력받습니다.
raw_input = input("inch 단위의 숫자를 입력해주세요 : ")

#입력받은 데이터를 숫자 자료형으로 변경하고, cm 단위로 변경합니다.
inch = int(raw_input)
cm = inch * 2.54

#출력합니다.
print(inch, "inch는 cm 단위로", cm, "cm입니다. ")

a = input("1문자 : ")
b = input("2문자 : ")
print(a, b)
temp = a
a=b
b=temp
print(a, b)


print("hello".isupper())


x = 10
y = 20
print("{}".format(10))
print("{} {}".format(10, 20))
print("x: {} y : {} x*y: {} x/y: {} x**y: {}".format(x, y, x+y, x*y, x**y))
#format 함수는 문자열의 {}내부에 format함수의 매개변수를 대입, 포매팅 하는 함수

#format() 함수로 숫자를 문자열로 변환하기
format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기 ".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
format_d = "{} {} {}".format(1, "문자열", True)

#출력하기
print(format_a)
print(format_b)
print(format_c)
print(format_d)

a= "HEllo ddddddd KKKKKK mmmmmmmm"
print(a.lower())
print(a)

a= "HEllo ddddddd KKKKKK mmmmmmmm"
b = a.lower()
print(b)
print(b.upper())
#원본을 변화시키지 않는 함수 : 비파괴 함수



#문자열 관련 함수
#1. lower()
#2. upper()
#3. strip() : 공백 제거
#4. lstirp() : 좌 공백 제거
#5. rstirp() : 우 공백 제거


s= """111


222    54456


333


"""

print(s)
x=(s.strip())
print(x)


#isalnum()
#isalpha()
#isdigit()
#isspace()

#find() 문자열 내부에 특정 문자가 어디에 위치하는지
aa= "안녕하세요.".find("안녕")
print(aa)

#문자열과 in 연산자
#in 키워드로 문자열 내부에 특정 문자열 존재 여부 확인

#split() 문자열 분리
a = "1 2 3 4 5 6 7".split(" ")
print(a)

#f문자열
x= 200
print(f"{x}")
print("{}".format(x))

#152p
r = int(input("구의 반지름을 입력해주세요 : "))
a = r*r*r*3.141592*(4/3)
b = 4*3.141592*r*r

print("= 구의 부피는", a, "입니다. ")
print("= 구의 겉넓이는", b, "입니다. ")

#153p
a = float(input("밑변의 길이를 입력해주세요 : "))
b = float(input("높이의 길이를 입력해주세요 : "))
c = (a*a + b*b)**(1/2)
print("= 빗변의 길이는 ", c , "입니다. ")


#count()
a = 'hello'
print(a.count('l')) #특정 문자 'l'의 개수 리턴

#index()
a="hello"
print(a.index('e')) #특정 문자 'e'의 위치 찾기
#문자열에서 위치를 찾는 함수 : find, index 두 종류
#find는 찾고자 하는 문자열이 없다면 -1 반환
#index는 찾고자 하는 문자열이 없으면 오류 발생

#replace(a,b) : 문자열에서 a를 b로 변경
a='hello'
print(a.replace('e', '1'))



#불 타입
#bool 자료형은 True 혹은 False를 나타내는 자료형이다.
#True : 참
#False : 거짓
#bool 타입은 보통 조건식과 함수의 리턴 값으로 나옴
print(1==1)
"abc" #true
""#false
[1, 2, 3]#true
[]#false
1#true
0#false

print(bool('abc'))
#bool 함수로 값의 참 거짓 식별 가능



#비교연산자
# == 같다
# >= 좌측이 크거나 같다
# > 좌측이 크다
# <= 우측이 크거나 같다
# < 우측이 크다
# != 같지 않다.


#리스트 데이터
#[1, 2, 3, 4, 5]
#여러 요소의 데이터를 하나로 묶어 하나의 데이터로 처리하는 데이터 형태
#대괄호로 생성
#각 요소는 쉼표로 구분한다.


#리스트 내부에 리스트 포함(중첩) 가능
a=[] # 빈리스트
a=[1] #숫자 요소1 리스트
a=[1,2,3] # 숫자 3개 요소 리스트
a=[1, "a"] #숫자와 문자 혼합 요소 리스트
a=[1, []] #2중 리스트
a= [1,2, [3, [4, ["a"]]]] #4중 리스트

#빈 리스트 생성 방법1 : 대괄호로 생성
a = []
#빈 리스트 생성 방법2 : list함수로 생성
a =list()

#리스트 인덱싱
a=[1,2,3]
print(a[0])
a[0] = 100
print(a)


# 문자열은 데이터를 바꿀 수 없음.
s = "abcde"
print(s[0])
s[0] = "m"


a= [1,2,3,[4,5,6,[7,8,9]]] # 2중 리스트
print(a[-1][-1][-1])

#리스트 슬라이싱
a=[1,2,3,4,5]
print(a[0:2])


#리스트 연산
a=[1,2,3]
b=[4,5,6]
print(a+b)

#리스트 연산 *
a=[2,3,4]
print(a*3)

#len() 함수로 요소 개수 반환
a=[1,2,3,4,5]
print(len(a))


#리스트 요소 삭제 del 키워드
a = [1,2,3]
del a[0]
print(a)

b = [1,2,3,4,5,6]
del b[2:4]
print(b)


#리스트 관련 함수
#append() 리스트에 요소 추가
a= [1,2,3]
a.append(4)
print(a)

a.append("A")
a.append([2,2])
print(a)

#sort() 리스트 정렬 함수
a= [1,4,3,2]
a.sort()
print(a)

#reverse() 리스트 뒤집는 함수
a=['a', 'c', 'b']
a.sort()
a.reverse()
print(a)

#index() 리스트 요소 찾기 함수
a=[1,2,3]
print(a.index(3))
print(a.index(100))

#append는 마지막 요소에 추가하는 방식
#insert는 지정 위치에 추가하는 방식
#insert(위치,값)
a = [1,2,3]
a.insert(0, 4)
print(a)


#remove() 함수로 리스트 요소 제거
a=[1,2,3,4,5,3,3,3,3,3,3,3]
a.remove(3)
print(a)

print(3 in a)

#pop() 마지막 요소 꺼내기
a = [1,2,3]
print(a.pop())
print(a)

#count() 특정 요소 개수 카운트
a=[1,2,3,4,5,5,5,5,5]
print(a.count(5))

#extend() : 리스트 더하기
a=[1,2,3]
a.extend([4,5])
print(a)


a=[1,2,3]
b=a+[4,5]
print(b)

a=[1,2,3]
a+=[4,5]
print(a)

#문자열의 join함수 : 구분자텍스트.join("문자열")
a="abc"
res='aaa'.join("xxx")
print(res)


#딕셔너리 데이터 형태
#{ }로 선언
#딕셔너리는 key:value의 쌍으로 구성된 데이터
#{key:value,key2:value2,key3:value3}
# 3개의 key:value 쌍으로 구성


d = {' name' : 'a', 'age': '20', 'loc' :  'korea'}

print(d)
print(type(d))

#딕셔너리 쌍 추가 및 삭제
#딕셔너리는 []에 key값 사용
#딕셔너리에 쌍 추가
a={1:'a'}
a[2] = 'b'
print(a)
print(a[1])

#딕셔너리 쌍 제거
del a[1]
print(a)

#딕셔너리 생성시 주의사항
#딕셔너리의 key는 고유한 값으로 중복이 되면 하나를 제외한 나머지 것이 모두 무시 됨
#동일한 key가 여러개 존재하지 않도록 생성
#변하지 않는 값 : immutable : int, float, tuple
#변할 수 있는 값 : mutable : list, set, dictionary
#딕셔너리의 key는 고유해야하고, 변하지 않는 값을 쓴다.
#따라서 딕셔너리의 키에 list는 불가능
#딕셔너리의 value는 어떤 값이나 가능하다.


#딕셔너리 관련 함수
#keys()
d={'name':'a','age':20, 'loc':[38.2222,111.2222]}
print(type(d.keys()))
print(d[list(d.keys()[0])])

#dictionary에 .keys()함수를 호출하면 dict_keys객체를 리턴(반환)한다.
print(type(d.keys())) #<class 'dict_keys'>
#dict_keys는 list()함수를 사용하여 list로 변환이 가능하다.
keyList=list(d.keys()) #리스트 변환 후 부터 리스트 인덱싱이 가능
print(keyList[0])


#values() 함수 : keys함수는 key객체 , values함수는 values객체 리턴
print(d.values()) #dict_values객체도 list로 변환
valueList=list(d.values())
print(valueList[0])


#key와 value를 쌍으로 얻는 item()함수
print(d.items()) #items()함수는 dict_items객체를 리턴한다.
itemsList=list(d.items())
print(itemsList[0]) #itemsList의 0번째 인덱스는 튜플 형태의 (키, 밸류) 데이터


#clear()함수 : 딕셔너리 비우기
d.clear()
print(d)

x={'a':1, 'b':2, 'c':3}
for i in range(len(x)):
    print(x[list(x.keys())[i]])

print(x.get('a'))
print(x['a'])
#get(x) 함수는 x라는 키에 대응하는 value를 얻을 수 있다.
#x['a']에서 a키가 없을 때 오류 발생
#get('a')에서 a키가 딕셔너리 내에 없으면 None을 리턴


print("안녕" in "안녕하세요")
print(3 in [1,2,3])
print('a' in x)
while 'a' in x:
    print("11111111111111")


#튜플 tuple 자료형
#튜플은 리스트와 비슷하지만 차이점이 있다.
#튜플은 (,)형태로 선언
#리스트는 요소 값 변경 가능/ 튜플은 변경 불가능

t = () #빈 튜플
t = (1, ) #요소가 하나일 때 쉼표를 넣어준다.
t = (1,2,3)
t = (1, 2,(3, 4))
tt = 1,2,3,4,5, "DDDDD"

print(type(tt))

print(tt[0])
print(len(tt))


#set 집합 자료형
s = set([1,2,3])
print(s)

s = set("hello")
print(s)
#중복을 허용하지 않는다.
#unordered 순서가 없어서 h e l o / o l e h로 나오게 된다
#unorderd 순서가 없음.
#orderd 순서가 있음.

#교집합 / 합집합 / 차집합

s1 = set([1,2,3,4,5,6])
s2 = set([7,8,9,10,5,6])

print(s1&s2) #교집합
print(s1.intersection(s2)) #함수를 이용한 교집합 반환

print(s1|s2) #합집합
print(s1.union(s2))  #함수를 이용한 합집합 반환

print(s2-s1) #차집합
print(s2.difference(s1)) #함수 이용 차집합 반환


#집합에 값 추가 add함수
s1.add(100)
print(s1)
#집합에서 값 제거 remove함수
s1.remove(1)
print(s1)




#if 조건문
print("가방"< "하마")
x = 50
print(10<x)
print(x<100)
print(10<x<100)

#and 연산자 : 양쪽 항이 모두 참일 때 -> 참
#or 연산자 : 한 쪽 항만 참이면 -> 참
#not 연산자 : 반대로 전환


print(not True)
x = 10
under20 = x<20
print(under20)

print(x<20 and x <200)

print(x<20 or x <200)

print(x<20 and x <1)
print(x<20 or x <1)

#if 조건문 상황을 나누어 실행 여부 결정

#if문의 형태
#if 조건식 :
#   수행문
#   수행문
#   수행문

x = 100
if x>50:
    print(x)
    print(x+1)
    print(x+2)
    print(x+3)

#입력을 받습니다.
number = input("정수입력 > ")
number = int(number)

#양수 조건
if number > 0:
    print("양수입니다.")

#음수 조건
if number < 0:
    print("음수입니다.")

#0조건
if number == 0:
    print("0입니다.")


if True:
    #들여쓰기 indent
    print()

#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/ 시간을 구합니다.
now = datetime.datetime.now()

#출력합니다.
print(now.year, "년")
print(now.month, " 월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

#if문의 구조
"""

if 조건식:
    if조건식이 참일 때 실행할 문장-1
    if조건식이 참일 때 실행할 문장-2
    if조건식이 참일 때 실행할 문장-3
else:
    if조건식이 참이 아닐 때 실행할 문장-1
    if조건식이 참이 아닐 때 실행할 문장-2
    if조건식이 참이 아닐 때 실행할 문장-3


"""

import datetime
now=datetime.datetime.now()
print(now)
print(type(now))

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now = datetime.datetime.now()

#오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다. !".format(now.hour))

#오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다. !".format(now.hour))



#사용자에게 70~100사이 숫자를 입력받고
#if문을 이용해서
#사용자가 입력한 숫자가 60미만이면 F
#60이상이면 D
#70이상이면 C
#80이상이면 B
#90이상이면 A 출력
user_input = input("0~100 사이 숫자 입력하시오 : ")
if user_input.isdigit()():
    user_input=int(user_input)
    if user_input<60:
        print("F")
    if user_input>=60:
        print("D")
    if user_input>=70:
        print("C")
    if user_input>=80:
        print("B")
    if user_input>=90:
        print("A")



last_number = 4
if last_number == 0 \
    or last_number == 2 \
    or last_number == 4 \
    or last_number == 6 \
    or last_number == 8:
    print("짝수입니다.")

if str(last_number) in "02468":

#if number % 2 == 0:

#하나의 if 조건문 세트 내에서
#if 무조건 처음, 하나만 가능, 조건식 필요
#elif 여러개 가능, 생략 가능, 조건식 필요
#else 생략가능, 하나만 가능, 조건식 불필요


number = input("정수입력")
number = int(number)

if number%2 == 0:
    print("짝")
else:
    print("홀")

#날짜/ 시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/ 시간을 구하고
# 쉽게 사용할 수 있게 월을 변수에 저장합니다.

now = datetime.datetime.now()
month = now.month

#조건문으로 계절을 확인합니다.
if 3 <= month <=5:
    print("현재는 봄입니다.")

elif 6 <= month <= 8:
    print("현재는 여름입니다.")

elif 9 <= month <= 11:
    print("현재는 가을입니다.")

else:
    print("현재는 겨울입니다.")


#사용자는 가진 돈을 입력한다.
#택시 요금은 5,000원이다.
#datetime을 이용해서 요일을 조회하고, 평일이면 학원을 가야하며 주말이면 학원을 가지 않는다.
#사용자는 날씨가 맑음 or 비 중 하나를 입력한다.
#날씨가 비가오면 택시를 타고 맑으면 걸어온다.


import datetime

now = datetime.datetime.today().weekday()
if now < 5 :
    money = int(input("가진 돈을 입력하세오 : "))
    if money >= 5000:
        w = input("맑음 or 비 둘 중 하나를 입력하세요 : ")
        if w == "맑음":
            print("걸어간다.")
        elif w == "비":
            print("택시를 타고 간다. ")
    else:
        print("걸어간다.")
else:
    print("학원을 가지 않아도 된다. ")




#188p

import datetime
now = datetime.datetime.now()

a = input("입력 :")
if a == ("안녕"):
    print("안녕하세요.")
elif a == ("안녕하세요."):
    print("안녕하세요.")
elif a == ("지금 몇 시야?"):
    print("지금은 ",now.hour, "시 입니다." )
elif a == ("지금 몇 시예요?"):
    print("지금은 ",now.hour, "시 입니다." )
elif (a in a):
    print(a)

#189p
a = int(input("정수를 입력해주세요 : "))
if a%2 != 0:
    print("2로 나누어 떨어지는 숫자가 아닙니다. ")
else:
    print("2로 나누어 떨어지는 숫자 입니다.")
if a%3 !=0:
    print("3으로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print("3으로 나누어 떨어지는 숫자 입니다.")
if a % 4 != 0:
    print("4로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print("4로 나누어 떨어지는 숫자 입니다.")
if a % 5 != 0:
    print("5로 나누어 떨어지는 숫자가 아닙니다.")
else:
    print("5로 나누어 떨어지는 숫자입니다.")




