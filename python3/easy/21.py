class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode | None:
		
		head = hare = ListNode()
		
		if list1 == None and list2 == None:
			return None
		if list1 == None or list2 == None:
			if list1 == None:
				return list2
			return list1

		hare, turtoise = (list1 , list2) if list1.val < list2.val else (list2, list1)

		head.next = hare

		while hare.next != None:
			if hare.next.val <= turtoise.val:
				hare = hare.next
			else:
				hare.next, turtoise = turtoise, hare.next
				hare = hare.next
		hare.next = turtoise

		return head.next


c = ListNode(5)
b = ListNode(3, c)
a = ListNode(1, b)

h = ListNode(8)
g = ListNode(6, h)
f = ListNode(4, g)

head = Solution()
head.mergeTwoLists(a, f)
