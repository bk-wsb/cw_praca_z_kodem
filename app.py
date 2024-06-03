from flask import Flask

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/')
@app.route('/index')
def greeting():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
