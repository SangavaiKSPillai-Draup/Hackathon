from flask import Flask, Blueprint
from skill_read.read_api import skill_api

app = Flask(__name__)
app.register_blueprint(skill_api, url_prefix='/skill')

if __name__ == "__main__": 
    app.run(debug=True)