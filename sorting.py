###Sorting
##Bubble Sort
def bubble_sort(arr):
  n =len(arr)
  for i in range (n-1):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1]=arr[j+1], arr[j]
  return arr

data=[64, 34, 25, 12, 22, 11, 90]
sorted_data=bubble_sort(data.copy())
print("data dalam sorting",data)
print("data setelah di sorting",sorted_data)

##Selection sort
def select_sort(arr):
  n=len(arr)
  for i in range(n-1):
    min_index = i
    for j in range (i+1,n):
      if arr[j]<arr[min_index]:
        min_index=j
    arr[i], arr[min_index] = arr[min_index],arr[i]
  return arr


data=[64, 25, 12, 22, 11]
sorted_data = select_sort(data.copy())
print("data dalam sorting",data)
print("data setelah di sorting",sorted_data)

##Insertion Sort
def insert_sort(arr):
  n=len(arr)
  for i in range (1, n):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
      arr[j+1]=arr[j]
      j -= 1
    arr[j+1] = key
  return arr

data = [64,34,25,12,11,11,90]
sorted_data=insert_sort(data.copy())
print("data dalam sorting",data)
print("data setelah di sorting",sorted_data)

##Merge Sort
def merge_sort(arr):
  if len(arr)>1:
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)

    i = j = k = 0

    while i < len(left_half)and j < len(right_half):
      if left_half[i] < right_half[j]:
        arr[k] = left_half[i]
        i += 1
        k += 1
      else:
        arr[k] = right_half[j]
        j += 1
        k += 1

    while i < len(left_half):
      arr[k]= left_half[i]
      i += 1
      k += 1

    while j < len(right_half):
      arr[k]= right_half[j]
      j += 1
      k += 1
  return arr

data= [64, 25, 12, 22, 11]
sorted_data=merge_sort(data.copy())
print("data dalam sorting",data)
print("data setelah di sorting",sorted_data)

#Quick sort
def quick_sort(arr):
  if len (arr)<1 :
    return arr

  pivot = arr[len(arr)//2]
  left =[x for x in arr if x < pivot]
  middle =[x for x in arr if x == pivot]
  right =[x for x in arr if x > pivot]

  return  quick_sort(left) + middle + quick_sort(right)

data= [12,61,84,64,21,35]
sorted_data=quick_sort(data.copy())
print("data dalam sorting",data)
print("data setelah di sorting",sorted_data)


##Studi kasus menggunakan Bubble Sort
def bubble_sort(arr):
  n =len(arr)
  for i in range (n-1):
    for j in range(n-i-1):
      if arr[j]["harga"] > arr[j+1]["harga"]:
        arr[j], arr[j+1]=arr[j+1], arr[j]
  return arr

#daftar harga barang
#menggunakan dictionary
barang=[
       {"nama":"kipas", "harga":22000},
       {"nama":"sisir", "harga":5000},
       {"nama":"baju", "harga":110000},
       {"nama":"tempat pensil", "harga":18000},
       {"nama":"setrika", "harga":98000}
]

#memanggil fungsi menggunakan perulangan
sorted_data=bubble_sort(barang.copy())#perintah memanggil function

print("Barang dan harga sebelum di sort")
print()
for nama in barang:
  print(f"barang :{nama["nama"]}, harga:{nama["harga"]}")
print()
print("-"*45)
print("\nbarang dan harga setelah di sort dari yang termurah")
print()
for nama in sorted_data:
  print("barang: ",nama["nama"], "harga: ",nama["harga"])

