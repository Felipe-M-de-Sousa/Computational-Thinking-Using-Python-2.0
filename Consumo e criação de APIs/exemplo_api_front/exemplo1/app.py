from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return 'Hello!'


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID


@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo


@app.route('/flask')
def hello_flask():
    return 'Hello Flask'


@app.route('/python/')
def hello_python():
    return 'Hello Python'

@app.route("/status/")
def homepage():
    return jsonify({"status": "OK"})


@app.route("/todo/")
def todoList():
    return jsonify({"tarefa0": "Descricao tarefa 0",
                    "tarefa1": "Descricao tarefa 1",
                    "tarefa2": "Descricao tarefa 2",
                    "tarefa3": "Descricao tarefa 3",
                    "tarefa4": "Descricao tarefa 4",
                    "tarefa5": "Descricao tarefa 5",
                    "tarefa6": "Descricao tarefa 6"})


@app.route("/pagina1")
def pagina1():
    return render_template("pagina1.html")


if __name__ == "__main__":
    app.run()
