import pandas as pd
import matplotlib.pyplot as plt

# Load CERN CMS dataset
df = pd.read_csv("Dimuon_DoubleMu.csv")

# Select invariant mass between 60 and 120 GeV
z_data = df[(df["M"] >= 60) & (df["M"] <= 120)]

# Plot the Z boson mass region
plt.figure(figsize=(10, 6))

plt.hist(z_data["M"], bins=60, edgecolor="black")

plt.axvline(91.2, linestyle="--",
            label="Expected Z boson mass (91.2 GeV)")

plt.title("CERN CMS - Z Boson Mass Analysis")
plt.xlabel("Invariant Mass (GeV)")
plt.ylabel("Number of Events")

plt.legend()
plt.grid(alpha=0.3)

plt.show()

# Display peak information
print("Z BOSON ANALYSIS")
print("----------------")
print("Events in mass region:", len(z_data))
print("Mean mass:", z_data["M"].mean())
print("Maximum mass:", z_data["M"].max())


counts, bins = __import__("numpy").histogram(
    z_data["M"], bins=60
)

peak_index = counts.argmax()

peak_mass = (bins[peak_index] + bins[peak_index + 1]) / 2

print("Estimated Z boson peak:", peak_mass, "GeV")
print("Reference Z boson mass: 91.2 GeV")


# Calculate percentage error

reference_mass = 91.2

percentage_error = (
    abs(peak_mass - reference_mass)
    / reference_mass
) * 100

print("\nACCURACY ANALYSIS")
print("-----------------")
print("Estimated mass:", peak_mass, "GeV")
print("Reference mass:", reference_mass, "GeV")
print("Percentage error:", round(percentage_error, 4), "%")