from flask import Flask, request, render_template
from utils import checklogin

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("loginpage.html")

@app.route("/authenticate/", methods = ['POST'])
def authenticate():
    return render_template("result.html", result = checklogin.usermsg(request.form["username"], request.form["password"]))

if __name__ == '__main__':
    app.debug = True
    app.run()
