import streamlit as st
import random

# Configurazione della pagina (titolo nella scheda del browser e icona)
st.set_page_config(page_title="Quiz Istituzioni", page_icon="🇮🇹", layout="centered")

# Il tuo dizionario di domande (qui ne metto 4 di esempio, tu metti le tue 100)
domande_risposte = {
    "Qual è la legge fondamentale dello Stato italiano?": "costituzione",
    "L'Italia è una repubblica... (forma di governo)?": "parlamentare",
    "Quale potere detiene il Parlamento?": "legislativo",
    "Chi è il Presidente del Consiglio nell'attuale governo del 2026?": "meloni"
}

# --- GESTIONE DELLO STATO (Memoria dell'app) ---
# Quando l'app parte la prima volta, mescoliamo le domande e partiamo da zero
if 'quiz_attivo' not in st.session_state:
    st.session_state.lista_domande = list(domande_risposte.keys())
    random.shuffle(st.session_state.lista_domande)
    st.session_state.indice = 0
    st.session_state.quiz_attivo = True

# --- INTERFACCIA GRAFICA ---
st.title("🇮🇹 Quiz sulle Istituzioni Italiane")
st.markdown("---")

# Se ci sono ancora domande da fare
if st.session_state.indice < len(st.session_state.lista_domande):
    domanda_corrente = st.session_state.lista_domande[st.session_state.indice]
    
    # Mostriamo a che punto siamo
    st.subheader(f"Domanda {st.session_state.indice + 1} di {len(st.session_state.lista_domande)}")
    st.info(f"**{domanda_corrente}**")
    
    # Casella di testo per la risposta
    # (Usiamo una chiave dinamica così si "pulisce" a ogni nuova domanda)
    risposta_utente = st.text_input("Scrivi la tua risposta e premi Invio:", key=f"input_{st.session_state.indice}")
    
    # Controllo della risposta quando l'utente digita qualcosa
    if risposta_utente:
        risposta_giusta = domande_risposte[domanda_corrente].strip().lower()
        
        if risposta_utente.strip().lower() == risposta_giusta:
            st.success("✅ Corretto! Passiamo alla prossima...")
            st.session_state.indice += 1
            st.rerun() # Ricarica la pagina per mostrare la domanda successiva
        else:
            st.error("❌ Sbagliato, ritenta!")

# Se le domande sono finite
else:
    st.balloons() # Animazione di festa sullo schermo!
    st.success("🎉 COMPLIMENTI! Hai completato tutte le domande del quiz!")
    
    # Bottone per ricominciare
    if st.button("🔄 Riavvia il Quiz"):
        del st.session_state.quiz_attivo # Cancella la memoria
        st.rerun() # Ricarica da zero
