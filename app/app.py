from flask import Flask, render_template
import requests

app = Flask(__name__)

SPACEX_API_URL = "https://api.spacexdata.com/v5/launches/next"

@app.route("/")
def index():
    try:
        response = requests.get(SPACEX_API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        launch_name = data.get("name", "N/A")
        launch_date = data.get("date_utc", "N/A")
        details = data.get("details", "No details available")

        return render_template(
            "index.html",
            name=launch_name,
            date=launch_date,
            details=details
        )

    except requests.exceptions.RequestException as e:
        # Safe fallback (NO 500 error)
        return render_template(
            "index.html",
            name="Unable to fetch launch data",
            date="N/A",
            details="SpaceX API may be temporarily unavailable."
        )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)