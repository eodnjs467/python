# 장점 : 데이터 공간을 미리 할당하지 않아도 ㄷ힘
# 단점 : 연결을 위한 별도의 데이터 공간이 필요하므로, 저장공간의 효율이 높지 않음
#     연결 정보를 찾는 시간이 필요하므로 접근 속도가 느림
#     중간 데이터 삭제시, 앞 뒤 데이터의 연결을 재구성 해야하는 부가적인 작업 필요

###################################################
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node=node.next

linkedlist1 = NodeMgmt(0)
linkedlist1.desc()
for data in range(1, 10):
    linkedlist1.add(data)


#외우자 그냥 .. . . . . . 특히 중간 삽입 ... 