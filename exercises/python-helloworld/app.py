from flask import Flask
from flask import json
import logging

app = Flask(__name__)


def hello_logging(endpoint):
    logger = logging.getLogger('hello')
    logger.info(f'{endpoint} endpoint was reached')

@app.route("/")
def hello():
    return "Hello Mici!"

@app.route('/status')
def status():
    """
    - should return an HTTP 200 status code
    - should return a JSON response
    - should return a response similar to this example: result: OK - healthy
    - A log line should be recorded the timestamp and the requested endpoint 
      e.g. "{{TIMESTAMP}}, {{ ENDPOINT_NAME}} endpoint was reached"
    """
    hello_logging('status')

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
    hello_logging('metrics')

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
    # Stream logs to a file
    FORMAT = '%(asctime)s : %(message)s'
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=FORMAT)
    
    app.run(host='0.0.0.0')
