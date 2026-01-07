# Geospatial Data Access Simulation
# Simulates role-based access control with risk warnings and logging

import os

# Users and their roles
users = {
    "alice": "admin",
    "bob": "analyst",
    "charlie": "guest"
}

# GIS datasets and risk levels
datasets = {
    "survey_data.csv": "medium",
    "drone_images.csv": "high",
    "client_locations.csv": "high",
    "terrain_maps.csv": "medium"
}

# Log file location
log_file = "access_log.txt"

# Ensure log file exists
if not os.path.exists(log_file):
    with open(log_file, "w") as f:
        f.write("Access Log\n")
        f.write("===========\n")

# Function to check access
def access_file(user, dataset):
    role = users.get(user)
    risk = datasets.get(dataset, "low")

    if not role:
        print(f"User {user} not found")
        return

    # Role-based access logic
    if role == "admin":
        allowed = True
    elif role == "analyst":
        allowed = dataset in ["survey_data.csv", "client_locations.csv", "terrain_maps.csv"]
    else:
        allowed = False

    # Print result
    if allowed:
        print(f"{user} ({role.title()}) can access {dataset}")
    else:
        print(f"{user} ({role.title()}) CANNOT access {dataset}")
        if risk == "high":
            print(f"WARNING: {dataset} is HIGH-RISK!")

    # Log access attempt
    with open(log_file, "a") as f:
        f.write(f"{user} ({role}) {'ACCESS' if allowed else 'DENIED'} {dataset}\n")

# Simulate all users accessing all datasets
for user in users:
    for dataset in datasets:
        access_file(user, dataset)
