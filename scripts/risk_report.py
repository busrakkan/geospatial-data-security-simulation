import pandas as pd
import os

# CSV paths
datasets_file = "../risk_assessment.csv"
users_file = "../users.csv"
rules_file = "../access_rules.csv"
iso_file = "../iso_controls.csv"   # New CSV

# --- Load CSVs ---
df_datasets = pd.read_csv(datasets_file)
df_users = pd.read_csv(users_file)
df_rules = pd.read_csv(rules_file)
df_iso = pd.read_csv(iso_file)

# --- Prepare dictionaries ---
datasets = {row['Asset']: row['Risk Level'].lower() for _, row in df_datasets.iterrows()}
users = {row['Username']: row['Role'].lower() for _, row in df_users.iterrows()}
access_rules = {row['Role'].lower(): row['Max Risk Level'].lower() for _, row in df_rules.iterrows()}

risk_order = {"low": 1, "medium": 2, "high": 3}

# --- ISO Control Mapping Function ---
def get_iso_controls(dataset_name, risk_level):
    controls = []
    for _, row in df_iso.iterrows():
        if row['Dataset Type / Risk Level'] == 'all' or row['Dataset Type / Risk Level'] == risk_level:
            controls.append(f"{row['ISO Control Area']} ({row['Notes / Recommendations']})")
    return "; ".join(controls)

# --- Generate Advisory Report ---
report_rows = []

for dataset, risk in datasets.items():
    # Roles & users with access
    roles_with_access = [role for role, max_risk in access_rules.items()
                         if risk_order[risk] <= risk_order[max_risk]]
    users_with_access = [user for user, role in users.items() if role in roles_with_access]

    # ISO Controls for this dataset
    iso_controls = get_iso_controls(dataset, risk)

    report_rows.append({
        "Dataset": dataset,
        "Risk Level": risk,
        "Roles with Access": ", ".join(roles_with_access),
        "Users with Access": ", ".join(users_with_access),
        "ISO/IEC 27001 Controls": iso_controls
    })

df_report = pd.DataFrame(report_rows)

# --- Save CSV ---
df_report.to_csv("../risk_advisory_report_with_iso.csv", index=False)

# --- Print summary ---
print("\n=== Risk & ISO Advisory Report ===")
print(df_report.head(10))
