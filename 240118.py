# 240118 클래스

#객체 지향 프로그래밍 언어
#객체 개체 object : OOP
#객체를 우선으로 생각해서 프로그래밍을 한다
#클래스 기반의 프로그래밍 언어
#클래스를 기반으로 객체를 생성한다.


#필요한 요소만을 사용해서 객체를 표현하는 것 : 추상화
#속성을 가질 수 있는 것 : 객체


#클래스 사용 : 틀을 정의
class calssname:                                                            #클래스 틀 만들고(classname)
    def __init__(self): #생성자 함수의 정의 __init__(self)
        pass

#클래스 내부 함수는 첫 매개변수로 self 입력
#self : 자기 자신



#클래스는 클래스 이름과 같은 함수(생성자)를 통해 객체를 만들어 낸다.                   #클래스 틀 만든다.(classname1)
classname1 = calssname() #classname클래스를 틀로 사용해서 classname1로 만듦.
print(classname1)

class Student:
    num = 1
    def __init__(self, name): # 생성자 함수
        self.name=name #self는 자기자신 #name 변수를 만든 것 # 뒤에 name은 매개변수
        self.age=100
        print('생성자')
    def __del__(self):
        print("소멸자")
    def xxx(self):
        self.name="111"



students = [Student('1번학생'), Student('2번학생')]
print(students)


x = Student("3번 학생")
print(type(x))
print(x.num)
print(x.age)
print(x.name)
print(Student.num)
# print(student.age) 출력 불가
x.xxx()





#학생을 생성할 수 있는 클래스 구조를 만든다.
#모든 학생은 1번 강의실에 소속되어있다.  #공통사항 -> 변수
#개인별 학생은 이름, 나이, 국어, 영어, 수학   #개별사항 -> self변수
#학생을 객체로 3명 만들어서
#학생 중 성적의 평균이 가장 높은 학생의 [소속강의실 번호, 이름, 나이]를 출력

#내가 푼 것
class Student:


    def __init__(self, name, age, korean, math, english):
        self.name = name
        self.age = age
        self.korean = korean
        self.math = math
        self.english = english

    def get_sum(self):
        return self.korean + self.math + self.english

    def get_avg(self):
        return self.get_sum() / 3



    def num_class(self):
        return "1강의실"

    def to_string(self):
        return "{}\n{}\n{}".format(self.num_class(),self.name ,self.age)


def get_max(x1):
    return max(x1.get_avg())

students = [Student('1번학생', 21,80,95,100 ),
            Student('2번학생',24,70,90,95),
            Student("3번학생",20,90,95,80)]

for student in students:
    print(student.to_string())
    print(get_max())



#강사님 해설
class Stu:
    classname = "classroom_1"
    def __init__(self, name, age, sub1, sub2, sub3):
        self.name=name
        self.age=age
        self.sub1=sub1
        self.sub2 = sub2
        self.sub3 = sub3
        self.avg=0
    def cal_avg(self):
        self.avg=(self.sub1+self.sub2+self.sub3)/3
        return (self.sub1+self.sub2+self.sub3)/3
stulist=[Stu("1번학생", 21, 80, 70, 80),
         Stu("2번학생", 22, 30, 40, 50),
         Stu("3번학생", 23, 60, 70, 50)]

for i in stulist:
    i.cal_avg()

max=[0,0]
for idx,i in enumerate(stulist):
    if i.avg>max[0]:
        max[0]=i.avg
        max[1]=i.name
print(max[1])


print(stulist[0].cal_avg())
print(stulist[0].avg)