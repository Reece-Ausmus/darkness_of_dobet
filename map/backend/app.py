from flask import Flask

app = Flask(__name__)

@app.route('/api/ping')
def ping():
    return {'message': 'Pong'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
