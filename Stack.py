##Stack dengan list
#append dan pop
stack = []

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")
stack.append("e")
stack.append("f")


print("\nisi dari stack awal")
print(*stack)

print("\nelement yang di pop")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nisi dari stack setelah di pop")
print(*stack)


#Stack dengan collections.deque
stack = deque()

stack.append("a")
stack.append("i")
stack.append("u")
stack.append("e")
stack.append("o")

print("stack awal")
print(*stack)

print("\nelement yang di pop")
print(stack.pop())
print(stack.pop())
print(stack.pop())


print("\nisi dari stack setelah di pop")
print(*stack)


#Stack dengan queue.LifeQueue
from queue import LifoQueue

stack=LifoQueue(maxsize=5)

print(stack.qsize())
print("empty: ",stack.empty())
print("full: ",stack.full())

stack.put("a")
stack.put("i")
stack.put("u")
stack.put("e")
stack.put("o")
print("\nsetelah menambahkan 5 elemen")
print("Full: ",stack.full())
print("Size: ",stack.qsize())

print("\nelement yang di pop") #jika didalam modul queue, gunakan get
print(stack.get())
print(stack.get())
print(stack.get())


print("\nempty: ",stack.empty())
print("full: ",stack.full())



##Stack dengan single linked list
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class stack:

  def __init__(self):
    self.head = Node("head")
    self.size = 0

  def __str__(self):
    cur=self.head
    out=" "
    while cur:
      out += str(cur.data) + "->"
      cur = cur.next
    return out[:-2]

  def getsize(self):
    return self.size == 0

  def isempty(self):
    return self.size==0

  def peek(self):

    if self.isempty():
      raise Exception ("peek from empty stack")
    return self.head.next.value

  def push(self, data):
    node = Node(data)
    node.next = self.head.next
    self.head.next= node
    self.size += 1

  def pop(self):
    if self.isempty():
        raise Exception("popping from empty stack")
    remove = self.head.next
    self.head.next = self.head.next.next
    self.size -= 1
    return remove.data

if __name__=="__main__":
  stack=stack()
  for i in range(1,11):
    stack.push(i)
  print(f"stack: {stack}")
  for _ in range(1,6):
    remove=stack.pop()
    print(f"pop: {remove}")
  print(f"stack: {stack}")
