"""import pandas as pd

# Simulated particle collision data(step1)
data = {
    "event_id": [1, 2, 3, 4, 5],
    "energy": [120, 150, 130, 900, 140],
    "momentum": [45, 50, 48, 300, 47],
    "particle_count": [4, 5, 4, 20, 5]
}

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Calculate average energy(step2)
average_energy = df["energy"].mean()

# Calculate standard deviation
std_energy = df["energy"].std()

# Set an anomaly threshold
threshold = average_energy + (2 * std_energy)

# Identify unusual events
anomalies = df[df["energy"] > threshold]

print("\nAverage Energy:", average_energy)
print("Anomaly Threshold:", threshold)

print("\nUnusual Events:")
print(anomalies)

# Calculate median energy(step3)
median_energy = df["energy"].median()

# Calculate absolute deviations
deviations = abs(df["energy"] - median_energy)

# Calculate MAD
mad = deviations.median()

# Set anomaly threshold
threshold = median_energy + (3 * mad)

# Identify unusual events
anomalies = df[df["energy"] > threshold]

print("\nMedian Energy:", median_energy)
print("MAD:", mad)
print("New Threshold:", threshold)

print("\nDetected Anomalies:")
print(anomalies)"""



import matplotlib.pyplot as plt
import pandas as pd

# Simulated particle collision data
data = {
    "event_id": [1, 2, 3, 4, 5],
    "energy": [120, 150, 130, 900, 140],
    "momentum": [45, 50, 48, 300, 47],
    "particle_count": [4, 5, 4, 20, 5]
}

df = pd.DataFrame(data)

print("PARTICLE COLLISION DATA")
print(df)

# Median Absolute Deviation (MAD)
median_energy = df["energy"].median()

deviations = abs(df["energy"] - median_energy)

mad = deviations.median()

threshold = median_energy + (3 * mad)

anomalies = df[df["energy"] > threshold]

print("\nMEDIAN ENERGY:", median_energy)
print("MAD:", mad)
print("ANOMALY THRESHOLD:", threshold)

print("\nDETECTED ANOMALIES:")
print(anomalies)


# Separate normal events and anomalies
normal = df[df["energy"] <= threshold]

# Create scatter plot
plt.scatter(
    normal["event_id"],
    normal["energy"],
    label="Normal Events"
)

plt.scatter(
    anomalies["event_id"],
    anomalies["energy"],
    label="Anomalies",
    marker="x",
    s=150
)

# Add graph details
plt.title("Particle Collision Energy Analysis")
plt.xlabel("Event ID")
plt.ylabel("Energy")
plt.axhline(
    y=threshold,
    linestyle="--",
    label="Anomaly Threshold"
)

plt.legend()
plt.grid(True)

plt.show()


