import streamlit as st

st.set_page_config(
     page_title="Customer registration",
     page_icon = "🧾",
     layout="centered"
 )

st.title("Welcome to the Customer Management System")
st.write("---")
st.write("""
This application is designed to streamline your customer registration and consultation process using a **modular architecture**. 
By separating concerns, we ensure the code is maintainable, scalable, and professional.
""")
st.divider()
st.subheader("Project Structure Overview")
structure_data = [
    {"Page": "🏠 Home (Main)", "Description": "This landing page.", "Purpose": "Provides an overview of the system."},
    {"Page": "📝 Registration", "Description": "Customer input form.", "Purpose": "Collects and validates new customer data."},
    {"Page": "🔍 Consultation", "Description": "Data visualization table.", "Purpose": "Displays the registered customers from the CSV file."}
]

st.table(structure_data)


st.info("Select a page from the sidebar to start.")