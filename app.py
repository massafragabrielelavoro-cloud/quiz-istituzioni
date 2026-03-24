import streamlit as st
import random
from streamlit_keyup import st_keyup # <--- Importiamo il nuovo componente live

st.set_page_config(page_title="Quiz Istituzioni", page_icon="🇮🇹", layout="centered")

domande_risposte = {
    "Qual è la legge fondamentale dello Stato italiano?": "costituzione",
    "L'Italia è una repubblica... (forma di governo)?": "parlamentare",
    "Quale potere detiene il Parlamento?": "legislativo",
    "Chi è il Presidente del Consiglio nell'attuale governo del 2026?": "meloni"
}

if 'quiz_attivo' not in st.session_state:
    st.session_state.lista_domande = list(domande_risposte.keys())
    random.shuffle(st.session_state.lista_domande)
    st.session_state.indice = 0
    st.session_state.quiz_attivo = True

st.title("🇮🇹 Quiz sulle Istituzioni Italiane")
st.markdown("---")

if st.session_state.indice < len(st.session_state.lista_domande):
    domanda_corrente = st.session_state.lista_domande[st.session_state.indice]
    
    st.subheader(f"Domanda {st.session_state.indice + 1} di {len(st.session_state.lista_domande)}")
    st.info(f"**{domanda_corrente}**")
    
    # QUI LA MAGIA: usiamo st_keyup al posto del normale text_input.
    # Il sistema legge in tempo reale ogni lettera digitata.
    risposta_utente = st_keyup("Scrivi la risposta (il sistema la convalida in automatico):", key=f"input_{st.session_state.indice}")
    
    if risposta_utente:
        risposta_giusta = domande_risposte[domanda_corrente].strip().lower()
        
        # Appena la parola digitata corrisponde a quella giusta, scatta in avanti!
        if risposta_utente.strip().lower() == risposta_giusta:
            st.success("✅ Esatto!")
            st.session_state.indice += 1
            st.rerun()

else:
    st.balloons()
    st.success("🎉 COMPLIMENTI! Hai completato tutte le domande del quiz!")
    
    if st.button("🔄 Riavvia il Quiz"):
        del st.session_state.quiz_attivo
        st.rerun()
