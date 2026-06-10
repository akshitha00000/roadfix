import streamlit as st
import sqlite3
import os
import pandas as pd
from database import create_table

create_table()

# Create folders
os.makedirs("uploads/complaints", exist_ok=True)
os.makedirs("uploads/repaired", exist_ok=True)

st.set_page_config(
    page_title="RoadFix Telangana",
    page_icon="🚧",
    layout="wide"
)

st.title("🚧 RoadFix Telangana")
st.subheader("Citizen Pothole Reporting & Tracking System")

menu = [
    "🏠 Home",
    "🚧 Submit Complaint",
    "📋 View Complaints",
    "🛠 Worker Dashboard",
    "📊 Analytics"
]

choice = st.sidebar.selectbox("Navigation", menu)

# ---------------- HOME ---------------- #

if choice == "🏠 Home":

    conn = sqlite3.connect("complaints.db")
    df = pd.read_sql_query("SELECT * FROM complaints", conn)

    total = len(df)

    pending = len(df[df["status"] == "Pending"])
    progress = len(df[df["status"] == "In Progress"])
    resolved = len(df[df["status"] == "Resolved"])

    conn.close()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Total", total)
    c2.metric("Pending", pending)
    c3.metric("In Progress", progress)
    c4.metric("Resolved", resolved)

    st.info("Welcome to RoadFix Telangana")

# ---------------- SUBMIT ---------------- #

elif choice == "🚧 Submit Complaint":

    st.header("Report a Pothole")

    name = st.text_input("Your Name")

    district = st.selectbox(
        "District",
        [
            "Hyderabad",
            "Warangal",
            "Karimnagar",
            "Nizamabad",
            "Khammam",
            "Nalgonda",
            "Mahabubnagar",
            "Sangareddy"
        ]
    )

    location = st.text_input("Location")

    description = st.text_area("Description")

    image = st.file_uploader(
        "Upload Pothole Image",
        type=["jpg", "jpeg", "png"]
    )

    if st.button("Submit Complaint"):

        image_path = ""

        if image:

            image_path = f"uploads/complaints/{image.name}"

            with open(image_path, "wb") as f:
                f.write(image.getbuffer())

        conn = sqlite3.connect("complaints.db")
        c = conn.cursor()

        c.execute("""
        INSERT INTO complaints
        (
            name,
            district,
            location,
            description,
            image_path,
            status,
            completion_note,
            repaired_image
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            district,
            location,
            description,
            image_path,
            "Pending",
            "",
            ""
        ))

        conn.commit()
        conn.close()

        st.success("Complaint Submitted Successfully!")

# ---------------- VIEW ---------------- #

elif choice == "📋 View Complaints":

    st.header("All Complaints")

    conn = sqlite3.connect("complaints.db")
    c = conn.cursor()

    c.execute("SELECT * FROM complaints")

    complaints = c.fetchall()

    conn.close()

    for complaint in complaints:

        st.markdown("---")

        st.subheader(f"Complaint #{complaint[0]}")

        st.write("Citizen:", complaint[1])
        st.write("District:", complaint[2])
        st.write("Location:", complaint[3])
        st.write("Description:", complaint[4])
        st.write("Status:", complaint[6])

        if complaint[5]:
            st.write("Before Repair")
            st.image(complaint[5], width=350)

        if complaint[7]:
            st.write("Completion Note")
            st.success(complaint[7])

        if complaint[8]:
            st.write("After Repair")
            st.image(complaint[8], width=350)

# ---------------- WORKER ---------------- #

elif choice == "🛠 Worker Dashboard":

    st.header("Worker Dashboard")

    conn = sqlite3.connect("complaints.db")
    c = conn.cursor()

    c.execute("SELECT * FROM complaints")

    complaints = c.fetchall()

    for complaint in complaints:

        with st.expander(
            f"Complaint #{complaint[0]} - {complaint[6]}"
        ):

            st.write("Location:", complaint[3])
            st.write("Description:", complaint[4])

            if complaint[5]:
                st.image(complaint[5], width=300)

            new_status = st.selectbox(
                f"Status {complaint[0]}",
                ["Pending", "In Progress", "Resolved"]
            )

            completion_note = st.text_area(
                f"Note {complaint[0]}"
            )

            repaired_image = st.file_uploader(
                f"Upload Repair Image {complaint[0]}",
                type=["jpg", "png", "jpeg"]
            )

            if st.button(f"Update Complaint {complaint[0]}"):

                repaired_path = complaint[8]

                if repaired_image:

                    repaired_path = (
                        f"uploads/repaired/"
                        f"{complaint[0]}_repair.jpg"
                    )

                    with open(repaired_path, "wb") as f:
                        f.write(
                            repaired_image.getbuffer()
                        )

                c.execute("""
                UPDATE complaints
                SET
                    status=?,
                    completion_note=?,
                    repaired_image=?
                WHERE id=?
                """,
                (
                    new_status,
                    completion_note,
                    repaired_path,
                    complaint[0]
                ))

                conn.commit()

                st.success("Updated Successfully")

    conn.close()

# ---------------- ANALYTICS ---------------- #

elif choice == "📊 Analytics":

    st.header("Analytics Dashboard")

    conn = sqlite3.connect("complaints.db")

    df = pd.read_sql_query(
        "SELECT * FROM complaints",
        conn
    )

    conn.close()

    if len(df) > 0:

        st.subheader("District-wise Complaints")

        district_counts = (
            df["district"]
            .value_counts()
        )

        st.bar_chart(district_counts)

        st.subheader("Status Distribution")

        status_counts = (
            df["status"]
            .value_counts()
        )

        st.bar_chart(status_counts)

        st.dataframe(df)

    else:

        st.info("No data available.")