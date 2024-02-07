# 연봉계산기
# 사용자 입력
# 세액표는 천원단위, 이상 미만으로 구간 설정되어 있음
# 1.연봉(원단위)
# 2.비과세액(원단위)
# 3.부양가족수(본인포함), 최소 1
#
# 출력사항
# 1.국민연금(4.5%)
# 2.건강보험금(3.545%)
# ㄴ3.요양보험:건강보험의 12.95%)
# 4.고용보험(0.9%)
# 5.근로소득세(표참고)
# ㄴ6.지방소득세:근로소득세의 10%
# 7.년 예상 실수령액 (원단위)
# 8.월 환산 실수령액 (원단위)
# * 모든 단계에서 1원단위는 절사 0으로 치환


import cal
inform = {'연봉':'', '비과세액':'','부양가족수':''}

while True:
    for i in list(inform.keys()):
        inform[i] = int(input(f"{i}을/를 입력하세요 : "))
    sal = inform[list(inform.keys())[0]]//12         # 월급
    cal = sal-inform[list(inform.keys())[1]]/12

    with open('2023_2.txt', 'r') as file:
        global e
        for line in file: # 파일에서 1라인씩 읽기, 반복 770~775가 한 바퀴 775 ~ 780이 한 바퀴 그렇게 해서 495바퀴
            chart_list = list(line.strip().split('\t')) # 탭 기준으로 분리해서 리스트화
            for j in range(len(chart_list)): #리스트 대상 13바퀴 반복문 ( 0 ~ 12 ) 770이 하나 775가 하나 그렇게 해서 13바퀴
                chart_list[j] = chart_list[j].strip().replace(',', '') #한 라인 내부 요소에 대한 쉼표 제거
                if not chart_list[j].isdigit(): #숫자로 변환가능한 텍스트가 아니면
                    if '-' == chart_list[j]: #해당 요소가 하이픈 문자라면
                        chart_list[j] = 0 #하이픈을 0으로 바꾼다.
                    else: #하이픈이 아닐 때
                        for alpha in chart_list[j]: # 770 이라는 문자열을 한 글자씩 반복문
                            if alpha not in '0123456789':       # 숫자가 아닌 문자가 포함된 경우
                                chart_list[j] = chart_list[j].replace(alpha, '') #770a라고 되어있으면 0~9까지의 숫자가 아닌 것은 제거하겠다. 그런 후 다시 chart_list에 넣겠다.
                chart_list[j] = int(chart_list[j]) #int함수로 변환하겠다.
            chart_list[0] *= 1000 # 770에서 7700000
            chart_list[1] *= 1000 # 775에서 7750000으로 변환

            temp1_list = chart_list[2:] # 금액 이상 미만을 제외한 나머지 데이터 -> 가족수별 세액
            temp1_list = sorted(temp1_list) #오름차순으로 변경
            temp1_list.sort(reverse=True) #오름차순으로 되어있던 것을 내림 차순으로 변경 나중에 temp1_list와 chart_list를 비교하기 위해서 내림차순으로 변경
            if chart_list[2:] != temp1_list: #원본 chart_list에 문제가 있는 상태
                if 0 in chart_list and chart_list.index(0) != len(chart_list)-1: #리스트 중간에 0이 발견된 경우
                    #chart_list.index(0)이면 2가 나오게 된다. 두번째 0이 있기 때문이다. 그리고 len(chart_list)는 13-1 따라서 12 둘은 같지 않다. True가 나오게 된다.
                    # chart_list안에도 0이 있어서 True가 나온다. 중간부분에 0이 있는지를 알아보기 위해서 사용
                    if chart_list[chart_list.index(0)+1] == 0: #chart_list[3]과 같음 따라서 발견된 0 다음칸도 0이라면
                        gap1 = (chart_list[chart_list.index(0)-1]-chart_list[chart_list.index(0)+2])//3
                        chart_list[chart_list.index(0)] = chart_list[chart_list.index(0)-1] - gap1
                        chart_list[chart_list.index(0)] = chart_list[chart_list.index(0)-1] - gap1
                    else:
                        chart_list[chart_list.index(0)] = (chart_list[chart_list.index(0)-1] + chart_list[chart_list.index(0)+1])//2
                for l in range(4, len(chart_list)): # 4부터 끝까지 4부터는 일정하게 빼지기 때문이다. 4부터 12까지
                    if chart_list[l] >= chart_list[l-1]: #앞에 요소보다 뒤에 요소가 값이 큰 경우
                        if l == len(chart_list)-1: #마지막 자리
                            gap2 = chart_list[l-2] - chart_list[l-1] # 마지막 자리일 때는 그 전과 그전 전의 차이를 비교해서 한다.
                            chart_list[l] = chart_list[l-1] - gap2
                        elif l > 4: # 첫 번째, 마지막을 제외한 모든 자리
                            chart_list[l] = (chart_list[l-1] + chart_list[l+1])//2
                        else: # l 이 4일 때 : 첫 번째 자리
                            gap2 = chart_list[l+1] - chart_list[l+2] # 4번째 자리일 때는 그 다음과 그 다음 다음의 차이를 비교해서 한다.
                            chart_list[l] = chart_list[l+1] + gap2

            print(chart_list)

            if chart_list[0] <= cal < chart_list[1]:            # 근로소득세 0번째 자리와 1번째 자리 값이 그 사이에 있으면
                e = chart_list[inform[list(inform.keys())[2]]+1] # 부양가족수

    t = {'np':0.045, 'hi':0.03545, 'ni':0.1295, 'ei':0.009, 'lit':0.1}

    res = []
    for m in list(t.keys()):
        if m == 'ni':
            res.append(cal*t['hi']*t[m])
        elif m == 'lit':
            res.append(e*t[m])
        else:
            res.append(cal*t[m])
    res.insert(res.index(e*t['lit'])-1, e)

    for k in range(len(res)):  # 반올림 하는 법
        t2 = res[k]*0.1
        res[k] = round(t2, 0)*10
        res[k] = int(str(res[k])[:str(res[k]).find('.')])

    g = sal  # 연봉, 실수령액 계산
    for j in res:
        g -= j
    h = g * 12
    res += [g, h]

    print('#'*30,
          f'\n국민연금({t["np"]*100:.1f}%): {res[0]}원'
          f'\n건강보험({t["hi"]*100:.3f}%): {res[1]}원'
          f'\nㄴ요양보험({t["ni"]*100:.2f}%): {res[2]}원'
          f'\n고용보험({t["ei"]*100:.1f}%): {res[3]}원'
          f'\n근로소득세(간이세액): {res[4]}원'
          f'\nㄴ지방소득세({t["lit"]*100:.1f}%): {res[5]}원'
          f'\n{"-"*30}'
          f'\n년 예상 실수령금액: {res[7]:.0f}원'
          f'\nㄴ월 환산금액: {res[6]:.0f}원'
          f'\n{"#"*30}')