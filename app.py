from flask import Flask, jsonify, request
import db_control
from db import create_tables

app = Flask(__name__)


@app.route('/freshers', methods=['GET'])
def get_details():
    details = db_control.insert_details()
    return jsonify(details)


if __name__ == '__main__':
    create_tables()
    app.run()
