from xmlrpc.server import SimpleXMLRPCServer

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print("RPC Calculator Server running on port 8000")

server.register_function(add, "add")
server.register_function(sub, "sub")
server.register_function(mul, "mul")
server.register_function(div, "div")

server.serve_forever()
