def num_islands(matrix):
    if not matrix:
        return 0
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    def dfs(matrix, i, j):
        # If out of bounds or it's water ('0'), return
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] == 0:
            return
        
        # Mark the current land cell as visited by setting it to '0'
        matrix[i][j] = 0
        
        # Explore all 4 possible directions (up, down, left, right)
        dfs(matrix, i - 1, j)  # Up
        dfs(matrix, i + 1, j)  # Down
        dfs(matrix, i, j - 1)  # Left
        dfs(matrix, i, j + 1)  # Right
    
    island_count = 0
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                # We found an unvisited land ('1'), so we perform DFS
                dfs(matrix, i, j)
                island_count += 1  # After DFS, we have found an island
    
    return island_count

# Example matrix
matrix = [[1, 1, 0, 0],
          [0, 1, 0, 1,],
          [0, 0, 1, 1],
          [1, 0, 0,1]]

print(num_islands(matrix))  # Output will be the number of islands


