from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Load schemes
with open("schemes.json") as f:
    schemes = json.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    matched_schemes = []
    if request.method == "POST":
        age = int(request.form["age"])
        income = int(request.form["income"])
        gender = request.form["gender"]
        occupation = request.form["occupation"]

        for scheme in schemes:
            if (
                age >= scheme["min_age"]
                and income <= scheme["max_income"]
                and (scheme["gender"] == "Any" or scheme["gender"] == gender)
                and (scheme["occupation"] == "Any" or scheme["occupation"] == occupation)
            ):
                matched_schemes.append(scheme)

    return render_template("index.html", schemes=matched_schemes)

if __name__ == "__main__":
    app.run(debug=True)
