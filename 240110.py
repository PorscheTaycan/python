#재귀함수
#일부 반복문으로 대체 가능
#Recursion / Recursive
#def myfunc():
#함수가 자기 자신을 다시 호출하는 함수


#함수 f(x) 2x + 1 -> 일반적인 함수
#팩토리얼 -> 재귀함수
# n!
#n! = n * (n -1) * (n -2) ------- * 1

def fac(n):
    output = 1
    for i in range(1, n + 1):
        output *= i

    return output

print(fac(50))


#fac(n) = n*fac(n-1)

def fac2(n):
    if n == 0: #끝
        return 1
    else: # 더해줘야함
        return n*fac2(n-1)
print(fac2(3))

d1={'1':{"1":{"1":{"1":100000}}}}
d2={'1':2000}

def show(dic):
    if type(dic['1']) != int: #정수가 아닐 때
        show(dic['1'])
    else: #정수일 때
        print(dic['1'])

show(d1)
show(d2)

def flatten(data):
    out = []
    for item in data:
        if type(item)==list:
            out+=flatten(item)
        else:
            out.append(item)
    return out
a = [[1,2,3],[4,[5,6]],7,[8,9]]
print(flatten(a))

a = 2
b = 10
full = 100
memo = {}
def s (c,d):
    key = str([c,d])
    if key in memo:
        return(memo)[key]

    if c < 0:
        return 0
    if c == 0:
        return 1

    for i in range(key):
        if
