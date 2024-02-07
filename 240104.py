a = [1,2,3]
b = {'key1': 1,2:100, 4: 'ss'}
c = 100
d = 'ss'
e = 'ss'

print(id(a), ":a list id")
print(id(b), ":b dict id")
print(id(c), ":c int id")
print(id(d), ":d str ss id")
print(id(e), ":e str ss id")
print("--"*20)
print(id(a[0]), "a[0] list 0 idx id")
print(id(a[1]), "a[1] list 0 idx id")
print(id(a[2]), "a[2] list 0 idx id")

print("--"*20)
print(id(b['key1']))
print(id(b[2]))


#반복문 for
print(range(100))
print(type(range(100)))
if True:
    print("if실행문")
for i in range(3):
    print(i)
    print("for실행문")

#for i in 반복가능한 이터러블객체 :
#   실행문장
#   실행문장

for i in "hello":
    print("123123")


for i in [2,2,3,4,5,5,5,5,5]:
    print(i)

x=200
d1={"key1": 100, "key2": x}
for i in d1:
    print(i)
    print(d1[i])

print(i)

for i in list(d1.values()):
    print(i)

print(id(i))
print(id(x))

s="안녕하세요"
for i in s:
    print(i)

for i in range(len(s)):
    print(s[i])

s2='11111'
for i in s2:
    print(id(i))
print(id(s2))

print(id(d1))
print(id(d1['key1']))
print(id(d1.keys()))

x=[(1,2),(3,4),(5,6)]
for (a,b) in x:
    if a + b == 7:
        break
    print(a+b)



#continue 키워드
#for 반복문의 진행 중 continue 키워드가
#실행되면 for 문의 처음으로 돌아감.
#continue는 반복문의 자식으로만 사용 가능
#다음 바퀴로 ( 해당 바퀴 생략)

#break 키워드
#for 반복문의 진행 중 break 키워드가 실행되면
#for문을 완전히 탈출함.
#종료 ( 모든 바퀴 생략)


#range() 범위 객체를 생성하는 range 함수
r = range(10)
print(r)
print(list(r))

r1=range(5,10)
print(r1)


list2 = [[1,2,3],[4,5,6],[7,8,9]]

for x in list2:
    for a in x:
        print(a)



#리스트와 for문의 사용법 2
# case 1    정석임.
a = [1,2,3,4]
res = []
for num in a:
    res.append(num*3)

print(res)

#case 2
a = [1,2,3,4]
res=[num*3 for num in a if num%2 == 0] #if num%2 == 0 은 추가적인 조건임. 짝수의 결과만 나오게 if 문은 생략 가능
print(res)


#딕셔너리가 있다.
#딕셔너리에는 5개의 키가 있다.
#5개의 키는 5명의 사람 이름이다.
#value에는 각 인원의 키(cm), 몸무게(kg) 값이
#리스트로 묶여서 할당되어 있음

#사용자에게 어떤 사람인지를 입력받고
#입력 받는 사람의 키와 몸무게를 출력하는 코드
#bmi는 몸무게(kg)을 키의 제곱(m)로 나눈 값
#미터단위의 키는 소수점 2자리까지만 표현
#ex) 165cm -> 1.65m


a = {"유진":[161, 54], "민지":[184, 71], "지현":[134,38], "지은":[165,52], "가연":[160,50]}
b = input("사용자의 이름을 입력하시오 : ")
for name, data in a.items():
    if name == b:
        h, w = data
        bmi = w / ((h/100)**2)
        print("{}의 키는 {}cm 몸무게는 {}kg으로 bmi는 {:.1f}입니다".format(name, h, w, bmi))

character = {
    "name" : "기사",
    "level" : 12,
    "items" : {
        "sword" : "불꽃의 검",
        "armor" : "풀플레이트"
    },
    "skill" : ["베기", "세게 베기", "아주 세게 베기"]
}


#NameError 오류
name = 10
dict_key={"name":"망고", "type":"당절임"}

#반복문 while
#for문과 마찬가지로 실행문 반복하는 역할
#while문의 기본 구조 형태
#while 조건문:
#   실행문
#   실행문

#while문은 while뒤에 작성되어 있는 조건문이
#참인 동안 계속 반복된다.

count = 10
while count > 5:
    count -=1
    if count%2==0:
        continue
    print(count)

#while 에서도 continue와 break를 for문에서 사용하는 것과
#동일하게 작동한다.

num = 0
while num != 3:
    print("1. 음료 2. 햄버거 3. 나가기 ")
    userInput = int(input("메뉴 번호 선택하세요:"))
    print(num, "선택")
    break




#무한루프
#무한으로 반복되는 조건의 while문

count = 0
s = ""
while 1:
    count += 1
    if count == 10:
        break
    s+=str(count)
    for i in range (3):
        s+=","
        s+=str(i)
    print(s)
    s=""

count1 = 0
count2 = 0
while 1:
    print("1단계")
    count1+=1
    while 1:
        print("2단계")
        count+=2
        if count2>10:
            for i in range(3):
                print("for문")
            count2=0
            break
        print("227")
    print("228")
    if count1 == 3:
        break


output = ""

for i in range(1,10):
    for j in range(0, i):
        output += "*"
    output+= "\n"


print(output)

output = ""

for i in range(1, 15): # 1~14
    for j in range(14, i, -1): #14~i // 공백을 그리는 부분
        output += ' '
    for k in range(0, 2 * i -1): # 0~2*i -1 // 별 그리는 부분
        output += '*'
    output += '\n' #줄 바꿈 부분

print(list(range(1, 10, 2)))
print(list(range(10, 1, -1)))



print(output) # 최종 출력 부분


"""

$###############$
 $#############$
  $###########$
   $#########$
    $#######$
     $#####$
      $###$
       $#$
        $


"""

output = ""
for i in range(1, 15): # 1~14
    for j in range(0, i):  # 14~i // 공백을 그리는 부분
        output += ' '
    for k in range(17 - 2 * i): # 0~2*i -1 // 별 그리는 부분
        if k == 0 or k == 17-2*i -1:
            output += '$'
        else:
            output += '#'


    output += '\n' #줄 바꿈 부분
print(output) # 최종 출력 부분

#강사님
n = 8
print("-"*100)
n = int(input("몇 행?"))
o = '\n'
for i in range(n):
    o+= " " * i
    o+="$"
    o+="#"*(2*(n-i)-3)
    if i!=len(list(range(n)))-1:
        o+="$" #끝에 하나만 입력
    o+="\n"

print(o)

# 시간
# time
import time
print(time.time()) #UTC를 기준으로 나오는 시간

#시간과 관련된 기능을 가져옵니다.
import time

#변수를 선언합니다.
number = 0
print(time.time(), "start t")
#5초 동안 반복합니다.
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
print(number)
#출력합니다.
print("5초 동안 {} 번 반복했습니다.".format(number))

#시간이나 날짜시간 객체는 해당 함수를
#인터프리터가 읽어서 호출하는 시점의 시간을 반환
