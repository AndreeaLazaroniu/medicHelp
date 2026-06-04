import streamlit as st
from home import show_welcome
from auth import show_login, show_register
from dashboard_medic import show_medic_dashboard

# Configurare pagină
st.set_page_config(page_title="Diagnostic Cancer Sân AI", layout="wide")

# Inițializare stare sesiune pentru navigare
if 'page' not in st.session_state:
    st.session_state.page = 'welcome'
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Modifică logica de la finalul fișierului app.py:
if st.session_state.logged_in:
    # Aici poți adăuga logică pentru a verifica rolul (ex: dacă e medic)
    show_medic_dashboard()
else:
    if st.session_state.page == 'welcome':
        show_welcome()
    elif st.session_state.page == 'login':
        show_login()
    elif st.session_state.page == 'register':
        show_register()