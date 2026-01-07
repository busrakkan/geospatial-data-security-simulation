# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Geospatial Data Security Simulation", layout="wide")

st.title("🌐 Geospatial Data Security Simulation")

# --- Load CSVs ---
base_path = "../"  # adjust if your CSVs are in the parent folder
datasets_file = os.path.join(base_path, "risk_assessment.csv")
users_file = os.path.join(base_path, "users.csv")
rules_file = os.path.join(base_path, "access_rules.csv")
iso_file = os.path.join(base_path, "iso_controls.csv")

df_datasets = pd.read_csv(datasets_file)
df_users = pd.read_csv(users_file)
df_rules = pd.read_csv(rules_file)
df_iso = pd.read_csv(iso_file)

# --- Prepare dictionaries ---
datasets = {row['Asset']: row['Risk Level'].lower() for _, row in df_datasets.iterrows()}
users = {row['Username']: row['Role'].lower() for _, row in df_users.iterrows()}
access_rules = {row['Role'].lower(): row['Max Risk Level'].lower() for _, row in df_rules.iterrows()}
risk_order = {"low": 1, "medium": 2, "high": 3}

# --- Access Check Function ---
def can_access(user, dataset):
    role = users.get(user)
    risk = datasets.get(dataset, "low")
    if not role:
        return False
    max_risk = access_rules.get(role, "low")
    return risk_order[risk] <= risk_order[max_risk]

# --- Sidebar: User Access Simulation ---
st.sidebar.header("Access Simulation")
selected_user = st.sidebar.selectbox("Select User", list(users.keys()))

st.sidebar.write(f"Role: {users[selected_user].title()}")
access_results = {dataset: can_access(selected_user, dataset) for dataset in datasets}

# --- Display Access Table ---
st.subheader("User Access Simulation")
access_df = pd.DataFrame({
    "Dataset": list(access_results.keys()),
    "Risk Level": [datasets[d] for d in datasets],
    "Access Allowed": ["✅" if v else "❌" for v in access_results.values()]
})
st.dataframe(access_df)

# --- Risk Visualization ---
st.subheader("Risk Level Distribution")
risk_counts = df_datasets['Risk Level'].value_counts()
fig = px.bar(
    x=risk_counts.index,
    y=risk_counts.values,
    labels={'x': 'Risk Level', 'y': 'Number of Datasets'},
    color=risk_counts.index,
    color_discrete_map={'low':'green','medium':'orange','high':'red'}
)
st.plotly_chart(fig, use_container_width=True)

# --- ISO Controls Lookup ---
st.subheader("ISO/IEC 27001 Controls by Dataset")
def get_iso_controls(dataset_name, risk_level):
    controls = []
    for _, row in df_iso.iterrows():
        if row['Dataset Type / Risk Level'] == 'all' or row['Dataset Type / Risk Level'].lower() == risk_level:
            controls.append(f"{row['ISO Control Area']} ({row['Notes / Recommendations']})")
    return "; ".join(controls)

iso_df = pd.DataFrame({
    "Dataset": list(datasets.keys()),
    "Risk Level": list(datasets.values()),
    "ISO Controls": [get_iso_controls(d, datasets[d]) for d in datasets]
})
st.dataframe(iso_df)
