from itertools import tee
from logging import exception
import requests
from datetime import datetime
import socket
import random
import flask
from flask import jsonify, request
app = flask.Flask(__name__)
 
def bestemmia(a):
    print(a)
    #convert a to literal
    a = a.replace("\\", "")
    a = a.replace("\"", "")
    a = a.replace("\'", "")
    a = a.replace("\n", "")
    a = a.replace("\r", "")
    a = a.replace("\t", "")
    a = a.replace("\b", "")
    a = a.replace("\f", "")
    a = a.replace("\v", "")
    a = a.replace("\0", "")
    a = a.replace("\x0b", "")
    a = a.replace("\x0c", "")
    a = a.replace("\x1b", "")
    a = a.replace("\x1c", "")
    a = a.replace("\x1d", "")
    a = a.replace("\x1e", "")
    a = a.replace("\x1f", "")
    a = a.replace("\x7f", "")
    a = a.replace("\x80", "")
    insulti = ["mannaggia", "bestia", "inutile", "porco/a", "maiale", "canaccio", "cane"]
    today = datetime.today().strftime('%Y-%m-%d')
    if a != "":
        #check if a is a valid date
        try:
            datetime.strptime(a, '%Y-%m-%d')
        except ValueError:
            return("questa data è vera quanto è vero il porco di dio!")
    url = "https://www.santodelgiorno.it/santi.json?data="

    payload = dict(key1='nome', key2='data')
    print(requests.post(url + today, data=payload))
    res = requests.post(url + today, data=payload)
    print(res.json)
    print(res.json()[0]['nome'])
    mannaggia =  insulti[random.randint(0, len(insulti)-1)] + " " + res.json()[0]['nome'] + "\n" 
    mannaggia.replace("", "\\")
    return mannaggia



@app.route('/api/bestemmia', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'date' in request.args:
        date = str(request.args['date'])
        print("ID ==" + str(date))
        return bestemmia(str(date))
    else:
        a = ""
        return bestemmia(a)


app.run()
'''
def main():
    a = ""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 8084))
    #define web api /api/bestemmia that takes an argument id 
    #and returns a json object with the bestemmia for that day
    #if id is not specified, it returns the bestemmia for today
    #if id is specified, it returns the bestemmia for that day

    while True:
        s.listen(1)
        conn, addr = s.accept()
        try:
            data = conn.recv(1024)
        except OSError:
            conn.close
            break
        if not data:
            break
        a = data.decode()
        print(a)
        conn.send(bestemmia(a).encode())
        conn.close()
if __name__ == "__main__":
    main()
'''
