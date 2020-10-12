from flask import escape,jsonify

import finviz

def quote(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 't' in request_json:
        ticker = request_json['t']
    elif request_args and 't' in request_args:
        ticker = request_args['t']
    else:
        ticker = 'AMZN'

    return jsonify(finviz.get_stock(ticker))