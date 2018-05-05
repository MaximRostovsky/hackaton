
# coding: utf-8

# In[19]:


from flask import Flask;
from flask import render_template;
app = Flask(__name__)


# In[20]:


@app.route("/")
def startServer():
    return render_template("Page.html");

# На анализ
@app.route("/json", methods = ['POST'])
def goDeeper(inJSON):
    return;


# In[17]:




