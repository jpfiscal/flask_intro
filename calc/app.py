# Put your app in here.
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/<operation>')
def calc(operation):
    a = request.args["a"]
    b = request.args["b"]
    print(request.args)
    
    def add(a, b):
        """Add a and b."""
        return f"{float(a) + float(b)}"
    
    def sub(a, b):
        """Substract b from a."""
        return float(a) - float(b)

    def mult(a, b):
        """Multiply a and b."""
        return float(a) * float(b)

    def div(a, b):
        """Divide a by b."""
        return float(a) / float(b)

    if operation == "add":
        return f"<p>The result you're looking for is: {add(a,b)}</p>"
    elif operation == "sub":
        return f"<p>The result you're looking for is: {sub(a,b)}</p>"
    elif operation == "mult":
        return f"<p>The result you're looking for is: {mult(a,b)}</p>"
    elif operation == "div":
        return f"<p>The result you're looking for is: {div(a,b)}</p>"
    else:
        return f"Unrecognized operation: {operation}"
