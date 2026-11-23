import pandas as pd
import matplotlib.pyplot as plt

# Load CERN data
df = pd.read_csv("Dimuon_DoubleMu.csv")

# Extract invariant mass
invariant_mass = df["M"]

# Display basic statistics
print("INVARIANT MASS ANALYSIS")
print("-----------------------")

print(invariant_mass.describe())

# Plot invariant mass distribution
plt.figure(figsize=(10, 6))

plt.hist(invariant_mass, bins=120)

plt.title("CERN CMS Dimuon Invariant Mass Distribution")
plt.xlabel("Invariant Mass (GeV)")
plt.ylabel("Number of Events")

plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()