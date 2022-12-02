class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

def makeLinkedList(l1):

	nodes = []
	for i in l1:
		nodes.append(ListNode(i))
	for i in range(len(nodes)-1):
		nodes[i].next = nodes[i+1]
	return nodes[0]


		
from typing import Optional
class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		
		asa = head = mainPoint = ListNode()

		point1, point2 = l1, l2
		while point1 != None:
			if point2 != None:
				#len(l1) == len(l2)
				sum = point1.val+point2.val+mainPoint.val
				point1, point2 = point1.next, point2.next
	
			else:
				#len(l1) > len(l2)
				sum = point1.val+mainPoint.val
				point1= point1.next

			mainPoint.next = ListNode()
			if sum >= 10:
				mainPoint.next=ListNode(1)
				sum = sum - 10
			mainPoint.val = sum
			head = mainPoint
			mainPoint = mainPoint.next
		
		while point2 != None:
			#len(l1) < len(l2)
			sum = point2.val+mainPoint.val
			point2= point2.next
			mainPoint.next = ListNode()
			#carry = 0
			if sum >= 10:
				mainPoint.next=ListNode(1)
				sum = sum - 10
			mainPoint.val = sum
			head = mainPoint
			mainPoint = mainPoint.next

			

		
		if head.next.val == 0:
			head.next = None
		return asa

l1 = [1,2,3]
l2 = [4,5,5,5,5]
a = makeLinkedList(l1)

f = makeLinkedList(l2)

head = Solution()
asa = head.addTwoNumbers(a,f)

#asa = makeLinkedList(a)
while asa != None:
	print(f"{asa.val} ->", end= " ")
	asa = asa.next
