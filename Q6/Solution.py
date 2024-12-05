from flask import Flask, jsonify
from dataclasses import dataclass


class User:
    name: str
    age: int

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


app = Flask(__name__)


@app.route("/data", methods=["GET"])
def get_data():
    user = User(name="Alice", age=30)
    return jsonify(user.__dict__)


if __name__ == "__main__":
    app.run(debug=True)
