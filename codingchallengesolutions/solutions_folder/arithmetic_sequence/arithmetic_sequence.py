class Solution:
	def isArithmeticSequence(self, arr: List[int]) -> bool:
		if len(arr) <= 2:
			return True
		smallest = min(arr[0], arr[1])
		secondSmallest = max(arr[0], arr[1])
		for eachValue in arr[2:]:
			if(eachValue < smallest):
				secondSmallest = smallest
				smallest = eachValue
			elif(eachValue < secondSmallest):
				secondSmallest = eachValue
		difference = secondSmallest - smallest
		map = {}
		for eachValue in arr:
			map[eachValue] = True
		for i in range(len(arr)):
			if smallest + (difference*i) not in map:
				return False
		return True