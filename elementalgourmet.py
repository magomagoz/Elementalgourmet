# Salvare questo file come app.py per il deploy su GitHub / Streamlit Cloud
import streamlit as st
import streamlit.components.v1 as components

# Configurazione dell'istanza web in modalità lusso discreto
st.set_page_config(
    page_title="ELEMENTAL | Masterpieces, Untouched.",
    page_icon="🕋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Iniezione CSS per forzare l'interfaccia proprietaria di ELEMENTAL
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;600&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #0a0a0a !important;
            color: #e5e5e5 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Rimozione degli elementi standard e watermark di Streamlit */
        [data-testid="stHeader"], footer, #tabs-bui3-tabpanel-0 {
            visibility: hidden;
            display: none;
        }
        
        .brand-title {
            font-size: 3.5rem;
            font-weight: 200;
            letter-spacing: 10px;
            text-align: center;
            color: #ffffff;
            text-transform: uppercase;
            margin-top: 60px;
            margin-bottom: 5px;
        }
        
        .brand-tagline {
            font-size: 0.95rem;
            font-weight: 300;
            letter-spacing: 6px;
            text-align: center;
            color: #b3925c;
            text-transform: uppercase;
            margin-bottom: 60px;
        }
        
        .section-header {
            font-size: 1.3rem;
            font-weight: 300;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: #ffffff;
            border-bottom: 1px solid #222222;
            padding-bottom: 12px;
            margin-top: 50px;
            margin-bottom: 25px;
        }
        
        /* Contenitore rigido per i video loop materici */
        .video-container {
            width: 100%;
            border-radius: 2px;
            overflow: hidden;
            border: 1px solid #1a1a1a;
            margin-bottom: 15px;
        }
        
        /* Stile sartoriale per il form di prenotazione riservata */
        div[data-testid="stForm"] {
            border: 1px solid #222222 !important;
            background-color: #111111 !important;
            padding: 40px !important;
            border-radius: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Logo e payoff centrali
st.markdown('<div class="brand-title">ELEMENTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-tagline">Masterpieces, Untouched.</div>', unsafe_allow_html=True)

# Griglia asimmetrica per la riproduzione dei video loop multimediali
# Salvare questo file come app.py per il deploy su GitHub / Streamlit Cloud
import streamlit as st
import streamlit.components.v1 as components

# Configurazione dell'istanza web in modalità lusso discreto
st.set_page_config(
    page_title="ELEMENTAL | Masterpieces, Untouched.",
    page_icon="🕋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Iniezione CSS per forzare l'interfaccia proprietaria di ELEMENTAL
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;600&display=swap');
        
        html, body, [data-testid="stAppViewContainer"] {
            background-color: #0a0a0a !important;
            color: #e5e5e5 !important;
            font-family: 'Inter', sans-serif !important;
        }
        
        /* Rimozione degli elementi standard e watermark di Streamlit */
        [data-testid="stHeader"], footer, #tabs-bui3-tabpanel-0 {
            visibility: hidden;
            display: none;
        }
        
        .brand-title {
            font-size: 3.5rem;
            font-weight: 200;
            letter-spacing: 10px;
            text-align: center;
            color: #ffffff;
            text-transform: uppercase;
            margin-top: 60px;
            margin-bottom: 5px;
        }
        
        .brand-tagline {
            font-size: 0.95rem;
            font-weight: 300;
            letter-spacing: 6px;
            text-align: center;
            color: #b3925c;
            text-transform: uppercase;
            margin-bottom: 60px;
        }
        
        .section-header {
            font-size: 1.3rem;
            font-weight: 300;
            letter-spacing: 4px;
            text-transform: uppercase;
            color: #ffffff;
            border-bottom: 1px solid #222222;
            padding-bottom: 12px;
            margin-top: 50px;
            margin-bottom: 25px;
        }
        
        /* Contenitore rigido per i video loop materici */
        .video-container {
            width: 100%;
            border-radius: 2px;
            overflow: hidden;
            border: 1px solid #1a1a1a;
            margin-bottom: 15px;
        }
        
        /* Stile sartoriale per il form di prenotazione riservata */
        div[data-testid="stForm"] {
            border: 1px solid #222222 !important;
            background-color: #111111 !important;
            padding: 40px !important;
            border-radius: 2px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Logo e payoff centrali
st.markdown('<div class="brand-title">ELEMENTAL</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-tagline">Masterpieces, Untouched.</div>', unsafe_allow_html=True)

# Griglia asimmetrica per la riproduzione dei video loop multimediali
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">01. La Materia</div>', unsafe_allow_html=True)
    # Video Loop: il taglio millimetrico (Sostituire il source con un video in CDN proprietaria o repository GitHub)
    video_html_1 = """
    <div class="video-container">
        <video width="100%" autoplay loop muted playsinline style="display:block;">
            <source src="https://assets.mixkit.co/videos/preview/mixkit-slicing-a-piece-of-cured-ham-41584-large.mp4" type="video/mp4">
        </video>
    </div>
    """
    components.html(video_html_1, height=280, scrolling=False)
    st.caption("Il gesto millimetrico del taglio. Affinamento di Jamón Ibérico de Bellota 100% (48 Mesi).")

with col2:
    st.markdown('<div class="section-header">02. Il Tempo</div>', unsafe_allow_html=True)
    # Video Loop: l'apertura e la texture dei formaggi rari
    video_html_2 = """
    <div class="video-container">
        <video width="100%" autoplay loop muted playsinline style="display:block;">
            <source src="https://assets.mixkit.co/videos/preview/mixkit-close-up-of-a-cheese-wheel-42240-large.mp4" type="video/mp4">
        </video>
    </div>
    """
    components.html(video_html_2, height=280, scrolling=False)
    st.caption("La spaccatura materica della forma. Parmigiano Reggiano DOP da Vacche Rosse (60 Mesi).")

# Introduzione al concetto del Menù
st.markdown('<div class="section-header">03. L\'Edit Europeo delle Eccellenze</div>', unsafe_allow_html=True)
st.write("Un inventario rigidamente curato di ciò che la natura e l'affinamento hanno già reso perfetto. Senza l'interferenza della fiamma.")

# Portale Private Concierge per clientela selezionata
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


# Introduzione al concetto del Menù
st.markdown('<div class="section-header">03. L\'Edit Europeo delle Eccellenze</div>', unsafe_allow_html=True)
st.write("Un inventario rigidamente curato di ciò che la natura e l'affinamento hanno già reso perfetto. Senza l'interferenza della fiamma.")

# Portale Private Concierge per clientela selezionata
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

