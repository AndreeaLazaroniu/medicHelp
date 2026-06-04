import streamlit as st

def show_welcome():
    st.title("Sistem Expert pentru Diagnosticul Cancerului la Sân")
    st.subheader("Platformă de analiză multimodală bazată pe AI")
    
    st.markdown("""
    Această aplicație utilizează algoritmi avansați de Machine Learning pentru a asista:
    * **Medicii:** În analiza parametrilor clinici și a imaginilor ecografice.
    * **Pacienții:** În vizualizarea dosarului medical și a rezultatelor.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Autentificare (Login)", use_container_width=True):
            st.session_state.page = 'login'
            st.rerun()
    with col2:
        if st.button("Creare Cont (Register)", use_container_width=True):
            st.session_state.page = 'register'
            st.rerun()