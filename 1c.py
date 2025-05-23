def depth_limited_search(graph, node, goal, limit, depth=0):

 print(f"Visiting: {node}, Depth: {depth}")

 if node == goal:

 return True # Goal found

 if depth >= limit: # Stop at depth limit

 return False

 for neighbor in graph.get(node, []): # Explore neighbors
 if depth_limited_search(graph, neighbor, goal, limit, depth + 1):

 return True

 return False # Goal not found within limit

# Defining a simple graph using an adjacency list

graph = {

 'A': ['B', 'C'],

 'B': ['D', 'E'],

 'C': ['F', 'G'],

 'D': [],

 'E': [],

 'F': [],

 'G': []

}

# Running Depth-Limited Search

start_node = 'A'

goal_node = 'G'

depth_limit = 2

found = depth_limited_search(graph, start_node, goal_node, depth_limit)

if found:

 print(f"\nGoal '{goal_node}' found within depth limit {depth_limit}")

else:

 print(f"\nGoal '{goal_node}' NOT found within depth limit {depth_limit}")
