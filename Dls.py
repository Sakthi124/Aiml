def depth_limited_search(graph, node, goal, limit):

 if node == goal:

 return True # Goal found

 if limit == 0:

 return False # Stop if depth limit is reached

 for neighbor in graph.get(node, []):

 if depth_limited_search(graph, neighbor, goal, limit - 1):

 return True

 return False

# Function for Iterative Deepening Search (IDS)
def iterative_deepening_search(graph, start, goal, max_depth):

 for depth in range(max_depth + 1):

 print(f"Searching at depth {depth}...")

 if depth_limited_search(graph, start, goal, depth):

 print(f"Goal '{goal}' found at depth {depth}")

 return

 print(f"Goal '{goal}' NOT found within depth {max_depth}")

# Example Graph Representation (Adjacency List)

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

# Run IDS to find goal node 'H' starting from 'A'

iterative_deepening_search(graph, 'A', 'H', 3)
