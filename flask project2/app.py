from flask import Flask,render_template,request,flash

app=Flask(__name__)
app.secret_key="123"

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="POST":
        if request.form.get("success"):
            flash("Success Message","Success")

        if request.form.get("warning"):
            flash("Warning Message","Warning")

        if request.form.get("primary"):
            flash("Primary Message","Primary")

        if request.form.get("secondary"):
            flash("Secondary Message","Secondary")

        if request.form.get("info"):
            flash("Info Message Message","Info")

        if request.form.get("danger"):
            flash("Danger Message","Danger")

        if request.form.get("dark"):
            flash("Dark Message","Dark")

    return render_template("message.html")
if __name__=="__main__":
    app.run(debug=True)
