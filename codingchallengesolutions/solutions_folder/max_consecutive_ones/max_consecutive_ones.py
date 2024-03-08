class Solution:
	def getMaxConsecutiveOnes(self, arr: List[int]) -> int:
		count = 0
		maximum = 0
		for i in range(len(arr)): 
			if arr[i] == 1:
				count += 1
				if maximum < count:
					maximum = count
			else:
				count = 0
		return maximum
		


