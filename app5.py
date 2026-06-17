import streamlit as st
import time

# 1. STRUCTURAL PAGE LAYOUT SETUP
st.set_page_config(
    page_title="Lending Army Terminal",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Parse active module from URL query parameters to support pure HTML scrolling card click actions
query_params = st.query_params
if "mod" in query_params:
    st.session_state.selected_module = query_params["mod"]

# Active state session management variables
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "selected_competitor" not in st.session_state:
    st.session_state.selected_competitor = "None"
if "pitch_customized" not in st.session_state:
    st.session_state.pitch_customized = False
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

# Reset view metrics when toggling between operational nodes
def reset_pitch_flow(target_module):
    st.query_params["mod"] = target_module
    st.session_state.selected_module = target_module
    st.session_state.selected_competitor = "None"
    st.session_state.pitch_customized = False
    st.rerun()

# 2. PREMIUM CRED DESIGN SYSTEM & ULTRATESTED SLIDING ENGINE
st.markdown("""
    <style>
    /* Base Engine UI Configuration */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0A0A0C !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* Clean Top Header Space Clearances */
    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; }
    
    /* CRED Intro Transition Graphics Engine */
    @keyframes credTracking {
        0% { letter-spacing: -0.2em; opacity: 0; filter: blur(12px); }
        40% { opacity: 1; filter: blur(0px); }
        70% { letter-spacing: 0.15em; opacity: 1; }
        100% { opacity: 0; letter-spacing: 0.2em; filter: blur(4px); }
    }
    
    .cred-splash-container {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        background: #050507;
        z-index: 99999;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .cred-splash-logo {
        font-size: 42px;
        font-weight: 900;
        text-transform: uppercase;
        color: #FFFFFF;
        animation: credTracking 2.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        text-shadow: 0 0 30px rgba(255,255,255,0.2);
    }

    /* Typography & Header Blocks */
    .app-brand-tag {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #8E8E93;
        margin-bottom: 4px;
    }
    .app-main-title {
        font-size: 28px;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #FFFFFF;
        margin-bottom: 24px;
    }

    /* Market Share Analytics Telemetry Panel */
    .telemetry-card {
        background: linear-gradient(135deg, #121216 0%, #1C1C1E 100%);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 28px;
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
        font-size: 20px;
        font-weight: 800;
        color: #FFFFFF;
        letter-spacing: -0.02em;
    }
    .telemetry-val.leader-color {
        color: #00CD52 !important;
        text-shadow: 0 0 10px rgba(0,205,82,0.2);
    }
    .telemetry-lbl {
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #8E8E93;
        margin-top: 2px;
    }
    
    /* ROBUST HORIZONTAL SCROLLING CONTAINER (PURE INJECTED HTML ENGINE) */
    .scrolling-wrapper-surface {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 16px;
        padding: 4px 4px 16px 4px;
        width: 100%;
        -webkit-overflow-scrolling: touch;
    }
    .scrolling-wrapper-surface::-webkit-scrollbar {
        height: 5px;
    }
    .scrolling-wrapper-surface::-webkit-scrollbar-thumb {
        background: rgba(255, 255, 255, 0.15);
        border-radius: 10px;
    }
    
    /* Pure Interactive Native Card Styling Hooks */
    .interactive-slider-card {
        flex: 0 0 auto;
        width: 240px;
        background: #121214;
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 22px;
        padding: 20px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        text-decoration: none !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .interactive-slider-card:hover {
        border-color: rgba(255, 255, 255, 0.25);
        background: #1C1C1E;
        transform: translateY(-2px);
    }
    .interactive-slider-card.card-active {
        border-color: #00CD52 !important;
        background: rgba(0, 205, 82, 0.04) !important;
    }
    .card-mod-tag {
        font-size: 9px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: #8E8E93;
        margin-bottom: 4px;
    }
    .card-mod-title {
        font-size: 16px;
        font-weight: 800;
        color: #FFFFFF;
        margin-bottom: 8px;
    }
    .card-mod-desc {
        font-size: 12px;
        color: #AEAEB2;
        line-height: 1.4;
    }
    
    /* Selection Fields Dropdowns Integration Layout */
    div.stSelectbox > label {
        color: #8E8E93 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 700 !important;
        margin-bottom: 8px;
    }
    div[data-testid="stSelectbox"] > div {
        background-color: #121214 !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 14px !important;
        padding: 4px;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        color: white !important;
        font-weight: 600 !important;
    }
    
    /* Output Blocks Layout Presentation Modals */
    .solution-popup-card {
        background: #FFFFFF;
        border-radius: 24px;
        padding: 26px;
        margin-top: 16px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
    }
    .solution-popup-card.err-border { border-left: 6px solid #FF3B30; }
    .solution-popup-card.flow-border { border-left: 6px solid #00CD52; }
    .solution-popup-card.ritual-border { border-left: 6px solid #FF9500; }
    
    .status-pill {
        display: inline-block;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: 0.05em;
        padding: 5px 12px;
        border-radius: 50px;
        margin-bottom: 14px;
    }
    .status-pill.err-color { background: #FFEBEE; color: #D32F2F; }
    .status-pill.flow-color { background: #E8F9EE; color: #007A31; }
    .status-pill.ritual-color { background: #FFF3E0; color: #E65100; }
    
    .popup-title {
        color: #1C1C1E;
        font-size: 22px;
        font-weight: 800;
        margin: 0 0 16px 0;
    }
    .meta-label {
        font-size: 11px;
        color: #71717A;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.04em;
        margin-bottom: 6px;
        margin-top: 14px;
    }
    .diagnostic-reason-text {
        background: #F4F4F5;
        color: #1C1C1E;
        padding: 14px 16px;
        border-radius: 14px;
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 10px;
    }
    .action-steps-box {
        background: #E8F5E9;
        border: 1px solid #C8E6C9;
        border-radius: 14px;
        padding: 16px;
    }
    
    .ritual-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        color: #1C1C1E;
    }
    .ritual-table th {
        background: #F4F4F5;
        text-align: left;
        padding: 10px;
        font-size: 12px;
        text-transform: uppercase;
        font-weight: 700;
        color: #71717A;
        border-bottom: 2px solid #E4E4E7;
    }
    .ritual-table td {
        padding: 12px 10px;
        font-size: 14px;
        border-bottom: 1px solid #E4E4E7;
        vertical-align: top;
    }
    .ritual-table tr:last-child td { border-bottom: none; }
    .step-highlight { font-weight: 700; color: #000000; }
    
    /* Pitch CTA Accent Button elements */
    div.pitch-trigger-box button {
        background-color: #00CD52 !important;
        border: none !important;
        text-align: center !important;
        min-height: auto !important;
        padding: 14px 20px !important;
        border-radius: 14px !important;
    }
    div.pitch-trigger-box button p {
        color: #000000 !important;
        text-align: center !important;
        font-weight: 700 !important;
        opacity: 1 !important;
    }
    
    hr { border-color: rgba(255,255,255,0.08) !important; margin: 24px 0 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. RUNTIME APP ENTRY TRANSITION (CRED SPLASH FLOW)
if not st.session_state.splash_done:
    splash_placeholder = st.empty()
    with splash_placeholder.container():
        st.markdown("""
            <div class="cred-splash-container">
                <div class="cred-splash-logo">LENDING ARMY</div>
            </div>
        """, unsafe_allow_html=True)
    time.sleep(2.1)
    splash_placeholder.empty()
    st.session_state.splash_done = True

# 4. ACTIVE DATA STRUCTURAL ENTITIES
DATA_FLOW_MATRIX = {
    "Smart Speaker": {
        "Paytm": {
            "points": [
                "Expose hidden monthly device rentals using Paytm Business App filters.",
                "Highlight the current PhonePe special retention setup fee discount (₹99/₹149).",
                "Contrast Paytm's online bot responses with PhonePe's localized Area Sector Incharge framework."
            ],
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh har mahine ka hidden rental kat raha hai aapka. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (sirf ₹99/₹149 LTV ke hisab se). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota. PhonePe par humara system bilkul alag hai. Humne aapke Kanpur ke isi market area mein ek dedicated Sector Incharge bitha rakha hai. Ek call ghumao, humara ladka turant aapki dukaan par hazir hoga."
        },
        "BharatPe": {
            "points": [
                "Leverage the fact that over 70% of local consumers natively handle payments via PhonePe.",
                "Explain how routing transactions through third parties delays primary settlement clearance.",
                "Highlight immediate localized ground support systems."
            ],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se 70% se 80% log PhonePe use karte hain. Jab consumer hi PhonePe ka hai, toh aap BharatPe ke QR par ghumakar settlement kyun delay kar rahe ho? Seedha PhonePe ka Smart Speaker lagao. Customers ke liye bhi frictionless payment hoga aur isi transaction volume ke basis par aapka loan offer bhi raat-o-raat active ho jayega. Rahi baat service ki—toh BharatPe ka na toh koi on-ground aadmi milta hai aur na hi unka support system local hai."
        },
        "Google Pay": {
            "points": [
                "Position the speaker as a gateway to lending products, not just an audio monitor.",
                "Frame GPay as a distant tech platform completely isolated from human service networks."
            ],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha. PhonePe ka Smart Speaker lagane ka matlab hai ki aapka business humare system mein top priority par aa jata hai. Iske lagte hi aapka business loan jald approve ho jata hai. Google Pay ka koi local office ya on-ground team nahi hai Kanpur mein. PhonePe ka hamara local Sector Incharge hamesha aapke area mein round par rehta hai."
        },
        "Banks": {
            "points": [
                "Expose how individual banking entries clutter daily tracking logs and clear statements.",
                "Highlight unified end-of-day single settlement architecture keeping metrics pristine."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook mein 100 entries bhar jayengi. PhonePe par aisa kachra nahi hota! Hum din bhar ka poora collection ek sath, single settlement mein aapke bank mein bhejte hain, jisse har din ka dhandha track karna bilkul aasan ho jata hai."
        }
    },
    "Merchant Lending": {
        "Paytm": {
            "points": [
                "Expose true structural processing fees making actual APR metrics spike to 36%-37%.",
                "Offer clean direct interest tracking paths at 1.25%-1.5% transparency thresholds."
            ],
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye. Hidden charges, processing fees aur GST milakar saal ka 36% se 37% tak baithta hai. Ek baar PhonePe ka loan banner check kariye, hum aapko pehli dafa mein hi 1.25% se 1.5% ke clear interest rate par loan de rahe hain. Koi hidden jhamela nahi hai."
        },
        "BharatPe": {
            "points": [
                "Introduce the Continuous Eligibility model backing fast Top-Ups without rigid final lockouts.",
                "Guarantee faster repeat access tracks upon active closure cycles."
            ],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko 'Continuous Eligibility' deta hai. Iska matlab yeh hai ki agar aapka loan chal raha hai aur aapko beech mein paise ki zaroorat padi, toh aapko live Top-Up ka option mil jata hai. Aur jaise hi aap purana loan close karte ho, within 1 week aapko naya repeat loan ka banner mil jata hai."
        }
    }
}

# 5. CORE ACTIVE WORKSPACE SURFACE INTERFACE
st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Lending Army Active Workspace</div>', unsafe_allow_html=True)

# THE LANDING TELEMETRY PANEL
if not st.session_state.selected_module:
    st.markdown("""
        <div class="telemetry-card">
            <div class="app-brand-tag" style="font-size:10px; margin-bottom:12px; color:rgba(255,255,255,0.4);">Territory Market Share Snapshot</div>
            <div class="telemetry-grid">
                <div class="telemetry-item"><div class="telemetry-val leader-color">38.6%</div><div class="telemetry-lbl">🟢 PhonePe</div></div>
                <div class="telemetry-item"><div class="telemetry-val">37.6%</div><div class="telemetry-lbl">Paytm</div></div>
                <div class="telemetry-item"><div class="telemetry-val">9.6%</div><div class="telemetry-lbl">BharatPe</div></div>
                <div class="telemetry-item"><div class="telemetry-val">5.8%</div><div class="telemetry-lbl">Google Pay</div></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# 6. FIXED REBUILT HORIZONTAL SLIDING MODULES ENGINE (TRUE SCROLLABLE INTERFACE)
mod_1_class = "card-active" if st.session_state.selected_module == "Smart Speaker" else ""
mod_2_class = "card-active" if st.session_state.selected_module == "Merchant Lending" else ""
mod_3_class = "card-active" if st.session_state.selected_module == "Gate Meeting Rituals" else ""
mod_4_class = "card-active" if st.session_state.selected_module == "Merchant Visit Rituals" else ""

st.markdown(f"""
    <div class="scrolling-wrapper-surface">
        <a href="?mod=Smart+Speaker" target="_self" class="interactive-slider-card {mod_1_class}">
            <div>
                <div class="card-mod-tag">Module 01</div>
                <div class="card-mod-title">ECB</div>
            </div>
            <div class="card-mod-desc">Smart Speaker deployments and counter metrics.</div>
        </a>
        <a href="?mod=Merchant+Lending" target="_self" class="interactive-slider-card {mod_2_class}">
            <div>
                <div class="card-mod-tag">Module 02</div>
                <div class="card-mod-title">Lending</div>
            </div>
            <div class="card-mod-desc">Merchant evaluation profiles and pitches.</div>
        </a>
        <a href="?mod=Gate+Meeting+Rituals" target="_self" class="interactive-slider-card {mod_3_class}">
            <div>
                <div class="card-mod-tag">Module 03</div>
                <div class="card-mod-title">Objections</div>
            </div>
            <div class="card-mod-desc">Dynamic on-counter merchant queries.</div>
        </a>
        <a href="?mod=Merchant+Visit+Rituals" target="_self" class="interactive-slider-card {mod_4_class}">
            <div>
                <div class="card-mod-tag">Module 04</div>
                <div class="card-mod-title">Visits</div>
            </div>
            <div class="card-mod-desc">Merchant field visit roadmaps and criteria list.</div>
        </a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 7. TOTAL REBUILD: CLEAN COMPETITOR SELECTION FLOW FROM DROPDOWN (NO LOGOS)
if st.session_state.selected_module:
    current_mod = st.session_state.selected_module
    
    if current_mod in ["Smart Speaker", "Merchant Lending"]:
        st.markdown('<hr/>', unsafe_allow_html=True)
        st.markdown('<div class="app-brand-tag" style="margin-bottom:2px;">COMPETITOR PROFILE SELECTION:</div>', unsafe_allow_html=True)
        
        # Pulling back clean drop down option parameters
        competitor_options = ["None", "Paytm", "BharatPe", "Google Pay", "Banks"]
        
        # Ensure selected index updates perfectly based on state logs
        current_index = competitor_options.index(st.session_state.selected_competitor) if st.session_state.selected_competitor in competitor_options else 0
        
        selected_comp = st.selectbox(
            "Choose Target Competitor Counter Agent to Audit",
            options=competitor_options,
            index=current_index,
            key="competitor_dropdown_selector"
        )
        
        # Sync selection state instantly to prevent state drift errors
        if selected_comp != st.session_state.selected_competitor:
            st.session_state.selected_competitor = selected_comp
            st.session_state.pitch_customized = False
            st.rerun()
            
        if selected_comp != "None":
            # Guard checking array safety levels
            if selected_comp in DATA_FLOW_MATRIX[current_mod]:
                node = DATA_FLOW_MATRIX[current_mod][selected_comp]
                
                st.markdown(f"""
                    <div class="solution-popup-card flow-border" style="margin-top:20px;">
                        <div class="status-pill flow-color">COMPETITIVE FIELD MATRIX: {selected_comp.upper()}</div>
                        <div class="popup-title">{current_mod} Strategy vs {selected_comp}</div>
                        <div class="meta-label">Counter Tactical Attack Points / मुख्य बातें</div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown(
                    f"""<div class="action-steps-box" style="background: #F0FDF4; border-color: #DCFCE7; border-radius:14px; padding:16px; margin-top:-10px;">
                        <ul style="list-style: none; padding: 0; margin: 0;">
                            {"".join([f"<li style='color: #1B5E20; font-size:14px; margin-bottom:8px;'>✅ {pt}</li>" for pt in node["points"]])}
                        </ul>
                    </div>""", 
                    unsafe_allow_html=True
                )
                    
                st.write("")
                st.markdown('<div class="pitch-trigger-box">', unsafe_allow_html=True)
                if st.button(f"Generate Live Localized Pitch Script vs {selected_comp}", key="generate_pitch_btn"):
                    st.session_state.pitch_customized = True
                st.markdown('</div>', unsafe_allow_html=True)
                
                if st.session_state.pitch_customized:
                    st.markdown(f"""
                        <div class="solution-popup-card flow-border" style="margin-top:16px;">
                            <div class="meta-label" style="margin-top:0px;">Hinglish Counter Pitch / मर्चेंट को क्या समझाएं</div>
                            <div class="diagnostic-reason-text" style="background: #FAFAFA; border: 1px solid #E4E4E7; line-height:1.5; font-size:14.5px; color:#1C1C1E; font-weight:400;">
                                "{node['pitch']}"
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info(f"Strategy template for {selected_comp} under {current_mod} is currently being compiled.")

    # MODULE ROUTINES METRICS
    elif current_mod == "Gate Meeting Rituals":
        st.markdown("""
            <div class="solution-popup-card ritual-border">
                <div class="status-pill ritual-color">GATE MEETING GUIDELINES</div>
                <div class="popup-title">10 KA DUM TEAM MANAGEMENT</div>
                <table class="ritual-table">
                    <tr><th>Gate Meeting Checklist</th><th>Operational Description Breakdown</th></tr>
                    <tr><td><span class="step-highlight">1. Attendance</span></td><td>1-QR Code Scan Check<br>2-Selfie verification logs<br>3-Submit daily track log.</td></tr>
                    <tr><td><span class="step-highlight">2. Team Grooming</span></td><td>Dress code parameters check.</td></tr>
                </table>
            </div>
        """, unsafe_allow_html=True)

    elif current_mod == "Merchant Visit Rituals":
        st.markdown("""
            <div class="solution-popup-card ritual-border">
                <div class="status-pill ritual-color">VISITATION CHECKLIST</div>
                <div class="popup-title">5 KA PUNCH AUDIT CYCLE</div>
                <table class="ritual-table">
                    <tr><th>Step Node</th><th>Objective Summary</th></tr>
                    <tr><td><span class="step-highlight">Step 1</span></td><td>QR Deployment & Test Transaction validation.</td></tr>
                    <tr><td><span class="step-highlight">Step 2</span></td><td>Identify active competitive layouts on site.</td></tr>
                </table>
            </div>
        """, unsafe_allow_html=True)
