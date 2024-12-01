from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Task data
tasks = []

@app.route('/')
def index():
    # Calculate the average completion percentage
    if len(tasks) == 0:  # Avoid division by zero
        avg_completion = 0
    else:
        avg_completion = sum(task['completion_percent'] for task in tasks) / len(tasks)
    return render_template('index.html', tasks=tasks, avg_completion=avg_completion)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task_name = request.form['task_name']
        stakeholder = request.form['stakeholder']
        responsible = request.form['responsible']
        due_date = request.form['due_date']
        status = request.form['status']
        completion_percent = int(request.form['completion_percent'])

        tasks.append({
            'task_name': task_name,
            'stakeholder': stakeholder,
            'responsible': responsible,
            'due_date': due_date,
            'status': status,
            'completion_percent': completion_percent
        })
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if tasks and 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
