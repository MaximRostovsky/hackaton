
# coding: utf-8

# In[19]:


from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
app = Flask(__name__)


# In[20]:


@app.route("/")
def startServer():
    return render_template("Page.html")

# На анализ
@app.route("/json", methods = ['POST'])
def goDeeper():
    content = request.form
    print(content)
    file = request.files
    print(file)
    return jsonify(0)


# In[17]:




