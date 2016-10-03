from flask import Markup
import hashlib
import csv

def hashify(password):
    h = hashlib.md5(password.encode())
    return(h.hexdigest())

def userreg(username, password):
    database = csv.reader(open("data/users.csv"))
    for user in database:
        if username == user[0]:
            return Markup("<div id =\"msg\"class=\"form\"><button>Hey...you seem familiar. try logging in bro</button></div>")
    with open('data/users.csv', 'a') as f:
        w = csv.writer(f)
        w.writerow([username, hashify(password)])
    return Markup("<div id =\"msg\"class=\"form\"><button>Welcome to the club</button></div>")

def userlog(username, password):
    database = csv.reader(open("data/users.csv"))
    for user in database:
        if username == user[0]:
            if hashify(password)==user[1] :
                return Markup("<div id =\"msg\"class=\"form\"><button>Hey there "+username+" </button></div>")
            return Markup("<div id = \"msg\" class=\"form\"><button>That is the incorrect password sir</button></div>")
    return Markup("<div id = \"msg\" class=\"form\"><button>That is a nonexistent username sir</button></div>")


