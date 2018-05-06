
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
    pathToSave = 'C:\Hackaton\image1.jpeg'
    file.save(pathToSave)

    result = analyze(content, pathToSave);
    return jsonify(result)

# Анализ фото и данных для расчета скоринга
def analyze(content, filePath):
    pass



