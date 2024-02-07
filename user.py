from list import List
from bomb import Bomb
from item import Item
from map import Map
tick=0


class User:
    def __init__(self, item_instance, ticks):  # 시작 좌표 (1, 1)
        self.x = 1
        self.y = 1
        self.has_bomb = False
        self.is_die = False
        self.life_count = 3
        self.items = [5, 5, 6, 6, 6, 7]
        self.shield_value = item_instance.shield_value
        self.b_count = 0
        self.ticks = 0
        self.item_instance = item_instance
        self.b_count = 0
        self.shield_value = self.items.count(7)
        self.bomb_list = []
        self.original_ticks = ticks



    # def get_list(self):
    #     if (self.x == item x 좌표) and (self.y == item y 좌표):
    #         result = self.items.append()
    #         return result


    def move_x(self, direction):
        if direction == 4:
            self.x -= 1  # 왼쪽으로 이동
        elif direction == 6:
            self.x += 1  # 오른쪽으로 이동
        return self.x,

    def move_y(self, direction):
        if direction == 2:
            self.y -= 1  # 아래쪽으로 이동
            if self.y <= -13:
                self.y = -12
        elif direction == 8:
            self.y += 1  # 위쪽으로 이동
            if self.y >= 0:
                self.y += 0
        return self.y

    def bomb(self, direction):
        if direction == 5:
            print("폭탄이 설치되었습니다.")
            self.has_bomb = True
        return False

    def get_item_list(self,x,y,map=[[]]):
        if map[y][x] == 5:
            self.items.append(5)
        elif map[y][x] == 6:
            self.items.append(6)
        elif map[y][x] == 7:
            self.items.append(7)
        elif map[y][x] == 8:
            self.items.append(8)
        return self.items

    def die(self, bomb):  # 생명 표현
        player_x = self.x
        player_y = self.y
        bomb_ranges = bomb.bomb_range()

        for direction_range in bomb_ranges:
            if (  # 유저 좌표와 폭탄 범위의 값이 같을 때
                    direction_range[0][0] <= player_x <= direction_range[-1][0]
                    and direction_range[-1][1] <= player_y <= direction_range[0][1]
            ):
                if self.shield_value > 0:  # 쉴드가 있다면
                    self.shield_value -= 1
                    print("쉴드가 사용되었습니다.")
                    return True
                elif self.life_count > 0:  # 생명이 0개 초과일 때
                    self.life_count -= 1
                    print(f"목숨 -1, 남은 목숨 {self.life_count}개")
                return True
        return False



    def bomb_count(self, user_instance):  # 폭탄 개수 증가시키는 함수
        # b_range = User.user_instance.items.count(6)
        user_instance.get_item_list()

        user_instance.b_count += 1
        print(f"폭탄 개수가 1 증가하여 현재 폭탄 개수는 {user_instance.b_count}개 입니다.")
        self.bomb_box()

        return user_instance.b_count, 2

    def bomb_box(self): #폭탄이 담기는 리스트 함수
        self.bomb_list = []
        self.bomb_list.append(bomb_instance)

    def tick(self, external_ticks=None, tf=None):
        if external_ticks is not None:
            self.ticks = external_ticks

        return self.ticks

    def set_ticks(self, ticks, tf=True):  # 기본값으로 True를 사용하거나 필요에 따라 다른 기본값을 선택할 수 있습니다.
        self.ticks = ticks
        if self.bomb_list and self.bomb_list[-1].ticks is None:
            self.bomb_list[-1].set_ticks(self.ticks + 4)
            self.items.append(6)  # 4틱 후에 아이템 리스트에 6 추가
            print(user_instance.items, "4")

    def use_bomb(self):
        # 리스트에 담긴 폭탄 갯수만큼 사용 및 충전
        if 6 in self.items:
            print("폭탄을 사용합니다.")
            user_instance.items.remove(6)  # 아이템 리스트에서 폭탄 제거
            print(user_instance.items, "1")

            # 여기서 추가된 부분: 사용한 폭탄을 bomb_list에 추가
            new_bomb = Bomb(self.x, self.y, user_imf="some_info", ticks=4)  # 폭탄이 터지기까지 4틱 소요

            new_bomb.set_ticks(self.ticks + 4)  # 폭탄을 4틱 뒤에 추가하도록 수정
            self.bomb_list.append(new_bomb)
            print(user_instance.items, "3")

            # 여기서 4틱 후에 items에 추가되도록 수정
            self.set_ticks(self.ticks + 4, tf=False)

            # 사용한 폭탄을 4틱 후에 추가
            bomb_coordinates = bomb_instance.bomb_range()
            self.bomb_coordinates = bomb_coordinates

            return True

        return False





    def bomb_range_increase(self):
        #result = Item.range(Item.get_item_imf()[3])
        result = item_instance.b_range
        if result is not None:
            print("폭탄 범위가 +1 증가되었습니다.")
            bomb_instance.b_range += 1
            self.bomb_box()
            print(f"폭탄 리스트에 새로운 폭탄이 추가되었습니다. 현재 폭탄 리스트: {self.bomb_list}")  # 주석처리 해야 함. print문으로 폭탄 리스트 갱신되는 거 확인하는 용
            return True
        return False






# game_map.end_map()
item_instance = Item(1, "some_info")

user_instance = User(item_instance, tick)
bomb_instance = Bomb(user_instance.x, user_instance.y, "some_info", 30000)

print(user_instance.use_bomb)


while True:
    try:
        direction = int(input("이동 방향을 입력하세요 (2: 아래, 4: 왼쪽, 6: 오른쪽, 8: 위쪽, 5: 폭탄 설치): "))
        x_set = user_instance.move_x(direction)
        y_set = user_instance.move_y(direction)

        if user_instance.bomb(direction):
            bomb_instance = Bomb(user_instance.x, user_instance.y, "some_info", tick)
            print("폭탄 좌표: ({}, {})".format(x_set, y_set))
            bomb_coordinates = bomb_instance.bomb_range()
            print(bomb_instance.bomb_range())
            if any((user_instance.x, user_instance.y) in direction_range for direction_range in bomb_coordinates):
                print("폭탄 범위 안에 있음")
                if user_instance.die(bomb_instance):
                    user_instance.use_bomb()

        else:
            print("현재 좌표: ({}, {})".format(x_set, y_set))

        #user_instance.life(bomb_instance)
        bomb_instance.tick(tick)
        tick += 1
    except ValueError:
        pass