import heapq

class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])  # 맨해튼 거리

    def search(self):
        pq = []
        heapq.heappush(pq, (0, self.start))
        came_from = {self.start: None}
        cost_so_far = {self.start: 0}

        while pq:
            _, current = heapq.heappop(pq)

            if current == self.goal:
                break

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                next_pos = (current[0] + dx, current[1] + dy)

                if 0 <= next_pos[0] < self.rows and 0 <= next_pos[1] < self.cols and self.grid[next_pos[0]][next_pos[1]] == 0:
                    new_cost = cost_so_far[current] + 1

                    if next_pos not in cost_so_far or new_cost < cost_so_far[next_pos]:
                        cost_so_far[next_pos] = new_cost
                        priority = new_cost + self.heuristic(self.goal, next_pos)
                        heapq.heappush(pq, (priority, next_pos))
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

a_star = AStar(grid, start, goal)
path = a_star.search()
print(path)
