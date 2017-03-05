import Structures

list = Structures.SimpleList()

list.append("hola")
list.append("mundo")
list.append("adios")

list.report()

print(list.remove(0))
print(list.remove(0))
print(list.remove(0))


queue = Structures.Queue()

queue.enqueue(1)
queue.enqueue(2014)
queue.enqueue(50)

queue.report()

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


stack = Structures.Stack()

stack.push(1)
stack.push(2017)
stack.push(52)

stack.report()

print(stack.pop())
print(stack.pop())
print(stack.pop())

matrix = Structures.SparseMatrix()

matrix.insert("a.com", "rt")
matrix.insert("s.com", "rto")
matrix.insert("s.com", "rts")
matrix.insert("s.com", "rtb")
matrix.insert("a.com", "rti")
matrix.insert("f.com", "rto")
matrix.insert("f.com", "rts")
matrix.insert("k.com", "rtb")


import subprocess
script = open('Matrix.dot', 'w+')
script.write("hola mundo")
script.close()
subprocess.call(['rm', 'Matrix.dot'])
