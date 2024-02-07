with open('2023_2.txt', 'r') as file:
    money = {} #빈 딕셔너리 선언
    for idx, i in enumerate(file): #파일의 모든 라인에 대한 반복
        f = i.split('\t') # 개별 라인에 대한 split으로 \t를 기준으로 리스트화
        money[idx] = f #딕셔너리의 0번키부터 위 split된 리스트를 밸류로 추가
    for i in money: #딕셔너리의 모든 키에 대한 반복
        for idx, j in enumerate(money[i]): #딕셔너리의 모든 키에 대한 밸류에 대한 반복
            money[i][idx] = money[i][idx].strip() #딕셔너리 밸류의 리스트 내부 모든 요소에 대한 공백제거
            money[i][idx] = money[i][idx].replace(',' , '') #쉼표 제거
            if '\n' in j: # \n이 나오면 split후 앞에 것만 살리는 작업
                money[i][idx] = money[i][idx].split('\n')[0]
            if money[i][idx] == '-': #하이픈을 0으로 바꾸는 작업
                money[i][idx] = "0"

annual_income = int(input("연봉이 얼마입니까? (원 단위로 입력하시오.)"))
tax_free = int(input("비과세액은 얼마입니까? (원 단위로 입력하시오.)"))
dependent = int(input('부양 가족수는 몇 명입니까? (본인 포함해서 작성하시요.)'))
monthly = str(int(annual_income-tax_free)//12)



for searchidx, i in enumerate(money):
    if money[i][0]<= monthly < money[i][1]:
        print(money[i][0])
        print(searchidx)
        print(money[searchidx])

        # national_pension = (int(monthly * 0.045) // 1)
        # health_insurance = (monthly * 0.03545) // 1
        # recuperation_insurance = (health_insurance * 0.1295) // 1
        # employment_insurance = (monthly * 0.009) // 1

        print('근로소득세:{}'.format(money[searchidx][int(dependent)+1]))
        print(type(money[searchidx][int(dependent)+1]))
        #print('실수령액은 :  {}'.format(money[searchidx][int(dependent)+1])-annual_income-tax_free-national_pension-health_insurance-recuperation_insurance-employment_insurance))

