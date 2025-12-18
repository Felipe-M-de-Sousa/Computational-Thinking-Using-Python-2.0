from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Lista de tarefas (inicialmente vazia)
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/adicionar_tarefa', methods=['POST'])
def adicionar_tarefa():
    nova_tarefa = request.form.get('tarefa')
    if nova_tarefa:
        tasks.append(nova_tarefa)
    return redirect(url_for('index'))


@app.route('/tarefas')
def tarefas():
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)
