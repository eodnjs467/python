# 전위 : root -> 왼 -> 오
# 중위 : 왼 -> root -> 오
# 후위 : 왼 -> 오 -> root

class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class NodeMgmt:
    def __init__(self, node):
        self.head = node

    def insert(self, value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value:   # value 가 현재 값보다 크면 왼쪽
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:                           # value 가 현재 값보다 크면 오른쪽
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            elif value > self.current_node.value:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        search = False
        self.current_node, self.parent = self.head, self.head
        while self.current_node:
            if self.current_node.value == value:
                search = True
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            elif value > self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if search == False:
            return False
        # Case1
        if self.current_node.left == None and self.current_node.right == None:  # 삭제할 노드가 자식이 없는 경우
            if value < self.parent.value:                                       # 삭제할 노드가 부모기준 왼쪽일 경우
                self.parent.left = None
            else:                                                               # 삭제할 노드가 부모기준 오른쪽일 경우
                self.parent.right = None
        #Case2
        if self.current_node.left != None and self.current_node.right == None:  # 삭제할 노드가 자식이 왼쪽에 하나 있는경우
            if value < self.parent.value:                                       # 부모노드보다 작으면
                self.parent.left = self.current_node.left                       # 왼쪽에 현재 왼쪽값 그대로 넣어
            else:
                self.parent.right = self.current_node.left                      # 오른쪽에 현재 왼쪽 값 넣어
        elif self.current_node.left == None and self.current_node.right != None:    # 삭제할 노드가 자식이 오른쪽에 하나 있는경우
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

head = Node(1)
binary_tree = NodeMgmt(head)
binary_tree.insert(2)
binary_tree.insert(0)
binary_tree.insert(4)
binary_tree.insert(8)
binary_tree.insert(-2)
binary_tree.search(8)