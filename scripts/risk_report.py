# Risk Summary & Compliance Advisory Simulation

import pandas as pd

# File paths
datasets_file = "../risk_assessment.csv"
users_file = "../users.csv"
rules_file = "../access_rules.csv"

# --- Load CSV files ---
df_datasets = pd.read_csv(datasets_file)
df_users = pd.read_csv(users_file)
df_rules = pd.read_csv(rules_file)

# --- Prepare dictionaries ---
datasets = {row['Asset']: row['Risk Level'].lower() for _, row in df_datasets.iterrows()}
users = {row['Username']: row['Role'].lower() for _, row in df_users.iterrows()}
access_rules = {row['Role'].lower(): row['Max Risk Level'].lower() for _, row in df_rules.iterrows()}

# Risk hierarchy
risk_order = {"low": 1, "medium": 2, "high": 3}

# --- Generate report ---
report = []

for dataset, risk in datasets.items():
    # Identify roles that can access this dataset
    roles_with_access = [role for role, max_risk in access_rules.items()
                         if risk_order[risk] <= risk_order[max_risk]]
    # Identify users with access
    users_with_access = [user for user, role in users.items() if role in roles_with_access]

    # Advisory notes
    note = ""
    if risk == "high" and "guest" in roles_with_access:
        note = "High-risk dataset accessible by low-permission role! Consider restricting access."
    elif risk == "high" and len(users_with_access) > 5:
        note = "High-risk dataset accessible by many users! Review access rights."
    elif risk == "medium" and "guest" in roles_with_access:
        note = "Medium-risk dataset accessible by guest users. Consider restricting."

    report.append({
        "Dataset": dataset,
        "Risk Level": risk,
        "Roles with Access": ", ".join(roles_with_access),
        "Users with Access": ", ".join(users_with_access),
        "Advisory Note": note
    })

# --- Convert to DataFrame and print ---
df_report = pd.DataFrame(report)
print("\n=== Risk & Access Advisory Report ===\n")
print(df_report.to_string(index=False))

# Optional: save report to CSV
df_report.to_csv("risk_advisory_report.csv", index=False)
print("\nReport saved as 'risk_advisory_report.csv'")
