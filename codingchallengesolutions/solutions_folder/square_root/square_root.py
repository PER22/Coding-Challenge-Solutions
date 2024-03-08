class Solution:
	def searchRoot(self, n: int) -> int:
		if n == 0 or n == 1:
			return n
		
		upper_bound = 1
		while upper_bound * upper_bound < n :
			upper_bound *= 2
		lower_bound = upper_bound // 2	
		while lower_bound <= upper_bound:
			midpoint = (upper_bound + lower_bound) // 2
			square = midpoint * midpoint
			if square == n:
				return midpoint
			elif square < n:
				lower_bound = midpoint + 1
			else:
				upper_bound = midpoint - 1
        
		return lower_bound - 1
		

				
			
		


