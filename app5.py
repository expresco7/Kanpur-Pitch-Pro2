import streamlit as st
import time
import os

# 1. STRUCTURAL PAGE LAYOUT SETUP
st.set_page_config(
    page_title="Pitch Pro Terminal",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Active state session management variables
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "selected_competitor" not in st.session_state:
    st.session_state.selected_competitor = "Select Competitor..."
if "pitch_customized" not in st.session_state:
    st.session_state.pitch_customized = False
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

# Reset view metrics when toggling between operational nodes
def reset_pitch_flow(target_module):
    st.session_state.selected_module = target_module
    st.session_state.selected_competitor = "Select Competitor..."
    st.session_state.pitch_customized = False

# 2. MOBILE-FIRST DESIGN SYSTEM (CRED STYLE SHEETS)
st.markdown("""
    <style>
    /* Base Engine Mobile UI Configuration */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0A0A0C !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* Strict Mobile Viewport Padding Limits & High-Density Spacing */
    [data-testid="stAppViewContainer"] .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
        max-width: 25rem !important; /* Locks layout to exact mobile device width bounds */
        margin: 0 auto !important;
    }
    
    /* Remove default element margins to reduce empty space */
    [data-testid="stVerticalBlock"] > div {
        padding-bottom: 0.4rem !important;
        margin-bottom: 0px !important;
    }
    
    /* Invisible App Bars */
    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; display: none !important; }
    
    /* Symmetrical Carousel Architecture */
    .stHorizontalBlock {
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        padding: 4px 4px 10px 4px !important;
        gap: 12px !important;
        margin-bottom: 0px !important;
    }
    .stHorizontalBlock::-webkit-scrollbar { height: 4px; }
    .stHorizontalBlock::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.01); border-radius: 10px; }
    .stHorizontalBlock::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.12); border-radius: 10px; }
    .stHorizontalBlock > div { min-width: 175px !important; max-width: 175px !important; flex: 0 0 auto !important; padding: 0 !important; }
    
    /* Advanced Interactive Card Shell Component */
    .carousel-card-shell {
        position: relative;
        background: linear-gradient(135deg, #141419 0%, #1A1A22 100%);
        border: 1px solid rgba(255,255,255,0.07);
        border-radius: 18px;
        padding: 16px;
        height: 140px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    }
    .carousel-card-title {
        font-size: 13px;
        font-weight: 800;
        letter-spacing: -0.01em;
        color: #FFFFFF;
        line-height: 1.3;
        margin-top: 4px;
        text-transform: uppercase;
    }
    
    /* Clean Overlay Mapping Native Streamlit Buttons to Fill the Card Body */
    .carousel-card-shell div.stButton {
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        margin: 0 !important; padding: 0 !important;
    }
    .carousel-card-shell div.stButton > button {
        background-color: transparent !important;
        border: none !important;
        border-radius: 18px !important;
        width: 100% !important;
        height: 100% !important;
        text-align: left !important;
        padding: 16px !important;
        transition: background-color 0.2s ease;
    }
    .carousel-card-shell div.stButton > button:hover, 
    .carousel-card-shell div.stButton > button:active {
        background-color: rgba(255, 255, 255, 0.03) !important;
    }
    .carousel-card-shell div.stButton > button p {
        color: #8E8E93 !important; font-size: 10px !important; font-weight: 700 !important;
        text-transform: uppercase !important; letter-spacing: 0.05em !important;
        position: absolute; bottom: 16px; left: 16px; margin: 0 !important;
    }
    .carousel-card-shell div.stButton > button:hover p { color: #FFFFFF !important; }

    /* --- RESTORED ORIGINAL TELEMETRY CARD FRAMEWORK --- */
    .telemetry-card {
        background: linear-gradient(135deg, #121216 0%, #1C1C1E 100%);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 20px;
        padding: 16px;
        margin-bottom: 12px !important;
    }
    .telemetry-grid {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .telemetry-item {
        text-align: center;
        flex: 1;
        border-right: 1px solid rgba(255,255,255,0.08);
    }
    .telemetry-item:last-child {
        border-right: none;
    }
    .telemetry-val {
        font-size: 18px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.02em;
    }
    .telemetry-val.leader-color {
        color: #00CD52 !important;
        text-shadow: 0 0 10px rgba(0,205,82,0.2);
    }
    .telemetry-lbl {
        font-size: 9px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #8E8E93;
        margin-top: 2px;
    }

    /* --- PREMIUM CRED GLASS ENCLOSED TROUBLESHOOTING DECK --- */
    .illuminated-triage-panel {
        background: linear-gradient(145deg, #0F0F13 0%, #15151C 100%) !important;
        border: 1px solid rgba(255, 149, 0, 0.22) !important;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5), 0 0 20px rgba(255, 149, 0, 0.02) !important;
        border-radius: 22px !important;
        padding: 20px !important;
        margin-top: 15px !important;
        margin-bottom: 10px !important;
    }
    .terminal-main-header {
        font-size: 12px !important;
        font-weight: 800 !important;
        letter-spacing: 0.08em !important;
        text-transform: uppercase !important;
        color: #FF9500 !important;
        display: block !important;
        margin-bottom: 14px !important;
    }
    .custom-input-heading {
        color: #8E8E93 !important;
        font-size: 10px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.06em !important;
        font-weight: 700 !important;
        margin-bottom: 6px !important;
        margin-top: 12px !important;
        display: block !important;
    }
    
    div[data-testid="stSelectbox"] > div { background-color: #070709 !important; border: 1px solid rgba(255,255,255,0.05) !important; border-radius: 10px !important; }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] { color: white !important; font-size: 13px !important; }
    
    /* Output Data Interface Modals */
    .solution-popup-card { background: #FFFFFF; border-radius: 20px; padding: 20px; margin-top: 12px; box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3); }
    .solution-popup-card.err-border { border-left: 5px solid #FF3B30; }
    .solution-popup-card.obj-border { border-left: 5px solid #5856D6; }
    .solution-popup-card.flow-border { border-left: 5px solid #00CD52; }
    .solution-popup-card.ritual-border { border-left: 5px solid #FF9500; }
    .status-pill { display: inline-block; font-size: 9px; font-weight: 800; letter-spacing: 0.05em; padding: 4px 10px; border-radius: 50px; margin-bottom: 10px; text-transform: uppercase; }
    .status-pill.err-color { background: #FFEBEE; color: #D32F2F; }
    .status-pill.obj-color { background: #E8EAF6; color: #3F51B5; }
    .status-pill.flow-color { background: #E8F9EE; color: #007A31; }
    .status-pill.ritual-color { background: #FFF3E0; color: #E65100; }
    .popup-title { color: #1C1C1E; font-size: 18px; font-weight: 800; margin: 0 0 12px 0; line-height: 1.3; }
    .meta-label { font-size: 10px; color: #71717A; text-transform: uppercase; font-weight: 700; letter-spacing: 0.04em; margin-bottom: 4px; margin-top: 12px; }
    .diagnostic-reason-text { background: #F4F4F5; color: #1C1C1E; padding: 12px 14px; border-radius: 10px; font-size: 13.5px; font-weight: 500; margin-bottom: 8px; line-height: 1.4; }
    .action-steps-box { background: #E8F5E9; border: 1px solid #C8E6C9; border-radius: 10px; padding: 14px; font-size: 13px; }
    
    /* General Utilities */
    .app-brand-tag { font-size: 10px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; color: #8E8E93; margin-bottom: 2px; }
    .app-main-title { font-size: 24px; font-weight: 800; letter-spacing: -0.02em; color: #FFFFFF; margin-bottom: 16px; }
    div.pitch-trigger-box button { background-color: #00CD52 !important; border: none !important; padding: 12px 16px !important; width: 100%; border-radius: 12px !important; }
    div.pitch-trigger-box button p { color: #000000 !important; font-weight: 700 !important; font-size: 13px !important; }
    div.floating-back-container { position: fixed; bottom: 20px; left: 20px; z-index: 9999; }
    div.floating-back-container button { background-color: #1C1C1E !important; border: 1px solid rgba(255,255,255,0.12) !important; border-radius: 30px !important; padding: 6px 14px !important; }
    div.floating-back-container button p { color: #FFFFFF !important; font-size: 10px !important; font-weight: 700; text-transform: uppercase; }
    hr { border-color: rgba(255,255,255,0.05) !important; margin: 12px 0 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. RUNTIME APP ENTRY TRANSITION (CRED SPLASH FLOW)
if not st.session_state.splash_done:
    splash_placeholder = st.empty()
    with splash_placeholder.container():
        st.markdown("""
            <div class="cred-splash-container">
                <div class="cred-splash-logo">PITCH PRO</div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(1.5)
    splash_placeholder.empty()
    st.session_state.splash_done = True

# 4. DATA MATRIX
DATA_FLOW_MATRIX = {
    "Smart Speaker": {
        "Paytm": {
            "points": [
                "Expose the hidden monthly device rentals via the Paytm Business App filter history.",
                "Highlight the current PhonePe special retention discount (₹99/₹149 setup fee).",
                "Contrast Paytm's frustrating online ticket/chatbot support with PhonePe's dedicated Area Sector Incharge."
            ],
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh har mahine ka hidden rental kat raha hai aapka. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (sirf ₹99/₹149 LTV ke hisab se). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota...",
            "audio": "loan_paytm.mp3"
        },
        "BharatPe": {
            "points": ["Leverage the fact that 70% to 80% of local consumers natively use PhonePe."],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se 70% se 80% log PhonePe use karte hain...",
            "audio": "loan_bharatpe.mp3"
        },
        "Google Pay": {
            "points": ["Position the speaker as a gateway to the merchant ecosystem, not just an audio box."],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha...",
            "audio": "loan_gpay.mp3"
        },
        "Banks": {
            "points": ["Expose that bank QRs dump every single transaction directly into the bank account."],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai...",
            "audio": "loan_bank.mp3"
        }
    },
    "Merchant Lending": {
        "Paytm": {
            "points": ["Expose true Annual Percentage Rate (APR) of 36%–37% hidden under processing blocks."],
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye...",
            "audio": "loan_paytm.mp3"
        },
        "BharatPe": {
            "points": ["Pitch PhonePe's 'Continuous Eligibility' model allowing active Top-Ups without full closure."],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko 'Continuous Eligibility' deta hai...",
            "audio": "loan_bharatpe.mp3"
        },
        "Google Pay": {
            "points": ["Highlight 100% collateral-free, paperless lending backed purely by QR volume."],
            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge...",
            "audio": "loan_gpay.mp3"
        },
        "Banks": {
            "points": ["Detail how bank QRs clutter the main bank ledger with individual micro-transactions."],
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai...",
            "audio": "loan_bank.mp3"
        }
    }
}

TECHNICAL_ERRORS = {
    "pan_mismatch": {"title": "PAN Name Mismatch", "reason": "PAN Card aur Aadhaar Card mein naam alag hai.", "actions": ["Sahi naam update karayen."]},
    "kyc_failed_link": {"title": "KYC Verification Failed", "reason": "PAN aur Aadhaar aapas mein Link nahi hai.", "actions": ["PAN ko Aadhaar se Link karwaen."]}
}

COUNTER_OBJECTIONS = {
    "eligibility": {"title": "Mere paas PhonePe QR hai, par Loan ke liye Eligible kaise banu?", "reason": "Merchant niyamit aur sahi vyavahar badhana aavashyak hai.", "actions": ["Rojana PhonePe QR par payments le."]}
}

# 5. CORE WORKSPACE SURFACE INTERFACES
st.markdown('<div class="active-workspace-surface">', unsafe_allow_html=True)
st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Pitch Pro Terminal</div>', unsafe_allow_html=True)

# Telemetry Matrix Layer (RESTORED TO ORIGINAL 4-COLUMN INLINE DESIGN)
if not st.session_state.selected_module:
    st.markdown("""
        <div class="telemetry-card">
            <div class="app-brand-tag" style="font-size:9px; margin-bottom:10px; color:rgba(255,255,255,0.4);">Territory Market Share Snapshot</div>
            <div class="telemetry-grid">
                <div class="telemetry-item"><div class="telemetry-val leader-color">38.6%</div><div class="telemetry-lbl">🟢 PhonePe</div></div>
                <div class="telemetry-item"><div class="telemetry-val">37.6%</div><div class="telemetry-lbl">Paytm</div></div>
                <div class="telemetry-item"><div class="telemetry-val">9.6%</div><div class="telemetry-lbl">BharatPe</div></div>
                <div class="telemetry-item"><div class="telemetry-val">5.8%</div><div class="telemetry-lbl">GPay</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Proportional Mobile Carousel Grid Generation
carousel_cols = st.columns(4)
modules = ["Smart Speaker", "Merchant Lending", "Gate Meeting Rituals", "Merchant Visit Rituals"]
keys = ["mod_ecb", "mod_lending", "mod_gate", "mod_visit"]

for i, col in enumerate(carousel_cols):
    with col:
        st.markdown(f"""
            <div class="carousel-card-shell">
                <div>
                    <div class="app-brand-tag" style="font-size:8px; color:rgba(255,255,255,0.3);">0{i+1}</div>
                    <div class="carousel-card-title">{modules[i]}</div>
                </div>
        """, unsafe_allow_html=True)
        if st.button("Explore", key=keys[i]): 
            reset_pitch_flow(modules[i])
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("<hr/>", unsafe_allow_html=True)

# 6. DYNAMIC SUB WORKSPACE COMPONENT
if st.session_state.selected_module:
    current_mod = st.session_state.selected_module
    
    if current_mod in ["Smart Speaker", "Merchant Lending"]:
        st.markdown('<div class="app-brand-tag">Playbooks</div>', unsafe_allow_html=True)
        comp_options = ["Select Competitor...", "Paytm", "BharatPe", "Google Pay", "Banks"]
        
        selected_dropdown = st.selectbox(
            "Target Matrix", options=comp_options,
            index=comp_options.index(st.session_state.selected_competitor) if st.session_state.selected_competitor in comp_options else 0,
            key="competitor_dropdown_matrix"
        )
        
        if selected_dropdown != "Select Competitor...":
            st.session_state.selected_competitor = selected_dropdown
            node = DATA_FLOW_MATRIX[current_mod][st.session_state.selected_competitor]
            
            st.markdown(f"""
                <div class="solution-popup-card flow-border">
                    <div class="status-pill flow-color">{st.session_state.selected_competitor} Strategy</div>
                    <div class="popup-title">{current_mod} Key Vectors</div>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""<div class="action-steps-box" style="background:#0F1912; border-color:rgba(0,205,82,0.15); color:#A3E635;">
                {"".join([f"<p style='margin-bottom:6px;'>✅ {pt}</p>" for pt in node["points"]])}
            </div>""", unsafe_allow_html=True)
                
            st.write("")
            st.markdown('<div class="pitch-trigger-box">', unsafe_allow_html=True)
            if st.button(f"Generate Interactive Script", key="generate_pitch_btn"):
                st.session_state.pitch_customized = True
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.session_state.pitch_customized:
                st.markdown(f"""
                    <div class="solution-popup-card flow-border">
                        <div class="meta-label">Merchant Counter Dialogue Script</div>
                        <div class="diagnostic-reason-text" style="background:#13131A; border:1px solid rgba(255,255,255,0.05); color:#E4E4E7;">"{node['pitch']}"</div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.write("")
                st.markdown('<div class="app-brand-tag">🎙️ Audio Reference Stream:</div>', unsafe_allow_html=True)
                base_dir = os.path.dirname(os.path.abspath(__file__))
                try:
                    with open(os.path.join(base_dir, node["audio"]), "rb") as f:
                        st.audio(f.read(), format="audio/mp3")
                except FileNotFoundError:
                    st.warning("Audio feed file synchronization outstanding on remote path.")

    # Floating Mobile Back Controller Action
    st.markdown('<div class="floating-back-container">', unsafe_allow_html=True)
    if st.button("← Dashboard", key="floating_back_nav_action"):
        st.session_state.selected_module = None
        st.session_state.selected_competitor = "Select Competitor..."
        st.session_state.pitch_customized = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 7. ENCLOSED COMMAND DECK TROUBLESHOOTING BOARD
if not st.session_state.selected_module:
    st.markdown("""
        <div class="illuminated-triage-panel">
            <span class="terminal-main-header">⚡ INSTANT TROUBLESHOOTING TERMINAL</span>
    """, unsafe_allow_html=True)

    st.markdown('<span class="custom-input-heading">Troubleshoot Technical Errors</span>', unsafe_allow_html=True)
    selected_err = st.selectbox(
        "Technical Errors", options=["None"] + list(TECHNICAL_ERRORS.keys()),
        format_func=lambda x: "Select Merchant Error..." if x == "None" else TECHNICAL_ERRORS[x]["title"],
        key="tech_errors_aligned_dropdown", label_visibility="collapsed"
    )
    
    st.markdown('<span class="custom-input-heading">Resolve Counter Objections</span>', unsafe_allow_html=True)
    selected_obj = st.selectbox(
        "Counter Objections", options=["None"] + list(COUNTER_OBJECTIONS.keys()),
        format_func=lambda x: "Select Merchant Objection..." if x == "None" else COUNTER_OBJECTIONS[x]["title"],
        key="counter_objections_aligned_dropdown", label_visibility="collapsed"
    )
    
    st.markdown('</div>', unsafe_allow_html=True) # Closes card wrapper cleanly around dropdown targets
    
    if selected_err != "None":
        node = TECHNICAL_ERRORS[selected_err]
        actions_html = "".join([f"<li>{act}</li>" for act in node["actions"]])
        st.markdown(f"""
            <div class="solution-popup-card err-border">
                <div class="status-pill err-color">Diagnostic</div>
                <div class="popup-title">{node['title']}</div>
                <div class="diagnostic-reason-text">{node['reason']}</div>
                <div class="action-steps-box" style="background:#1A0F11; color:#FCA5A5; border-color:rgba(239,68,68,0.15);"><ul>{actions_html}</ul></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif selected_obj != "None":
        node = COUNTER_OBJECTIONS[selected_obj]
        actions_html = "".join([f"<li>{act}</li>" for act in node["actions"]])
        st.markdown(f"""
            <div class="solution-popup-card obj-border">
                <div class="status-pill obj-color">Resolution</div>
                <div class="popup-title">{node['title']}</div>
                <div class="diagnostic-reason-text">{node['reason']}</div>
                <div class="action-steps-box" style="background:#111322; color:#C7D2FE; border-color:rgba(99,102,241,0.15);"><ul>{actions_html}</ul></div>
            </div>
        """, unsafe_allow_html=True)
