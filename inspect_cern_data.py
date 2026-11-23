import pandas as pd

# Load real CERN collision data
df = pd.read_csv("Dimuon_DoubleMu.csv")

# Display basic information
print("CERN CMS COLLISION DATA")
print("------------------------")

# Display dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# Display first five records
print("\nFirst Five Events:")
print(df.head())

# Display dataset information
print("\nDataset Information:")
df.info()



# DATA QUALITY ANALYSIS

print("\nDATA QUALITY ANALYSIS")
print("---------------------")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:")
print(df.duplicated().sum())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())