from item import Item
class Bomb:
    def __init__(self, x, y, user_imf, ticks):
        self.x = x
        self.y = y
        self.user_imf = user_imf
        self.ticks = ticks
        self.original_ticks = ticks
        self.b_range = 3
        self.isalive = True


    def tick(self, external_ticks=None,tf=None):
        if tf == False:
            if external_ticks is not None:
                self.ticks = external_ticks
            print("폭탄이 터졌습니다!")
            self.isalive = False
        elif self.isalive == True and external_ticks is not None :
                self.ticks = external_ticks
                if self.ticks == self.original_ticks + 4:
                    print("폭탄이 터졌습니다!")
                    self.isalive = False

        return self.ticks

    def bomb_range(self):
        coordinates = []
        for i in range(-self.b_range, self.b_range + 1):
            if i != 0:
                coordinates.append((self.x + i, self.y))
            else:
                for j in range(-self.b_range, self.b_range + 1):
                    coordinates.append((self.x, self.y + j))
        down, up, left, right, setpoint = [], [], [], [], []
        sort_list = []
        for x, y in coordinates:
            if x == self.x and y < self.y:  # 하
                down.append((x, y))
            elif x == self.x and y > self.y:  # 상
                up.append((x, y))
            elif y == self.y and x < self.x:  # 좌
                left.append((x, y))
            elif y == self.y and x > self.x:  # 우
                right.append((x, y))
        up.sort(reverse=True)
        down.sort()
        left.sort(reverse=True)
        right.sort()
        setpoint.append((self.x,self.y))
        sort_list.append(up)
        sort_list.append(down)
        sort_list.append(left)
        sort_list.append(right)
        sort_list.append(setpoint)
        return sort_list

    def set_b_range(self,new_b_range):
        self.b_range = new_b_range
        return self.b_range

    def get_bomb_imf(self):
        return [self.x, self.y, self.user_imf, self.ticks, self.b_range, self.isalive]

    def set_ticks(self, ticks):
        self.ticks = ticks