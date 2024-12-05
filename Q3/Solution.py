from flask import Flask, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Submit Form</title>
</head>
<body>
    <h1>Submit Your Name</h1>
    <form action="/submit" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="person_name" name="person_name" required>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
"""


@app.route("/submit", methods=["GET","POST"])
def submit():
    if request.method == "POST":
        data = request.form["person_name"]
        return f"Wassgud, {data}"


@app.route("/", methods=["GET"])
def index():
    return HTML_TEMPLATE


if __name__ == "__main__":
    app.run(debug=True)
