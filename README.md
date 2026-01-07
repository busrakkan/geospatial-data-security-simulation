# **Geospatial Data Security Simulation**

## **Project Overview**  
*Geospatial Data Security Simulation* is a **simulated cybersecurity and IT governance project** for a fictional GIS company, **GeoMaps Consulting**. It demonstrates a **structured, data-driven approach** to identifying and mitigating risks in a small geospatial organization that manages sensitive spatial datasets, including **survey data, drone imagery, and client location information**.

This simulation reflects a **cybersecurity advisory mindset** combined with **GIS domain knowledge**, similar to work performed in **IT Security consulting, risk assessments, and ISO/IEC 27001 advisory** for small companies or public organizations.

---

## **Project Goals**

- Conduct a **cybersecurity risk assessment** for a small GIS organization  
- Identify **threats to IT assets** and assess **risk levels**  
- Map risks to **ISO/IEC 27001 control areas**  
- Draft short **policies** for **information security**, **access control**, and **incident management**  
- Demonstrate **technical simulation of access control** using Python  
- Produce **structured documentation and advisory-style reporting**  
- Provide **interactive visualization and user access simulation** through a **Streamlit web app**

---

## **Organization Overview**

**GeoMaps Consulting (Fictional GIS Company)**  

- **Employees / Roles:**  
  - **Admin:** Full access to all data and systems  
  - **Analyst:** Access to GIS datasets and reports only  
  - **Guest:** View-only access  

- **IT Assets:**  
  - GIS server (central storage of datasets)  
  - Workstations / laptops  
  - Cloud storage for sharing and backups  
  - Drones and GPS devices for data collection  

- **Data Types & Sensitivity:**  
  - Survey data (*medium sensitivity*)  
  - Client location data (*high sensitivity*)  
  - Proprietary mapping datasets (*high sensitivity*)  

---

## **Sample Risk Assessment Table**

| Asset         | Threat                      | Impact | Likelihood | Risk Level | Suggested Control                  |
|---------------|----------------------------|--------|------------|------------|-----------------------------------|
| GIS Server    | Unauthorized access / hacking | High   | Medium     | High       | MFA, role-based access, audit logs|
| Laptops       | Theft or loss               | Medium | Medium     | Medium     | Full-disk encryption, passwords   |
| Cloud Storage | Misconfigured permissions   | High   | Medium     | High       | Access review, audit, encryption  |
| Drone Data    | Data corruption / loss      | High   | Low        | Medium     | Backup strategy, encryption       |

---

## **ISO/IEC 27001 Gap Mapping (Sample)**

| Control Area          | Status      | Notes / Recommendations                  |
|-----------------------|------------|-----------------------------------------|
| Access Control         | Partial    | Implement MFA for server/cloud access   |
| Asset Management       | Missing    | Maintain asset inventory & classification |
| Backup & Recovery      | Missing    | Schedule regular backups of GIS data    |
| Incident Management    | Missing    | Document incident response procedure    |
| Data Protection        | Partial    | Encrypt sensitive datasets               |

---

## **Mini Policies (Included)**

- **Information Security Policy**  
  - Roles & responsibilities  
  - Confidentiality of client data  
  - General IT security measures  

- **Access Control Policy**  
  - Role-based access rules (Admin / Analyst / Guest)  
  - Password rules, MFA, session limits  

- **Incident Reporting Procedure**  
  - Steps for reporting lost devices, data breaches, or unauthorized access  
  - Responsible contacts  

---

## **Python Simulations**

### **1. Role-Based Access Simulation**
- **Script:** `scripts/access_control.py`  
- **Purpose:** Simulate **role-based access control** for GIS datasets using data-driven CSVs  
- **How it Works:**  
  - Users, roles, and datasets are **read from CSV files** (no hardcoding)  
  - Admin → full access; Analyst → limited access; Guest → view-only  
  - Access attempts are optionally logged in `access_log.txt`  

### **2. Risk & ISO Advisory Report**
- **Script:** `scripts/risk_report.py`  
- **Purpose:** Automatically generates a **structured advisory report** combining:  
  - Dataset risk levels  
  - User access rights  
  - ISO/IEC 27001 control recommendations  
- **Output:** `risk_advisory_report_with_iso.csv`  

### **3. Risk Visualization**
- **Script:** `scripts/risk_visualization.py`  
- **Purpose:** Generates **bar charts of datasets by risk level** and other visual insights  
- **Libraries:** `matplotlib`, `plotly`  

### **4. Interactive Web App**
- **Script:** `scripts/app.py`  
- **Framework:** [Streamlit](https://streamlit.io/)  
- **Features:** - User access simulation via **dropdown** - Interactive **risk level distribution charts** - ISO/IEC 27001 controls lookup per dataset  
  - Fully **data-driven from CSV files**, no hardcoding  
- **Run Command:** `streamlit run scripts/app.py`

---

## **Skills Demonstrated**

- **Cybersecurity risk assessment & IT governance**
- **ISO/IEC 27001 awareness & gap analysis**
- **Information security policy drafting**
- **Python scripting for role-based access control**
- **GIS domain knowledge** (datasets, servers, drones)
- **Data visualization & interactive reporting**
- **Documentation & advisory-style reporting**

---

## **Dependencies**

This project requires the following Python packages:

- pandas
- matplotlib
- plotly
- streamlit

---

## **Usage Instructions**

1. Ensure **all CSV files** (`risk_assessment.csv`, `users.csv`, `access_rules.csv`, `iso_controls.csv`) are present in the root project folder.
2. Navigate to the `scripts/` folder.
3. **Run Access Simulation:**

---

## **Note**

This project is **fully simulated**, requires no real organization or sensitive data, and demonstrates **entry-level cybersecurity and advisory skills in a GIS context**. All users, datasets, access rules, and ISO recommendations are **read dynamically from CSVs**, making it **flexible, scalable, and professional**.