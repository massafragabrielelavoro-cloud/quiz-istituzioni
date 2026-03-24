import streamlit as st
import random

st.set_page_config(page_title="Daje Ali che se le fai giuste ti aspetta il pigiamino", page_icon="", layout="centered")

# Le tue domande (sostituiscile pure con le tue 100)
domande_risposte = {
    "Qual è la legge fondamentale dello Stato italiano?": "costituzione",
    "L'Italia è una repubblica... (forma di governo)?": "parlamentare",
    "Quale potere detiene il Parlamento?": "legislativo",
    "Chi è il Presidente del Consiglio nell'attuale governo del 2026?": "meloni",
    "Qual è la Camera bassa del Parlamento italiano?": "camera"
}

# Inizializzazione della memoria del gioco
if 'quiz_attivo' not in st.session_state:
    st.session_state.lista_domande = list(domande_risposte.keys())
    random.shuffle(st.session_state.lista_domande)
    st.session_state.indice = 0
    st.session_state.streak = 0            # Contatore per la Combo
    st.session_state.mostra_aiuto = False  # Gestione del pulsante Aiutino
    st.session_state.quiz_attivo = True

st.title("Daje Ali che se le fai giuste ti aspetta il pigiamino")

# --- PUNTO 3: SISTEMA DI COMBO ---
# Creiamo due colonne per mostrare i punteggi in modo elegante
col1, col2 = st.columns(2)
with col1:
    st.metric(label="✅ Progresso", value=f"{st.session_state.indice} / {len(st.session_state.lista_domande)}")
with col2:
    st.metric(label="🔥 Combo (Risposte esatte di fila)", value=st.session_state.streak)

st.markdown("---")

if st.session_state.indice < len(st.session_state.lista_domande):
    
    # --- PUNTO 2: BARRA DI AVANZAMENTO ---
    progresso = st.session_state.indice / len(st.session_state.lista_domande)
    st.progress(progresso)
    
    domanda_corrente = st.session_state.lista_domande[st.session_state.indice]
    risposta_giusta = domande_risposte[domanda_corrente].strip().lower()
    
    st.subheader(f"Domanda {st.session_state.indice + 1}")
    st.info(f"**{domanda_corrente}**")
    
    # --- PUNTO 1: IL BOTTONE AIUTINO ---
    if st.button("💡 Mi arrendo, dammi un aiutino!"):
        st.session_state.mostra_aiuto = True
        
    if st.session_state.mostra_aiuto:
        prima_lettera = risposta_giusta[0].upper()
        lunghezza = len(risposta_giusta)
        st.warning(f"Indizio: Inizia con la lettera **{prima_lettera}** ed è lunga **{lunghezza}** lettere.")
    
    # Casella di testo per la risposta
    risposta_utente = st.text_input("Scrivi la risposta e premi Invio:", key=f"input_{st.session_state.indice}")
    
    if risposta_utente:
        # Se la risposta è corretta
        if risposta_utente.strip().lower() == risposta_giusta:
            st.success("✅ Ma allora mi ascolti")
            st.session_state.indice += 1
            st.session_state.streak += 1           # Aumenta la combo
            st.session_state.mostra_aiuto = False  # Nascondi l'aiuto per la prossima domanda
            st.rerun()                             # Passa alla prossima schermata
        # Se la risposta è sbagliata
        else:
            st.error("❌ Ma dio caro, hai sbagliato già! (La tua combo è tornata a zero)")
            st.session_state.streak = 0            # Azzera la combo

else:
    # Schermata Finale
    st.progress(1.0) # Barra piena al 100%
    st.balloons()
    st.success("🎉 COMPLIMENTI! Hai completato l'intero quiz!")
    
    if st.button("🔄 Riavvia il Quiz"):
        # Cancella la memoria e riavvia da zero
        del st.session_state.quiz_attivo
        st.rerun()
