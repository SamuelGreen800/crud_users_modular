from flask import  redirect, render_template, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    
    return redirect('/users')


@app.route('/users')
def read():
    users = User.get_all()
    print(users)
    return render_template('read.html', all_users = users)



@app.route('/users/new')
def new():
    return render_template('create.html')

### ---------------------------------------------- problem_______________________________

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    data = {'id':id}
    User.save(request.form)
    return redirect('/users')
##---------------------------------------------------------------------------------------------
@app.route('/users/edit/<int:id>')
def edit(id):
    data = {'id':id}
    return render_template('edit.html', user=User.get_one(data))

@app.route('/users/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/users/view/<int:id>')
def view(id):
    data = {'id':id}
    return render_template('view.html', user=User.get_one(data))

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {'id':id}
    User.delete(data)
    return redirect('/users')