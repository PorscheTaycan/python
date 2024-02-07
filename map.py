from bomb import Bomb
import random

tick=0
class Map:
    def __init__(self, size=15): #size= 15 범위설정
        self.size = size
        self.map = self.create_map() #맵만드는 함수 구현
        self.map[1][1] = 2
        self.map[13][13] = 3
    def set_user_position(self,x,y):
        # if Item.shield_value==0:
        #     self.map[x][y] = 2
        # else:
        #     self.map[x][y] = 12
        self.map[y][x] = 2
    def set_ai_position(self,x,y):
        self.map[y][x] = 3
    def del_user(self,x = 1,y = 1):
        if self.map[y][x] != 11:
            del self.map[y][x]
            self.map[y].insert(x, "*")
    def create_map(self): #맵만들기
        # 맵 초기화
        game_map = [] #빈리스트 만들기

        for i in range(self.size):#15 행
            row = [] #행
            for j in range(self.size): #15 열
                if i == 0 or i == self.size - 1 or j == 0 or j == self.size - 1: #i가 0이거나 14이거나 j가 0이거나 j=14이거나
                    row.append(0)  # 외벽
                elif i % 2 == 0 and j % 2 == 0:
                    row.append(1)  # 고정 벽
                else:
                    row.append('-')  # 빈 공간
            game_map.append(row)
        return game_map

    def set_bomb_position(self, x, y):
        self.map[y][x] = 11

    def break_wall(self): #아이템이 나오는 벽 만들기
        for i in range(1,self.size-1): #외곽 제외
            for j in range(1,self.size-1): #외곽 제외
                if self.map[i][j]=='-': #빈칸이라면?
                    if not (i<=3 and j<=3) or (i>=11 and j>=11) : #처음 위치에서 제외범위 만들기
                        if (i % 3 == 0 and j % 3 ==0)or(i % 3 == 1 and j % 3 ==1): #규칙성 식
                            self.map[i][j]=4 #좌표에 4찍기
    def remove_wall_in_bomb_range(self, bomb):
        sorted_ranges = bomb.bomb_range() #이중리스트
        if bomb.ticks==bomb.original_ticks+4:
            self.map[bomb.x][bomb.y] = "+"
            for direction_range in sorted_ranges:  # 상, 하, 좌, 우 방향별로 순회 밑에서 브레이크만나면 다음방향으로
                for x, y in direction_range: #상방향이면 거기안 원소들 x,y로 출력
                    if 0 <= x < self.size and 0 <= y < self.size:
                        # 장애물에 따라 처리
                        if self.map[x][y] in [0, 1]:
                            break  # 해당 방향으로의 폭발 중단 아무일도 안벌어지게하는거임
                        elif self.map[x][y] == 4:
                            ran_list = ['-', 5, 6, 7, 8]
                            probabilities = [0.2,0.2, 0.2, 0.2, 0.2]  # 각 아이템의 확률
                            # 무작위로 아이템 선택
                            selected = random.choices(ran_list, weights=probabilities)[0]
                            self.map[x][y] = selected  # 아이템 벽은 공백으로 제거
                            break
                        else:
                            self.map[x][y] = 9  # 폭발 범위 표시
    def clear_explosion(self,bomb):
        if bomb.ticks == bomb.original_ticks + 5: #5틱지났으면 범위 삭제
            for i in range(self.size):
                for j in range(self.size):
                    if self.map[i][j] in [9, '+']:  # 폭발 범위 또는 폭탄 위치
                        self.map[i][j] = '-'
    def display_map(self): #사이사이 띄어쓰기넣어서 출력
        for row in self.map:
            row_string = ''
            for cell in row:
                row_string += str(cell) + ' '
            print(row_string)
    def end_map(self): #$를 맞으면 죽는벽으로 구현하기, 틱 50이상일때 시작하는걸로 우선 나중에 수정
        a = 1
        b = self.size - 1
        while a<b:
            for i in range(a,b):
                self.map[a][i]='$'
                self.display_map()

            for i in range(a+1,b):
                self.map[i][b-1]='$'
                self.display_map()

            for i in range(b-2,a-1,-1):
                self.map[b-1][i]='$'
                self.display_map()

            for i in range(b - 2, a - 1, -1):
                self.map[i][a] = '$'
                self.display_map()
            a += 1
            b -= 1
    def item_coordinate(self):
        item_coor={}
        for i in range(1, self.size - 1):  # 외곽 제외
            for j in range(1, self.size - 1):  # 외곽 제외
                if self.map[i][j] in [5,6,7,8]:
                    item_type=self.map[i][j]
                    item_coor[item_type]=i,j
        return item_coor


    def get(self):
        return self.map


# 맵 생성 및 표시
game_map = Map()
game_map.break_wall()
bomb_instance = Bomb(7, 9, "some_info", 17)
bomb_instance.tick(21)
game_map.remove_wall_in_bomb_range(bomb_instance)
game_map.display_map()
bomb_instance.tick(22)
game_map.clear_explosion(bomb_instance)
game_map.display_map()
bomb_instance.tick(23)
game_map.display_map()
bomb_instance.tick(24)
game_map.display_map()
bomb_instance.tick(25)
game_map.display_map()
