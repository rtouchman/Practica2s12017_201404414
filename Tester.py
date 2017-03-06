import Structures

list = Structures.SimpleList()

list.append("hola")
list.append("mundo")
list.append("adios")

#list.report()

print(list.remove(0))
print(list.remove(0))
print(list.remove(0))


queue = Structures.Queue()

queue.enqueue(1)
queue.enqueue(2014)
queue.enqueue(50)

#queue.report()

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


stack = Structures.Stack()

stack.push(1)
stack.push(2017)
stack.push(52)

#stack.report()

print(stack.pop())
print(stack.pop())
print(stack.pop())

matrix = Structures.SparseMatrix()

print(matrix.insert("a.com", "rt"))
