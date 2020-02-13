#https://www.acmicpc.net/problem/9037

def check(N, candy):
    for i in range(N):
        if candy[i] % 2 ==1:
            candy[i] +=1
    return len(set(candy)) == 1     #candy 의 배열을 set으로 하면 중복이 다 제거돼서 == 1 해서 같은지 체크

def teacher(N, candy):
    tmp_lst = [0 for i in range(N)]     #오른쪽에 전달해줘야 하는 사탕수를 미리 저장
    for idx in range(N):
        if candy[idx] % 2:
            candy[idx] += 1
        candy[idx] //= 2
        tmp_lst[(idx+1) % N] = candy[idx]   #오른쪽 친구가 가질 사탕 수  내꺼의 반이니까

    for idx in range(N):
        candy[idx] += tmp_lst[idx]          #가지고있는 캔디 + 오른쪽으로 분배한 캔디

    return candy

def process():
    N, candy = int(input()), list(map(int, input().split()))
    cnt = 0
    while not check(N, candy):
        cnt += 1
        candy = teacher(N, candy)
    print(cnt)


for i in range(int(input())):
    process()
