import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
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
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):

        searched = False
        self.current_node = self.head
        self.parent = self.head

        # 삭제할 노드와 그 부모 노드 찾기
        while self.current_node:
            if value == self.current_node.value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        # Leaf Node이면
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # 자식이 1개인 Node이면
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:  # 삭제할 노드가 부모노의 왼쪽 노드
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # 자식이 2개인 Node이면
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.getNewOne()

                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
                self.parent.left = self.change_node
            else:
                self.getNewOne()

                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right
                self.parent.right = self.change_node

        return True

    def getNewOne(self): # 자식 노드중 가장 왼쪽에 있는 노드를 가져옴
        self.change_node = self.current_node.right
        self.change_parent = self.current_node.right

        while self.change_node.left != None:
            self.change_parent = self.change_node
            self.change_node = self.change_node.left

        if self.change_node.right != None:
            self.change_parent.left = self.change_node.right
        else:
            self.change_parent.left = None

# Test Code
bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print(bst_nums)

# random하게 고른 숫자들을 BST에 삽입, 루트 노트는 500으로 넣기로함
head = Node(500)
binary_tree = NodeMgmt(head)
for num in bst_nums:
    binary_tree.insert(num)

# 검색
for num in bst_nums:
    if binary_tree.search(num) == False:
        print("search Failed", num)

# 삭제 test
delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print("delete failed", del_num)