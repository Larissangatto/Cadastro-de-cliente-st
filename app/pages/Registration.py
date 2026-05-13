import streamlit as st 
from datetime import date
from services.client_service import register_client

st.title("Costumer registration")
st.divider()

name= st.text_input("Name: ",
                    key= "name_costumer")
birth= st.date_input("Date of birth", format ="MM/DD/YYYY")
type = st.selectbox("Type",
                    ["Individual", "Company"])

if st.button("Salve costumer"):
    register_client(name, birth,type)
    st.success("Customer registered successfully.")