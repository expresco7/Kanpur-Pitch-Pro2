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
if "pitch_customized" not in st.session_state:
    st.session_state.pitch_customized = False
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

# Reset view metrics when toggling between operational nodes
def reset_pitch_flow(target_module):
    st.session_state.selected_module = target_module
    st.session_state.pitch_customized = False
    st.rerun()

# 2. DESIGN SYSTEM & SLIDING ENGINE
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
        background: #050507; z-index: 99999;
        display: flex; flex-direction: column;
        justify-content: center; align-items: center;
    }
    .cred-splash-logo { font-size: 42px; font-weight: 900; color: #FFFFFF; }
    
    .app-brand-tag { font-size: 10px; font-weight: 700; letter-spacing: 0.15em; text-transform: uppercase; color: #8E8E93; margin-bottom: 8px; }
    .app-main-title { font-size: 24px; font-weight: 800; color: #FFFFFF; margin-bottom: 20px; }
    
    /* Horizontal Slider Pattern */
    .slider-container {
        display: flex;
        overflow-x: auto;
        gap: 12px;
        padding-bottom: 20px;
        scrollbar-width: none;
    }
    .slider-container::-webkit-scrollbar { display: none; }
    
    /* Market Share Panel */
    .market-share-box {
        background: #1C1C1E; border-radius: 20px; padding: 20px; margin-bottom: 24px;
        display: flex; flex-direction: column; gap: 10px;
    }
    .market-stats { display: flex; justify-content: space-between; }
    .stat-item { text-align: center; }
    .stat-val { font-size: 16px; font-weight: 800; color: #00CD52; }
    .stat-lbl { font-size: 9px; color: #8E8E93; text-transform: uppercase; }

    /* Button/Slider Styling */
    div.stButton > button {
        background-color: #121214 !important; border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 20px !important; padding: 20px !important;
        height: 100px !important; width: 140px !important;
        display: flex !important; flex-direction: column !important;
        justify-content: center !important; align-items: center !important;
    }
    
    .solution-popup-card { background: #FFFFFF; border-radius: 24px; padding: 24px; margin-top: 16px; }
    .popup-title { color: #1C1C1E; font-size: 20px; font-weight: 800; margin-bottom: 12px; }
    .status-pill { background: #E8F9EE; color: #007A31; padding: 4px 10px; border-radius: 20px; font-size: 10px; font-weight: 800; margin-bottom: 10px; display: inline-block; }
    .action-steps-box { background: #F4F4F5; border-radius: 14px; padding: 16px; margin-top: 10px; color: #1C1C1E; }
    </style>
""", unsafe_allow_html=True)

# 3. SPLASH SCREEN
if not st.session_state.splash_done:
    st.markdown('<div class="cred-splash-container"><div class="cred-splash-logo">PITCH PRO</div></div>', unsafe_allow_html=True)
    time.sleep(1.5)
    st.session_state.splash_done = True
    st.rerun()

# 4. DATA
DATA_FLOW_MATRIX = {
    "Smart Speaker": {
        "Paytm": {"points": ["Expose hidden rental fees.", "Highlight retention discount.", "Contrast bot support vs local Incharge."], "pitch": "Bhaiya, check your Soundbox history for hidden rentals. PhonePe gives you dedicated local support, no chat bots."},
        "BharatPe": {"points": ["70%+ native PhonePe users.", "Delayed settlements on 3rd party QR.", "Local support network."], "pitch": "70% of your customers use PhonePe. Don't delay settlements using other QRs. We have dedicated local Incharges."},
        "Google Pay": {"points": ["Gateway to lending ecosystem.", "No local human architecture."], "pitch": "GPay is just a box. Our Smart Speaker unlocks business loans and keeps your shop priority in our system."},
        "Banks": {"points": ["Unified single settlement.", "No tedious passbook entries."], "pitch": "Bank QRs clutter your ledger with 100s of entries. PhonePe gives you a single daily settlement."}
    },
    "Merchant Lending": {
        "Paytm": {"points": ["Expose 36%+ APR.", "Clear 1.25% rates."], "pitch": "Paytm's APR often hits 36% with hidden fees. PhonePe offers transparent 1.25% rates."},
        "BharatPe": {"points": ["Continuous Eligibility.", "Fast top-ups."], "pitch": "We offer Continuous Eligibility for top-ups, unlike rigid models."}
    }
}

# 5. UI COMPONENTS
st.markdown('<div class="app-brand-tag">Kanpur Division</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Pitch Pro</div>', unsafe_allow_html=True)

# Landing Page Market Share (Disappears if module selected)
if not st.session_state.selected_module:
    st.markdown("""
        <div class="market-share-box">
            <div class="app-brand-tag">Territory Market Share</div>
            <div class="market-stats">
                <div class="stat-item"><div class="stat-val">38.6%</div><div class="stat-lbl">PhonePe</div></div>
                <div class="stat-item"><div class="stat-val">37.6%</div><div class="stat-lbl">Paytm</div></div>
                <div class="stat-item"><div class="stat-val">9.6%</div><div class="stat-lbl">BharatPe</div></div>
                <div class="stat-item"><div class="stat-val">5.8%</div><div class="stat-lbl">Google</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Horizontal Sliding Modules
st.markdown('<div class="slider-container">', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("ECB"): reset_pitch_flow("Smart Speaker")
with c2:
    if st.button("LENDING"): reset_pitch_flow("Merchant Lending")
with c3:
    if st.button("GATE"): reset_pitch_flow("Gate Meeting Rituals")
with c4:
    if st.button("VISIT"): reset_pitch_flow("Merchant Visit Rituals")
st.markdown('</div>', unsafe_allow_html=True)

# Drill-down logic
if st.session_state.selected_module:
    if st.button("← Back to Dashboard"): 
        st.session_state.selected_module = None
        st.rerun()

    current_mod = st.session_state.selected_module
    
    if current_mod in ["Smart Speaker", "Merchant Lending"]:
        comp = st.selectbox("Select Target Competition:", ["Paytm", "BharatPe", "Google Pay", "Banks"])
        node = DATA_FLOW_MATRIX[current_mod].get(comp)
        
        if node:
            st.markdown(f"""
                <div class="solution-popup-card">
                    <div class="status-pill">STRATEGY: {comp.upper()}</div>
                    <div class="popup-title">{current_mod} Strategy</div>
                    <div class="action-steps-box">{''.join([f'<li>{p}</li>' for p in node['points']])}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Generate Pitch"): st.session_state.pitch_customized = True
            if st.session_state.pitch_customized:
                st.write(node['pitch'])

    elif current_mod == "Gate Meeting Rituals":
        st.markdown('<div class="solution-popup-card"><h3>10 KA DUM</h3><p>Gate meeting routines including attendance, grooming, and SKH.</p></div>', unsafe_allow_html=True)

    elif current_mod == "Merchant Visit Rituals":
        st.markdown('<div class="solution-popup-card"><h3>5 KA PUNCH</h3><p>Deployment checklist and journey audit.</p></div>', unsafe_allow_html=True)
