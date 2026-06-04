import streamlit as st
# import requests
import sys
import os

# Adaugă folderul părinte (root) la calea de căutare a modulelor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database import get_connection, hash_password

def show_login():
    st.button("← Înapoi", on_click=lambda: setattr(st.session_state, 'page', 'welcome'))
    st.header("Autentificare")
    
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Parolă", type="password")
        role = st.selectbox("Rol", ["Medic", "Pacient", "Admin"])
        submit = st.form_submit_button("Conectare")
        
        if submit:
            # Aici va fi apelul către FastAPI pentru verificare
            # st.success(f"Te-ai logat cu succes ca {role} (Simulare)")
            # st.session_state.logged_in = True
            # Redirecționare către dashboard-ul specific (va fi implementat ulterior)
            conn = get_connection()
            curr = conn.cursor()
            hashed = hash_password(password)
            curr.execute("SELECT * FROM users WHERE email=? AND password=? AND role=?", 
                     (email, hashed, role))
            user = curr.fetchone()
            conn.close()

            if user:
                st.session_state.logged_in = True
                st.session_state.user_info = {"name": user[1], "role": user[4]}
                st.rerun()
            else:
                st.error("Credențiale invalide!")

def show_register():
    st.button("← Înapoi", on_click=lambda: setattr(st.session_state, 'page', 'welcome'))
    st.header("Creare Cont Nou")
    
    with st.form("register_form"):
        nume = st.text_input("Nume Complet")
        email = st.text_input("Email")
        password = st.text_input("Parolă", type="password")
        confirm_password = st.text_input("Confirmă Parola", type="password")
        role = st.radio("Alege Rolul:", ["Pacient", "Medic"])
        
        submit = st.form_submit_button("Înregistrare")
        
        if submit:
            if password == confirm_password:
                try:
                    conn = get_connection()
                    curr = conn.cursor()
                    hashed = hash_password(password)
                    curr.execute("INSERT INTO users (name, email, password, role) VALUES (?,?,?,?)", 
                             (nume, email, hashed, role))
                    conn.commit()
                    conn.close()
                    st.success("Cont creat! Te poți loga.")
                except Exception as e:
                    st.error("Emailul există deja sau a apărut o eroare.")