class Solution:
    
    def canGetCheese(self, maze):
        if not maze or not maze[0]:
            return False

        height, width = len(maze), len(maze[0])
        dp = [[False] * width for _ in range(height)]
        dp[-1][-1] = True  # Assuming the bottom-right cell is the goal

        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                # If not the bottom-right cell
                if i != height - 1 or j != width - 1:
                    right = dp[i][j+1] if j + 1 < width else False
                    down = dp[i+1][j] if i + 1 < height else False
                    dp[i][j] = maze[i][j] == 1 and (right or down)

        return dp[0][0]
