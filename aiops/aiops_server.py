from flask import Flask, Response
import requests
import pandas as pd
from sklearn.ensemble import IsolationForest
import time

app = Flask(__name__)

PROMETHEUS_URL = "http://127.0.0.1:9090"

QUERY = '100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'


def get_cpu_data():

    end = time.time()
    start = end - 3600

    response = requests.get(
        f"{PROMETHEUS_URL}/api/v1/query_range",
        params={
            "query": QUERY,
            "start": start,
            "end": end,
            "step": "60"
        }
    )

    response.raise_for_status()

    data = response.json()

    result = data["data"]["result"]

    if not result:
        raise Exception("No CPU data returned by Prometheus")

    values = result[0]["values"]

    dataset = pd.DataFrame(
        values,
        columns=["timestamp", "cpu"]
    )

    dataset["cpu"] = pd.to_numeric(dataset["cpu"])

    return dataset


def detect_anomaly():

    dataset = get_cpu_data()

    X = dataset[["cpu"]]

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    dataset["prediction"] = model.fit_predict(X)

    latest = dataset.iloc[-1]

    cpu = latest["cpu"]

    if latest["prediction"] == -1:
        anomaly = 1
    else:
        anomaly = 0

    return cpu, anomaly


@app.route("/metrics")
def metrics():

    try:

        cpu, anomaly = detect_anomaly()

        output = f"""
# HELP aiops_cpu_usage Current CPU usage analyzed by AIOps
# TYPE aiops_cpu_usage gauge
aiops_cpu_usage {cpu}

# HELP aiops_cpu_anomaly AIOps detected CPU anomaly
# TYPE aiops_cpu_anomaly gauge
aiops_cpu_anomaly {anomaly}
"""

        return Response(
            output,
            mimetype="text/plain"
        )

    except Exception as e:

        return Response(
            f"# AIOps error: {e}\n",
            mimetype="text/plain",
            status=500
        )


app.run(
    host="0.0.0.0",
    port=8000
)