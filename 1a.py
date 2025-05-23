from collections import deque
def bfs(graph, start):
 visited = set() # Set to track visited nodes
 queue = deque([start]) # Initialize queue with start node
 while queue:
 node = queue.popleft() # Dequeue a node
 if node not in visited:
 print(node, end=" ") # Process the node
 visited.add(node) # Mark node as visited
 queue.extend(graph[node]) # Add all neighbors (even visited ones)
# Define the graph as an adjacency list
graph = {
 1: [2, 3],
 2: [1, 4, 5],
 3: [1, 6],
 4: [2],
 5: [2, 7],
 6: [3],
 7: [5]
}
# Perform BFS traversal from node 1
print("BFS Traversal:")
bfs(graph, 1)
