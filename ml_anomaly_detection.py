"""import pandas as pd
from sklearn.ensemble import IsolationForest

# Simulated particle collision data
data = {
    "event_id": [1, 2, 3, 4, 5],
    "energy": [120, 150, 130, 900, 140],
    "momentum": [45, 50, 48, 300, 47],
    "particle_count": [4, 5, 4, 20, 5]
}

df = pd.DataFrame(data)

# Select features for machine learning
features = df[["energy", "momentum", "particle_count"]]

# Create the Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.2,
    random_state=42
)

# Train the model and make predictions
df["prediction"] = model.fit_predict(features)

# Label the results
df["status"] = df["prediction"].map({
    1: "Normal",
    -1: "Anomaly"
})

# Statistical anomaly detection using MAD

median_energy = df["energy"].median()

deviations = abs(df["energy"] - median_energy)

mad = deviations.median()

mad_threshold = median_energy + (3 * mad)

# Identify anomalies using MAD
df["MAD_Result"] = df["energy"].apply(
    lambda x: "Anomaly" if x > mad_threshold else "Normal"
)

# Compare both methods
df["Methods_Agree"] = (
    df["MAD_Result"] == df["status"]
)

print("\nMETHOD COMPARISON")
print(df[[
    "event_id",
    "MAD_Result",
    "status",
    "Methods_Agree"
]])

print("\nMAD Threshold:", mad_threshold)

print(
    "\nNumber of agreements:",
    df["Methods_Agree"].sum()
)

# Display results
print("\nMACHINE LEARNING RESULTS")
print(df)

# Display detected anomalies
print("\nDETECTED ANOMALIES")
print(df[df["prediction"] == -1])





import matplotlib.pyplot as plt

# Separate normal events and anomalies
normal_events = df[df["prediction"] == 1]
anomaly_events = df[df["prediction"] == -1]

# Plot normal events
plt.scatter(
    normal_events["event_id"],
    normal_events["energy"],
    label="Normal Events",
    marker="o",
    s=100
)

# Plot anomalies
plt.scatter(
    anomaly_events["event_id"],
    anomaly_events["energy"],
    label="Anomalies",
    marker="X",
    s=180
)

# Add graph information
plt.title("Machine Learning - Particle Collision Anomaly Detection")
plt.xlabel("Event ID")
plt.ylabel("Energy")

plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()"""



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Load CERN dataset
df = pd.read_csv("Dimuon_DoubleMu.csv")

# Select particle measurements
features = ["E1", "px1", "py1", "pz1",
            "E2", "px2", "py2", "pz2"]

X = df[features].dropna()

# Build Isolation Forest model
model = IsolationForest(
    contamination=0.02,
    random_state=42
)

# Detect anomalies
predictions = model.fit_predict(X)

# Add results
X = X.copy()
X["Anomaly"] = predictions

# Count results
normal = (predictions == 1).sum()
anomalies = (predictions == -1).sum()

print("CERN ANOMALY DETECTION")
print("----------------------")
print("Normal events:", normal)
print("Anomalous events:", anomalies)
print("Total events:", len(X))

# Visualize results
plt.figure(figsize=(9, 5))

plt.scatter(
    X["E1"],
    X["E2"],
    c=X["Anomaly"],
    cmap="coolwarm",
    s=5
)

plt.xlabel("Particle 1 Energy (GeV)")
plt.ylabel("Particle 2 Energy (GeV)")
plt.title("CERN CMS - Machine Learning Anomaly Detection")
plt.colorbar(label="Normal / Anomaly")
plt.show()




# Extract anomalous events
anomalies = X[X["Anomaly"] == -1]

# Display first 10 anomalies
print("\nFIRST 10 ANOMALOUS EVENTS")
print(anomalies.head(10))

# Statistical summary
print("\nANOMALY STATISTICS")
print(anomalies.describe())

# Save anomalies
anomalies.to_csv("cern_anomalous_events.csv", index=False)

print("\nAnomalies saved successfully!")




import matplotlib.pyplot as plt

# Separate normal and anomalous events
normal_events = X[X["Anomaly"] == 1]
anomalous_events = X[X["Anomaly"] == -1]

# Create comparison plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Compare Particle 1 Energy
axes[0].hist(
    normal_events["E1"],
    bins=50,
    alpha=0.6,
    density=True,
    label="Normal"
)

axes[0].hist(
    anomalous_events["E1"],
    bins=50,
    alpha=0.6,
    density=True,
    label="Anomalous"
)

axes[0].set_title("Particle 1 Energy Comparison")
axes[0].set_xlabel("Energy (GeV)")
axes[0].set_ylabel("Density")
axes[0].legend()

# Compare Particle 2 Energy
axes[1].hist(
    normal_events["E2"],
    bins=50,
    alpha=0.6,
    density=True,
    label="Normal"
)

axes[1].hist(
    anomalous_events["E2"],
    bins=50,
    alpha=0.6,
    density=True,
    label="Anomalous"
)

axes[1].set_title("Particle 2 Energy Comparison")
axes[1].set_xlabel("Energy (GeV)")
axes[1].set_ylabel("Density")
axes[1].legend()

plt.tight_layout()
plt.savefig("cern_anomaly_comparison.png", dpi=300)
plt.show()

print("Anomaly comparison completed!")







