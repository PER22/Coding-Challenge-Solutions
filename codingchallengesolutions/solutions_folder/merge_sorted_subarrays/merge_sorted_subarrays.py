class Solution:
	
	def merge(self, arr: List[int], endIndex: int) -> List[int]:
		result = []
		left_pointer = 0
		right_pointer = endIndex + 1
		while left_pointer <= endIndex and right_pointer < len(arr):
			if arr[right_pointer] < arr[left_pointer]:
				result.append(arr[right_pointer])
				right_pointer += 1
			else: 
				result.append(arr[left_pointer])
				left_pointer += 1
		
		if right_pointer < len(arr):
			result.extend(arr[right_pointer:])
		else:
			result.extend(arr[left_pointer:endIndex+1])
		return result


