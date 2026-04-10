from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! With this we are done with Docker Sessions'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


# Developer -->Build  --> Docker Image --> Push to Registry --> Pull from Registry --> Run Container