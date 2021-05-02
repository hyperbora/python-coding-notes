from collections import deque
from pprint import pprint


class Node:
    def __init__(self, index, depth):
        self.left = None
        self.right = None
        self.index = index
        self.depth = depth


def inorder(root):
    arr = []
    stack = []
    head = root
    while True:
        if head:
            stack.append(head)
            head = head.left
        elif stack:
            head = stack.pop()
            arr.append(head.index)
            head = head.right
        else:
            break
    return arr


if __name__ == "__main__":
    root = Node(1, 1)
    arr = [
        [2, 3],
        [4, -1],
        [5, -1],
        [6, -1],
        [7, 8],
        [-1, 9],
        [-1, -1],
        [10, 11],
        [-1, -1],
        [-1, -1],
        [-1, -1]
    ]
    queries = [2, 4]

    q = deque([root])
    for left, right in arr:
        parent = q.popleft()
        if left != -1:
            left_child = Node(left, parent.depth + 1)
            parent.left = left_child
            q.append(left_child)
        if right != -1:
            right_child = Node(right, parent.depth + 1)
            parent.right = right_child
            q.append(right_child)
    # answer = []
    # for query in queries:
    #     level_q = deque([root])
    #     while level_q:
    #         head = level_q.pop()
    #         if head.depth == query or head.depth % query == 0:
    #             if head.left or head.right:
    #                 head.left, head.right = head.right, head.left
    #         if head.left:
    #             level_q.append(head.left)
    #         if head.right:
    #             level_q.append(head.right)
    #     answer.append(inorder(root))

    # pprint(answer)
    pprint(inorder(root))
