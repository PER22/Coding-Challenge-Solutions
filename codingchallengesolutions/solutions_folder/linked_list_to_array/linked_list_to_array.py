class Solution:
	def linkedListToArray(self, head: ListNode) -> List[int]:
		arr = []
		while head != None:
			arr.append(head.data)
			head = head.next
		return arr