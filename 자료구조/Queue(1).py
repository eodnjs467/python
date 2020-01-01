# 1. 큐 구조(FIFO 정책)
#
# * 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조
#     * 음식점에서 가장먼저 줄을 서는 행위와 동일
#     *FIFO(First-in, First-out)또는 LOLO(Last-in, Last-out) 방식으로 스택과 꺼내는 순서가 반대

# 2. 알아둘 용어
# Enqueue : 큐에 데이터를 넣는 기능
# Dequeue : 큐에서 데이터를 꺼내는 기능

# 3. 파이썬 queue 라이브러리 활용해서 큐 자료구조 사용하기
# Queue() : 가장 일반적인 큐 자료구조
# LifoQueue() : 나중에 입력된 데이터가 먼저 출력되는 구조(스택구조라고 보면 됨)
# PriorityQueue() : 데이터마다 우선순위를 넣어서, 우선순위가 높은 순으로 데이터 출력

# 3-1. Queue()로 큐 만들기(가장 일반적인 큐, FIFO방식)
import queue

data_queue = queue.Queue()
data_queue.put("funcoding")
data_queue.put(1)
data_queue.qsize()
data_queue.get()    # 제일 먼저 넣은 "funcoding" 가 출력됐음
data_queue.qsize()

# 3-2. LifoQueue()로 큐 만들기(LIFO(Last-in, First-out))
import queue
data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(1)
data_queue.qsize()
data_queue.get()

# 3-3. PriotiyQueue()로 큐 만들기    // 우선순위를 지정하여 순위가 높은 것 부터 출력이 됨
import queue
data_queue = queue.PriorityQueue()
data_queue.put((10, "korea"))   # put((우선순위, 값))
data_queue.put((5, 1))
data_queue.put((15,"china"))
data_queue.qsize()
data_queue.get()

# 참고 : 어디에 큐가 많이 쓰일까?
# 운영체제에서 멀티태스킹을 위한 프로세스 스케줄링 방식을 구현하기 위해 많이 사용됨
# 큐의 경우에는 장단점이 없음.

# 프로그래밍 연습
# 연습1 : 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()
def enqueue(data):
    queue_list.append(data)
def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data
for index in range(10):
    enqueue(index)
len(queue_list)
dequeue()