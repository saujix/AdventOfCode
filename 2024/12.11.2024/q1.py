from collections import deque

# Read the input grid
grid = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        grid.append(list(line.strip()))

# Directions for checking adjacent cells (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Function to check if a cell is valid
def is_valid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

# BFS function to calculate area and sides of a region
def bfs(grid, visited, x, y, n, m):
    plant_type = grid[x][y]
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 0
    sides = 0

    while queue:
        cx, cy = queue.popleft()
        area += 1

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if not is_valid(nx, ny, n, m) or grid[nx][ny] != plant_type:
                sides += 1  # Fence needed for this side
            elif not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return area, sides

# Main function to calculate total cost
def calculate_total_cost(grid):
    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    total_cost = 0

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                # Find a new region and calculate its area and sides
                area, sides = bfs(grid, visited, i, j, n, m)
                total_cost += area * sides  # Cost = area * sides

    return total_cost

# Calculate and print the total cost
total_cost = calculate_total_cost(grid)
print("New total price of fencing all regions:", total_cost)