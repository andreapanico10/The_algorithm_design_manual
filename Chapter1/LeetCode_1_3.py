''' First use of linked list in Python: nice example

    Given the head of a linked list, rotate the list to the right by k places.

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
# Function to insert a node at the beginning
# of the linked list
def push(head_ref, new_number):
 
    # allocate node
    new_node = ListNode(0)
     
    # put in the data
    new_node.val = new_number
         
    # link the old list at the end
    #of the new node
    new_node.next = head_ref
         
    # move the head to point to the new node
    head_ref = new_node
     
    return head_ref    

# Function to print linked list 
# to list
def linkedListToList(head):
    out_list = []
    element = head
    out_list.append(element.val)
    
    while(element.next):
        element = element.next
        out_list.append(element.val)
    return out_list

# Function to remove the last node
# of the linked list
def removeLastNode(head):
    
    second_last = head
    while(second_last.next.next):
        second_last = second_last.next
    
    last_element = second_last.next
    second_last.next = None
    
    return head, last_element

class Solution(object):

 
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        for i in range(k):
            head, last_elem = removeLastNode(head)
            head = push(head, last_elem.val)
        
        return head
        #linkedListToList(head)
        #output = linkedListToList(head)
        #return output