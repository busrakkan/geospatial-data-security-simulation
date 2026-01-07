# Simple role-based access simulation for GIS datasets

users = {
    "alice": "admin",
    "bob": "analyst",
    "charlie": "guest"
}

datasets = ["survey_data.csv", "drone_images.csv", "client_locations.csv"]

def access_file(user, dataset):
    role = users.get(user)
    if not role:
        print(f"User {user} not found")
        return
    if role == "admin":
        print(f"{user} (Admin) can access {dataset}")
    elif role == "analyst":
        if dataset in ["survey_data.csv", "client_locations.csv"]:
            print(f"{user} (Analyst) can access {dataset}")
        else:
            print(f"{user} (Analyst) cannot access {dataset}")
    else:
        print(f"{user} (Guest) cannot access {dataset}")

# Simulate access attempts
for user in users:
    for dataset in datasets:
        access_file(user, dataset)
