import sys

input = sys.stdin.readline
answer = 0

def initGraph(n):
    return [[[] for _ in range(n)] for _ in range(n)]

def move(atom, n):
    atom.x = (atom.x + dx[atom.d] * atom.s) % n
    atom.y = (atom.y + dy[atom.d] * atom.s) % n

class Atom:
    def __init__(self, x, y, m, s, d):
        self.x = x
        self.y = y
        self.m = m
        self.s = s
        self.d = d

    def info(self):
        return (self.x, self.y, self.m, self.s, self.d)

# 상, 북동, 우, 남동, 하, 남서, 좌, 북서, 
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
atoms = []

for _ in range(m):
    x, y, m, s, d = map(int, input().split())
    atoms.append(Atom(x - 1, y - 1, m, s, d))

for turn in range(k):
    graph = initGraph(n)

    # 1. 원자 이동
    for atom in atoms:
        move(atom, n)
        graph[atom.x][atom.y].append(atom)
    
    nAtoms = list()
    # 2.원자가 겹치는지 확인
    for i in range(n):
        for j in range(n):
            collisions = len(graph[i][j])
            if collisions <= 1: 
                for atom in graph[i][j]:
                    nAtoms.append(atom)
                continue

            totalM = 0
            totalS = 0
            dirSet = set()
            # 원지기 겹친다면
            for atom in graph[i][j]:
                totalM += atom.m
                totalS += atom.s
                dirSet.add(atom.d % 2)

            # 질량이 0이라면 소멸
            if totalM // 5 == 0:
                graph[i][j].clear()
                continue
            
            dividedM = totalM // 5
            dividedS = totalS // collisions
            nDir = [0, 2, 4, 6] if len(dirSet) == 1 else [1, 3, 5, 7]

            for dir in nDir:
                nAtoms.append(Atom(i, j, dividedM, dividedS, dir))

    atoms = nAtoms[:]

for atom in atoms:
    answer += atom.m

print(answer)
