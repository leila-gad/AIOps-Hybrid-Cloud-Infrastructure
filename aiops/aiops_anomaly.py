import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv("cpu_dataset.csv")

# Prepare data for ML
X = dataset[["cpu"]]

# Create Isolation Forest
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

# Detect anomalies
dataset["prediction"] = model.fit_predict(X)

# Convert prediction to labels
dataset["anomaly"] = dataset["prediction"].map({
    1: "Normal",
    -1: "Anomaly"
})

# Display detected anomalies
anomalies = dataset[dataset["anomaly"] == "Anomaly"]

print("\nDetected anomalies:")
print(anomalies[["timestamp", "cpu"]])

# Save results
dataset.to_csv("cpu_anomaly_results.csv", index=False)

# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(12, 6))

# Plot CPU usage
plt.plot(
    dataset["timestamp"],
    dataset["cpu"],
    label="CPU Usage"
)

# Plot anomalies
plt.scatter(
    anomalies["timestamp"],
    anomalies["cpu"],
    label="Detected Anomaly"
)

plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps - CPU Anomaly Detection")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.savefig("cpu_anomalies.png")

plt.show()

print("\nGraph saved as cpu_anomalies.png")