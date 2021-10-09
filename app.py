from flask import Flask
import os
import socket
from multiprocessing import Value

app = Flask(__name__)

counter = Value('i', 0)

@app.route("/")
def counterWithoutIncrement():
    html = "<h3>" + str(counter.value) + "</h3>" 
    return html
	
@app.route("/stat")
def counterWithIncrement():

    html = "<h3>" + str(counter.value) + "</h3>" 
    counter.value += 1
    return html

@app.route("/about")
def hello():  
    html = "<h3>Hello, Adilya!</h3>" 
    return html
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
