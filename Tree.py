'''
program binary tree manual berdasarkan identitas saya
(Nama dan NPM)
'''
class node: #buat class dengan nama node
   def __init__(self, data): #tambahkan parameter self dan atribut bernama data
    self.data=data #variabel pemenyimpan nilai data
    self.left=None #variabel penyimpan nilai node kiri
    self.right=None #variabel penyimpan nilai node kanan

root=node(25)#node utama
root.left=node(9)#node parent kiri
root.right=node(21)#node parent kanan
root.left.left=node(13)#node child kiri
root.right.right=node(7)#node child kanan

#fungsi traversal inorder
def inorder(node):#buat var baru dan parameter
  if node: #jika node memiliki nilai
    inorder(node.left) #cek node kiri
    print(node.data, end=' ') #cetak node
    inorder(node.right) #cek node kanan

print('Berikut hasil traversal inorder tree dari nama dan npm saya')
inorder(root)



##Binary Search Tree data numerik unik
#Membuat class node dan BST juga fungsi insert
class node:
  def __init__(self, data):
    self.data=data
    self.left=None
    self.right=None
    
class BST:
  def __init__(self):
    self.root=None

  def insert(self,root,data):
    if root is None:#jika node belum ada
      return node(data)#tambahkan node

    if data < root.data:#jika node lebih kecil dari root
      root.left=self.insert(root.left, data)#masukkan ke node kiri
    else:
      root.right=self.insert(root.right, data)#masukkan ke node kanan
    return root#kembalikan semua nilai

#Memasukkan list angka dan memanggil fungsi insert
bst=BST()
root=None
data_list=[21,13,7, 77, 97, 8,99 ]
for value in data_list:
  root=bst.insert(root, value)

#membuat fungsi traversal inorder, preorder, postorder
def inorder(node): #kiri -> root-> kanan
  if node: 
    inorder(node.left)
    print(node.data, end=' ')
    inorder(node.right)
def preorder(node):#root -> kiri -> kanan
  if node:
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)
def postorder(node): #kiri -> kanan -> root
  if node:
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")

#memanggil semua fungsi traversal
print("\nHasil dari inorder traversal")
inorder(root)
print("\nHasil dari preorder traversal")
preorder(root)
print("\nHasil dari postorder traversal")
postorder(root)

#Search key BST
print("\nBerikut ini pencarian dua digit terakhir NPM")
print("dan juga angka yang tidak ada di list")
print("yaitu 21 dan 67")

def search(node,key): #parameter yang diproses ialah node dan key
  if node is None or node.data==key:
    return node
  if key < node.data: #jika key lebih kecil dari root
    return search(node.left, key) #cari node kiri,
  return search(node.right, key)#cari node kanan samakan dengan key

key=21
hasil=search(root,key) #panggil fungsi search dan parameternya
if hasil:
  print(f"\n {key} ditemukan dalam tree")
else:
  print(f"\n {key} tidak ditemukan dalam tree")

key=67
hasil=search(root,key)
if hasil:
  print(f"\n {key} ditemukan dalam tree")
else:
  print(f"\n {key} tidak ditemukan dalam tree")



