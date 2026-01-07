# Fully data-driven Geospatial Data Access Simulation

import pandas as pd
import os

# File paths
datasets_file = "../risk_assessment.csv"
users_file = "../users.csv"
rules_file = "../access_rules.csv"
log_file = "access_log.txt"

# --- Read CSV files ---
try:
    df_datasets = pd.read_csv(datasets_file)
    df_users = pd.read_csv(users_file)
    df_rules = pd.read_csv(rules_file)
except FileNotFoundError as e:
    print(f"ERROR: {e}")
    exit()

# Convert datasets to dict: {dataset: risk_level}
datasets = {row['Asset']: row['Risk Level'].lower() for _, row in df_datasets.iterrows()}

# Convert users to dict: {username: role}
users = {row['Username']: row['Role'].lower() for _, row in df_users.iterrows()}

# Convert rules to dict: {role: max_risk_level}
access_rules = {row['Role'].lower(): row['Max Risk Level'].lower() for _, row in df_rules.iterrows()}

# Ensure log file exists
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("Access Log\n===========\n")

# Risk hierarchy for comparison
risk_order = {"low": 1, "medium": 2, "high": 3}

# --- Access check function ---
def access_file(user, dataset):
    role = users.get(user)
    dataset_risk = datasets.get(dataset, "low")
    max_allowed_risk = access_rules.get(role, "low")

    if not role:
        print(f"User {user} not found")
        return

    allowed = risk_order[dataset_risk] <= risk_order[max_allowed_risk]

    # Print output
    if allowed:
        print(f"{user} ({role.title()}) can access {dataset} [{dataset_risk}]")
    else:
        print(f"{user} ({role.title()}) CANNOT access {dataset} [{dataset_risk}]")
        if dataset_risk == "high":
            print(f"WARNING: {dataset} is HIGH-RISK!")

    # Log access attempt
    with open(log_file, "a") as f:
        f.write(f"{user} ({role}) {'ACCESS' if allowed else 'DENIED'} {dataset} [{dataset_risk}]\n")

# --- Simulate access ---
for user in users:
    for dataset in datasets:
        access_file(user, dataset)
