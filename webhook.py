import json
import os

from flask import Flask
from flask import request
from flask import make_response

# flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
	req = re