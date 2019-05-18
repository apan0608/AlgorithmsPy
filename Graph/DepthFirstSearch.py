# You have been given a graph consisting of N nodes and M edges. The nodes in this graph are enumerated from 1 to N .
# The graph can consist of self-loops as well as multiple edges. This graph consists of a special node called the head node. 
# You need to consider this and the entry point of this graph. You need to find and print the number of nodes that are unreachable from this head node.

# Input Format
# The first line consists of a 2 integers N and M denoting the number of nodes and edges in this graph. 
# The next M lines consist of 2 integers a and b denoting an undirected edge between node a and b. 
# The next line consists of a single integer x denoting the index of the head node.

# *Output Format *:
# You need to print a single integer denoting the number of nodes that are unreachable from the given head node.

class UndirectedGraph():
    noOfNodes = 100
    graph = []
    # graphInput = ['8 1', '8 3', '7 4', '7 5', '2 6', '10 7', '2 8', '10 9', '2 10', '5 10'] # added 6, 5 for testing 
    graphInput = [ 
        '23 1',
        '69 2',
        '52 3',
        '73 4',
        '83 5',
        '69 6',
        '96 7',
        '60 8',
        '49 9',
        '52 10',
        '79 11',
        '62 12',
        '79 13',
        '73 14',
        '73 15',
        '83 16',
        '73 17',
        '93 18',
        '78 19',
        '75 20',
        '79 21',
        '85 22',
        '89 23',
        '21 24',
        '85 25',
        '14 26',
        '68 27',
        '31 28',
        '99 29',
        '4 30',
        '94 31',
        '85 32',
        '15 33',
        '82 34',
        '75 35',
        '100 36',
        '77 37',
        '61 38',
        '89 39',
        '90 40',
        '57 41',
        '76 42',
        '98 43',
        '45 44',
        '96 45',
        '52 46',
        '5 47',
        '21 48',
        '83 49',
        '4 50',
        '9 51',
        '18 52',
        '14 53',
        '36 54',
        '37 55',
        '40 56',
        '74 57',
        '5 58',
        '83 59',
        '94 60',
        '78 61',
        '78 62',
        '21 63',
        '26 64',
        '39 65',
        '94 66',
        '97 67',
        '76 68',
        '5 69',
        '7 70',
        '50 71',
        '39 72',
        '78 73',
        '76 74',
        '7 75',
        '63 77',
        '74 78',
        '19 79',
        '82 80',
        '18 81',
        '79 82',
        '14 83',
        '12 84',
        '57 85',
        '69 86',
        '60 87',
        '93 88',
        '63 89',
        '62 90',
        '17 91',
        '31 92',
        '78 93',
        '93 94',
        '73 95',
        '61 96',
        '63 97',
        '21 98',
        '30 99',
        '85 100']       

    # arr = [[0 for i in range(no_of_cols)] for j in range(no_of_rows)]
    def __init__(self):
        self.graph = self.makeGraph(self.graphInput)

   # using a two dimensional list to represent graph 
    # node 1 is graph[0], all items in graph[0] are the nodes it connects to. 
    # node - 1 to get it's index
    def makeGraph(self, graphInfo: list) -> list:       
        graph = []
        for i in range(self.noOfNodes):
            graph.append([]) # add a list as a item                
        for edge in graphInfo:
            nodes = edge.split()
            nodeIndex = self.getIndex(int(nodes[0]))
            adjacent = int(nodes[1])
            graph[nodeIndex].append(adjacent)        
        return graph

    def depthFirstSearch(self, headNode: int) -> list:
            stack = []
            visited = [False] * self.noOfNodes
            current = headNode
            visited[self.getIndex(headNode)] = True
            stack.append(current)            
            while len(stack) > 0:
                current = stack[len(stack) - 1] # get the last one 
                while len(self.getNotVisited(current, visited)) > 0:
                    current = self.getNotVisited(current, visited)[0]               
                    stack.append(current)
                    visited[self.getIndex(current)] = True                  
                current = stack.pop()                          
                print('Node {} is visied'.format(current))


    # this one uses recursive algorithm to search graph, less code 
    def depthFirstSearchRecursive(self, node: int, visited: list):
        if visited[self.getIndex(node)] == False:            
            visited[self.getIndex(node)] = True
            print('Node {} is visied'.format(node))
            adjenctNodes = self.getAdjancentNodes(node)
            for adj in adjenctNodes:
                self.depthFirstSearchRecursive(adj, visited)


    def getNotVisited(self, node: int, visited: list) -> list:
        adjancent = self.getAdjancentNodes(node)
        return [node for node in adjancent if visited[self.getIndex(node)] == False]

    # get adjancent nodes  
    def getAdjancentNodes(self, node: int) -> list:
        index = self.getIndex(node)
        return self.graph[index]


        # from the graph list, get the nodes and make a grahp
    def getIndex(self, node: int) -> int:
        return node - 1
        

graph = UndirectedGraph()
headNode = 10
graph.depthFirstSearch(headNode)

print('using depth first search')
visited = [False] * graph.noOfNodes
graph.depthFirstSearchRecursive(headNode, visited)








