from flask import Flask, render_template, request,session
from flask_session import Session
app = Flask(__name__)
app.config['SECRET_KEY'] = "some_random"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT']= False

Session(app)
notes = []
@app.route('/', methods=['GET',"POST"])
def index():
    if ('notes' not in session) or (session["notes"]==None):
        session['notes'] = []
    note=request.form.get("note")
    if session.get("notes"):
         session["notes"] = session["notes"].extend([note])
    else:
        session['notes'] = [note]
        print(session)
    return render_template("home.html", notes=session['notes'])

@app.route("/login", methods=["POST", "GET"])

def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
