import heapq # Import heap queue for priority queue

def uniform_cost_search(graph, start, goal):

 priority_queue = [(0, start)] # Min-Heap storing (cost, node)

 visited = set()

 while priority_queue:

 cost, node = heapq.heappop(priority_queue) # Get node with lowest cost

 if node in visited:

 continue # Skip if already visited
 visited.add(node)

 if node == goal:

 return cost # Return the least-cost path

 for neighbor, edge_cost in graph.get(node, []):

 if neighbor not in visited:

 heapq.heappush(priority_queue, (cost + edge_cost, neighbor))

 return float("inf") # Return if no path found

# Example graph as adjacency list

graph = {

 'A': [('B', 1), ('C', 4)],

 'B': [('D', 2), ('E', 5)],

 'C': [('F', 3)],

 'D': [('G', 1)],

 'E': [('G', 2)],

 'F': [('G', 6)],

 'G': [] # Goal node

}

# Run UCS from 'A' to 'G'

start_node = 'A'

goal_node = 'G'

result = uniform_cost_search(graph, start_node, goal_node)

print(f"Shortest Cost from {start_node} to {goal_node}: {result}")

RESULT:

Thus the program for Uniform-Cost Search was implemented a
