# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello() function.
def hello():
    return 'Hello from Flask in Docker!'

# This block creates a file inside the shared 'logs' volume to demonstrate
# that data written inside the container is also accessible on the host machine
# It's used to verify that the volume mapping (./logs:/app/logs) works as expected
with open("logs/test.txt", "w") as f:
    f.write("This file was written from inside the container.")

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(host="0.0.0.0")
