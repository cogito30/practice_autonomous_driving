import heapq

def dijkstra(grid, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while pq:
        current_cost, current = heapq.heappop(pq)

        if current == goal:
            break

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_pos = (current[0] + dx, current[1] + dy)

            if 0 <= next_pos[0] < len(grid) and 0 <= next_pos[1] < len(grid[0]) and grid[next_pos[0]][next_pos[1]] == 0:
                new_cost = current_cost + 1

                if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                    cost_so_far[next_pos] = new_cost
                    heapq.heappush(pq, (new_cost, next_pos))
                    came_from[next_pos] = current

    return came_from

# 맵 정의 (0: 도로, 1: 장애물)
grid = [
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

# 시작 위치와 목표 위치
start, goal = (0, 0), (3, 4)

dijkstra_path = dijkstra(grid, start, goal)
print(dijkstra_path)
