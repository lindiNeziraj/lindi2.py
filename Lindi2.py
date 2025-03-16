import streamlit as st
import pandas as pd
st.title("Formulari qe do plotsoni")
st.write("Ky formular ju nihmon per pune!")
Emri = st.text_input("Emri: ")
Mbiemri = st.text_input("Mbiemri: ")
Mosha = st.number_input("Mosha: ", min_value=0, max_value=100, step=1)
Email = st.text_input("Jepni Emailin tuaj ketu: ")
Komenti = st.text_area("Jep nje koment ketu per punen qe deshironi! ")

if Emri and Mbiemri and Mosha and Email and Komenti:
    st.write("Formulari eshte plotesuar Urime dhe Suksese nga Kompania jone!")
else:
    st.error("Plotso te gjithe Formularin sakte!")