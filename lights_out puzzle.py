from random import choice
import copy
import random
import Queue
import sys
sys.setrecursionlimit(10000)
import time


def create_puzzle(rows,columns):    #  1 on  0 off
    select=[1,0]
    start=[]
    row_range=range(rows)
    column_range=range(columns)     
    for r in row_range:   
        start.append([])
        for c in column_range:
            cell = select[1]
            start[r].append(cell)
    return start

def toggle_cell(cell):
    if cell == 0:
     return 1
    else:
     return 0
def scramble(puzzle):
    i=0
    while (i<len(puzzle)):
        j=0
        while (j<len(puzzle[0])):
            if random.random()<0.5:
              puzzle=perform_move(puzzle,i,j)
            else:
                pass
            j=j+1
        i=i+1
    return puzzle

def perform_move(puzzle,row,column):

    new_puzzle=[]
    i=0
    new_puzzle=copy.deepcopy(puzzle)
    
    new_puzzle[row][column] = toggle_cell(new_puzzle[row][column])
    if row+1 < len(puzzle):
      new_puzzle[row+1][column] = toggle_cell(new_puzzle[row+1][column])
    if row-1 >= 0:
      new_puzzle[row-1][column] = toggle_cell(new_puzzle[row-1][column])
    if column+1 < len(puzzle[0]):
      new_puzzle[row][column+1] = toggle_cell(new_puzzle[row][column+1])
    if column-1 >= 0:
      new_puzzle[row][column-1] = toggle_cell(new_puzzle[row][column-1])
    return new_puzzle
    

# My graph for BFS and DFS search are both undirected graphs
# Each state of the puzzle can represent a node in graph.
# Two nodes have an edge between them if there is a light on toggling which the other node can be reached from the first node.
# getState function is to convert each puzzle's state to an integer value



#The algorithms for BFS is starting with a Queue contains starting puzzle and an empty [].
#bfs_vis: track visited nodes
#depth: how deep the tree is 
#Queue will pop an puzzle's state from beginning, and if this state is unvisited and not equal to 0 ,
#add this state to visited, then transfer this state to an interger value, and then generate a series of children which can be reached by toggling any node in current puzzle, and store path between them
# repeat this process until it find a state equals to 0, then return its cost and path.




   
def getState(puzzle):    
   value=0
   base=1
   for i in range(len(puzzle)):
       for j in range(len(puzzle[0])):
           value=value+base*int(puzzle[i][j])
           base=base*2
   return value
   
    

def BFS(puzzle):
  bfs_vis={}
  bfs_cost=0     # number of steps 
  bfs_path=[]    # return a list of moves that solves the puzzle
  depth=0
  num=0
  move={}
  Aft_state={}
  Pre_state={}
  Q=[puzzle,[]]
  while len(Q) != 0:
    state=Q[0]
    Q.pop(0)
    
    if len(state) == 0:
         Q.append(state)
         depth+=1
    else:
        value=getState(state)
        if value not in bfs_vis:
            if value == 0:
                while True:
                    BUF=0
                    i=0
                    while i<len(Aft_state)-1:
                        if(Aft_state[i] is state):
                            sign=i
                            BUF=1
                            break
                        else:
                            pass
                        i=i+1
                    if(BUF==0):
                      break
                    else:
                        pass
                    bfs_path.append(move[sign])
                    state=Pre_state[sign]
                return bfs_cost,bfs_path
            else:
                bfs_cost+=1
                bfs_vis[value] = True 
                for i in range(len(state)):
                    for j in range(len(state[0])):
                        newstate=perform_move(state,i,j)
                        Q.append(newstate)
                        Pre_state[num]=state
                        Aft_state[num]=newstate
                        move[num]=[i,j]
                        num+=1

                    
dfs_cost=0
dfs_vis={}
dfs_path=[]







# Dfs_find function using recursive way to solve problem, it convert starting puzzle to an integer value if it's 0 then return 1, otherwise searching from (0,0) of puzzle,
# if not visited then added to visited, repeating this process until it find an answer , return 1 if it finds a solution.


def Dfs_find(state):
    global dfs_cost
    nowvalue=getState(state)
    if(nowvalue==0):
        return 1
    V=0
    for i in range(len(state)):
        for j in range(len(state[0])):
            newstate=perform_move(state,i,j)
            newvalue=getState(newstate)
            if newvalue not in dfs_vis:
                dfs_vis[newvalue]=True
                dfs_cost+=1
                if [i,j] not in dfs_path:
                    dfs_path.append([i,j])
                else:
                    pass
                V = Dfs_find(newstate)
                if V==1:
                    return 1
                else:
                    pass
                dfs_path.pop()
            else:
                pass
    return 0


def DFS(puzzle):
    global dfs_vis
    global dfs_cost
    global dfs_path
    state=puzzle
    value=getState(puzzle)
    dfs_vis[value]=True
    Dfs_find(state)
    cost=dfs_cost
    path=dfs_path
    dfs_cost=0
    dfs_vis={}
    dfs_path=[]
    return cost,path



#DFS
i=0
s1=0
L1=0
start = time.time()
while i<100:
    c=scramble(create_puzzle(4,4))
    s1=s1+DFS(c)[0]
    L1=L1+len(DFS(c)[1])
    i=i+1
end = time.time()
print "DFS total length", L1
print "DFS total steps", s1
print "DFS wallclock time taken" ,(end - start)

#BFS 
i=0
s2=0
L2=0
start = time.time()
while i<100:
    b=scramble(create_puzzle(4,4))
    s2=s2+BFS(b)[0]
    L2=L2+len(BFS(b)[1])
    i=i+1
end = time.time()
print "BFS total length", L2
print "BFS total steps", s2
print "BFS wallclock time taken" ,(end - start)



