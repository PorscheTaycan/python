#연봉계산기
#사용자 입력
#1. 연봉 (원 단위)
#2. 비과세액 (원 단위)
#3. 부양가족수 (본인 포함), 최소 : 1, 최대 11

#출력 사항
#1. 국민연금 (4.5%)
#2. 건강보험 (3.545%)
#3. 요양보험 : 건강 보험의 12.95%
#4. 고용보험 : (0.9%)
#5. 근로소득세 (표참고)
#6. 지방소득세 : 근로소득세의 10%
#7. 년 예상 실수령액 (원 단위)
#8. 월 환산 실수령액 (원 단위)
# * 모든 단계에서는 1원 단위는 절사 0으로 치환

with open('2023.txt', 'r') as file:
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





def findError2(money):
    for idx, i in enumerate(money):
        templist = []
        for idx2, listitem in enumerate(money[i]):
            if idx2 > 1:
                templist.append(listitem.isdigit())
            money2[idx] = templist
        print(money2, 'money2')
        resultdict= {}
        for idx2, i in enumerate(money2):
            if money2[i].count(True)!= 11:
                if 'notTrue' not in resultdict.keys():
                    resultdict['notTrue'] = []
                resultdict['notTrue'].append(idx2+1)
        return resultdict
errordict = findError2(money)
print(errordict)


def checkRow(dict,rowIndex):
    print('\n')
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in dict[i]:
                if not j.isdigit():
                    print(j)





def checkNoise(dict, rowIndex):
    print('\n')
    for idx, i in enumerate(dict):
        if idx == rowIndex:
            for j in range(len(money[rowIndex-1])):
                if j>1:
                    for char in dict[i][j]:
                        if not char.isdigit():
                            dict[i][j] = dict[i][j].replace(char, '')
                    print(dict[i][j])

def


for i in errordict:
    for j in errordict[i]:
        checkRow(money, j-1)
        checkNoise(money, j-1)

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


# while True:
#     annual_income = int(input("연봉이 얼마입니까? (원 단위로 입력하시오.)"))
#     tax_free = int(input("비과세액은 얼마입니까? (원 단위로 입력하시오.)"))
#     dependent = int(input('부양 가족수는 몇 명입니까? (본인 포함해서 작성하시요.)'))
#     if 1 <= dependent <= 11:
#             monthly = (annual_income-tax_free)//12
#
#             national_pension = (monthly * 0.045) // 1
#             health_insurance = (monthly * 0.03545) // 1
#             recuperation_insurance = (health_insurance * 0.1295) // 1
#             employment_insurance = (monthly * 0.009) // 1
#
#             print('국민연금은 ', national_pension, '원 입니다. ')
#             print('건강보험은 ' , health_insurance, '원 입니다. ')
#             print('요양보험은 ', recuperation_insurance, '원 입니다. ')
#             #print('근로소득세는 ', , '원 입니다.')
#             print('지방 소득세는 ' , employment_insurance, '원 입니다. ')
#             #print('년 예상 실수령액은 ', , '원 입니다.)
#             #print('월 환산금액은 ' , , '원 입니다. ')
#
#
#
#     else:
#         print("부양 가족수가 맞지 않습니다.")
#
