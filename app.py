from flask import request, jsonify
from flask import Flask
from marshmallow import ValidationError

from builder import build_query
from models import RequestSchema

app = Flask(__name__)


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    try:
        RequestSchema().load(data)
    except ValidationError as error:
        return jsonify(error.messages), 400

    first_result = build_query(
        cmd=data['cmd1'],
        value=data['value1'],
        file_name=data['file_name'],
        data=None,
    )
    second_result = build_query(
        cmd=data['cmd2'],
        value=data['value2'],
        file_name=data['file_name'],
        data=first_result,
    )

    return jsonify(second_result)


if __name__ == '__main__':
    app.run()
