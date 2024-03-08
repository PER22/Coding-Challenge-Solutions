class Solution:
	def searchRange(self, arr: List[int], key: int) -> List[int]:
		def find_first():
			low, high = 0, len(arr) - 1
			first_occurrence = -1
			while low <= high:
				mid = low + (high - low) // 2
				if arr[mid] < key:
					low = mid + 1
				elif arr[mid] > key:
					high = mid - 1
				else:
					first_occurrence = mid
					high = mid - 1 
			return first_occurrence

		def find_last():
			low, high = 0, len(arr) - 1
			last_occurrence = -1
			while low <= high:
				mid = low + (high - low) // 2
				if arr[mid] < key:
					low = mid + 1
				elif arr[mid] > key:
					high = mid - 1
				else:
					last_occurrence = mid
					low = mid + 1  
			return last_occurrence

		return find_first(), find_last()


