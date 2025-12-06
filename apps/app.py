from flask import Flask
from waitress import server

app = Flask(__name__)

# route()デコレータ
@app.route("/")
def index():
    return "-hello-"

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)