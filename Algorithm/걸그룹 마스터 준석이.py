#https://www.acmicpc.net/problem/16165

N, M = map(int, input().split())

team_mem, mem_team = {}, {}

for i in range(N):
    team_name, mem_num = input(), int(input())
    team_mem[team_name]=[]
    for j in range(mem_num):
        name = input()
        team_mem[team_name].append(name)
        mem_team[name] = team_name

for i in range(M):
    name, quiz = input(), int(input())
    if quiz == 1:
        print(mem_team[name])
    else:
        for mem in sorted(team_mem[name]):
            print(mem)