class Solution:
	
	def merge(self, arr1, arr2):
		i, j = 0, 0
		merged_array = []

		while i < len(arr1) and j < len(arr2):
			if arr1[i] < arr2[j]:
				merged_array.append(arr1[i])
				i += 1
			else:
				merged_array.append(arr2[j])
				j += 1

		while i < len(arr1):
			merged_array.append(arr1[i])
			i += 1

		while j < len(arr2):
			merged_array.append(arr2[j])
			j += 1

		return merged_array
		
		
	def mergeSort(self, arr: List[int]) -> List[int]:
		if len(arr) < 2:
			return arr
		
		left = arr[:len(arr)//2]
		right = arr[len(arr)//2:]
		
		left = self.mergeSort(left)
		right = self.mergeSort(right)
		
		return self.merge(left, right)