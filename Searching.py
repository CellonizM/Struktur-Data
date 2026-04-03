##Searching Dalam Python
#Linear Search
def linsearch(arr, N, x):

  for i in range(0,N):
    if(arr[i]==x):
      return i
  return -1

#Driver Code
if __name__ == "__main__":
  arr = [20,40,30,50,10]
  x = 10
  N = len(arr)

  #Memanggil Function
  result=linsearch(arr,N,x) #memberitahu index dari data yang dicari
  if(result== -1):
    print("data tidak ditemukan")
  else:
    print("data ditemukan pada index ke : ",result)


#Binary Search
def binsearch(arr,l,r,x):

  while l <= r:

      mid = (l + r) // 2

      #fungsi mengecek jika x ada di median
      if arr[mid] == x:
        return mid

      #fungsi jika x lebih besar, buang sebelah kiri
      elif arr[mid] < x:
        l = mid + 1

      #fungsi jika x lebih kecil, buang sebelah kanan
      else:
        r = mid - 1

  #jika kondisinya sampai sini,
  #maka elementnya tidak ada
  return -1

#driver code
if __name__=="__main__":
  arr=[2,4,8,12,16,23,38,56,72,91]
  x = 23

  #memanggil fungsi
  result = binsearch(arr,0,len(arr)-1,x)
  if result != -1: #jika result tidak sama dengan -1
    print("element ada di index : ",result)
  else:
    print("elemen tidak ada di array")


#Binary Rekursif
def binarys(arr,l,r,x):

  #Check base case
  if r >= l:

    mid = (l+r) // 2

    #mengecek apakah elemen ada di mid
    if arr[mid]==x:
      return mid

    #Jika elemen lebih kecil dari mid
    #maka nilainya ada di bagian kiri array
    elif arr[mid] > x:
      return binarys(arr, l, mid-1, x)

    else: #elemen ada di bagian kanan array
      return binarys(arr, mid + 1, r, x)
      #karena lebih besar dari mid

  #jika sampai pada kondisi ini maka
  #elemen tidak ada dalam array
  else:
    return -1

#driver code
if __name__=="__main__":
  arr=[2,5,8,12,16,23,38,56,72,91]
  x=8

  #Memanggil fungsi
  result = binarys(arr, 0, len(arr)-1, x)

  if result != -1:
    print("element ada pada indeks ke : ",result)
  else:
    print("elemen tidak ada pada array ")


#Jump Search
import math

def jumpsearch(arr, x, n):

  #menentukan ukuran blok untuk dilompati
  step = math.sqrt(n)

  #Menemukan blok dimana elemennya ada
  prev=0
  while arr[int(min(step,n)-1)] < x:
      prev = step
      step += math.sqrt(n)
      if prev >= n:
        return -1

  #Melakukan linear search untuk x di
  #awal block dengan prev
  while arr[int(prev)] < x:
      prev += 1

      #Jika kita mencapai blok selanjutnya atau yang terakhir
      #dari array, maka elemen tidak ada
      if prev == min(step,n):
        return -1

  #kembalikan prev jika elemen ditemukan
  if arr[int(prev)] == x:
      return prev

  return -1


#Driver code
arr=[0,1,1,2,3,5,8,13,21,
     34,55,89,144,233,377,610]
x=144
n=len(arr)

#temukan index dari x dengan jump search
index=jumpsearch(arr,x,n)

#print lokasi index nya dan juga elemennya
index =int(index)
print("angka",x, "ada di index",index)

##Studi Kasus
#1. Mencari nilai max dan min dengan linear
class pair:
  def __init__(self):
    self.min=0
    self.max=0

def getminmax(arr: list, n: int) -> pair:
  minmax=pair()

  #Jika hanya ada satu element, kembalikan nilainya
  #sebagai max dan min
  if n == 1:
    minmax.max = arr[0]
    minmax.min = arr[0]
    return minmax
  #jika ada lebih dari satu elemen, maka mulai
  #pencarian min dan max
  if arr[0] > arr[1]:
    minmax.max = arr[0]
    minmax.min = arr[1]
  else:
    minmax.max = arr[1]
    minmax.min = arr[0]

  for i in range(2,n):
    if arr[i] > minmax.max:
      minmax.max = arr[i]
    elif arr[i] < minmax.min:
      minmax.min = arr[i]
  return minmax


  #Driver code
if __name__ =="__main__":
    arr=[24,345,485,165,134,45,95,25,147]
    arr_size=9
    minmax=getminmax(arr,arr_size)
    print("Elemen minimum nya adalah",minmax.min)
    print("Elemen minimum nya adalah",minmax.max)



#2. Menemukan angka hilang dan angka yang muncul dua kali
def printtwoel(arr):
  n = len(arr)
  temp=[0]*n #membuat variabel array temp dengan niilai awalnya 0
  repeatnum = -1
  missnum = -1

  for i in range(n):
    temp[arr[i]-1] += 1
    if temp[arr[i]-1]>1:
      repeatnum = arr[i]
  for i in range(n):
    if temp[i] == 0:
      missnum = i + 1
      break


  print("angka yang terulang =",repeatnum)
  print("angka yang hilang =",missnum)

#arr = [6,4,3,3,2,5]
arr = [3,5,1,6,4,3]
printtwoel(arr)
