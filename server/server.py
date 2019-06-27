from flask import Flask, jsonify

app = Flask(__name__)




@app.route('/hello')
def hello():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True, port=5000) #run app in debug mode on port 5000