from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)
    completedesc =db.Column(db.String(200))
    
@app.route('/')
def index():
    alltasks = Todo.query.all()
    return render_template('index.html', alltasks=alltasks)

@app.route('/create', methods=['POST'])  
def create():
    todo = Todo(text=request.form['taskDescription'], complete=False, completedesc='false')
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<id>')
def update(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    todo.complete = True
    todo.completedesc = 'true'
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    todo = Todo.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
 