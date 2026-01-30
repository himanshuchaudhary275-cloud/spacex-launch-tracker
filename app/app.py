from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    # SpaceX v5 API to get the nearest upcoming launch
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

    response = requests.post(url, json=payload)
    data = response.json()["docs"][0]

    launch_name = data.get("name", "N/A")
    launch_date = data.get("date_utc", "N/A")

    return render_template(
        "index.html",
        name=launch_name,
        date=launch_date
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
