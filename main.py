from flask import *
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    data_set = {"slackUsername": 'Kariithi', "backend": True, "age": 25, "bio": 'Hello, my name is Kariithi!'}
    json_dump = json.dumps(data_set)

    return json_dump