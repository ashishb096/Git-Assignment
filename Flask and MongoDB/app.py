from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page!"

@app.route('/api/<name>')
def name(name):

    length = len(name)
    if length > 5:
        result = 'Name is to loong!: '+ name
        return result
    else :
        result = 'nice name: ' + name
        return result
    return "Welcome to the second page"


if __name__ == '__main__':
    app.run(debug=True)
