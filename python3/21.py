class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode | None:
		
		asa = ten = ListNode()
		
		if list1 == None and list2 == None:
			return None
		if list1 == None or list2 == None:
			if list1 == None:
				return list2
			return list1

		ten, dummy = (list1 , list2) if list1.val < list2.val else (list2, list1)

		asa.next = ten

		while ten.next != None:
			if ten.next.val <= dummy.val:
				ten = ten.next
			else:
				ten.next, dummy = dummy, ten.next
				ten = ten.next
		ten.next = dummy

		return asa.next


c = ListNode(5)
b = ListNode(3, c)
a = ListNode(1, b)

h = ListNode(8)
g = ListNode(6, h)
f = ListNode(4, g)

asa = Solution()
asa.mergeTwoLists(a, f)
