import streamlit as st
import time

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

# 2. CRED DESIGN SYSTEM & HIGH-CONTRAST INTERACTION ENGINE
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0A0A0C !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; }
    
    .cred-splash-container {
        position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
        background: #050507; z-index: 99999; display: flex; flex-direction: column;
        justify-content: center; align-items: center;
    }
    .cred-splash-logo {
        font-size: 42px; font-weight: 900; text-transform: uppercase; color: #FFFFFF;
    }
    .app-brand-tag { font-size: 11px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #8E8E93; margin-bottom: 4px; }
    .app-main-title { font-size: 26px; font-weight: 800; letter-spacing: -0.02em; color: #FFFFFF; margin-bottom: 24px; }
    
    .telemetry-card {
        background: linear-gradient(135deg, #121216 0%, #1C1C1E 100%);
        border: 1px solid rgba(255,255,255,0.06); border-radius: 20px; padding: 20px; margin-bottom: 28px;
    }
    .telemetry-grid { display: flex; justify-content: space-between; align-items: center; }
    .telemetry-item { text-align: center; flex: 1; border-right: 1px solid rgba(255,255,255,0.08); }
    .telemetry-item:last-child { border-right: none; }
    .telemetry-val { font-size: 20px; font-weight: 800; color: #FFFFFF; }
    .leader-color { color: #00CD52 !important; }
    .telemetry-lbl { font-size: 10px; font-weight: 700; text-transform: uppercase; color: #8E8E93; margin-top: 2px; }
    
    div.stButton > button {
        background-color: #1C1C1E !important; border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 18px !important; padding: 20px !important; text-align: left !important; width: 100% !important;
    }
    .solution-popup-card { background: #FFFFFF; border-radius: 24px; padding: 26px; margin-top: 16px; }
    .flow-border { border-left: 6px solid #00CD52; }
    .status-pill { display: inline-block; font-size: 10px; font-weight: 800; padding: 5px 12px; border-radius: 50px; margin-bottom: 14px; background: #E8F9EE; color: #007A31; }
    .popup-title { color: #1C1C1E; font-size: 20px; font-weight: 800; margin: 0 0 16px 0; }
    .meta-label { font-size: 11px; color: #71717A; text-transform: uppercase; font-weight: 700; margin-bottom: 6px; }
    .diagnostic-reason-text { background: #F4F4F5; color: #1C1C1E; padding: 14px 16px; border-radius: 14px; font-size: 14px; }
    .action-steps-box { background: #E8F5E9; border: 1px solid #C8E6C9; border-radius: 14px; padding: 16px; }
    </style>
""", unsafe_allow_html=True)

# 3. SPLASH SCREEN
if not st.session_state.splash_done:
    st.markdown('<div class="cred-splash-container"><div class="cred-splash-logo">PITCH PRO</div></div>', unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# 4. DATA
DATA_FLOW_MATRIX = {
    "Smart Speaker": {
        "Paytm": {"points": ["Hidden monthly rentals", "PhonePe setup discount", "Local Area Incharge support"], "pitch": "Bhaiya, Paytm ka hidden rental kat raha hai. PhonePe par humara local Incharge har waqt service ke liye available hai!"},
        "BharatPe": {"points": ["70-80% PhonePe users", "No local support", "Faster settlement"], "pitch": "Consumer PhonePe ka hai, toh settlement delay kyun? Seedha PhonePe Smart Speaker lagao aur local team ka bharosa pao."},
        "Google Pay": {"points": ["No local office", "No human service", "Lending priority"], "pitch": "GPay speaker sirf ek box hai. PhonePe lagane par loan eligibility aur shop priority milti hai."},
        "Banks": {"points": ["Daily ledger clutter", "Unified settlement"], "pitch": "Bank QR passbook mein kachra bhar dete hain. PhonePe ka single daily settlement ledger ko clean rakhta hai."}
    },
    "Merchant Lending": {
        "Paytm": {"points": ["High hidden APR", "Transparent interest"], "pitch": "Paytm ka hidden interest 36% padta hai. PhonePe deta hai 1.25% se 1.5% clear rate."},
        "BharatPe": {"points": ["Continuous Eligibility", "Fast top-ups"], "pitch": "PhonePe 'Continuous Eligibility' deta hai. Loan chalu rehte bhi top-up lo, koi jhamela nahi."}
    }
}

# 5. UI
st.markdown('<div class="app-brand-tag">Kanpur Division</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Pitch Pro</div>', unsafe_allow_html=True)

if not st.session_state.selected_module:
    st.markdown("""
        <div class="telemetry-card">
            <div class="telemetry-grid">
                <div class="telemetry-item"><div class="telemetry-val leader-color">38.6%</div><div class="telemetry-lbl">PhonePe</div></div>
                <div class="telemetry-item"><div class="telemetry-val">37.6%</div><div class="telemetry-lbl">Paytm</div></div>
                <div class="telemetry-item"><div class="telemetry-val">9.6%</div><div class="telemetry-lbl">BharatPe</div></div>
                <div class="telemetry-item"><div class="telemetry-val">5.8%</div><div class="telemetry-lbl">Google</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ECB\nSpeaker Config"): reset_pitch_flow("Smart Speaker")
        if st.button("GATE\nMeeting Rituals"): reset_pitch_flow("Gate Meeting Rituals")
    with col2:
        if st.button("LENDING\nEvaluation Profiles"): reset_pitch_flow("Merchant Lending")
        if st.button("VISIT\nDeployment Guide"): reset_pitch_flow("Merchant Visit Rituals")

else:
    if st.button("← Back to Dashboard"):
        st.session_state.selected_module = None
        st.rerun()
    
    mod = st.session_state.selected_module
    if mod in ["Smart Speaker", "Merchant Lending"]:
        comp = st.selectbox("Select Competition", ["Select Competitor...", "Paytm", "BharatPe", "Google Pay", "Banks"])
        if comp != "Select Competitor...":
            node = DATA_FLOW_MATRIX[mod][comp]
            st.markdown(f'<div class="solution-popup-card flow-border"><div class="status-pill">{comp.upper()} PLAYBOOK</div><div class="popup-title">{mod} Strategy</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="action-steps-box"><ul>{"".join([f"<li>{p}</li>" for p in node["points"]])}</ul></div>', unsafe_allow_html=True)
            
            if st.button("Generate Custom Pitch", use_container_width=True): st.session_state.pitch_customized = True
            if st.session_state.pitch_customized:
                st.markdown(f'<div class="meta-label">Hinglish Pitch</div><div class="diagnostic-reason-text">{node["pitch"]}</div>', unsafe_allow_html=True)
