from flask import Flask, render_template, Blueprint
from repositories import book_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/index")
def books():
    books = book_repository.select_all()
    return render_template("/index.html", all_books = books)

# @tasks_blueprint.route("/tasks/new")
# def new_task():
#     users = user_repository.select_all()
#     return render_template("tasks/new.html", all_users = users)

# @tasks_blueprint.route("/tasks/addtask", methods = ['POST'])
# def add_task():
#     description = request.form['description'] #you need to import request from flask (see line 2)
#     user_id = request.form['user_id']
#     duration = request.form['duration']
#     completed = request.form['completed']
#     user_object = user_repository.select(user_id)
#     task_object = Task(description, user_object, duration, completed)
#     task_repository.save(task_object)
#     return redirect('/tasks')

# @tasks_blueprint.route('/tasks/<id>/delete', methods = ['POST'])
# def black_hole(id):
#     task_repository.delete(id)
#     return redirect('/tasks')

# @tasks_blueprint.route('/tasks/<id>', methods = ['GET'])
# def show_task_description(id):
#     task = task_repository.select(id)
#     return render_template('tasks/show.html', task = task)

# @tasks_blueprint.route('/tasks/<id>', methods =['POST'])
# def update_task(id):
#     description = request.form['description'] 
#     user_id = request.form['user_id']
#     duration = request.form['duration']
#     completed = request.form['completed']
#     user_object = user_repository.select(user_id)
#     task_to_update = Task(description, user_object, duration, completed, id)
#     task_repository.update(task_to_update)
#     return redirect('/tasks')

# @tasks_blueprint.route('/tasks/<id>/edit', methods = ['GET'])
# def edit_task(id):
#     task = task_repository.select(id)
#     users_list = user_repository.select_all()
#     return render_template('tasks/edit.html', task = task, all_users = users_list)



