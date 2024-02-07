class Item:
    def __init__(self, selected, bomb=None, direction=None):
        self.x = 0
        self.y = 0
        self.selected = selected
        self.b_range = 0
        self.b_count = 0
        self.shield_value = 0
        self.throw_move= 6
        self.bomb=bomb
        self.direction=direction

        if selected == 5:
            self.range()
        elif selected == 6:
            self.count()
        elif selected == 7:
            self.count()
        elif selected == 8:
            self.throw()

    def range(self):
        self.b_range += 1
        print("폭탄 범위 증가")  # 중첩 가능
        return self.b_range

    def count(self):
        self.b_count += 1
        print("폭탄 개수 증가")  # 중첩 가능
        return self.b_count

    def shield(self):
        self.shield_value += 1
        print("방어")
        return self.shield_value

    def throw(self):
        self.x = self.bomb.get_bomb_imf()[0]
        self.y = self.bomb.get_bomb_imf()[1]
        if self.direction == 8:  # 'up':
            self.y += self.throw_move
        elif self.direction == 2:  # 'down':
            self.y -= self.throw_move
        elif self.direction == 4:  # 'left':
            self.x -= self.throw_move
        elif self.direction == 6:  # 'right':
            self.x += self.throw_move
        print("던지기")
        return (self.x, self.y)

    def get_item_imf(self):
        return [self.selected, self.b_range, self.b_count, self.shield_value, self.throw_move, self.bomb, self.direction]
