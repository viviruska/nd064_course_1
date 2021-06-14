from flask import Flask
from flask import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Mici!"

@app.route('/status')
def status():
    """
    should return an HTTP 200 status code
    should return a JSON response
    should return a response similar to this example: result: OK - healthy
    """
    data = {
        "result": "OK - healthy"
    }

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/metrics')
def healthcheck():
    """
    should return an HTTP 200 status code
    should return a JSON response
    should return a response similar to this example: data: {UserCount: 140, UserCountActive: 23}
    """
    data = {
        "status": "success",
        "code": 0,
        "data": {
            "UserCount": 140,
            "UserCountActive": 23
        }
    }

    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
