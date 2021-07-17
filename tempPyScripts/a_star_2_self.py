from heapq import heappop,heappush
#import heapq
class Node:
    def __init__(self,parent=None,position=None):
        self.parent = parent
        self.position = position

        self.f,self.g,self.h=0,0,0

    def __eq__(self,other):
        return(self.position == other.position)

    def __lt__(self,other):
        return(self.f < other.f)

def return_path(curr_node,maze):
    path = []
    r,c = len(maze),len(maze[0])

    res = [[-1 for i in range(c)] for _ in range(r)]
    curr = curr_node
    while(curr):
        path.append(curr.position)
        curr = curr.parent
    path.reverse()
    start_v = 0
    for i in range(len(path)):
        r,c = path[i][0],path[i][1]
        res[r][c] = start_v
        start_v +=1
    return(res)

def search(maze,cost,start,end):
    start_node = Node(parent = None,position = tuple(start))
    #start_node.f,start_node.g,start_node.h = 0,0,0
    end_node = Node(parent = None, position = tuple(end))
    #end_node.h,end_node.g,end_node.f = 0,0,0

    yet_to_visit_list = []
    visited_list = []
    yet_to_visit_heap = []

    heappush(yet_to_visit_heap,(start_node.f,start_node))

    yet_to_visit_list.append(start_node)

    move = [[-1,0],
            [0,-1],
            [1,0],
            [0,1]]

    r,c = len(maze),len(maze[0])

    while(len(yet_to_visit_list)>0):
        curr_node_tuple = heappop(yet_to_visit_heap)

        curr_node = curr_node_tuple[1]
        visited_list.append(curr_node)

        if(curr_node == end_node):
            return(return_path(curr_node,maze))

        children = []
        for a,b in move:
            node_pos = (curr_node.position[0] + a, curr_node.position[1] + b)

            if(node_pos[0]<0 or node_pos[1]<0 or node_pos[0]>=r or node_pos[1]>=c):
                continue

            if(maze[node_pos[0]][node_pos[1]]!=0):
                continue
            new_node = Node(curr_node,node_pos)

            new_node.g = cost + curr_node.g

            new_node.h = abs(end_node.position[0] - node_pos[0]) + abs(end_node.position[1] - node_pos[1])

            new_node.f = new_node.g + new_node.h

            l = len([i[1] for i in yet_to_visit_heap if i[1] == new_node and i[1].g< new_node.g])
            if(l>0):
                continue
            #kx = tuple(new_node.g,new_node)
            heappush(yet_to_visit_heap,(new_node.f,new_node))

if __name__ == '__main__':

    maze = [[0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]

    start = [0, 0] # starting position
    end = [4,5] # ending position
    cost = 1 # cost per movement

    path = search(maze,cost, start, end)
    for i in path:
        print(i)
