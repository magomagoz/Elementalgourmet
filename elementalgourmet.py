# Salvare questo file come app.py per il deploy su GitHub / Streamlit Cloud
import streamlit as st
import os

# --- 1. CONFIGURAZIONE OBBLIGATORIA (Deve essere la prima istruzione Streamlit) ---
st.set_page_config(
    page_title="ELEMENTAL | Masterpieces, Untouched.",
    page_icon="🕋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. LOGO VETTORIALE SVG: IL CERCHIO LINEARE ---
logo_svg = """
<div style="display: flex; justify-content: center; margin-top: 3rem; margin-bottom: 1rem;">
    <svg width="110" height="110" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="512" height="512" rx="96" fill="#0B0B0B"/>
        <circle cx="256" cy="256" r="170" stroke="#D4AF37" stroke-width="4" stroke-linecap="round"/>
        <path d="M211 180 L211 332 M211 180 L301 180 M211 256 L281 256 M211 332 L301 332" 
              stroke="#D4AF37" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
</div>
"""
st.markdown(logo_svg, unsafe_allow_html=True)


# --- 3. INIEZIONE CSS SARTORIALE ED EFFETTI CINEMATICI ---
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;600&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #0a0a0a !important;
            color: #e5e5e5 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Rimozione degli elementi standard e watermark di Streamlit */
        [data-testid="stHeader"], footer {
            visibility: hidden;
            display: none;
        }
        
        .brand-title {
            font-size: 3.5rem;
            font-weight: 200;
            letter-spacing: 12px;
            text-align: center;
            color: #ffffff;
            text-transform: uppercase;
            margin-top: 10px;
            margin-bottom: 5px;
        }
        
        .brand-tagline {
            font-size: 0.90rem;
            font-weight: 300;
            letter-spacing: 7px;
            text-align: center;
            color: #b3925c;
            text-transform: uppercase;
            margin-bottom: 60px;
        }
        
        .section-header {
            font-size: 1.2rem;
            font-weight: 300;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: #ffffff;
            border-bottom: 1px solid #1c1c1c;
            padding-bottom: 12px;
            margin-top: 40px;
            margin-bottom: 25px;
        }
        
        /* Contenitore per l'effetto di movimento ipnotico (Ken Burns) */
        .kinetic-container {
            width: 100%;
            height: 380px;
            border-radius: 2px;
            overflow: hidden;
            border: 1px solid #1a1a1a;
            position: relative;
            background-color: #0d0d0d;
        }
        
        .kinetic-image {
            width: 100%;
            height: 100%;
            object-fit: cover;
            filter: brightness(0.85) contrast(1.05);
            animation: luxuryBreathe 28s ease-in-out infinite alternate;
            -webkit-animation: luxuryBreathe 28s ease-in-out infinite alternate;
        }
        
        /* Definizione del movimento fluido e impercettibile */
        @keyframes luxuryBreathe {
            0% { transform: scale(1.0) translate(0, 0); }
            100% { transform: scale(1.08) translate(-1%, -0.5%); }
        }
        @-webkit-keyframes luxuryBreathe {
            0% { -webkit-transform: scale(1.0); }
            100% { -webkit-transform: scale(1.08); }
        }
        
        /* Stile per il form di prenotazione riservata */
        div[data-testid="stForm"] {
            border: 1px solid #1c1c1c !important;
            background-color: #0d0d0d !important;
            padding: 40px !important;
            border-radius: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)


# --- 4. IDENTITÀ CENTRALE ---
st.markdown('<div class="brand-title">ELEMENTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-tagline">Masterpieces, Untouched.</div>', unsafe_allow_html=True)


# --- 5. SEZIONE MULTIMEDIALE KINETIC (Sostituisce i vecchi video) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">01. La Materia</div>', unsafe_allow_html=True)
    # Foto d'autore selezionata per il Pata Negra Jamón Ibérico
    st.markdown("""
        <div class="kinetic-container">
            <img class="kinetic-image" src="https://images.unsplash.com/photo-1627664813831-26e957c73ef9?q=80&w=1200&auto=format&fit=crop" alt="Jamón Ibérico">
        </div>
    """, unsafe_allow_html=True)
    st.caption("Il gesto millimetrico del taglio. Affinamento di Jamón Ibérico de Bellota 100% (5 Jotas, 48 Mesi).")

with col2:
    st.markdown('<div class="section-header">02. Il Tempo</div>', unsafe_allow_html=True)
    # Foto d'autore selezionata per la texture del Parmigiano d'Eccellenza
    st.markdown("""
        <div class="kinetic-container">
            <img class="kinetic-image" src="https://images.unsplash.com/photo-1608686207856-001b95cf60ca?q=80&w=1200&auto=format&fit=crop" alt="Parmigiano Reggiano">
        </div>
    """, unsafe_allow_html=True)
    st.caption("La spaccatura materica della forma. Parmigiano Reggiano DOP da Vacche Rosse (60 Mesi).")


# --- 6. FILOSOFIA E CONCIERGE ---
st.markdown('<div class="section-header">03. L\'Edit Europeo delle Eccellenze</div>', unsafe_allow_html=True)
st.write("Un inventario rigidamente curato di ciò che la natura e l'affinamento hanno già reso perfetto. Senza l'interferenza della fiamma.")

st.markdown('<div class="section-header">04. Richiesta di Accesso</div>', unsafe_allow_html=True)
with st.form("private_concierge_form"):
    st.write("L'esperienza ELEMENTAL accoglie un numero limitato di ospiti per sessione. Inserire i dettagli per richiedere l'inserimento in lista d'attesa.")
    client_name = st.text_input("Nome Completo / Ente")
    client_email = st.text_input("Canale di Contatto Riservato (Email/Signal)")
    selected_hub = st.selectbox("Hub di Riferimento", ["Roma", "Milano", "Londra", "Parigi", "Dubai"])
    special_notes = st.text_area("Note e Preferenze di Concierge (Allergie, Esigenze di Sicurezza o Privacy)")
    
    submit_btn = st.form_submit_button("Invia Richiesta di Accreditamento")
    if submit_btn:
        if client_name and client_email:
            st.success("Richiesta registrata nei nostri sistemi. Il Private Concierge di ELEMENTAL la contatterà in modo cifrato entro 4 ore.")
        else:
            st.error("Campi obbligatori mancanti. Impossibile processare la richiesta.")
