import keyword
print(keyword.kwlist)

#주석 처리 :인터프리터가 읽지 않도록 처리
# 키워드는 대소문자를 구분
#True
True
#true
#키워드는 개별적으로 기능을 가지고 있다.


#식별자 id  print()이것도 식별자임
#키워드는 식별자로 사용 X
#특수문자는 언더바 _만 허용
#숫자로 시작할 수 없다.
#공백을 포함 X
x=10

#스네이크 케이스 : 단어 사이 언더바를 붙여 생성하는 방식
#item_list
#캐멀 케이스 : 단어들의 첫 글자를 대문자로 작성하여 구분하는 방식
#ItemList

#연산자
#값과 값 사이에 연산 기능
#단독적으로 사용 X

#리터럴 : 자료
1
"ㅍㅍㅍㅍㅍㅍ"
print()
#파이참에서 IDE 에서 함수는 보라색
#print() 콘솔에 출력하는 함수

print(20)
print("234235")

print("Hello World")

# 하나만 사용합니다.
print("# 하나만 출력합니다. ")
print("Hello Python Programming...!")
print()

#여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "윤인성입니다!")
print()

#아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")


#문자열 : 텍스트
#숫자 : 50, 100, 100.1
#불 : True/ False


print(10)
print(type(10))
print(type("hello"))
print(type(True))

#문자열
#따옴표로 텍스트를 감싸준다.
#'hello'
#"hello"
#문자열은 공백 포함 가능
#문자열의 공백은 문자열의 길이에 포함된다.
# 큰 따옴표와 작은 따옴표 같이 쓰는 경우

print("'안녕하세요'라고 말했다. ")
print(len("'안녕하세요'라고 말했다. "))
print(len(" "))

#syntax error 구문 오류 or 문법 오류
#빨간 밑줄 부분

#이스케이프 코드
#\t : 탭 기능
#\n : 줄 바꿈 기능
#\\ : \ 문자 그대로 표현하는 기능
#\' : 작은 따옴표 작성
#\" : 큰 따옴표 작성
print("안녕하세요\n안녕하세요")
print("안녕하세요\t안녕하세요")

print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("구름 \t 3\t강서구")
print("HH\tHHHHH\nHHHHHH\'HHH\"HH")

print("""123""")
print("""123

\t123
1111123 111~~
""")

print("12"
      "3")

#연산자
# + - / *
#1. 문자열 + 문자열 : 문자열의 연결 결과
print("ABC" + "DEF")

# 2. 문자 + 숫자 : 불가능
# print("hello" + 100)

#3. 문자열 * 숫자 : 문자열 반복
print("123"* 10)

#문자열의 인덱싱
#대괄호 안에 인덱스 번호
#인덱스 번호는 첫 자리가 0
#제로 인덱스
# -1은 마지막 인덱스를 의미

x = "hello"
print(x)

print(x[1])
print(x[-1])

print(x[-2])

print("안녕하세요"[0])
print("안녕하세요"[-1])

#문자열의 슬라이싱
#대괄호 안에 start:end 형태로 사용
#ex) [0:4]
#start <= x < end
print("안녕하세요"[0:4])
#슬라이싱에서 : 의 좌우를 비우면 끝에서 끝을 의미
print("안녕하세요"[:])


#IndexError(index out of range)

#print("안녕하세요"[5])

print(len("안녕하세요     "))

#숫자 데이터
# 정수 실수로 구분
# 정수 int : 0, 1, 100, -100
#실수 float : 0.0, 1.5, -100.2
#floating point 부동 소수점
#소수점이 움직이는 숫자
# ex) 52.273 = 0.52273 x 10의 2제곱
# ex) 52.273 = 5.2273 x 10의 1제곱

print(200)
print("200")
print(100.0)
print(type(100.0))
print(type(100))

#숫자의 연산자
#+ - * /
#숫자는 사칙연산 모두 사용가능
# 문자열은 + 와 * 만 가능
# // : 나눈 몫을 구하는 연산자
#% : 나눈 나머지를 구하는 연산자

print(4/2)
#정수와 정수의 사칙 연산 중 나누기 연산은 실수 형태 결과
print(4//2)
#//연산자는 정수형태로 몫만
print(4%2)
# %는 나머지 값 결과


print(10//3) # 10을 3으로 나눈 몫
print(10%3) # 10을 3으로 나눈 나머지


#제곱연산자 **
print(5**2)
print(5**3)

#변수
pi = 3.141592
x=10
y=20
x1="ddddd"

print(id(10))
print(id(11))

x=y
print(id(y))
print(id(x))
a=10
b=20
print(a*b)

#변수 선언과 할당
pi = 3.14159265
r = 10

#변수 참조
print("원주율 = ", pi)
print("반지름 = ", r)
print("원의 둘레 = ", 2 * pi * r)
print("원의 넓이 = ", pi * r * r)
print("원주율 = ", a, b, a*b, a+100)

#대입 연산자 : =
# ex) x = 10 형태롤 우측항의 값을 대입연산자 좌측항에 할당
#복합 대입 연산자 :
# +=
# -=
# *=
# /=

x= 100
x+=1 #1번식 : 복합 연산자 활용 O 숫자 덧셈 후 대입
x=x+1 # 2번식 : 복합 대입 연산자 활용 X
#1번과 2번은 같은 기능을 한다.

print(x)


x-=100
print(x)
x=x*100
print(x)


y="안녕하세요"
y+="!!"
print(y)
y*=3
print(y)

#사용자 입력 함수 input()
y = input("값을 입력해주세요:")
print("after input ")
print(y)

#input 함수 괄호 안에 입력한 내용을 프롬프트 문자열이라고 한다.
#사용자에게 입력 요구하는 안내 멘트.

#인터프리터 방식인 파이썬이 input함수를 호출 call 하면
#실행 도중에 해당 라인에서 블록 상태가 된다.

z = input("타입 확인을 위한 사용자 값 입력 : ")
#input을 통해 입력한 값은 전부 문자열로 처리 됨.

z = int(z)
print(type(z))
print(z)

z = float(z)
z = str(z)
print(type(z))

print(z)
print(len(z))
float(z[2:])
print(z)

string_a = input("입력A> ")
int_a = int(string_a)

string_b = input("입력B> ")
int_b = int(string_b)

print("문자열 자료: ", string_a + string_b)
print("숫자 자료: ", int_a + int_b)


output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a)
print(type(output_b), output_b)

input_a = float(input("첫 번째 숫자>"))
input_b = float(input("두 번째 숫자>"))

print("덧셈 결과:", input_a + input_b)
print("뺄셈 결과:", input_a - input_b)
print("곱셈 결과:", input_a * input_b)
print("나눗셈 결과:", input_a / input_b)





