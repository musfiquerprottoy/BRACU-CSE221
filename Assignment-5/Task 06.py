import sys
from collections import deque


def solve():
    R, H = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(R):
        line = sys.stdin.readline().strip()
        grid.append(line)

    visited = [[False for _ in range(H)] for __ in range(R)]
    max_diamonds = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(R):
        for j in range(H):
            if grid[i][j] != '#' and not visited[i][j]:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                current_diamonds = 0

                while queue:
                    x, y = queue.popleft()
                    if grid[x][y] == 'D':
                        current_diamonds += 1

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < R and 0 <= ny < H:
                            if not visited[nx][ny] and grid[nx][ny] != '#':
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                if current_diamonds > max_diamonds:
                    max_diamonds = current_diamonds

    print(max_diamonds)

solve()