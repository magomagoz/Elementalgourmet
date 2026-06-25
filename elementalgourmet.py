# Salvare questo file come app.py per il deploy su GitHub / Streamlit Cloud
import streamlit as st
import streamlit.components.v1 as components
import urllib.request
import os

# --- LOGO VETTORIALE SVG: IL CERCHIO LINEARE ---
logo_svg = """
<div style="display: flex; justify-content: center; margin-bottom: 2rem;">
    <svg width="120" height="120" viewBox="0 0 512 512" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect width="512" height="512" rx="96" fill="#0B0B0B"/>
        <circle cx="256" cy="256" r="170" stroke="#D4AF37" stroke-width="4" stroke-linecap="round"/>
        <path d="M211 180 L211 332 M211 180 L301 180 M211 256 L281 256 M211 332 L301 332" 
              stroke="#D4AF37" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
</div>
"""

st.markdown(logo_svg, unsafe_allow_html=True)

# --- CONFIGURAZIONE MULTIMEDIALE ---
video1_url = "https://assets.mixkit.co/videos/preview/mixkit-slicing-a-piece-of-cured-ham-41584-large.mp4"
video1_path = "materia_prosciutto.mp4"

video2_url = "https://assets.mixkit.co/videos/preview/mixkit-close-up-of-a-cheese-wheel-42240-large.mp4"
video2_path = "tempo_formaggio.mp4"

# Funzione avanzata di download con camuffamento User-Agent
def download_video(url, output_path):
    if not os.path.exists(output_path):
        try:
            # Creiamo una richiesta spacciandoci per un browser reale
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            }
            req = urllib.request.Request(url, headers=headers)
            
            # Leggiamo i dati dal server e li salviamo sul disco di Streamlit
            with urllib.request.urlopen(req) as response, open(output_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            st.error(f"Errore nel download di {output_path}: {e}")

# Eseguiamo il download per entrambi i video
download_video(video1_url, video1_path)
download_video(video2_url, video2_path)

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


# --- BLOCCO LAYOUT (Resta invariato) ---
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">01. La Materia</div>', unsafe_allow_html=True)
    if os.path.exists(video1_path):
        st.video(video1_path, autoplay=True, loop=True, muted=True)
    st.caption("Il gesto millimetrico del taglio. Affinamento di Jamón Ibérico de Bellota 100% (48 Mesi).")

with col2:
    st.markdown('<div class="section-header">02. Il Tempo</div>', unsafe_allow_html=True)
    if os.path.exists(video2_path):
        st.video(video2_path, autoplay=True, loop=True, muted=True)
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
