from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.spacexdata.com/v5/launches/query"

    payload = {
        "query": {
            "upcoming": True
        },
        "options": {
            "sort": {
                "date_utc": "asc"
            },
            "limit": 1
        }
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()

        docs = response.json().get("docs", [])

        if not docs:
            launch_name = "No upcoming launches found"
            launch_date = "N/A"
        else:
            launch_name = docs[0].get("name", "N/A")
            launch_date = docs[0].get("date_utc", "N/A")

    except Exception as e:
        launch_name = "SpaceX API unavailable"
        launch_date = "Please try again later"

    return render_template(
        "index.html",
        name=launch_name,
        date=launch_date
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
