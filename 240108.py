
df_menu = {'빅맥': [4500], '1955': [5000], '맥스파이시 상하이 버거': [4500], '맥치킨버거': [3500]}
sg_menu = {'그릴드머쉬룸버거': [8000] , '골든에그치즈버거': [7800], '트리플 어니언버거': [7900], '비프버거': [4500]}
beef_menu = {'빅맥': [4500],'치즈버거': [3500], '쿼터파운더버거': [5000], '더블쿼터파운더 치즈버거': [6000]}
chicken_menu = {'맥스파이시 상하이 버거': [4500], '맥치킨버거': [3500],'맥크리스피디럭스버거': [4300] }
bul_menu = {'더블불고기버거': [4000], '슈비버거': [4500]}
side = {"감자튀김": [2000], "치즈스틱+감자튀김": [3500], "치즈스틱": [2500]}
l_side = {"감자튀김": [2500], "치즈스틱+감자튀김": [4000], "치즈스틱": [3000]}
side_menu = {'토마토 치킨 스낵랩': [2000], '상하이 치킨 스낵랩': [2000], '코울슬로': [1500], '치즈스틱 2조각': [1800], '치즈스틱 4조각 ': [3000]
             , '맥너겟 4조각' : [3000], '맥너겟 6조각' : [4000], '치킨텐더 2조각' : [3500], '감자튀김 S':[1000], '감자튀김 M ': [1300],
             '감자튀김 L' : [1500], '스위트앤사워': [500], '스위트칠리':[500], '케이준' : [500]}
coffee_menu = {"바닐라라떼 ": [3000], '아메리카노' : [2000], '카페라떼' : [2500], '카푸치노' : [2500], '드립 커피' : [1800]}
drink_menu = {'코카콜라' : [1500], '환타' : [1500], '스프라이트' : [1500]}
fruit_menu = {'골드 맥피즈' : [2000] , '자두천도복숭아 칠러' : [2500] , '제주 한라봉 칠러' : [2500]}
shake_menu = {'초코쉐이크' : [2500], '바닐라쉐이크' : [2500], '딸기쉐이크' : [2500]}
dessert_menu = {'라즈베리크림치즈파이' : [1500], '오레오맥플러리' : [3000], '초코오레오맥플러리' : [3000], '딸기오레오맥플러리':[3000]}
happy_menu = {'맥너겟 4조각' : [3500], '햄버거해피밀' : [3500], '불고기버거해피밀' : [3800]}
category = {'추천 메뉴' : df_menu, '버거' : sg_menu, '음료' : drink_menu, '사이드': side_menu, '디저트': dessert_menu, '해피밀':happy_menu}
drink={'코카콜라' :[], '스프라이트':[], '환타':[]}


def sum_list(total,res=0):

    for i in total:
        if type(i) == str:
            res += int(i)
        else:
            pass
    return res

while True:
    order = []
    total= []
    a = input("1. 매장 식사 2. 포장 결정해주세요 ")
    for i in range(len(list(side_menu.keys()))):
        cg = input("카테고리를 선택 하세요 1. 추천 메뉴 2. 버거 3. 음료 4. 사이드 5. 디저트 6. 해피밀 ")
        if cg == '1':  # 카테고리에서 추천 메뉴 선택
            choice = int(input("1. 빅맥 2. 1955 3. 맥스파이시 상하이 버거 4. 맥치킨버거 "))
            selected_burger = list(category.keys())[choice-1]

            for i in selected_burger :
                mu = input('1. 단품 2. 일반세트 3. 라지세트')
                burger_price = list(df_menu.values())[choice-1]
                if mu == '1':  # 단품으로 선택
                    print("{}의 단품 가격은 {}원입니다.".format(list(df_menu.keys())[choice-1], burger_price))
                    amount_value = 1
                    while True:
                        amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                        if amount == '1':
                            amount_value += 1
                        elif amount == '2':
                            if amount_value > 1:
                                amount_value -= 1
                            else:
                                print("1개 이하 설정 불가")
                        else:
                            break

                    for i in range(len(df_menu.values())):
                        c = int(input(("{}를 {} 개 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(df_menu.keys())[choice - 1] ,amount_value))))
                        if c == 1:
                            order.append('{}'.format(list(df_menu.keys())[choice - 1]))
                            total.append('{}'.format(list(df_menu.values())[choice - 1][0]))
                            jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))
                            if jang == 1:
                                break
                            else:
                                print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                break
                        else:
                            break
                    break

                elif mu == '2':  # 일반세트로 선택
                    set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                    set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                    if set_side == 1:
                        print("{}의 세트 가격은 {}원입니다. ".format(list(df_menu.keys())[choice-1], list(df_menu.values())[choice-1][0]+list(side.values())[set_side-1][0]))
                    elif set_side == 2:
                        print("{}의 세트 가격은 {}원입니다. ".format(list(df_menu.keys())[choice-1], list(df_menu.values())[choice-1][0] +list(side.values())[set_side-1][0]))
                    elif set_side == 3:
                        print("{}의 세트 가격은 {}원입니다. ".format(list(df_menu.keys())[choice-1], list(df_menu.values())[choice-1][0] +list(side.values())[set_side-1][0]))
                    else:
                        print("잘못된 입력입니다. 일반세트 선택이 취소됩니다.")
                        continue

                    amount_value = 1
                    while True:
                        amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                        if amount == '1':
                            amount_value += 1
                        elif amount == '2':
                            if amount_value > 1:
                                amount_value -= 1
                            else:
                                print("1개 이하 설정 불가")
                        else:
                            break

                    for i in range(len(df_menu.values())):
                        c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(df_menu.keys())[choice - 1],list(drink.keys())[set_drink -4]))))
                        if c == 1:
                            order.append('{}.{}'.format(list(df_menu.keys())[choice - 1],list(drink.keys())[set_drink -4]))
                            total.append('{}'.format(list(df_menu.values())[choice - 1][0] + list(l_side.values())[set_side - 1][0]))
                            jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                            if jang == 1:
                                break
                            else:
                                print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                break
                        else:
                            break
                    break

                elif mu == '3':  # 라지세트로 선택
                    set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                    set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                    if set_side == 1:
                        print("{}의 라지세트 가격은 {}원입니다. ".format(list(df_menu.keys())[choice - 1], list(df_menu.values())[choice - 1][0] + list(l_side.values())[set_side - 1][0]))
                    elif set_side == 2:
                        print("{}의 라지세트 가격은 {}원입니다. ".format(list(df_menu.keys())[choice-1], list(df_menu.values())[choice - 1][0] + list(l_side.values())[set_side - 1][0]))
                    elif set_side == 3:
                        print("{}의 라지세트 가격은 {}원입니다. ".format(list(df_menu.keys())[choice-1],list(df_menu.values())[choice - 1][0] + list(l_side.values())[set_side - 1][0]))
                    else:
                        print("잘못된 입력입니다. 라지세트 선택이 취소됩니다.")
                        continue

                    amount_value = 1
                    while True:
                        amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                        if amount == '1':
                            amount_value += 1
                        elif amount == '2':
                            if amount_value > 1:
                                amount_value -= 1
                            else:
                                print("1개 이하 설정 불가")
                        else:
                            break

                    for i in range(len(df_menu.values())):
                        c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(df_menu.keys())[choice - 1],list(drink.keys())[set_drink -4]))))
                        if c == 1:
                            order.append('{}.{}'.format(list(df_menu.keys())[choice - 1],list(drink.keys())[set_drink -4]))
                            total.append('{}'.format(list(df_menu.values())[choice - 1][0] + list(l_side.values())[set_side - 1][0]))
                            jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                            if jang == 1:
                                break
                            else:
                                print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                break
                        else:
                            break
                    break
                break

        if cg == '2': # 카테고리에서 버거 선택
            bg = input("1. 시그니처 버거 2. 비프버거 3. 치킨&슈림프 버거 4. 불고기&기타 버거 ")
            if bg == '1': # 버거 들어간 후 시그니처 버거 선택
                si = int(input("1. 그릴드 머쉬룸 버거 2. 골든에그 치즈버거 3. 트리플 어니언 버거"))
                sb = list(sg_menu.keys())[si-1]
                if sb:
                    mu = input('1. 단품 2. 일반세트 3. 라지세트')
                    burger_price = list(sg_menu.values())[si - 1]
                    if mu == '1':  # 단품으로 선택
                        print("{}의 단품 가격은 {}원입니다.".format(list(sg_menu.keys())[si - 1], burger_price))
                        amount_value = 1
                        while True:
                            amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                            if amount == '1':
                                amount_value += 1
                            elif amount == '2':
                                if amount_value > 1:
                                    amount_value -= 1
                                else:
                                    print("1개 이하 설정 불가")
                            else:
                                break

                        for i in range(len(sg_menu.values())):
                            c = int(input(("{}를 {} 개 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(sg_menu.keys())[si - 1], amount_value))))
                            if c == 1:
                                order.append('{}'.format(list(sg_menu.keys())[si - 1]))
                                total.append('{}'.format(list(sg_menu.values())[si - 1][0]))
                                jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))
                                if jang == 1:
                                    break
                                else:
                                    print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                    break
                            else:
                                break
                        break
                    elif mu == '2':  # 일반세트로 선택
                        set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                        set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                        if set_side == 1:
                            print("{}의 세트 가격은 {}원입니다. ".format(list(sg_menu.keys())[si - 1], list(sg_menu.values())[si - 1][0] + list(side.values())[set_side - 1][0]))
                        elif set_side == 2:
                            print("{}의 세트 가격은 {}원입니다. ".format(list(sg_menu.keys())[si - 1], list(sg_menu.values())[si - 1][0] + list(side.values())[set_side - 1][0]))
                        elif set_side == 3:
                            print("{}의 세트 가격은 {}원입니다. ".format(list(sg_menu.keys())[si - 1], list(sg_menu.values())[si - 1][0] + list(side.values())[set_side - 1][0]))
                        else:
                            print("잘못된 입력입니다. 일반세트 선택이 취소됩니다.")
                            continue

                        amount_value = 1
                        while True:
                            amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                            if amount == '1':
                                amount_value += 1
                            elif amount == '2':
                                if amount_value > 1:
                                    amount_value -= 1
                                else:
                                    print("1개 이하 설정 불가")
                            else:
                                break

                        for i in range(len(sg_menu.values())):
                            c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(sg_menu.keys())[si - 1], list(drink.keys())[set_drink - 4]))))
                            if c == 1:
                                order.append('{}.{}'.format(list(sg_menu.keys())[si - 1], list(drink.keys())[set_drink - 4]))
                                total.append('{}'.format( list(sg_menu.values())[si - 1][0] + list(l_side.values())[set_side - 1][0]))
                                jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))
                                if jang == 1:
                                    break
                                else:
                                    print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                    break
                            else:
                                break
                        break

                    elif mu == '3':  # 라지세트로 선택
                        set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                        set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                        if set_side == 1:
                            print("{}의 라지세트 가격은 {}원입니다. ".format(list(sg_menu.keys())[si - 1], list(sg_menu.values())[si - 1][0] + list(l_side.values())[set_side - 1][0]))
                        elif set_side == 2:
                            print("{}의 라지세트 가격은 {}원입니다. ".format(list(sg_menu.keys())[si - 1], list(sg_menu.values())[si - 1][0] + list(l_side.values())[set_side - 1][0]))
                        elif set_side == 3:
                            print("{}의 라지세트 가격은 {}원입니다. ".format(list(sg_menu.keys())[si - 1], list(sg_menu.values())[si - 1][0] + list(l_side.values())[set_side - 1][0]))
                        else:
                            print("잘못된 입력입니다. 라지세트 선택이 취소됩니다.")
                            continue

                        amount_value = 1
                        while True:
                            amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                            if amount == '1':
                                amount_value += 1
                            elif amount == '2':
                                if amount_value > 1:
                                    amount_value -= 1
                                else:
                                    print("1개 이하 설정 불가")
                            else:
                                break

                        for i in range(len(sg_menu.values())):
                            c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(sg_menu.keys())[si - 1], list(drink.keys())[set_drink - 4]))))
                            if c == 1:
                                order.append('{}.{}'.format(list(sg_menu.keys())[si - 1], list(drink.keys())[set_drink - 4]))
                                total.append('{}'.format(list(sg_menu.values())[si - 1][0] + list(l_side.values())[set_side - 1][0]))
                                jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                if jang == 1:
                                    break
                                else:
                                    print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                    break
                            else:
                                break
                        break
                continue

            if bg == '2': # 버거 들어간 후 비프 버거 선택
                    beef = int(input("1. 빅맥 2. 치즈버거 3. 쿼터파운더버거 4. 더블쿼터파운더 치즈버거"))
                    bc = list(beef_menu.keys())[beef-1]
                    if bc:
                        mu = input('1. 단품 2. 일반세트 3. 라지세트')
                        burger_price = list(beef_menu.values())[beef - 1]
                        if mu == '1':  # 단품으로 선택
                            print("{}의 단품 가격은 {}원입니다.".format(list(beef_menu.keys())[beef - 1], burger_price))
                            amount_value = 1
                            while True:
                                amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                if amount == '1':
                                    amount_value += 1
                                elif amount == '2':
                                    if amount_value > 1:
                                        amount_value -= 1
                                    else:
                                        print("1개 이하 설정 불가")
                                else:
                                    break

                            for i in range(len(beef_menu.values())):
                                c = int(input(("{}를 {} 개 선택하신게 맞습니까? 1. 예 2. 아니요".format(
                                    list(beef_menu.keys())[beef - 1], amount_value))))

                                if c == 1:
                                    order.append('{}'.format(list(beef_menu.keys())[beef - 1]))
                                    total.append('{}'.format(list(beef_menu.values())[beef - 1][0]))
                                    jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))
                                    if jang == 1:
                                        break
                                    else:
                                        print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                        break
                                else:
                                    break
                            break
                        elif mu == '2':  # 일반세트로 선택
                            set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                            set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                            if set_side == 1:
                                print("{}의 세트 가격은 {}원입니다. ".format(list(beef_menu.keys())[beef - 1], list(beef_menu.values())[beef - 1][0] + list(side.values())[set_side - 1][0]))
                            elif set_side == 2:
                                print("{}의 세트 가격은 {}원입니다. ".format(list(beef_menu.keys())[beef - 1], list(beef_menu.values())[beef - 1][0] + list(side.values())[set_side - 1][0]))
                            elif set_side == 3:
                                print("{}의 세트 가격은 {}원입니다. ".format(list(beef_menu.keys())[beef - 1], list(beef_menu.values())[beef - 1][0] + list(side.values())[set_side - 1][0]))
                            else:
                                print("잘못된 입력입니다. 일반세트 선택이 취소됩니다.")
                                continue

                            amount_value = 1
                            while True:
                                amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                if amount == '1':
                                    amount_value += 1
                                elif amount == '2':
                                    if amount_value > 1:
                                        amount_value -= 1
                                    else:
                                        print("1개 이하 설정 불가")
                                else:
                                    break

                            for i in range(len(beef_menu.values())):
                                c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(beef_menu.keys())[beef - 1], list(drink.keys())[set_drink - 4]))))
                                if c == 1:
                                    order.append('{}.{}'.format(list(beef_menu.keys())[beef - 1], list(drink.keys())[set_drink - 4]))
                                    total.append('{}'.format( list(beef_menu.values())[beef - 1][0] + list(l_side.values())[set_side - 1][0]))
                                    jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                    if jang == 1:
                                        break
                                    else:
                                        print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                        break
                                else:
                                    break
                            break
                        elif mu == '3':  # 라지세트로 선택
                            set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                            set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                            if set_side == 1:
                                print("{}의 라지세트 가격은 {}원입니다. ".format(list(beef_menu.keys())[beef - 1], list(beef_menu.values())[beef - 1][0] + list(l_side.values())[set_side - 1][0]))
                            elif set_side == 2:
                                print("{}의 라지세트 가격은 {}원입니다. ".format(list(beef_menu.keys())[beef - 1], list(beef_menu.values())[beef - 1][0] + list(l_side.values())[set_side - 1][0]))
                            elif set_side == 3:
                                print("{}의 라지세트 가격은 {}원입니다. ".format(list(beef_menu.keys())[beef - 1], list(beef_menu.values())[beef - 1][0] + list(l_side.values())[set_side - 1][0]))
                            else:
                                print("잘못된 입력입니다. 라지세트 선택이 취소됩니다.")
                                continue

                            amount_value = 1
                            while True:
                                amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                if amount == '1':
                                    amount_value += 1
                                elif amount == '2':
                                    if amount_value > 1:
                                        amount_value -= 1
                                    else:
                                        print("1개 이하 설정 불가")
                                else:
                                    break

                            for i in range(len(beef_menu.values())):
                                c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(beef_menu.keys())[beef - 1], list(drink.keys())[set_drink - 4]))))
                                if c == 1:
                                    order.append('{}.{}'.format(list(beef_menu.keys())[beef - 1],list(drink.keys())[set_drink - 4]))
                                    total.append('{}'.format(list(beef_menu.values())[beef - 1][0] + list(l_side.values())[set_side - 1][0]))
                                    jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                    if jang == 1:
                                        break
                                    else:
                                        print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                        break
                                else:
                                    break
                            break
                    continue

            if bg == '3': #버거 들어간 후 치킨&슈림프 버거 선택
                    chicken = int(input("1. 맥 스파이시 상하이 버거 2. 맥치킨버거 3. 맥 크리스피 디럭스 버거"))
                    sc = list(chicken_menu.keys())[chicken-1]
                    if sc:
                        bc = list(chicken_menu.keys())[chicken-1]
                        if bc:
                            mu = input('1. 단품 2. 일반세트 3. 라지세트')
                            burger_price = list(chicken_menu.values())[chicken - 1]
                            if mu == '1':  # 단품으로 선택
                                print("{}의 단품 가격은 {}원입니다.".format(list(chicken_menu.keys())[chicken - 1], burger_price))
                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(df_menu.values())):
                                    c = int(input(("{}를 {} 개 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(chicken_menu.keys())[chicken - 1], amount_value))))
                                    if c == 1:
                                        order.append('{}'.format(list(chicken_menu.keys())[chicken - 1]))
                                        total.append('{}'.format(list(chicken_menu.values())[chicken - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))
                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break

                            elif mu == '2':  # 일반세트로 선택
                                set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                                set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                                if set_side == 1:
                                    print("{}의 세트 가격은 {}원입니다. ".format(list(chicken_menu.keys())[chicken - 1], list(chicken_menu.values())[chicken - 1][0] + list(side.values())[set_side - 1][0]))
                                elif set_side == 2:
                                    print("{}의 세트 가격은 {}원입니다. ".format(list(chicken_menu.keys())[chicken - 1], list(chicken_menu.values())[chicken - 1][0] + list(side.values())[set_side - 1][0]))
                                elif set_side == 3:
                                    print("{}의 세트 가격은 {}원입니다. ".format(list(chicken_menu.keys())[chicken - 1], list(chicken_menu.values())[chicken - 1][0] + list(side.values())[set_side - 1][0]))
                                else:
                                    print("잘못된 입력입니다. 일반세트 선택이 취소됩니다.")
                                    continue

                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(chicken_menu.values())):
                                    c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(chicken_menu.keys())[chicken - 1], list(drink.keys())[set_drink - 4]))))
                                    if c == 1:
                                        order.append('{}.{}'.format(list(chicken_menu.keys())[chicken - 1], list(drink.keys())[set_drink - 4]))
                                        total.append('{}'.format(list(chicken_menu.values())[chicken - 1][0] + list(l_side.values())[set_side - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break

                            elif mu == '3':  # 라지세트로 선택
                                set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                                set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                                if set_side == 1:
                                    print("{}의 라지세트 가격은 {}원입니다. ".format(list(chicken_menu.keys())[chicken - 1],list(chicken_menu.values())[chicken - 1][0] + list(l_side.values())[set_side - 1][0]))
                                elif set_side == 2:
                                    print("{}의 라지세트 가격은 {}원입니다. ".format(list(chicken_menu.keys())[chicken - 1], list(chicken_menu.values())[chicken - 1][0] + list(l_side.values())[set_side - 1][0]))
                                elif set_side == 3:
                                    print("{}의 라지세트 가격은 {}원입니다. ".format(list(chicken_menu.keys())[chicken - 1], list(chicken_menu.values())[chicken - 1][0] + list(l_side.values())[set_side - 1][0]))
                                else:
                                    print("잘못된 입력입니다. 라지세트 선택이 취소됩니다.")
                                    continue

                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(chicken_menu.values())):
                                    c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(chicken_menu.keys())[chicken - 1], list(drink.keys())[set_drink - 4]))))
                                    if c == 1:
                                        order.append('{}.{}'.format(list(chicken_menu.keys())[chicken - 1], list(drink.keys())[set_drink - 4]))
                                        total.append('{}'.format(list(chicken_menu.values())[chicken - 1][0] + list(l_side.values())[set_side - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break
                        continue

            if bg == '4': #버거 들어간 후 불고기& 기타 버거 선택
                    bul = int(input("1. 더블 불고기 버거 2. 슈비버거"))
                    sc = list(bul_menu.keys())[bul-1]
                    if sc:
                        bc = list(bul_menu.keys())[bul-1]
                        if bc:
                            mu = input('1. 단품 2. 일반세트 3. 라지세트')
                            burger_price = list(bul_menu.values())[bul - 1]
                            if mu == '1':  # 단품으로 선택
                                print("{}의 단품 가격은 {}원입니다.".format(list(bul_menu.keys())[bul - 1], burger_price))
                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(bul_menu.values())):
                                    c = int(input(("{}를 {} 개 선택하신게 맞습니까? 1. 예 2. 아니요".format(
                                        list(bul_menu.keys())[bul - 1], amount_value))))

                                    if c == 1:
                                        order.append('{}'.format(list(bul_menu.keys())[bul - 1]))
                                        total.append('{}'.format(list(bul_menu.values())[bul - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))
                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break


                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(bul_menu.values())):
                                    c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(bul_menu.keys())[bul - 1], list(drink.keys())[set_drink - 4]))))
                                    if c == 1:
                                        order.append('{}.{}'.format(list(bul_menu.keys())[bul - 1], list(drink.keys())[set_drink - 4]))
                                        total.append('{}'.format(list(bul_menu.values())[bul - 1][0] + list(l_side.values())[set_side - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break
                            elif mu == '2':  # 일반세트로 선택
                                set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                                set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                                if set_side == 1:
                                    print("{}의 세트 가격은 {}원입니다. ".format(list(bul_menu.keys())[bul - 1], list(bul_menu.values())[bul - 1][0] + list(side.values())[set_side - 1][0]))
                                elif set_side == 2:
                                    print("{}의 세트 가격은 {}원입니다. ".format(list(bul_menu.keys())[bul - 1], list(bul_menu.values())[bul - 1][0] + list(side.values())[set_side - 1][0]))
                                elif set_side == 3:
                                    print("{}의 세트 가격은 {}원입니다. ".format(list(bul_menu.keys())[bul - 1], list(bul_menu.values())[bul - 1][0] + list(side.values())[set_side - 1][0]))
                                else:
                                    print("잘못된 입력입니다. 일반세트 선택이 취소됩니다.")
                                    continue

                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(bul_menu.values())):
                                    c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(bul_menu.keys())[bul - 1], list(drink.keys())[set_drink - 4]))))
                                    if c == 1:
                                        order.append('{}.{}'.format(list(bul_menu.keys())[bul - 1], list(drink.keys())[set_drink - 4]))
                                        total.append('{}'.format(list(bul_menu.values())[bul - 1][0] + list(l_side.values())[set_side - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break

                            elif mu == '3':  # 라지세트로 선택
                                set_side = int(input("세트 사이드를 정해주세요 1. 감자튀김 2. 감자튀김 + 치즈스틱 2조각 3. 치즈스틱 "))
                                set_drink = int(input("세트 음료를 정해주세요 4. 코카콜라 5. 스프라이트 6. 환타"))
                                if set_side == 1:
                                    print("{}의 라지세트 가격은 {}원입니다. ".format(list(bul_menu.keys())[bul - 1], list(bul_menu.values())[bul - 1][0] + list(l_side.values())[set_side - 1][0]))
                                elif set_side == 2:
                                    print("{}의 라지세트 가격은 {}원입니다. ".format(list(bul_menu.keys())[bul-1], list(bul_menu.values())[bul - 1][0] + list(l_side.values())[set_side - 1][0]))
                                elif set_side == 3:
                                    print("{}의 라지세트 가격은 {}원입니다. ".format(list(bul_menu.keys())[bul-1], list(bul_menu.values())[bul - 1][0] + list(l_side.values())[set_side - 1][0]))
                                else:
                                    print("잘못된 입력입니다. 라지세트 선택이 취소됩니다.")
                                    continue

                                amount_value = 1
                                while True:
                                    amount = input('1. 수량 + 2. 수량 - 그 외 입력 다음단계')
                                    if amount == '1':
                                        amount_value += 1
                                    elif amount == '2':
                                        if amount_value > 1:
                                            amount_value -= 1
                                        else:
                                            print("1개 이하 설정 불가")
                                    else:
                                        break

                                for i in range(len(bul_menu.values())):
                                    c = int(input(("{}.{}를 선택하신게 맞습니까? 1. 예 2. 아니요".format(list(bul_menu.keys())[bul - 1],list(drink.keys())[set_drink -4]))))
                                    if c == 1:
                                        order.append('{}.{}'.format(list(bul_menu.keys())[bul - 1],list(drink.keys())[set_drink -4]))
                                        total.append('{}'.format(list(bul_menu.values())[bul - 1][0] + list(l_side.values())[set_side - 1][0]))
                                        jang = int(input(('장바구니에 담았습니다. 더 주문하시나요? 1. 예 2. 결제합니다.')))

                                        if jang == 1:
                                            break
                                        else:
                                            print('결제합니다. 총 ', sum_list(total) * amount_value, '가격입니다.')
                                            break
                                    else:
                                        break
                                break
                    continue



        if cg == '3': # 카테고리에서 음료 선택
            drink = input("1. 커피 2. 탄산음료 3. 과일음료 4. 쉐이크")
            if drink == '1': #음료 들어간 후 커피 선택
                coffee = int(input("1. 바닐라라떼 2. 아메리카노 3. 카페라떼 4. 카푸치노 5. 드립커피"))
                dr = list(coffee_menu.keys())[coffee-1]
                print("{}의 가격은 {}입니다. ".format(list(coffee_menu.keys())[coffee-1], (list(coffee_menu.values())[coffee-1])))
            if drink == '2': #음료 들어간 후 탄산음료 선택
                coke = int(input("1. 코카콜라 2. 환타 3. 스프라이트"))
                dr = list(coffee_menu.keys())[coke-1]
                print("{}의 가격은 {}입니다. ".format(list(drink_menu.keys())[coke-1], (list(coffee_menu.values())[coke-1])))
            if drink == '3': #음료 들어간 후 과일음료 선택
                fruit = int(input("1. 골드 맥피즈 2. 자두천도복숭아 칠러 3. 제주한라봉 칠러"))
                dr = list(fruit_menu.keys())[fruit - 1]
                print("{}의 가격은 {}입니다. ".format(list(fruit_menu.keys())[fruit - 1], (list(fruit_menu.values())[fruit - 1])))
            if drink == '4': #음료 들어간 후 쉐이크 선택
                shake = int(input("1. 초코쉐이크 2. 바닐라쉐이크 3. 딸기 쉐이크"))
                dr = list(shake_menu.keys())[shake - 1]
                print("{}의 가격은 {}입니다. ".format(list(shake_menu.keys())[shake - 1],(list(shake_menu.values())[shake - 1])))



        if cg == '4': #카테고리에서 사이드 선택
            side = input("1. 스낵랩 2. 코울슬로 3. 치즈스틱 4. 맥너겟 5. 치킨텐더 6. 감자튀김 7. 소스")
            if side == '1':
                sn = int(input("1. 토마토 치킨 스낵랩 2. 상하이 치킨 스낵랩"))
                print("{}의 가격은 {}입니다. ".format(list(side_menu.keys())[sn - 1], (list(side_menu.values())[sn - 1])))
            if side == '2':
                print("{}의 가격은 {}입니다. ".format(list(side_menu.keys())[2], (list(side_menu.values())[2])))
            if side == '3':
                stick = int(input("1. 치즈스틱 2조각 2. 치즈스틱 4조각"))
                print("{}의 가격은 {}입니다. ".format(list(side_menu.keys())[stick+2],(list(side_menu.values())[stick+2])))
            if side == '4':
                mac = int(input('1. 맥너겟 4조각 2. 맥너겟 6조각'))
                print('{}의 가격은 {}입니다.'.format(list(side_menu.keys())[mac+4],(list(side_menu.values())[mac+4])))
            if side == '5':
                print("{}의 가격은 {}입니다. ".format(list(side_menu.keys())[7], (list(side_menu.values())[7])))
            if side == '6':
                fride = int(input('감자튀김 사이즈를 고르세요 1. S 2. M 3. L'))
                print("{}의 가격은 {}입니다.".format(list(side_menu.keys())[fride+7], (list(side_menu.values())[fride+7])))
            if side == '7':
                source = int(input('1. 스위트앤사워 2. 스위트칠리 3. 케이준'))
                print("{}의 가격은 {}입니다.".format(list(side_menu.keys())[source+10], (list(side_menu.values())[source+10])))

        if cg == '5': #카테고리에서 디저트 선택
            dessert = int(input("1. 라즈베리 크림치즈 파이 2. 맥플러리"))
            if dessert==2:
                des = int(input("1. 오레오 맥플러리 2. 초코오레오 맥플러리 3. 딸기오레오 맥플러리"))
                ds = list(dessert_menu.keys())[dessert]
                print("{}의 가격은 {}입니다. ".format(list(dessert_menu.keys())[dessert], (list(dessert_menu.values())[dessert])))
            elif dessert==1:
                print("{}의 가격은 {}입니다. ".format(list(dessert_menu.keys())[dessert-1],(list(dessert_menu.values())[dessert-1])))

        if cg == '6': #카테고리에서 해피밀 선택
            import datetime as dt

            now = dt.datetime.now().time()
            open = dt.time(10,30)
            close = dt.time(23, 0)
            if open <= now <= close:
                happy = int(input("1. 맥너겟 4조각 해피밀 2. 햄버거 해피밀 3. 불고기버거 해피밀"))
                print("{}의 가격은 {}입니다.".format(list(happy_menu.keys())[happy-1], (list(happy_menu.values())[happy-1])))
            else:
                print("해피밀 시간이 아닙니다.")

        continue
