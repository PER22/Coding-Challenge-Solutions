class Solution:
	def largestContiguousSum(self, arr: List[int]) -> int:
		if not arr:
			return 0
		if len(arr) == 1:
			return arr[0]
		max_so_far = arr[0]
		max_ending_here = arr[0]
		for i in range(1, len(arr)):
			max_ending_here = max(max_ending_here + arr[i], arr[i])
			max_so_far = max(max_so_far, max_ending_here)
		return max_so_far

			