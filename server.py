from flask import Flask, render_template, redirect, request
from user import User

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    users = User.get_all()
    return render_template('/result.html', users=users)

@app.route('/user/<int:id>/show')
def user_show(id):
    data = {
        "id": id
    }
    return render_template("show.html", user=User.get_one(data))

@app.route('/user/<int:id>/edit')
def user_edit(id):
    data ={
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/user/<int:id>/update', methods=['post'])
def user_update(id):
    data = {
        **request.form,
        "id":id
    }
    User.update(data)
    return redirect('/dashboard')


@app.route('/create_user', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"],
    }
    User.save(data)
    return redirect('/dashboard')

@app.route('/user/<int:id>/delete')
def user_delete(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/dashboard')

if __name__ == "__main__":
    app.run(debug=True)