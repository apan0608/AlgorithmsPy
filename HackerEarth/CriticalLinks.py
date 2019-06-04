# This problem is taken from hacherearth, but not resolved. 
# The problem is really blurry and didn't explain it self to me
class CriticalLinks():
    graph: list # a two dimentional array represent a graph
    nodes: dict # represents all the nodes in graph
    edges: list # list of tuple representing the edges between the nodes
    # two disconnected compoenents have different number of node, less than this 
    nodeDifferenceLimit: int 

    # get the number of criticle links in the graph
    def getCriticalLinkCount(self) -> int:
        criticalEdgeCount = 0
        for edgeToRemove in self.edges:
            visitedA = self.depthFirstSearch(edgeToRemove[1], [], edgeToRemove) # start from end node           
            if len(visitedA) == len(self.nodes): # all nodes are visited
                continue
            unvisitedNodes = [node for node in self.nodes.keys() if node not in visitedA]
            for unvisitedNode in unvisitedNodes:                
                visitedB = self.depthFirstSearch(unvisitedNodes[0], [], edgeToRemove)
            if self.validateCriticalLink(visitedA, visitedB):
                criticalEdgeCount += 1 # the edge is a criticle edge
        return criticalEdgeCount

    # validate if the link is critical, visistedA is on one side and visitedB is on the other side
    # visitedA and visitedB can not overlap, all elements should be unique to each other 
    # visitedA + visitedB has to form the whole map, they need to traverse all the nodes 
    def validateCriticalLink(self, visitedA: list, visitedB: list) -> bool:
        countA = len(visitedA)
        countB = len(visitedB)
        if countA - countB >= self.nodeDifferenceLimit:
            return False
        if countA + countB != len(self.nodes):
            return False
        for nodeA in visitedA:
            if nodeA in visitedB:
                return False
        return True

    # return a list of visited nodes, Avoid searching for removed edge
    def depthFirstSearch(self, rootNode: int, visited: list, removedEdge: tuple) -> list:
        visited.append(rootNode)
        adjancentNodes = self.getAdjancentNodes(rootNode)
        for node in adjancentNodes:
            if removedEdge is not None and rootNode == removedEdge[0] and node == removedEdge[1]:
                continue
            if node not in visited:
                self.depthFirstSearch(node, visited, removedEdge)
        return visited

    # return a list of nodes that are connected to the rootNode
    def getAdjancentNodes(self, node: int) -> list:
        index = self.getIndex(node)
        return self.graph[index]        

    # given a node, get it's index
    def getIndex(self, node: int) -> int:
        return self.nodes[node]

    def makeGraph(self, graphInput: list, edges: list):
        counts = graphInput.split()
        noOfNodes = int(counts[0])
        noOfEdges = int(counts[1])
        nodeIndex = 0
        self.nodeDifferenceLimit = int(counts[2])
        self.graph = [[] for i in range(noOfNodes)] # list of list 
        self.nodes = {} # [i + 1 for i in range(noOfNodes)]
        self.edges = []
        for i in range(noOfEdges):
            edge = edges[i].split()
            startNode = int(edge[0])
            endNode = int(edge[1])
            if startNode not in self.nodes.keys():
                self.nodes[startNode] = nodeIndex
                nodeIndex += 1
            if endNode not in self.nodes.keys():
                self.nodes[endNode] = nodeIndex
                nodeIndex += 1
            self.edges.append((startNode, endNode))
            self.graph[self.getIndex(startNode)].append(endNode)
        # print(self.graph)
        # print(self.nodes)
        # print(self.nodeDifferenceLimit)
        # print(self.edges)

problem = CriticalLinks()
graphInfo = '340 164 380'
edges = [
    '301 89',
    '329 69',
    '214 22',
    '184 171',
    '8 271',
    '221 285',
    '186 283',
    '116 125',
    '21 95',
    '147 294',
    '59 57',
    '157 251',
    '262 70',
    '77 325',
    '282 259',
    '185 242',
    '220 173',
    '183 305',
    '194 26',
    '7 73',
    '168 99',
    '229 14',
    '41 217',
    '138 274',
    '311 284',
    '99 241',
    '212 255',
    '23 133',
    '197 100',
    '330 138',
    '230 174',
    '251 321',
    '218 93',
    '158 284',
    '330 36',
    '228 158',
    '135 117',
    '171 175',
    '205 180',
    '320 175',
    '335 79',
    '287 206',
    '205 182',
    '210 61',
    '281 199',
    '198 42',
    '244 321',
    '235 334',
    '73 264',
    '277 275',
    '299 164',
    '92 93',
    '152 134',
    '140 16',
    '185 331',
    '62 179',
    '69 221',
    '44 146',
    '62 125',
    '206 214',
    '196 276',
    '255 99',
    '128 21',
    '92 200',
    '284 240',
    '134 243',
    '276 97',
    '207 87',
    '102 218',
    '315 286',
    '209 248',
    '124 149',
    '128 39',
    '294 189',
    '164 32',
    '62 19',
    '179 189',
    '329 306',
    '209 293',
    '37 25',
    '64 43',
    '139 339',
    '139 5',
    '298 241',
    '95 272',
    '58 303',
    '179 182',
    '111 307',
    '220 277',
    '27 255',
    '180 89',
    '145 230',
    '149 6',
    '195 17',
    '170 103',
    '253 233',
    '145 51',
    '232 156',
    '268 61',
    '268 22',
    '204 325',
    '196 254',
    '38 178',
    '220 130',
    '114 119',
    '44 165',
    '207 61',
    '54 227',
    '66 120',
    '115 235',
    '223 28',
    '339 239',
    '290 102',
    '54 217',
    '162 193',
    '110 25',
    '178 305',
    '279 215',
    '15 30',
    '4 128',
    '20 260',
    '165 98',
    '320 218',
    '324 257',
    '210 99',
    '23 92',
    '126 21',
    '202 287',
    '335 256',
    '36 156',
    '320 145',
    '53 157',
    '322 203',
    '244 336',
    '104 119',
    '335 124',
    '250 159',
    '221 101',
    '249 205',
    '17 118',
    '303 251',
    '81 300',
    '144 282',
    '246 138',
    '69 281',
    '165 49',
    '298 217',
    '77 151',
    '291 192',
    '146 55',
    '183 12',
    '50 92',
    '43 270',
    '193 291',
    '6 81',
    '280 180',
    '332 232',
    '11 7',
    '45 129',
    '144 326',
    '281 180',
    '246 238',
    '57 322',
    '48 219']

graphInfo = '5 4 100'
edges = ['1 2', '2 3', '3 4', '4 5']
 
problem.makeGraph(graphInfo, edges)
print(problem.getCriticalLinkCount())


    





