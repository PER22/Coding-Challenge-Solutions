class Solution:
	def pascalTriangleRow(self, rowNo: int) -> List[int]:
		if rowNo == 0: 
			return []
		if rowNo == 1:
			return [1]
		if rowNo == 2:
			return [1,1]
		nth_row = [1]
		for i in range(1,rowNo):
			nth_row.append(int(nth_row[i-1] * (rowNo - i)/i))
		return nth_row