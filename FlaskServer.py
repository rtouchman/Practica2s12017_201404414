from flask import Flask, request, Response
from Structures import SimpleList, Queue, Stack, SparseMatrix

app = Flask("EDD_Practica2")

list = SimpleList()
queue = Queue()
stack = Stack()
matrix = SparseMatrix()


@app.route('/List/add', methods=['POST'])
def add():
    data = request.form['data']
    list.append(str(data))
    return "Se ha agregado " + str(data) + " exitosamente"


@app.route('/List/search', methods=['POST'])
def search():
    data = request.form['data']
    index = list.search(data)
    if index is None:
        return "[EDD-ERR]No se encontró el dato..."
    else:
        return "El dato se encuentra en el índice " + str(index)


@app.route('/List/remove', methods=['POST'])
def remove():
    index = request.form['index']
    list.remove(index)
    return "Se ha eliminado el dato en la posición " + str(index) + " exitosamente"


@app.route('/List/report', methods=['GET'])
def reportList():
    list.report()
    return "Generando reporte de la lista simple"


@app.route('/Queue/enqueue', methods=['POST'])
def enqueue():
    data = request.form['data']
    queue.enqueue(data)
    return "Se ha encolado " + str(data) + " exitosamente"


@app.route('/Queue/dequeue', methods=['GET'])
def dequeue():
    data = queue.dequeue()
    if data is None:
        return "[EDD-ERR]La cola está vacía..."
    else:
        return "Se ha esencolado " + str(data) + " exitosamente"


@app.route('/Queue/report', methods=['GET'])
def reportQueue():
    queue.report()
    return "Generando reporte de la cola"


@app.route('/Stack/push', methods=['POST'])
def push():
    data = request.form['data']
    stack.push(data)
    return "Se ha apilado " + str(data) + " exitosamente"


@app.route('/Stack/pop', methods=['GET'])
def pop():
    data = stack.pop()
    if data is None:
        return "[EDD-ERR]La fila está vacía..."
    else:
        return str(data) + " ha sido desapilado exitosamente"


@app.route('/Stack/report', methods=['GET'])
def reportStack():
    stack.report()
    return "Generando reporte de la pila"


@app.route('/Matrix/insert', methods=['POST'])
def insert():
    domain = request.form['domain']
    name = request.form['name']
    result = matrix.insert(domain, name)
    if result is None:
        return "[EDD-ERR]No se pudo insertar el nodo, seguramente ya existía en la matriz..."
    else:
        return "El nodo " + str(result) + " se ha insertado correctamente"


@app.route('/Matrix/search/domain', methods=['POST'])
def searchDomain():
    domain = request.form['domain']
    response = matrix.searchDomain(domain)
    return "En el dominio " + str(domain) + " se han encontrado los siguientes datos:" + str(response)


@app.route('/Matrix/search/letter', methods=['POST'])
def searchLetter():
    letter = request.form['letter']
    response = matrix.searchDomain(letter[0])
    return "Se han encontrado los siguientes datos con la inicial " + str(letter) + ":" + str(response)


@app.route('/Matrix/delete', methods=['POST'])
def delete():
    domain = request.form['domain']
    name = request.form['name']
    result = matrix.delete(domain, name)
    if result is None:
        return "[EDD-ERR]No se encontró el dato en la matriz..."
    else:
        return "Se ha eliminado " + str(result) + "exitosamente"


@app.route('/Matrix/report/headers', methods=['GET'])
def reportMatrix():
    matrix.reportMatrix()
    return "Generando reporte de los nodos en la primera cara de la matriz"


@app.route('/Matrix/report/node', methods=['POST'])
def report():
    domain = request.form['domain']
    name = request.form['name']
    result = matrix.report(domain, name)
    if result is None:
        return "[EDD-ERR]No se encontró el dato en la matriz"
    else:
        return "Generando el grafico del nodo " + str(result)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
