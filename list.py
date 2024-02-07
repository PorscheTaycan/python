import bomb
import item

class List:
    def __init__(self):
        self.bombs = []
        self.items = []
        self.b_count = 1
        # self.bombs = bombs
        # self.items = items

    def add_item(self, *items):  # 아이템 리스트 번호 표기로 보기
        for i in items:
            if isinstance(i, item.Item):
                self.items.append(i.get_item_imf()[0])
        print(self.b_count)
        return self.b_count, self.items


    def add_bomb(self, *bombs):
        for i in bombs:
            if isinstance(i, bomb.Bomb):
                self.b_count = self.items.count(6)
                print(self.b_count)
                if len(self.bombs) <= self.b_count:
                    print(self.b_count)
                    self.bombs.append(i)
                    print(f"폭탄이 추가되었습니다.")

        return self.bombs

    def apply(self):
        b_range = self.items.count(5)

        #shield_value = self.items.count()
        new_bombs = []
        for i in self.bombs:
            if isinstance(i, bomb.Bomb):
                i.set_b_range(b_range+3)
                new_bombs.append(i)

        self.bombs = new_bombs

        return self.bombs


bomb1 = bomb.Bomb(x=0, y=0, user_imf="some_info", ticks=17) # 폭탄 생성
bomb2 = bomb.Bomb(x=1, y=1, user_imf="some_info", ticks=20)
bomb3 = bomb.Bomb(x=0, y=0, user_imf="some_info", ticks=30)
item1 = item.Item(selected=5)
item2 = item.Item(selected=5)
item3 = item.Item(selected=7)
item4 = item.Item(selected=6)
item5 = item.Item(selected=7)
item6 = item.Item(selected=8,bomb=bomb1,direction=6)
item7 = item.Item(selected=5)

list = List()
list.add_item(item1,item2,item3,item4,item5,item6,item7)
list.add_bomb(bomb1,bomb2,bomb3)

list.apply()
print(list.bombs,"0")
print(bomb1,"1")
print(list.items)
for b in list.bombs:
    print(b.bomb_range())