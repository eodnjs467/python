# 큐, 스택 복습
import queue
data_queue = queue.Queue()
data_queue.put("대")
data_queue.put("원")
data_queue.put("아")
data_queue.put("공")
data_queue.put("부")
data_queue.put("하")
data_queue.put("자")
data_queue.qsize()
data_queue.get()

import queue
data_queue2 = queue.LifoQueue()
data_queue2.put(1)
data_queue2.put(2)
data_queue2.put(3)
data_queue2.put(4)
data_queue2.put(5)
data_queue2.qsize()
data_queue2.get()

import queue
data_queue3 = queue.PriorityQueue()
data_queue3.put((2, "원"))
data_queue3.put((1, "대"))
data_queue3.put((3, "아"))
data_queue3.put((6, "해"))
data_queue3.put((4, "공"))
data_queue3.put((5, "부"))
data_queue3.get()


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



stack_list = list()
def push(data):
    stack_list.append(data)
def pop():
    data = stack_list[-1]
    del stack_list[-1]
    return data
for index in range(1, 11):
    push(index)
len(stack_list)
pop()

#######################################################################################################################
# 대표적인 데이터 구조 : 링크드 리스트(Linked List)
# 1. 링크드 리스트 구조
#     연결리스트라고도 함
#     배열은 순차적으로 연결된 공간에 데이터를 나열하는 구조
#     링크드 리스트는 떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조
#
# 링크드 리스트 기본 구조와 용어
#     노드(Node) : 데이터 저장단위(데이터값, 포인터)로 구성
#     포인터(Pointer) : 각 노드 안에서, 다음이나 이전의 노드와의 연결 정보를 가지고 있는 공간

# 노드 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

node1 = Node(1)     #노드 1개 생성
node2 = Node(2)     #노드 1개 생성
node1.next = node2  #노드1과 2를 연결
head = node1        #맨 처음 노드를 알아야하기 때문에 head 에 노드1값을 줌

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def add(data):
        node = head
        while node.next:
            node = node.next
        node.next = Node(data)
    node1 = Node(1)
    head = node1
    for index in range(2, 10):
       add(index)

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)