import streamlit as st

# 1. PAGE LAYOUT CONFIGURATION
st.set_page_config(
    page_title="Lending Army Terminal",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Initialize Session State tracking variables to remember user clicks
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "selected_competitor" not in st.session_state:
    st.session_state.selected_competitor = None

# 2. PREMIUM DARK MODE DESIGN SYSTEM (COLORS & FONTS)
st.markdown("""
    <style>
    /* Global Background Adjustments */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0A0A0C !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* Clean Hide Default Elements */
    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; }
    
    /* Custom Header Typography */
    .app-brand-tag {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #8E8E93;
        margin-bottom: 4px;
    }
    .app-main-title {
        font-size: 26px;
        font-weight: 800;
        letter-spacing: -0.02em;
        color: #FFFFFF;
        margin-bottom: 24px;
    }
    
    /* Horizontal Swipe Layout (Carousel Container) */
    .swipe-container {
        display: flex;
        gap: 16px;
        overflow-x: auto;
        padding: 4px 4px 20px 4px;
        scroll-snap-type: x mandatory;
        -webkit-overflow-scrolling: touch;
    }
    .swipe-container::-webkit-scrollbar { display: none; }
    
    /* Native Dropdown Element Overrides */
    div.stSelectbox > label {
        color: #8E8E93 !important;
        font-size: 11px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.05em !important;
        font-weight: 700 !important;
        margin-bottom: 8px;
    }
    div[data-testid="stSelectbox"] > div {
        background-color: #1C1C1E !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 14px !important;
        color: #FFFFFF !important;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        color: white !important;
    }
    
    /* Spring Animated Interactive Solution Cards */
    @keyframes springPop {
        0% { transform: scale(0.95) translateY(20px); opacity: 0; }
        100% { transform: scale(1) translateY(0); opacity: 1; }
    }
    .solution-popup-card {
        background: #FFFFFF;
        border-radius: 28px;
        padding: 26px;
        margin-top: 12px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        animation: springPop 0.45s cubic-bezier(0.175, 0.885, 0.32, 1.15) forwards;
    }
    .solution-popup-card.err-border { border-left: 6px solid #FF3B30; }
    .solution-popup-card.obj-border { border-left: 6px solid #5856D6; }
    .solution-popup-card.pitch-border { border-left: 6px solid #00CD52; }
    
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
    .status-pill.obj-color { background: #E8EAF6; color: #3F51B5; }
    .status-pill.pitch-color { background: #E8F9EE; color: #007A31; }
    
    .popup-title {
        color: #1C1C1E;
        font-size: 22px;
        font-weight: 800;
        margin: 0 0 16px 0;
    }
    .meta-label {
        font-size: 11px;
        color: #A1A1AA;
        text-transform: uppercase;
        font-weight: 700;
        letter-spacing: 0.04em;
        margin-bottom: 6px;
    }
    .diagnostic-reason-text {
        background: #F4F4F5;
        color: #1C1C1E;
        padding: 14px 16px;
        border-radius: 14px;
        font-size: 15px;
        font-weight: 500;
        margin-bottom: 20px;
    }
    .action-steps-box {
        background: #E8F5E9;
        border: 1px solid #C8E6C9;
        border-radius: 14px;
        padding: 16px;
    }
    .action-steps-box ul { list-style: none; padding: 0; margin: 0; }
    .action-steps-box li {
        color: #1B5E20;
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 10px;
        display: flex;
        align-items: flex-start;
    }
    .action-steps-box li:last-child { margin-bottom: 0; }
    .check-icon { color: #4CAF50; font-weight: 900; margin-right: 10px; }
    
    hr { border-color: rgba(255,255,255,0.08) !important; margin: 24px 0 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. TECHNICAL & OBJECTIONS MASTER DATA MATRIX
LOAN_ERRORS_DATA = {
    "pan_mismatch": {"title": "PAN Name Mismatch", "reason": "PAN Card और Aadhaar Card में नाम अलग है।", "actions": ["सही नाम अपडेट कराएं।", "PAN में नाम सुधारकर फिर से KYC करें।"]},
    "kyc_link_failed": {"title": "KYC Verification Failed", "reason": "PAN और Aadhaar आपस में Link नहीं है।", "actions": ["PAN को Aadhaar से Link करवाएं।", "Link होने के बाद 24 घंटे बाद Retry करें।"]},
    "kyc_incomplete": {"title": "Unable to Verify Your KYC", "reason": "KYC Process बीच में रुक गया / पूरा नहीं हो पाया।", "actions": ["कुछ समय (TAT) इंतजार करें।", "TAT पूरा होने के बाद भी Issue रहे तो War Room में Raise करें।"]},
    "face_match_failed": {"title": "Face Match Failed", "reason": "Selfie और Aadhaar/PAN Photo Match नहीं हुई।", "actions": ["Bright Light में Clear Selfie लें।", "चश्मा/कैप हटाकर Try करें।"]},
    "kyc_failed": {"title": "KYC Failed", "reason": "दी गई Details Verification Document से Match नहीं हुई।", "actions": ["दी गई जानकारी सही भरें।", "यह Terminal Error है - Next Merchant पर Move करें।"]},
    "digilocker_error": {"title": "DigiLocker Error", "reason": "UIDAI/DigiLocker की तरफ से Technical Issue है।", "actions": ["2 घंटे Wait करें और फिर से Try करें।"]},
    "unable_to_process": {"title": "Unable to Process Request", "reason": "System/Server Problem या Lending Partner की तरफ से Temporary Issue है।", "actions": ["कुछ समय बाद Retry करें।"]},
    "enacht_failed": {"title": "Unable to Process Your E-NACH Mandate", "reason": "Bank Details, IFSC, Account Type या E-NACH Consent में Problem है।", "actions": ["Bank Details दोबारा Check करें।", "सही Account Type (Savings) और IFSC चुनें।"]},
    "upi_mandate_error": {"title": "UPI Mandate Setup Failed", "reason": "UPI ID या Bank से Mandate Setup नहीं हो पाया।", "actions": ["UPI ID Active और Same Bank की हो।", "Bank App में Mandate Approve करें।"]},
    "disbursement_fail": {"title": "Loan Disbursement Failed", "reason": "Bank Account, IFSC, KYC या System Issue के कारण Disbursement नहीं हो पाया।", "actions": ["Bank Details और IFSC Verify करें।", "Issue रहे तो War Room में Raise करें।"]}
}

OBJECTIONS_DATA = {
    "eligibility": {"title": "PhonePe QR है, पर Loan के लिए Eligible कैसे बनूँ?", "reason": "मर्चेंट द्वारा नियमित व्यवहार बढ़ाना आवश्यक है।", "actions": ["रोजाना PhonePe QR पर ज्यादा से ज्यादा UPI Payments लें।", "आपकी लगातार Transaction History ही आपको Loan के लिए Eligible बनाती है।"]},
    "higher_offer": {"title": "मुझे Higher Loan Offer कैसे मिलेगा?", "reason": "लोन की राशि मुख्य रूप से लेनदेन और सिबिल पर आधारित है।", "actions": ["Loan Amount मुख्य रूप से आपके PhonePe QR Transactions और CIBIL Score पर निर्भर करता है।", "समय पर EDI Repayment करने से आपका CIBIL सुधरता है।"]},
    "missed_edi": {"title": "अगर मैं EDI Miss कर दूँ तो क्या होगा?", "reason": "विलंब से सिबिल स्कोर और भावी पात्रता प्रभावित होती है।", "actions": ["हम E-NACH के माध्यम से Auto-Debit कर सकते हैं।", "बार-बार Default करने से आपका CIBIL Score खराब होता है।"]},
    "banner_rejection": {"title": "Loan Banner दिखा, फिर भी मेरा Loan Reject क्यों हो गया?", "reason": "अंतिम स्वीकृति लेंडिंग पार्टनर के आंतरिक मापदंडों पर टिकी है।", "actions": ["Loan Offer Eligibility आपकी Activity के आधार पर होती है, पर Final Approval Lending Partner देता है।", "QR Usage जारी रखें और CIBIL सुधारें।"]},
    "differential_amt": {"title": "दूसरे Merchant को मुझसे ज्यादा Loan Amount क्यों ऑफर हुआ?", "reason": "मूल्यांकन प्रत्येक व्यवसाय के 20+ अलग मानदंडों पर किया जाता है।", "actions": ["Lending Company आपके Business को करीब 20 अलग-अलग Parameters पर Evaluate करती है।", "जैसे: Transaction Volume, Consistency, Business Vintage आदि।"]},
    "benefit_pitch": {"title": "Loan लेने का मेरे लिए क्या फायदा है?", "reason": "व्यवसाय विस्तार और सिबिल स्कोर में सुधार की सीधी सहायता।", "actions": ["Loan से आप Inventory बढ़ा सकते हैं, Business Expand कर सकते हैं।", "समय पर Repayment करने से CIBIL Score Improve होता है।"]},
    "edi_vs_emi": {"title": "मैं EMI की बजाय EDI क्यों लूँ?", "reason": "व्यवसाय के कैशफ्लो पर बिना दबाव डाले आसान दैनिक अदायगी।", "actions": ["EMI में हर महीने बड़ी Fixed Amount देनी पड़ती है।", "EDI में आपकी Daily Sales से छोटी-छोटी Amount कटती है, जिससे Repayment आसान हो जाता है।"]}
}

COMPETITION_PITCH_DATA = {
    "BharatPe": {
        "points": ["No daily auto-debit friction setup like BharatPe.", "PhonePe offers clear settlement logs right inside the app.", "Lower hidden processing fees compared to competitor models."],
        "script": "Sir, BharatPe me settlement delays aur internal hidden charges ka issue rehta hai. PhonePe Merchant Loan me aapko pure clear settlement breakdown milte hain aur instant clear payout hota hai bina kisi extra platform fees ke!",
    },
    "Paytm": {
        "points": ["Zero subscription soundbox bundle locks.", "Direct processing through top trusted lending public partners.", "Flexible daily EDI collection based on running transactional health metrics."],
        "script": "Sir, Paytm ka model setup fix rules pe chalta hai jahan sales kam hone par bhi stress badhta hai. PhonePe ka EDI system aapki running business account capability ke hisab se balanced hai, jisse workload bilkul nahi banta!"
    }
}

# 4. APP BRAND SURFACE HEADERS
st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Lending Army Active Workspace</div>', unsafe_allow_html=True)

# 5. STREAMLIT-NATIVE INTERACTIVE MODULE CAROUSEL (Replaces raw HTML buttons for click detection)
cols = st.columns(2)

with cols[0]:
    ecb_clicked = st.button("📊 MODULE 01: ECB", use_container_width=True)
    if ecb_clicked:
        st.session_state.selected_module = "ECB"

with cols[1]:
    lending_clicked = st.button("💼 MODULE 02: LENDING", use_container_width=True)
    if lending_clicked:
        st.session_state.selected_module = "LENDING"

st.markdown("<hr/>", unsafe_allow_html=True)

# 6. EXECUTING DYNAMIC LENDING COMPETITION FLOW
if st.session_state.selected_module == "LENDING":
    st.markdown('<div class="meta-label">Selected Focus: Merchant Pitching Guide</div>', unsafe_allow_html=True)
    
    # Choose Competitor Selector Dropdown
    competitor_choice = st.selectbox(
        "Choose Your On-Ground Competition:",
        options=["Select Competitor...", "BharatPe", "Paytm"]
    )
    
    if competitor_choice != "Select Competitor...":
        pitch_node = COMPETITION_PITCH_DATA[competitor_choice]
        points_html = "".join([f"<li><span class='check-icon'>✓</span> {pt}</li>" for pt in pitch_node["points"]])
        
        # Spring-loaded Popup Animation Container
        st.markdown(f"""
            <div class="solution-popup-card pitch-border">
                <div class="status-pill pitch-color">🔥 PITCHING STRATEGY VS {competitor_choice.upper()}</div>
                <div class="popup-title">Key Battleground Talking Points</div>
                <div class="meta-label">Points to Highlight / मुख्य बातें</div>
                <div class="action-steps-box" style="background: #F0FDF4; border-color: #DCFCE7;">
                    <ul>{points_html}</ul>
                </div>
                <div style="margin-top: 20px;"></div>
                <div class="meta-label">Customized Pitch Script / मर्चेंट को क्या बोलें</div>
                <div class="diagnostic-reason-text" style="background: #FAFAFA; border: 1px solid #E4E4E7;">
                    🗣️ "{pitch_node['script']}"
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Audio Playback Simulator Component
        st.write("")
        st.markdown('<div class="meta-label">Listen to Pitch Delivery Audio Practice:</div>', unsafe_allow_html=True)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

elif st.session_state.selected_module == "ECB":
    st.markdown("""
        <div class="solution-popup-card" style="border-left: 6px solid #A1A1AA;">
            <div class="status-pill" style="background: #F4F4F5; color: #71717A;">📊 CORE COMPLIANCE</div>
            <div class="popup-title">External Commercial Borrowings Matrix</div>
            <div class="diagnostic-reason-text">ECB parameters and limits structure are handled automatically via regional gateway nodes.</div>
        </div>
    """, unsafe_allow_html=True)

# 7. TROUBLESHOOT TECHNICAL ACTIONS SECTION (UNTOUCHED)
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
st.markdown('<div class="app-brand-tag">Direct Resolution Centers</div>', unsafe_allow_html=True)

col_err, col_obj = st.columns(2)

with col_err:
    selected_err = st.selectbox(
        "Troubleshoot Technical Errors",
        options=["None"] + list(LOAN_ERRORS_DATA.keys()),
        format_func=lambda x: "Select Error Signature..." if x == "None" else LOAN_ERRORS_DATA[x]["title"]
    )

with col_obj:
    selected_obj = st.selectbox(
        "Resolve Counter Objections",
        options=["None"] + list(OBJECTIONS_DATA.keys()),
        format_func=lambda x: "Select Merchant Objection..." if x == "None" else OBJECTIONS_DATA[x]["title"]
    )

# Render Diagnostic Solution output cards matching Selection
if selected_err != "None":
    node = LOAN_ERRORS_DATA[selected_err]
    actions_html = "".join([f"<li><span class='check-icon'>✓</span> {act}</li>" for act in node["actions"]])
    st.markdown(f"""
        <div class="solution-popup-card err-border">
            <div class="status-pill err-color">🚫 LENDING ERROR DIAGNOSTIC</div>
            <div class="popup-title">{node['title']}</div>
            <div class="meta-label">Reason / क्यों होता है</div>
            <div class="diagnostic-reason-text">{node['reason']}</div>
            <div class="meta-label">Immediate Solution / क्या करें</div>
            <div class="action-steps-box"><ul>{actions_html}</ul></div>
        </div>
    """, unsafe_allow_html=True)

elif selected_obj != "None":
    node = OBJECTIONS_DATA[selected_obj]
    actions_html = "".join([f"<li><span class='check-icon'>✓</span> {act}</li>" for act in node["actions"]])
    st.markdown(f"""
        <div class="solution-popup-card obj-border">
            <div class="status-pill obj-color">💬 OBJECTION RESOLUTION ENGINE</div>
            <div class="popup-title">{node['title']}</div>
            <div class="meta-label">Reason / क्यों होता है</div>
            <div class="diagnostic-reason-text">{node['reason']}</div>
            <div class="meta-label">Immediate Action / क्या करें</div>
            <div class="action-steps-box"><ul>{actions_html}</ul></div>
        </div>
    """, unsafe_allow_html=True)
