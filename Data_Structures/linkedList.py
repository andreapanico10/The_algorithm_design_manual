# Definition for singly-linked list.
class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
 
    def __str__(self):
        return str(self.val)

class LinkedList():
    def __init__(self):
      self.head = None

    def searchInLinkedList(node: Node, toFind) -> Node:
        
        if node == null:
            return null
        if node.val == toFind:
            return node
        else:
            return search(node.next, toFind)

    def insertInLinkedList( list , toInsert):
        
        newNode = Node() 
        newNode.val = toInsert
        newNode.next = list.head
        list.head = newNode
    
    def itemAhead(head : Node, toDelete: Node) -> Node:
        if ((head == null) or (head.next == null)):
            return null
        
        if head.next == toDelete:
            return head
        else:
            return itemAhead(head.next, toDelete)
    
    def deleteNode(initialNode : Node, toDelete : Node):

        head = initialNode

        pred = itemAhead(initialNode, toDelete)

        if pred == null:
            initialNode = head.next
        else:
            pred.next = toDelete.next


lista = LinkedList()

node1 = Node()
node1.val = 1

node2 = Node()
node2.val = 2

node1.next = node2
#Automatically node2.next = null

lista.insertInLinkedList(node2)
lista.insertInLinkedList(node1)

print(lista.__dict__)