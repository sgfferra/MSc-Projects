def floyd_warshall(distance, n, k):
   #Implements Floyd's algorithm recursively to find shortest paths.
    #Args: distance: A 2D matrix representing the distance matrix. n: The number of vertices in the graph. k: The intermediate vertex for the current recursive call.
    #Return:The updated distance matrix with shortest paths.
for i in range(n):
     for j in range(n):
        if distance[i][k] + distance[k][j] < distance[i][j]:
            distance[i][j] = distance[i][k] + distance[k][j]
                
    if k == n - 1:
        return distance
  
  else:
        return floyd_warshall(distance, n, k + 1)

#Example usage
dist = [[0, 3, INF, 7],
        [INF, 0, 4, 1],
        [INF, INF, 0, 5],
        [INF, INF, INF, 0]

result = floyd_warshall(dist, len(dist), 0)

print(result)  # Output: [[0 3 7 1], [INF 0 4 1], [INF INF 0 5], [INF INF INF 0]]