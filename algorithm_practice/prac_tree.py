# def popp(list):
#     if len(list) == 0:
#         return
#     else:
#         return list.pop()
#
# def push(sth, list):
#     return list.append(sth)
#
# lst = []
# print(lst)
# push('a', lst)
# print(lst)
# push('t', lst)
# print(lst)
# push('v', lst)
# print(lst)
# popp(lst)
# print(lst)
# push('7', lst)
# print(lst)
# popp(lst)
# print(lst)
# push('h', lst)
# print(lst)
#
# def ssss(list):
#     n = 0
#     for i in list:
#         if i == '(':
#             n += 1
#         elif i == ')':
#             n -= 1
#         else:
#             pass
#     if n != 0:
#         return -1
#     else:
#         return 1
# lst = '()()((()))'
# lst2 = '((()((((()()((()())((())))))'
# lst3 = list(lst)
# a = lst3.pop()
# print(lst3.pop())
# print(ssss(lst))
# print(ssss(lst2))
#
# def popsearch(list):
#     inn = 0
#     outt = 0
#     if list.pop() == '(':
#         inn += 1
#     elif list.pop == ')':
#         outt += 1
#     else:
#         pass
#     if inn == 0 and outt == 0:
#         return 1
#     else:
#         return -1

# DFS
# E = [1,2, 1,3, 2,4, 2,5, 4,6, 5,6, 6,7, 3,7]
# # E = list(input(, ))
# v = 1
#
# stack = []
# ran = len(set(E))
# print(ran)
# G = [[0 for _ in range(1+ran)] for _ in range(1+ran)]
# visited = ['F'] * len(set(E))
# print(len(E))
# for i in range(0, len(E), 2):
#     G[E[i]][E[i + 1]] = 1
#     G[E[i +1]][E[i]] = 1
# print(G)
# stack.append(v)
# visited[v-1] = 'T'
# print(v)
'''
def findnext(v):
    for i inrange(1,8):
        if G[v]
        
        
def dfs(v):
    print(v, end='')
    visited[v] = True
    
    while v:
        w = findnext(v)
        if w : push(v)
        while w:
            print(w, end='')
            visited[w] =True
            push(w)
            v = w 
            w =findnext(v)
        v = pop()
        
def dfsr(v):
    print(v, end=' ')
    visited[v] = 
    
    
'''

# while len(stack) != 0:
#     w = stack[-1]
#     flag = False
#     for i in range(1, len(G)):
#         if G[w][i] == 1 and visited[i] == 'F':
#             stack.append(i)
#             print(i)
#             visited[i] = 'T'
#             flag = True
#             break
#     if flag == True:
#         stack.pop()



    # v = E[0]
    # while visited in 'F':
    #     visited[v-1] = 'T'
    #     stack += v
    #     n = 0
    #     for i in set(E):
    #         for j in range(ran):
    #             G[i][j] == 1
    #             n += 1





# Graph.prototype.dfs = function() {
#   var stack = new Stack();
#   var temp = this.first;
#   while (temp) {
#     temp.inTree = false;
#     temp = temp.next;
#   }
#   temp = this.first;
#   stack.push(temp); // 스택에 첫 버텍스를 넣음
#   temp.inTree = true;
#   while (stack.count) { // 탐색을 완료할 때까지
#     temp = stack.pop(); // 넣었던 버텍스를 하나씩 꺼냄
#     console.log(temp.key);
#     temp.inTree = true;
#     var arc = temp.arc;
#     while (arc) {
#       if (!arc.destination.inTree) {
#         stack.push(arc.destination); // 꺼낸 것과 연결된 버텍스들을 스택에 넣음
#         arc.destination.inTree = true;
#       }
#       arc = arc.nextArc;
#     }
#   }
# };
# graph.dfs(); // A, X, H, P, E, Y, M, J, G

# lst=[[0]*7]*7
# E=[1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# # for i in range(int(len(a)/2)):
# #     lst[a[2*i]][a[2*i+1]] = 1
# # print(lst)
# G = [[0 for _ in range(len(set(E)))] for _ in range(len(set(E)))]
# # visited = ['F'] * len(set(graph))
# print(len(E))
# for i in range(0,len(E), 2):
#     G[E[i]][E[i + 1]] = 1
#     G[E[i +1]][E[i]] = 1
# print(G)

# import sys
# sys.stdin = open("input.txt", "r")

def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1 : return 0
    x = stack[top]
    top -= 1
    return x

def findnext(v):
    for i in range(1, 8):
        if G[v][i] and not visited[i]:
            return i
    return 0

def DFS(v):
    print(v, end=" ")
    visited[v] = True
    while v:
        w = findnext(v)
        if w : push(v)
        while w:
            print(w, end=" ")
            visited[w] = True
            push(w)
            v = w
            w = findnext(v)
        v = pop()

def DFSr(v):  #recursive DFS
     print(v, end=" ")
     visited[v] = True

     for i in range(1, 8):
         if G[v][i] and not visited[i]:
             DFSr(i)


edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
visited = [0] * (8)
G = [[0]* (8) for _ in range(8)]
stack = [0] * 10
top = -1

for i in range(0, len(edges), 2):
    G[edges[i]][edges[i+1]] = 1
    G[edges[i+1]][edges[i]] = 1

DFS(1)

visited = [0] * 8
G = [[0] * 8 for _ in range(8)]
print("\n=== recursive DFS ===")
for i in range(0, len(edges), 2):
     G[edges[i]][edges[i+1]] = 1
     G[edges[i+1]][edges[i]] = 1

DFSr(1)

