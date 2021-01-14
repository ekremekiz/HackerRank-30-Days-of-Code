import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        node_list_in_the_tree = list()
        node_values_in_the_tree = ""
        node_list_in_the_tree.append(root)
        while len(node_list_in_the_tree) > 0:
            node = node_list_in_the_tree.pop(0)
            if node.left != None:
                node_list_in_the_tree.append(node.left)
            if node.right != None:
                node_list_in_the_tree.append(node.right)
            node_values_in_the_tree += str(node.data) + " "
        print(node_values_in_the_tree)
                    
            

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
