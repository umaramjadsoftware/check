from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>kesy ho</p>"

@app.route("/umar")
def umar():
    return "<p>mera naam umar hy</p>"

app.run()