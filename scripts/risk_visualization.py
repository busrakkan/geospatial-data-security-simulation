# Risk & Access Visualization for Geospatial Data Security Simulation

import pandas as pd
import matplotlib.pyplot as plt

# File paths
datasets_file = "../risk_assessment.csv"
users_file = "../users.csv"
rules_file = "../access_rules.csv"

# --- Load CSVs ---
df_datasets = pd.read_csv(datasets_file)
df_users = pd.read_csv(users_file)
df_rules = pd.read_csv(rules_file)

# --- Prepare dictionaries ---
datasets = {row['Asset']: row['Risk Level'].lower() for _, row in df_datasets.iterrows()}
users = {row['Username']: row['Role'].lower() for _, row in df_users.iterrows()}
access_rules = {row['Role'].lower(): row['Max Risk Level'].lower() for _, row in df_rules.iterrows()}

# Risk hierarchy
risk_order = {"low": 1, "medium": 2, "high": 3}

# --- Count datasets per risk level ---
risk_counts = df_datasets['Risk Level'].value_counts()
print("\nDataset count per risk level:")
print(risk_counts)

# --- Count users with access to each risk level ---
risk_user_counts = {"low": 0, "medium": 0, "high": 0}

for dataset, risk in datasets.items():
    roles_with_access = [role for role, max_risk in access_rules.items()
                         if risk_order[risk] <= risk_order[max_risk]]
    users_with_access = [user for user, role in users.items() if role in roles_with_access]
    risk_user_counts[risk] += len(users_with_access)

print("\nNumber of users with access per dataset risk level:")
for risk, count in risk_user_counts.items():
    print(f"{risk.title()}: {count} users")

# --- Plot 1: Datasets per Risk Level ---
plt.figure(figsize=(8,5))
risk_counts.plot(kind='bar', color=['green', 'orange', 'red'])
plt.title("Number of GIS Datasets per Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Number of Datasets")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("datasets_per_risk_level.png")
plt.show()

# --- Plot 2: Users with Access per Risk Level ---
plt.figure(figsize=(8,5))
plt.bar(risk_user_counts.keys(), risk_user_counts.values(), color=['green', 'orange', 'red'])
plt.title("Number of Users with Access per Dataset Risk Level")
plt.xlabel("Risk Level")
plt.ylabel("Number of Users")
plt.tight_layout()
plt.savefig("users_per_risk_level.png")
plt.show()
