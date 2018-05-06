
# coding: utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
app = Flask(__name__)


@app.route("/")
def startServer():
    return render_template("Page.html")

# Разбор сообщения с фронта и передача на анализ
@app.route("/json", methods = ['POST'])
def goDeeper():
    content = request.form
    print(content)
    file = request.files['Photo']
    print(file)
    result = analyze(content, file);
    return jsonify(result)

def analyze():
    pass



