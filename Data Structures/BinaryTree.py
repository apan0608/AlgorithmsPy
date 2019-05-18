class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data 

class Solution:

    # def __new__(self):
    #     return self
    def copyList(self, original: list, right: list, left: list):
        midOfList = len(original) // 2        
        right = original[0 : midOfList]
        left = original[midOfList : len(original)]
    

    def copyList2(self, original: list, startIndex: int, endIndex: int) -> list:
        return original[ startIndex : endIndex ]


    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        print(root)

    def makeNode(self, nodes: list) -> TreeNode:
        
        if (len(nodes) == 0):
            return None
        
        else:
            value = nodes[0]
            del nodes[0]

        mid = len(nodes) // 2   
        # split node here to left and right 
        leftNodes = self.copyList2(nodes, 0, mid)
        rightNodes = self.copyList2(nodes, mid, len(nodes))

        # self.copyList(nodes, leftNodes, rightNodes)
        node = TreeNode(value)    
        node.left = self.makeNode(leftNodes)
        node.right = self.makeNode(rightNodes)
        return node


    def makeTree(self):
        nodes = [10,5,15,3,7, None,18, 21, 22, 2,3, 5 ,6]
        node = self.makeNode(nodes)    
        self.traverseTree(node)       


    def traverseTree(self, node):
        print(node.value)
        if node.left != None:
            self.traverseTree(node.left)
        if node.right != None:
            self.traverseTree(node.right)

    # instance method, needs to instantiate the class to call
    def test(self):
        nodes = [10,5,15,3,7, None,18]
        self.makeTree(nodes) #use self to call instance method with in a class

    @staticmethod
    def callStaticMethod():
        print("static method is triggered")

    @staticmethod
    def testWithStatic():
        Solution.callStaticMethod() # call a static
        s = Solution() # call an instance
        s.test()

    @classmethod
    def testWithClass(cls):
        print("class method called")
        Solution.callStaticMethod() #add calss signature when calling static method 
        cls.test()#we can use the instance(cls) here to call the instance method

s = Solution()
s.makeTree()
# class method need the class to be initialized 
# s = Solution()
# s.testWithClass()
# static method doesn't need an instance
# Solution.testWithStatic()
# Initialize class before we call the method
# s = Solution()
# s.test()
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
