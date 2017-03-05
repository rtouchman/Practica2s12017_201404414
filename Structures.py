import subprocess


class Node(object):
    def __init__(self, data=None, right=None):
        self.data = data
        self.right = right

    def __str__(self):
        return str(self.data)


class SimpleList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            buffer = self.head
            while buffer.right is not None:
                buffer = buffer.right

            buffer.right = Node(data)

    def search(self, data):
        i = 0
        if self.head.data == data:
            return i
        else:
            buffer = self.head
            while buffer.right is not None:
                if buffer.data == data:
                    return i
                else:
                    buffer = buffer.right
                    i += 1

            if buffer.data == data:
                return i
            else:
                return None

    def remove(self, index):
        result = self.head
        if self.head is None:
            return None

        if index == 0:
            self.head = self.head.right
            return result
        else:
            buffer = self.head
            for i in range(index - 1):
                buffer = buffer.right

            result = buffer.right
            buffer.right = buffer.right.right

            return result

    def report(self):
        if self.head is None:
            return

        buffer = self.head
        i = 0
        report = open('ListReport.dot', 'w+')
        report.write("digraph SimpleList{\n \t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
        while buffer.right is not None:
            report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.right) + "\"]\n")
            report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
            buffer = buffer.right
            i += 1

        report.write("}")
        report.close()
        gen = open('gen.sh', 'w+')
        gen.write("dot ListReport.dot -Tjpg -o SimpleList.jpg\n")
        gen.write("xdg-open SimpleList.jpg\n")
        gen.close()
        subprocess.call(['./gen.sh'], shell=True)


class Queue(object):
    def __init__(self, head = None):
        self.head = head

    def enqueue(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            buffer = self.head
            while buffer.right is not None:
                buffer = buffer.right

            buffer.right = Node(data)

    def dequeue(self):
        if self.head is None:
            return None
        else:
            buffer = self.head
            if buffer.right is None:
                self.head = None
                return buffer
            else:
                while buffer.right.right is not None:
                    buffer = buffer.right

                result = buffer.right
                buffer.right = None
                return result

    def report(self):
        if self.head is None:
            return

        buffer = self.head
        i = 0
        report = open('QueueReport.dot', 'w+')
        report.write("digraph Queue{\n \t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
        while buffer.right is not None:
            report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.right) + "\"]\n")
            report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
            buffer = buffer.right
            i += 1

        report.write("}")
        report.close()
        gen = open('gen.sh', 'w+')
        gen.write("dot QueueReport.dot -Tjpg -o Queue.jpg\n")
        gen.write("xdg-open Queue.jpg\n")
        gen.close()
        subprocess.call(['./gen.sh'], shell=True)


class Stack(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            buffer = self.head
            while buffer.right is not None:
                buffer = buffer.right

            buffer.right = Node(data)

    def pop(self):
        result = self.head
        self.head = self.head.right
        return result

    def report(self):
        if self.head is None:
            return

        buffer = self.head
        i = 0
        report = open('StackReport.dot', 'w+')
        report.write("digraph Stack{\n \t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
        while buffer.right is not None:
            report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.right) + "\"]\n")
            report.write("\t" + str(i + 1) + "->" + str(i) + "\n")
            buffer = buffer.right
            i += 1

        report.write("}")
        report.close()
        gen = open('gen.sh', 'w+')
        gen.write("dot StackReport.dot -Tjpg -o Stack.jpg\n")
        gen.write("xdg-open Stack.jpg\n")
        gen.close()
        subprocess.call(['./gen.sh'], shell=True)


class MatrixNode(object):
    def __init__(self, domain=None, name=None, right=None,  down=None, back=None):
        self.domain = domain
        self.name = name
        self.right = right
        self.down = down
        self.back = back

    def __str__(self):
        return str(self.name + "@" + self.domain)


class SparseMatrix(object):
    def __init__(self):
        self.head = MatrixNode("ENC", "ENC")

    def insert(self, domain, name):
        bX = self.right(self.head, domain, "ENC")
        bY = self.down(self.head, "ENC", name[0])
        bX = self.down(bX.right, domain, name)
        bY = self.right(bY.down, domain, name)
        bX.down.right = bY.right.right
        bY.right = bX.down
        bX.down = self.back(bX.down, domain, name)

    @staticmethod
    def right(node, domain, name):
        if node.domain > domain and node.domain != "ENC":
            temp = node
            node = MatrixNode(domain, name)
            node.right = temp
            return node
        buffer = node
        while buffer.right is not None and buffer.right.domain < domain:
            buffer = buffer.right

        if buffer.right is None:
            buffer.right = MatrixNode(domain, name)
        elif buffer.right.domain > domain:
            temp = buffer.right
            buffer.right = MatrixNode(domain, name)
            buffer.right.right = temp

        return buffer

    @staticmethod
    def down(node
             , domain, name):
        if node.name[0] > name[0] and node.name != "ENC":
            temp = node
            node = MatrixNode(domain, name)
            node.down = temp
            return node
        buffer = node
        while buffer.down is not None and buffer.down.name[0] < name[0]:
            buffer = buffer.down

        if buffer.down is None:
            buffer.down = MatrixNode(domain, name)
        elif buffer.down.name[0] > name[0]:
            temp = buffer.down
            buffer.down = MatrixNode(domain, name)
            buffer.down.down = temp

        return buffer

    @staticmethod
    def back(node, domain, name):
        buffer = node
        if node.domain == domain and node.name == name:
            return node

        while buffer.back is not None:
            buffer = buffer.back

        buffer.back = MatrixNode(domain, name)
        return buffer
