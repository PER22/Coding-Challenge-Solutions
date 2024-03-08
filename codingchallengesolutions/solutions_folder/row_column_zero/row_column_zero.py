class Solution:
    def setRowColumnZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        zeroed_rows = set()
        zeroed_columns = set()

        # Identify which rows and columns need to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zeroed_rows.add(i)
                    zeroed_columns.add(j)

        # Set identified rows to zero
        for row in zeroed_rows:
            for j in range(cols):
                matrix[row][j] = 0

        # Set identified columns to zero
        for col in zeroed_columns:
            for i in range(rows):
                matrix[i][col] = 0
