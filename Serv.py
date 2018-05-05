
# coding: utf-8

# In[14]:


from flask import Flask;
app = Flask(__name__)


# In[15]:


@app.route("/")
def startServer():
    return "Hello";

# На анализ
def goDeeper(inJSON):
    return;

