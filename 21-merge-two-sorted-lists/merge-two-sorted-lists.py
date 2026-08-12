# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        out = []
        if list1 == None:
            return list2
        curr = list1
        while curr != None:
            out.append(curr.val)
            curr = curr.next
        if list2 == None:
            return list1
        curr = list2
        while curr != None:
            out.append(curr.val)
            curr = curr.next
        out.sort()
        curr = list1
        i = -1
        c = 0
        while curr != None:
            i += 1
            curr.val = out[i]
            if curr.next == None and c==0:
                curr.next = list2
                curr = curr.next
                c = 1
            else:
                curr = curr.next
        return list1