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
		
		head = mainPoint = ListNode()

		point1, point2 = l1, l2
		while point1 != None:
			if point2 != None:
				sum = point1.val+point2.val+mainPoint.val
				mainPoint.next = ListNode()
				#carry = 0
				if sum >= 10:
					mainPoint.next=ListNode(1)
					sum = sum - 10
				mainPoint.val = sum
				#print(f"{one.val} -> {two.val}")
				mainPoint = mainPoint.next

				point1, point2 = point1.next, point2.next
		


		return head


a = makeLinkedList([3,4,5])

f = makeLinkedList([4,6,5])

head = Solution()
asa = head.addTwoNumbers(a,f)

#asa = makeLinkedList(a)
while asa != None:
	print(f"{asa.val} ->", end= " ")
	asa = asa.next
