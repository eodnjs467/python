N = int(input())
queue = []
for i in range(N):
    M = list(input().split())
    if M[0] == 'push':
        queue.append(int(M[1]))
    elif M[0] == 'pop':
        if len(queue) ==0:
            print('-1')
            continue
        print(queue.pop(0))
    elif M[0] == 'size':
        print(len(queue))
    elif M[0] == 'empty':
        if len(queue) == 0 : print('1')
        else: print('0')
    elif M[0] == 'front':
        if len(queue) == 0: print('-1')
        print(queue[0])
    elif M[0] == 'back':
        if len(queue) == 0: print('-1')
        print(queue[-1])