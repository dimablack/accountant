from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, world 2"


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5555))
    app.run(debug=True, host='0.0.0.0', port=port)
