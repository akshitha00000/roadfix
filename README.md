# 🚧 RoadFix Telangana

## Citizen Pothole Reporting & Tracking System

RoadFix Telangana is a web-based application developed to help citizens report potholes and road damage directly to local authorities. The platform enables efficient complaint management, status tracking, worker updates, and analytics for better road maintenance.

---

## 📌 Problem Statement

Poor road conditions and potholes cause accidents, vehicle damage, and inconvenience to citizens. Reporting these issues often involves lengthy manual processes and lacks transparency.

RoadFix Telangana provides a digital solution that allows citizens to report potholes with images, while authorities can track, manage, and resolve complaints efficiently.

---

## 🎯 Objectives

* Enable citizens to report potholes easily.
* Allow uploading of road damage images.
* Provide real-time complaint status tracking.
* Help workers update repair progress.
* Generate analytics for decision-making.

---

## ✨ Features

### 🏠 Home Dashboard

* Total complaints count
* Pending complaints
* In Progress complaints
* Resolved complaints

### 🚧 Submit Complaint

* Citizen name
* District selection
* Location details
* Complaint description
* Image upload support

### 📋 View Complaints

* View all submitted complaints
* Track complaint status
* View before and after repair images
* Read completion notes

### 🛠 Worker Dashboard

* Update complaint status
* Add completion notes
* Upload repaired road images
* Mark complaints as resolved

### 📊 Analytics Dashboard

* District-wise complaint analysis
* Complaint status distribution
* Data visualization using charts

---

## 🛠 Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### Database

* SQLite

### Data Analysis

* Pandas

### Additional Libraries

* Pillow
* Folium
* Streamlit-Folium

---

## 📂 Project Structure

```text
RoadFix-Telangana/
│
├── app.py
├── database.py
├── complaints.db
├── requirements.txt
│
├── uploads/
│   ├── complaints/
│   └── repaired/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone <repository-url>
cd RoadFix-Telangana
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows:

```bash
.venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 🚀 Future Enhancements

* GPS-based location tracking
* Interactive map integration
* Mobile application support
* AI-based pothole detection from images
* Government department integration
* Notification and alert system
* Complaint priority classification

---

## 👥 Target Users

* Citizens
* Municipal Authorities
* Road Maintenance Workers
* Government Departments

---

## 🌍 Impact

RoadFix Telangana promotes safer roads, faster complaint resolution, improved transparency, and active citizen participation in infrastructure maintenance.

---

## 🏆 Hackathon Project

Developed as a Hackathon Solution to improve road infrastructure management through technology and citizen engagement.

---

### Team Name

KanyaRasi

### Project Name

RoadFix Telangana

Made with ❤️ using Python and Streamlit.
