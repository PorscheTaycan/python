# 3가지 이상 함수 포함
#하나의 주제에 대한 모듈 ex) 원의 둘레 부피 등 계산
#모듈에 포함된 함수명, 매개변수, 사용법 메뉴얼을 추가 txt로 제공
#모듈 내 함수에서 자체적 print 사용하지 않음
#return 형태로 결과값 반환
#예외처리 적용, 매개변수 오류시 예외처리로 프로세스 종료 방지
# 원뿔, 원기둥, 정육면체, 삼각뿔, 삼각기둥, 사각뿔, 사각기둥 등..


def pyramid (a,b,h, *self):  #각뿔의 부피 공식

    try:
        return a * b * h * (1/3)

    except Exception as e:
        return e

def prism (a, b, h, *self): #각기둥의 부피 공식

    try:
        return a * b * h

    except Exception as e:
        return e


def cylinder (r, h, *self): #원기둥의 부피 공식

    try:
        return round(3.14 * r**2 * h)

    except Exception as e:
        return e

def cylinder_surface (r, h, *self): # 원기둥의 겉넓이 공식

    try:
        return round(2 * 3.14 * r**2 + 2*3.14 * r * h)

    except Exception as e:
        return e

def cone (r, h, *self):   # 원뿔의 겉넓이 공식

    try:
        return round(3.14*r*((r**2 + h**2)**(1/2)) + 3.14*r**2)

    except Exception as e:
        return e

def con_volume (r, h, *self): #원뿔의 부피 공식
    try:
        return round(3.14 * r**2 * h * (1/3))

    except Exception as e:
        return e

def sphere_volume (r, *self): #구의 부피

    try:
        return round((4/3)*3.14*r**3)

    except Exception as e:
        return e

def sphere_area (r, *self): #구의 겉넓이

    try:
        return round(4 * 3.14 * r**2)

    except Exception as e:
        return e



