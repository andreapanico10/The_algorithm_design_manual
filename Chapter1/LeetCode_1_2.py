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
 
    if head_ref == None:
        return None
    
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
    
    if head == None:
        return None
    
    second_last = head
   
    if head.next == None:
        return None
    
    while(second_last.next.next):
        second_last = second_last.next
    
    last_element = second_last.next
    second_last.next = None
    
    return head, last_element

def getLinkListLen(head):
    
    list_len = 0
    
    if head == None:
        return list_len
    
    second_last = head
    list_len += 1
    
    while(second_last.next):
        second_last = second_last.next
        list_len += 1
    return list_len

class Solution(object):

 
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None or k == 0:
            return head
        
        list_len = getLinkListLen(head)
        
        for i in range(k % list_len):
            head, last_elem = removeLastNode(head)
            head = push(head, last_elem.val)
        
        return head
        #linkedListToList(head)
        #output = linkedListToList(head)
        #return output