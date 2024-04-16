queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
print(queue)


from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')
print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)




from queue import Queue
q = Queue(maxsize = 3)
print(q.qsize()) 
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full()) 
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty()) 
print("Full: ", q.full())

