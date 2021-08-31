from vpython import *
#GlowScript 3.0 VPython
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None
 
 

class G2:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V
 

    def add_edge(self, src, dest):

        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        x=3
        y=4
        for i in range(self.V):
            rate(1)
            j=0
            T = text(text='Adjacency list of vertex {} '.format(i),pos=vector(-5-1,(-y*i)+2+10,0),color=color.yellow)
            #T.height=2*T.height
            L=box(pos=vector((x*j)-3-1,-y*i+10,0),size=vector(2,2,0.1), color=color.blue)
            T = text(text=i,pos=vector((x*j)-3-1,-y*i+10,0),color=color.white)
            temp = self.graph[i]
            while temp:
                rate(1)
                #T.height=0.5*T.height
                A = text(text='->',pos=vector((x*j)-2-1,-y*i+10,0),color=color.white)
                A.height=0.5*A.height
                L=box(pos=vector(x*j-1,-y*i+10,0),size=vector(2,2,0.1), color=color.green)
                T = text(text=temp.vertex,pos=vector(x*j-1,-y*i+10,0),color=color.black)
                #T.height=0.5*T.height
                
                temp = temp.next
                j=j+1
    
albutton=button(text="Adjacency List", pos = scene.title_anchor, bind=adjlist)

def adjlist():
    for obj in scene.objects:
        obj.visible = False
    print_options(clear=True)
    V = 6
    graph = G2(V)
    graph.add_edge(0, 2)
    graph.add_edge(0, 1)
    graph.add_edge(5, 4)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(1, 4)
    graph.add_edge(2, 4)
    graph.add_edge(5, 3)
    graph.print_graph()
                    
                    
                    
class G1:

     __n = 0

     __g =[[0 for x in range(10)] for y in range(10)]
       

     def __init__(self, x):
        self.__n = x

        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__g[i][j]= 0
 
     def displayAdjacencyMatrix(self):
        x=3
        y=4
        #sphere(pos=vector(-10,10,0), radius=0.75,color=vector(1,0.64,0))
        T = text(text='Adjacency matrix',pos=vector(-10-1,15,0),color=color.yellow)
        T.height=2*T.height
        T.length=2*T.length
        for i in range(0, self.__n):
            T = text(text='{}'.format(i),pos=vector((x*i)-10,1.5+10,0),color=color.white)
            #T.height=0.5*T.height
            T = text(text='{}'.format(i),pos=vector(-2-10,-y*i+10,0),color=color.white)
            #T.height=0.5*T.height
         

        for i in range(0, self.__n):

            for j in range(0, self.__n):
                rate(1)
                L=box(pos=vector(x*i-10,-y*j+10,0),size=vector(2,2,0.1), color=color.green)
                T = text(text='{}'.format(self.__g[i][j]),pos=vector(x*i-10,-y*j+10,0),color=color.black)
                #T.height=0.5*T.height
                
     def addEdge(self, x, y):

        if(x>= self.__n) or (y >= self.__n):
            print("Vertex does not exists !")

        if(x == y):
             print("Same Vertex !")
        else:

             self.__g[y][x]= 1
             self.__g[x][y]= 1
             
ambutton=button(text="Adjacency Matrix", pos = scene.title_anchor, bind=adjmatrix)

def adjmatrix():
    for obj in scene.objects:
        obj.visible = False
    print_options(clear=True)
    obj = G1(6);
      
    obj.addEdge(0, 2); 
    obj.addEdge(0, 1); 
    obj.addEdge(5, 4); 
    obj.addEdge(1, 3); 
    obj.addEdge(3, 4); 
    obj.addEdge(1, 4); 
    obj.addEdge(2, 4); 
    obj.addEdge(5, 3);
# the adjacency matrix created 
    obj.displayAdjacencyMatrix();
    

class Graph:
      
    adj = []
  

    def __init__(self, v, e):
          
        self.v = v
        self.e = e

        Graph.adj = [[0 for i in range(v)] 
                        for j in range(v)]

  

    def addEdge(self, start, e):
        

        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1

        #rate(0.5)
        if start==0:
            start=zero.pos
        elif start==1:
            start=one.pos
        elif start==2:
            start=two.pos
        elif start==3:
            start=three.pos
        elif start==4:
            start=four.pos            
        else:
            start=five.pos


        if e==0:
            e=zero.pos
        elif e==1:
            e=one.pos
        elif e==2:
            e=two.pos
        elif e==3:
            e=three.pos
        elif e==4:
            e=four.pos            
        else:
            e=five.pos
        
        c = curve(start, e)
            
            
        
    def newNode(self,list):
        
        global zero,one,two,three,four,five
 
        zero=cylinder(pos = vector(0,9,0), axis = vector(0,0,0.2), radius = 1.5, color=vector(1,0.64,0))
        T = text(text=list[0],pos=zero.pos,color=color.white)
        rate(0.5)
        
        one=cylinder(pos = vector(-4,3,0), axis = vector(0,0,0.2), radius = 1.5, color=vector(1,0.64,0))
        T = text(text=list[1],pos=one.pos,color=color.white)
        rate(0.5)
        
        two=cylinder(pos = vector(4,3,0), axis = vector(0,0,0.2), radius = 1.5, color=vector(1,0.64,0))
        T = text(text=list[2],pos=two.pos,color=color.white)
        rate(0.5)
        
        three=cylinder(pos = vector(-4,-3,0), axis = vector(0,0,0.2), radius = 1.5, color=vector(1,0.64,0))
        T = text(text=list[3],pos=three.pos,color=color.white)
        rate(0.5)
        
        four=cylinder(pos = vector(4,-3,0), axis = vector(0,0,0.2), radius = 1.5, color=vector(1,0.64,0))
        T = text(text=list[4],pos=four.pos,color=color.white)
        rate(0.5)
        
        five=cylinder(pos = vector(0,-9,0), axis = vector(0,0,0.2), radius = 1.5, color=vector(1,0.64,0))
        T = text(text=list[5],pos=five.pos,color=color.white)
        rate(0.5)
        
    
    def DFS(self, start, visited,count):
        
        if start==0:
            start1=zero.pos
            cur=zero
        elif start==1:
            start1=one.pos
            cur=one
        elif start==2:
            start1=two.pos
            cur=two
        elif start==3:
            start1=three.pos
            cur=three
        elif start==4:
            start1=four.pos
            cur=four
        else:
            start1=five.pos
            cur=5
        if(count==1):
            cur.color=color.blue
            count=count+1
                      

        print(start, end = ' ')
  

        visited[start] = True
  

        for i in range(self.v):

            if (Graph.adj[start][i] == 1 and
                    (not visited[i])):
                rate(0.5)        
                if i==0:
                    e1=zero.pos
                    zero.color= color.red
                elif i==1:
                    e1=one.pos
                    one.color= color.red
                elif i==2:
                    e1=two.pos
                    two.color= color.red
                elif i==3:
                    e1=three.pos
                    three.color= color.red
                elif i==4:
                    e1=four.pos
                    four.color= color.red                   
                else:
                    e1=five.pos
                    five.color= color.red

                curve(pos=[start1,e1], color= color.red)        
                self.DFS(i, visited,count)
                

    def BFS(self, start):
        #print(self.v)
        
                
        visited = [False] * self.v
        q = [start]
 
        visited[start] = True
        count=1
        while len(q)>0:
            
            vis = q[0]
            if vis==0:
                start1=zero.pos
                cur=zero
            elif vis==1:
                start1=one.pos
                cur=one
            elif vis==2:
                start1=two.pos
                cur=two
            elif vis==3:
                start1=three.pos
                cur=three
            elif vis==4:
                start1=four.pos
                cur=four
            else:
                start1=five.pos
                cur=five
            if (count==1):
                    cur.color=color.blue
                    count=count+1
            
                

            print(vis, end = ' ')
            #print('befor pop',q)
            q.pop(0)
            #print('after pop',q)
            for i in range(self.v):
                
                if (Graph.adj[vis][i] == 1 and
                      (not visited[i])):
                          
                    rate(0.5) 
                    #print('i',i)
                    if i==0:
                        e1=zero.pos
                        zero.color= color.red
                    elif i==1:
                        e1=one.pos
                        one.color= color.red
                    elif i==2:
                        e1=two.pos
                        two.color= color.red
                    elif i==3:
                        e1=three.pos
                        three.color= color.red
                    elif i==4:
                        e1=four.pos
                        four.color= color.red                   
                    else:
                        e1=five.pos
                        five.color= color.red

                    curve(pos=[start1,e1], color= color.red) 
                    q.append(i)
                    #print('after append',q)
                    #start1=e1
                    
                    visited[i] = True

  
dbutton=button(text="DFS", pos = scene.title_anchor, bind=dfs1)

def dfs1():
    for obj in scene.objects:
        obj.visible = False
    print_options(clear=True)
    
    v, e = 6, 8
    list=[0,1,2,3,4,5]
    T = text(text='Dfs',pos=vector(-7,11,0),color=color.yellow)
    T.height=1.5*T.height
    T.length=2*T.length
    G = Graph(v, e)
    G.newNode(list)

    G.addEdge(0, 2)
    G.addEdge(0, 1)
    G.addEdge(5, 4)
    G.addEdge(1, 3)


    G.addEdge(3, 4)
    G.addEdge(1, 4)
    G.addEdge(2, 4)
    G.addEdge(5, 3)

    visited = [False] * v
    print('Enter the vertex for which you want do dfs')
    vertex=int(input())
    print('DFS Traversal:')
    count=1
    G.DFS(vertex, visited,count)



bbutton=button(text="BFS", pos = scene.title_anchor, bind=bfs1)

def bfs1():
    
    for obj in scene.objects:
        obj.visible = False
    print_options(clear=True)
    
    T = text(text='Bfs',pos=vector(-7,11,0),color=color.yellow)
    T.height=1.5*T.height
    T.length=2*T.length
    #print()
    v, e = 6, 8
    arr=[0,1,2,3,4,5]
# Create the graph
    G = Graph(v, e)
    G.newNode(arr)

    G.addEdge(0, 2)
    G.addEdge(0, 1)
    G.addEdge(5, 4)
    G.addEdge(1, 3)


    G.addEdge(3, 4)
    G.addEdge(1, 4)
    G.addEdge(2, 4)
    G.addEdge(5, 3)
    print('Enter the vertex for which you want to do bfs')
    vertex=int(input())
    print('BFS Traversal:')
# Perform BFS
    G.BFS(vertex)
