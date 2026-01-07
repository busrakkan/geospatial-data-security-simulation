# run_all.py
import subprocess
import sys

print("\n=== Running Geospatial Data Security Simulation ===\n")

python_exe = sys.executable  # This ensures the same Python (virtualenv) is used

# Step 1: Access Simulation
print("1️⃣ Running Access Simulation...")
try:
    subprocess.run([python_exe, "access_control.py"], check=True)
except subprocess.CalledProcessError:
    print("Error: access_control.py failed.")
print("\n")

# Step 2: Risk & ISO Advisory Report
print("2️⃣ Generating Risk & ISO Advisory Report...")
try:
    subprocess.run([python_exe, "risk_report.py"], check=True)
except subprocess.CalledProcessError:
    print("Error: risk_report.py failed.")
print("\n")

# Step 3: Risk Visualization
print("3️⃣ Generating Risk Visualization Charts...")
try:
    subprocess.run([python_exe, "risk_visualization.py"], check=True)
except subprocess.CalledProcessError:
    print("Error: risk_visualization.py failed.")
print("\n")

print("✅ All steps completed. Check CSV files, charts, and access log for details.")
