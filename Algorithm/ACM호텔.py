TC = int(input())
answer = []
wx = []# floor *100 하면 호수
for i in range(TC):
    H, W, N = list(map(int, input().split()))
    for i in range(1, W+1):
        wx.append(i)
    cmd=(N % H)
    gh = N // H
    if N<=H and N%H<=H:
        cmd = 1
        answer.append(str(cmd))
    else:
        answer.append(str(cmd))
    if N//H<10:
        answer.append('0')
        answer.append(str(wx[gh]))
        print(''.join(answer))
        answer.clear()
        continue
    print(''.join(answer))
    answer.clear()




for i in range(TC):
    H, W, N = list(map(int, input().split()))
    if N%H == 0 :
        answer.append(str(1))
    else:
        answer.append(str(N%H))
    if N//H!=0 and N//H< 10:
        answer.append(str(0))
        answer.append(str(N//H+1))
    else:
        answer.append(str(N//H+1))
    print(''.join(answer))
    answer.clear()