# this is following hacker earch binary tree tutorial
# somne terms: Root, child, parent, siblings, descendant,
# Ancestor, leaf, internal node(at least one child), external node(no children) 
class Constant:
    Left = 'L'
    Right = 'R'

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class TreeProblem:
    
    # first line is no. of nodes and root node value 
    # the following lines are child nodes 
    # return the root node 
    def makeTree(self, inputs: list) -> TreeNode:
        line1 = inputs[0].split()
        noOfNodes = int(line1[0])
        nodeData = int(line1[1])
        root = TreeNode(nodeData)
        childInfoCount = noOfNodes - 1
        for i in range(childInfoCount):
            index = 1 + i * 2 # 2 nodes for root info, 2 lines for each chile
            position = inputs[index]
            data = int(inputs[index + 1])
            self.insertNode(root, position, data)
        return root

    
    # position L is the first level child 
    # RR is the second level child 
    def insertNode(self, root: TreeNode, postion: str, data: int) -> TreeNode:
        node = root
        for pos in postion: 
            if pos == Constant.Left:
                if node.left is None:
                    node.left = TreeNode(data) # the last item need to be inserted
                node = node.left
            else:
                if node.right is None:
                    node.right = TreeNode(data)
                node = node.right
        node.data = data
        return root

    # def markLeaves(self, root: TreeNode):
    # return the leaf after traverse , represented by L, LL, LR and etc
    # str is reference type in Python, list of char
    def traserveTree(self, node: TreeNode, position: str, leaves: list) -> list:
        if node and node.left:
            self.traserveTree(node.left, position + 'L', leaves)
        if node and node.right:
            self.traserveTree(node.right, position + 'R', leaves)
        if node.left == None and node.right == None:
            leaves.append(position)
        return leaves



    # Diameter is the number of nodes on the longest path between 
    # two leaves in the tree
    # given a list of leaf position 
    def getDiameter(self, leaves: list) -> int:
        diameter = 0
        for leaf in leaves:
            for otherLeaf in leaves:
                if otherLeaf == leaves:
                    continue
                else:
                    distance = self.resolveDistance(leaf, otherLeaf)
                    if distance > diameter:
                        diameter = distance
        return diameter
                
        # calculate farthest leaf on left to root and farthest leaf on right 

    def resolveDistance(self, leafA: str, leafB: str) -> int:
        shorter = lenA = len(leafA)
        lenB = len(leafB)
        substract = 0
        if shorter < lenB:
            shorter = lenB
        for i in range(shorter):
            if leafA[i] == leafB[i]:
                substract += 2
            else: 
                break
        return lenA + lenB + 1 - substract # 1 is the head node 



tree = TreeProblem()
inputs = [
'5 1',
'L',
'2',
'R',
'3',
'LL',
'4',
'LR',
'5']
root = tree.makeTree(inputs)
# print(root.left.right.data)
leaves = tree.traserveTree(root,'', [])
print(leaves)
diameter = tree.getDiameter(leaves)
print(diameter)






