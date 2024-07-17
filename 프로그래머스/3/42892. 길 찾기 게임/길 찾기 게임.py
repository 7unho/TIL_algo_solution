"""
nodeinfo = [nodeNum, x, y]
answer = 이진트리의 [[전위 순회], [후위 순회]]
전위 : +lr
후위 : lr+
"""
import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, index, x, y, left=None, right=None):
        self.index = index
        self.x = x
        self.y = y
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.y < other.y
    
    def __repr__(self):
        return (f"Node(number={self.index}, x={self.x}, y={self.y}, "
                f"left={self.left}, right={self.right})")
        
        
def solution(nodeinfo):
    global nodes
    N = len(nodeinfo)
    nodeinfo = [Node(i, nodeinfo[i - 1][0], nodeinfo[i - 1][1]) for i in range(1, N + 1)]
    nodeinfo.sort(reverse=True)
    
    root = constructTree(nodeinfo)
    preResult = []
    preOrder(root, preResult)

    postResult = []
    postOrder(root, postResult)

    return [preResult, postResult]

def preOrder(node, visits):
    # 1. 종료조건
    # 자식이 없을 때.
    if not node: return
    
    visits.append(node.index)
    preOrder(node.left, visits)
    preOrder(node.right, visits)

def postOrder(node, visits):
    if not node: return
    
    postOrder(node.left, visits)
    postOrder(node.right, visits)
    visits.append(node.index)

def insert(root, node, nodeinfo) -> any:
    """node를 root의 자식노드로 삽입"""
    if node.x < root.x:
        if not root.left:
            root.left = node
        else:
            insert(root.left, node, nodeinfo)
    else:
        if not root.right:
            root.right = node
        else:
            insert(root.right, node, nodeinfo)
    

def constructTree(nodeinfo) -> any:
    """이진 트리 생성 함수"""
    root = nodeinfo[0]

    for i in range(1, len(nodeinfo)):
        insert(root, nodeinfo[i], nodeinfo)

    return root
