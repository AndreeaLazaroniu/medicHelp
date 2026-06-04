import streamlit as st

st.title("Sistem Expert - Diagnostic Cancer de Sân")
st.sidebar.header("Navigare")
user_role = st.sidebar.selectbox("Rol utilizator", ["Medic", "Pacient", "Admin"])

if user_role == "Medic":
    st.subheader("Interfață Medic")
    input_type = st.radio("Alege tipul de date pentru evaluare:", ["Date Clinice (CSV)", "Imagine Ultrasunete (JPG)"])
    uploaded_file = st.file_uploader(f"Încarcă {input_type}")
    
    if st.button("Realizează Predicție AI"):
        st.info("Aici va fi apelat backend-ul FastAPI pentru analiză.")