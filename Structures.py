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
            for i in range(int(index) - 1):
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
        report.write("digraph SimpleList{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
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
        	result = self.head
        	self.head = self.head.right
        	return result

    def report(self):
        if self.head is None:
            return

        buffer = self.head
        i = 0
        report = open('QueueReport.dot', 'w+')
        report.write("digraph Queue{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
        while buffer.right is not None:
            report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.right) + "\"]\n")
            report.write("\t" + str(i + 1) + "->" + str(i) + "\n")
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
        report = open('StackReport.dot', 'w+')
        report.write("digraph Stack{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
        while buffer.right is not None:
            report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.right) + "\"]\n")
            report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
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
        bX = self.right(self.head, domain, "ENC", 1)
        bY = self.down(self.head, "ENC", name[0], 1)
        bX = self.down(bX.right, domain, name, 1)
        bY = self.right(bY.down, domain, name, 1)
        bX.down.right = bY.right.right
        bY.right = bX.down
        if bX.down.domain == domain and bX.down.name == name:
            return bX.down

        result = self.back(bX.down, domain, name)
        return result

    def searchDomain(self, domain):
        buffer = self.head
        while buffer.right is not None and buffer.right.domain != domain:
            buffer = buffer.right

        if buffer.right is None:
            return None
        else:
            buffer = buffer.right.down
            response = ""
            while buffer is not None:
                buffer2 = buffer
                while buffer2 is not None:
                    response += "\n\t" + str(buffer2.name)
                    buffer2 = buffer2.back

                buffer = buffer.down

            return response

    def searchLetter(self, letter):
        buffer = self.head
        while buffer.down is not None and buffer.down.name[0] != letter[0]:
            buffer = buffer.down

        if buffer.down is None:
            return None
        else:
            buffer = buffer.down.right
            response = ""
            while buffer is not None:
                buffer2 = buffer
                while buffer2 is not None:
                    response += "\n\t" + str(buffer2)
                    buffer2 = buffer2.back

                buffer = buffer.right

            return response

    def delete(self, domain, name):
        bX = self.right(self.head, domain, name, 0)
        if bX is None:
            return None

        bY = self.down(self.head, domain, name, 0)
        if bY is None:
            return None

        bX = self.down(bX.right, domain, name, 0)
        if bX is None:
            return None

        bY = self.right(bY.down, domain, name, 0)
        if bY is None:
            return None

        if bX.down.name == name and bY.right.domain == domain:
            result = bX.down
            if bX.down.back is None:
                bX.down = bX.down.down
                bY.right = bY.right.right
                return result

            bX.down = bX.down.back
            bX.down.down = result.down
            bX.down.right = result.right
            bY.right = bX.down
            self.validateHeaders(self.head)
            return result
        else:
            bX = bX.down
            while bX.back is not None and bX.back.name != name:
                bX = bX.back

            if bX.back is None:
                return None
            else:
                result = bX.back
                bX.back = bX.back.back
                result.back = None
                return result

    @staticmethod
    def right(node, domain, name, mode=1):
        if mode == 1:
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
        else:
            if node.domain > domain and node.domain != "ENC":
                return None

            buffer = node
            while buffer.right is not None and buffer.right.domain < domain:
                buffer = buffer.right

            if buffer.right is None or buffer.right.domain > domain:
                return None

            return buffer

    @staticmethod
    def down(node, domain, name, mode=1):
        if mode == 1:
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
        else:
            if node.name[0] > name[0] and node.name != "ENC":
                return None

            buffer = node
            while buffer.down is not None and buffer.down.name[0] < name[0]:
                buffer = buffer.down

            if buffer.down is None or buffer.down.name[0] > name[0]:
                return None

            return buffer

    @staticmethod
    def back(node, domain, name):
        if node.domain == domain and node.name == name:
            return None
        buffer = node

        while buffer.back is not None:
            if buffer.back.name == name:
                return None
            buffer = buffer.back

        buffer.back = MatrixNode(domain, name)
        return buffer.back

    @staticmethod
    def validateHeaders(node):
        buffer = node
        while buffer.right is not None:
            if buffer.right.down is None:
                buffer.right = buffer.right.right
            buffer = buffer.right

        buffer = node
        while buffer.down is not None:
            if buffer.down.right is None:
                buffer.down = buffer.down.down

            buffer = buffer.down

    def reportMatrix(self):
        buffer = self.head
        x = 0
        y = 0
        report = open('MatrixReport.dot', 'w+')
        report.write(
            "digraph SparseMatrix{\n\t")
        while buffer is not None:
            buffer2 = buffer
            x += 1
            while buffer2 is not None:
                y += 1
                if buffer2.right is not None:
                    report.write("\n\t\"" + str(buffer2) + "\"->\"" + str(buffer2.right) + "\"")

                if buffer2.down is not None:
                    report.write("\n\t\"" + str(buffer2) + "\"->\"" + str(buffer2.down) + "\"")

                report.write("\n\t\"" + str(buffer2) + "\"[label=\"" + str(buffer2) + "\" shape=\"square\" ]")

                buffer2 = buffer2.down

            buffer = buffer.right

        report.write("}")
        report.close()
        gen = open('gen.sh', 'w+')
        gen.write("dot MatrixReport.dot -Tjpg -o Matrix.jpg\n")
        gen.write("xdg-open Matrix.jpg\n")
        gen.close()
        subprocess.call(['./gen.sh'], shell=True)

    def report(self, domain, name):
        bX = self.right(self.head, domain, name, 0)
        bY = self.down(self.head, domain, name, 0)
        bX = self.down(bX.right, domain, name, 0)
        bY = self.right(bY.down, domain, name, 0)
        if bX.down.name == name and bY.right.domain == domain:
            buffer = bX.down
            i = 0
            report = open('MatrixNodeReport.dot', 'w+')
            report.write("digraph MatrixNode{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
            while buffer.back is not None:
                report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.back) + "\"]\n")
                report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
                buffer = buffer.back
                i += 1

            report.write("}")
            report.close()
            gen = open('gen.sh', 'w+')
            gen.write("dot MatrixNodeReport.dot -Tjpg -o MatrixNode.jpg\n")
            gen.write("xdg-open MatrixNode.jpg\n")
            gen.close()
            subprocess.call(['./gen.sh'], shell=True)
        else:
            bX = bX.down
            while bX.back is not None and bX.back.name != name:
                bX = bX.back

            if bX.back is None:
                return None
            else:
                buffer = bX.back
                i = 0
                report = open('MatrixNodeReport.dot', 'w+')
                report.write("digraph MatrixNode{\n\t" + str(i) + "[label=\"" + str(buffer) + "\"]\n")
                while buffer.back is not None:
                    report.write("\t" + str(i + 1) + "[label=\"" + str(buffer.back) + "\"]\n")
                    report.write("\t" + str(i) + "->" + str(i + 1) + "\n")
                    buffer = buffer.back
                    i += 1

                report.write("}")
                report.close()
                gen = open('gen.sh', 'w+')
                gen.write("dot MatrixNodeReport.dot -Tjpg -o MatrixNode.jpg\n")
                gen.write("xdg-open MatrixNodeReport.jpg\n")
                gen.close()
                subprocess.call(['./gen.sh'], shell=True)
                return

