import heapq

# Define the graph as an adjacency list with costs

graph = {

 'A': {'B': 2, 'C': 4},

 'B': {'D': 3, 'E': 1, 'C': 2},

 'C': {'F': 5, 'G': 3},

 'D': {},

 'E': {'H': 4},

 'F': {'H': 3},

 'G': {'H': 2},

 'H': {} # Goal node

}
# Define the heuristic function (Estimated cost to goal 'H')

heuristic = {

 'A': 7, 'B': 6, 'C': 2, 'D': 5, 'E': 4,

 'F': 3, 'G': 1, 'H': 0 # H is the goal node

}

# A* Search Algorithm

def a_star(graph, heuristic, start, goal):

 queue = [(0, start)] # Priority queue (F-score, Node)

 g_score = {node: float('inf') for node in graph} # Initialize g-scores

 g_score[start] = 0

 came_from = {} # Store path

 while queue:

 _, current = heapq.heappop(queue) # Pick node with lowest F-score

 if current == goal: # If goal reached, reconstruct the path

 path = []

 while current in came_from:

 path.append(current)

 current = came_from[current]

 path.append(start)

 return path[::-1] # Reverse path

 for neighbor, cost in graph[current].items():
temp_g = g_score[current] + cost # New g-score

 if temp_g < g_score[neighbor]: # If better path found

 g_score[neighbor] = temp_g

 f_score = temp_g + heuristic[neighbor] # F = G + H

 heapq.heappush(queue, (f_score, neighbor))

 came_from[neighbor] = current # Store best path
 return None # No path found

# Run A* Algorithm

start = 'A'

goal = 'H'

path = a_star(graph, heuristic, start, goal)

# Print the result

print(f"Shortest Path: {' -> '.join(path)}" if path else "No path found")
