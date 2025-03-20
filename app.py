from flask import flask,request,render_template
app = flask(__name__)
@app.route("/register", methods = ["GET", "post"])
def register();
    if request.method=="post":
        name = request.form["name"]
        email = request.form["password"]
        file return