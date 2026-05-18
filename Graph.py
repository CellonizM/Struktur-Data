##Latihan
#1.membuat graf tak berarah dengan representasi adjecency list
graf = {
    "A":["C","F"],
    "B":["A","C","D"],
    "C":["F"],
    "D":["B","D","E"],
    "E":["A","F","D"],
    "F":["C","A","B"],
}
# Membuat fungsi menampilkan simpul dan edge
def printgraf(graf):
  for node in graf:
    print(f"{node} -> {graf[node]}")


#2. Membuat traversal DFS dan BFS
#BFS
from collections import deque
def bfs (graf,start):
  visited=set()
  queue=deque([start])

  while queue:
    vertex = queue.popleft()
    if vertex not in visited:
      print(vertex, end=' ')
      visited.add(vertex)
      queue.extend([neighbor for neighbor in graf[vertex] if neighbor
                   not in visited])


#dfs
def dfs (graf, start, visited=None):
  if visited==None:
    visited=set()

  if start not in visited:
    print(start, end=' ')
    visited.add(start)
    for neighbor in graf[start]:
      dfs(graf,neighbor, visited)
  return visited


#3. Memodifikasi BFS agar mengembalikan
#   list urutan kunjungan
from collections import deque

def bfs_mod (graf,start):
  visited=set()
  queue=deque([start])

  while queue:
    vertex = queue.popleft()
    if vertex not in visited:
      print(vertex, end=' ')
      visited.add(vertex)
      queue.extend([neighbor for neighbor in graf[vertex] if neighbor
                   not in visited])
      print(visited)


#4. Membuat fungsi find_path
from collections import deque

print("A-F")
start=input("masukkan simpul awal : ").capitalize()
end=input("masukkan simpul akhir : ").capitalize()

def find_path (graf, start, end, path=[]):
  path += [start]
  if start == end:
    return path
  for node in graf[start]:
    if node not in path:
      new=find_path(graf,node,end,path)
      if new:
        return new
  return ("jalur tidak ditemukan")


#5. Membuat fungsi is_connected
def is_connect(graf):
  start=next(iter(graf))
  visited_node=dfs(graf,start)
  return len(visited_node)==len(graf)

#Menampilkan semua fungsi
print("Graf :")
printgraf(graf) # 1
print()
print("hasil bfs C : ") # 2
bfs(graf,"C")
print()
print("\nhasil dfs F : ") # 2
dfs(graf,"F")
print()
print("\nlist urutan kunjungan : ") # 3
bfs_mod(graf,"C")
print()
print(f"jalur dari {start} ke {end} : {find_path(graf,start,end)}") #4
print("\napakah semua simpul terhubung ?",is_connect(graf))

#Latihan personal
#Lengkapi fungsi menghitung jumlah tetangga tiap simpul dalam graf
graf = {
    "A":["C","F"],
    "B":["A","C","D"],
    "C":["F"],
    "D":["B","D","E"],
    "E":["A","F","D"],
    "F":["C","A","B"],
}
def count_neighbor(graf):
  result={}
  for node in graf:
    result[node]=len(graf[node])
  return result

count_neighbor(graf)
