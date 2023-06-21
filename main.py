from flask import Flask, jsonify, request
import finviz
import requests

app = Flask(__name__)

@app.route("/quote")
def quote():
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    ticker = request.args.get('t')
    
    if not ticker:
        return jsonify({'error': 'Ticker not provided.'}), 400
    
    # request_json = request.get_json(silent=True)
    # request_args = request.args

    # if request_json and 't' in request_json:
    #     ticker = request_json['t']
    # elif request_args and 't' in request_args:
    #     ticker = request_args['t']
    # else:
    #     ticker = 'AMZN'
    try:
        return jsonify(finviz.get_stock(ticker))
    except requests.exceptions.HTTPError as err:
        return jsonify({'error': str(err)}), err.response.status_code