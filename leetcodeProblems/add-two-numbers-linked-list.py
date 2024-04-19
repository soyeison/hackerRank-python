import copy
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_linked_list(head):
    temp = head
    stack = []
    while temp is not None:
        stack.append(temp.val)
        temp = temp.next
    temp = head
    while temp is not None:
        temp.val = stack.pop()
        temp = temp.next
    return head

def listoToLink(lst):
    if len(lst) == 1:
        return ListNode(lst[0])
    return ListNode(lst[0], listoToLink(lst[1:]))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reversel1 = reverse_linked_list(copy.deepcopy(l1))
        reversel2 = reverse_linked_list(copy.deepcopy(l2))
        sumitaL1 = ""
        sumitaL2 = ""
        while True:
            sumitaL1 += str(reversel1.val)
            if reversel1.next == None:
                break
            else:
                reversel1 = reversel1.next

        while True:
            sumitaL2 += str(reversel2.val)
            if reversel2.next == None:
                break
            else:
                reversel2 = reversel2.next


        resultNumberStr = str(int(sumitaL2) + int(sumitaL1))
        resultList = [int(x) for x in resultNumberStr]

        resultLinkedList = listoToLink(resultList)
        return reverse_linked_list(resultLinkedList)