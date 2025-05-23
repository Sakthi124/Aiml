import heapq

def greedy_bfs(graph, heuristics, start, goal):

 queue = [(heuristics[start], start)] # Priority queue (heuristic, node)

 visited = set()

 path = []

 while queue:

 _, current = heapq.heappop(queue) # Get the node with the lowest heuristic

 path.append(current)

 if current == goal:
 return path # Return the path when the goal is reached

 visited.add(current)

 for neighbor in graph[current]:

 if neighbor not in visited:

 heapq.heappush(queue, (heuristics[neighbor], neighbor))

 return None # No path found

# Example Graph

graph = {

 'A': ['B', 'C'],

 'B': ['D', 'E'],

 'C': ['F', 'G'],

 'D': [],

 'E': ['H'],

 'F': [],

 'G': [],

 'H': []

}

# Heuristic Values (Estimated cost to goal)

heuristics = {'A': 6, 'B': 4, 'C': 4, 'D': 3, 'E': 2, 'F': 4, 'G': 3, 'H': 0}

# Run Search

start, goal = 'A', 'H'

path = greedy_bfs(graph, heuristics, start, goal)

# Output Result

print(f"Path found: {' → '.join(path)}" if path else "No path found")
