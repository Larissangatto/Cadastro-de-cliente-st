import streamlit as st 
from datetime import date
from services.client_service import register_client

st.title("Costumer registration")
st.divider()

name= st.text_input("Name: ",
                    key= "name_costumer")
birth = st.date_input(
    "Date of birth",
    value=date.today(),
    min_value=date(1900, 1, 1),
    max_value=date.today(),
    format="MM/DD/YYYY"
)
type = st.selectbox("Type",
                    ["Individual", "Company"])

if st.button("Salve costumer"):
    register_client(name, birth,type)
    st.success("Customer registered successfully.")