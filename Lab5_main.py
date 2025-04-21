import random
def count_islands(matrix):

      n = len(matrix)
      m = len(matrix[0])
      visit = [[False]*m for _ in range(n)]
      def search(i, j):
            if i < 0 or i>=n or j < 0 or j >= m:
                  return
            if matrix[i][j] == 0 or visit[i][j]:
                  return
            visit[i][j] = True

            direction = [
                  (-1, -1), (-1, 0), (-1, 1),
                  (0, -1),            (0, 1),
                  (1, -1),  (1, 0),  (1, 1)
                  #напрямки пошуку
            ]
            for x, y in direction:
                  search(i + x, j + y)
      
      count = 0
      for i in range(n):
            for j in range(m):
                  if matrix[i][j] == 1 and not visit[i][j]:
                        search(i, j)
                        count +=1
      return count

# def generate_map(rows, cols, land_prob=0.4):
#       return [[1 if random.random() < land_prob else 0 for _ in range(cols)] for _ in range(rows)]

# def print_map(matrix, filename="map.txt"):
#       with open(filename, "w", encoding="utf-8") as f:
#             for row in matrix:
#                   line = "".join("█" if cell == 1 else "░" for cell in row)
#                   f.write(line + "\n")
                  

# rows, cols = 200, 200
# matrix = generate_map(rows, cols)
# print_map(matrix)
# islands = count_islands(matrix)
# print(islands)  

