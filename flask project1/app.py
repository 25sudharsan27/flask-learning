from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")

def intro():
    return render_template("index.html")

@app.route("/Register",methods=["POST","GET"])

def Register():
    if request.method == "POST":
        name=request.form.get("name")
        section=request.form.get("section")
        city=request.form.get("city")
        age=request.form.get("age")
        return render_template("register.html",name=name,section=section,city=city,age=age)

if "__main__"==__name__:
    app.run(debug=True)
