# **Geospatial Data Security Simulation**

**Project Overview**  
*Geospatial Data Security Simulation* is a simulated cybersecurity and IT governance project for a fictional GIS company, **GeoMaps Consulting**. The project demonstrates a structured approach to identifying and mitigating risks in a small geospatial organization that manages sensitive spatial datasets, including survey data, drone imagery, and client location information.  

This simulation showcases a **cybersecurity advisory mindset** combined with **GIS domain knowledge**, reflecting the type of work performed in consulting and risk assessment for small companies or public organizations.  

---

## **Project Goals**
- Conduct a **cybersecurity risk assessment** for a small GIS organization  
- Identify **threats to IT assets** and assess risk levels  
- Map risks to **ISO/IEC 27001 control areas**  
- Draft **short policies** for information security, access control, and incident management  
- Demonstrate **technical simulation** of access control using Python  
- Produce **structured documentation** suitable for advisory reporting  

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
  - Survey data (medium sensitivity)  
  - Client location data (high sensitivity)  
  - Proprietary mapping datasets (high sensitivity)  

---

## **Risk Assessment Table (Sample)**

| Asset         | Threat                      | Impact | Likelihood | Risk Level | Suggested Control                  |
|---------------|----------------------------|--------|------------|------------|-----------------------------------|
| GIS Server    | Unauthorized access / hacking | High   | Medium     | High       | MFA, role-based access, audit logs|
| Laptops       | Theft or loss               | Medium | Medium     | Medium     | Full-disk encryption, passwords   |
| Cloud Storage | Misconfigured permissions   | High   | Medium     | High       | Access review, audit, encryption  |
| Drone Data    | Data corruption / loss      | High   | Low        | Medium     | Backup strategy, encryption       |

---

## **ISO/IEC 27001 Gap Mapping**

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

## **Python Simulation**
**Purpose:** Simulate **role-based access control** for GIS datasets and demonstrate a basic technical aspect of data protection.

**Script Location:** `scripts/access_control.py`

**How it Works:**  
- Users: `Admin`, `Analyst`, `Guest`  
- Datasets: `survey_data.csv`, `drone_images.csv`  
- Admin can access all datasets, Analyst has limited access, Guest has view-only restrictions  
- Optional logging can track access attempts to simulate auditing  


---

## **Skills Demonstrated**
- **Cybersecurity risk assessment & IT governance**  
- **ISO/IEC 27001 awareness & gap analysis**  
- **Information security policy drafting**  
- **Python scripting for role-based access control**  
- **GIS domain knowledge** (datasets, servers, drones)  
- **Documentation & advisory-style reporting**  

---

## **Usage Instructions**
1. Navigate to the `scripts/` folder  
2. Run `python access_control.py`  
3. Observe which users can access which datasets  

---

**Note:** This project is **fully simulated**, requires no real organization or sensitive data, and demonstrates **entry-level cybersecurity and advisory skills** in a GIS context.
