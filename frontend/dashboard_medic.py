import streamlit as st
import pandas as pd
from PIL import Image

def show_medic_dashboard():
    st.title("👨‍⚕️ Panou Control Medic")
    st.sidebar.write("---")
    
    # Meniu lateral pentru navigare rapidă
    task = st.sidebar.radio("Sarcini disponibile:", 
                            ["Evaluare Pacient Nou", "Istoric Diagnosticări", "Statistici Modele AI"])

    if task == "Evaluare Pacient Nou":
        st.header("Evaluare Diagnostică Multimodală")
        
        # Selectarea sursei de date
        tab1, tab2 = st.tabs(["📊 Date Clinice (Tabelar)", "🖼️ Imagistică (Ultrasound)"])

        with tab1:
            st.write("Introduceți valorile celulare sau încărcați un fișier CSV (Wisconsin Dataset style).")
            # Exemplu de input manual pentru date clinice
            col1, col2 = st.columns(2)
            with col1:
                radius = st.number_input("Radius Mean", format="%.4f")
                texture = st.number_input("Texture Mean", format="%.4f")
            with col2:
                perimeter = st.number_input("Perimeter Mean", format="%.4f")
                smoothness = st.number_input("Smoothness Mean", format="%.4f")
            
            if st.button("Analizează Date Clinice", key="btn_tabular"):
                st.warning("Se apelează modelul XGBoost... (Aici va apărea rezultatul și SHAP)")

        with tab2:
            st.write("Încărcați o imagine ecografică pentru detectarea anomaliilor.")
            img_file = st.file_uploader("Alege imaginea JPG/PNG", type=['jpg', 'png', 'jpeg'])
            
            if img_file:
                st.image(img_file, caption="Imagine încărcată", width=300)
                if st.button("Analizează Imagine", key="btn_img"):
                    st.success("Se apelează modelul PyTorch... (Aici va apărea Grad-CAM)")
                    # Placeholder pentru Heatmap
                    st.image("https://via.placeholder.com/300x300.png?text=Grad-CAM+Heatmap", 
                             caption="Explicație AI (Grad-CAM)")

    elif task == "Istoric Diagnosticări":
        st.header("Istoric Pacienți")
        # Simulare tabel din baza de date
        data = {
            "ID Pacient": ["P001", "P002"],
            "Data": ["2026-04-10", "2026-04-12"],
            "Rezultat AI": ["Malign", "Benign"],
            "Confirmare Medic": ["Confirmat", "Infirmat (False Positive)"]
        }
        st.table(pd.DataFrame(data))

    if st.sidebar.button("Deconectare"):
        st.session_state.logged_in = False
        st.session_state.page = 'login'
        st.rerun()