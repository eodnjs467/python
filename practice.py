import itertools
def solution(M, load):



    a=[]
    count = 0
    M = input("트럭에 실을 수 있는 최대 무게를 설정해주세요.")
    if M>40: print("40이하로 입력하세요")

    load = input("[1,2,3,4,5,6] 처럼 입력하세요 최대 12개 ")
    for index in range(len(load)):
        if load[index] > 12:
            print("12이하로 설정하세요")
            count = count+1
            if count == len(load):
                return -1

        a.append(load[index])

    b = itertools.combinations(a,2)
    c = list(b)

    for i in range(1):
        for j in range(1):
            middle = 40 - (c[i][j] + c[i][j+1])
            middle =                            ## 0에 가까운 걸 찾아야함

    # load_max = 40
    # min = 0

    answer = 0
    return answer