from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://api.spacexdata.com/v4/launches/next"
    data = requests.get(url).json()
    return render_template("index.html", launch=data)

if __name__ == "__main__":
    print("Starting Flask app...")
    app.run(host="0.0.0.0", port=5000, debug=True)

