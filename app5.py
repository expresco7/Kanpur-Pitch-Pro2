import streamlit as st

# 1. STRUCTURAL PAGE LAYOUT SETUP
st.set_page_config(
    page_title="Lending Army Terminal",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Active user state session variables
if "selected_module" not in st.session_state:
    st.session_state.selected_module = None
if "selected_competitor" not in st.session_state:
    st.session_state.selected_competitor = None

# 2. APP DESIGN SYSTEM & NATIVE MODULE BUTTON CSS
st.markdown("""
    <style>
    /* Base Engine UI Configuration */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0A0A0C !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* Clean Top Header Space */
    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; }
    
    /* Typography Styles */
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
    
    /* Native Button Styling Overrides to replicate Card Layouts */
    div.stButton > button {
        background-color: #1C1C1E !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        border-radius: 18px !important;
        padding: 24px 20px !important;
        text-align: left !important;
        width: 100% !important;
        transition: all 0.25s ease-in-out !important;
    }
    div.stButton > button:hover {
        border-color: rgba(255,255,255,0.25) !important;
        background-color: #242426 !important;
        transform: translateY(-2px);
    }
    div.stButton > button p {
        color: #FFFFFF !important;
        text-align: left !important;
    }
    
    /* Dropdown Component Restyling */
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
    
    /* Interactive Dashboard Response Cards */
    @keyframes springPop {
        0% { transform: scale(0.96) translateY(15px); opacity: 0; }
        100% { transform: scale(1) translateY(0); opacity: 1; }
    }
    .solution-popup-card {
        background: #FFFFFF;
        border-radius: 28px;
        padding: 26px;
        margin-top: 12px;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
        animation: springPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.1) forwards;
    }
    .solution-popup-card.err-border { border-left: 6px solid #FF3B30; }
    .solution-popup-card.obj-border { border-left: 6px solid #5856D6; }
    .solution-popup-card.flow-border { border-left: 6px solid #00CD52; }
    
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
    .status-pill.flow-color { background: #E8F9EE; color: #007A31; }
    
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
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 10px;
        display: flex;
        align-items: flex-start;
        line-height: 1.4;
    }
    .action-steps-box li:last-child { margin-bottom: 0; }
    .check-icon { color: #4CAF50; font-weight: 900; margin-right: 10px; }
    
    hr { border-color: rgba(255,255,255,0.08) !important; margin: 24px 0 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. INTERACTIVE PLATFORM MASTER KNOWLEDGE DATABASE
DATA_FLOW_MATRIX = {
    "Smart Speaker": {
        "Paytm": {
            "points": [
                "Expose the hidden monthly device rentals via the Paytm Business App filter history.",
                "Highlight the current PhonePe special retention discount (₹99/₹149 setup fee).",
                "Contrast Paytm's frustrating online ticket/chatbot support with PhonePe's dedicated Area Sector Incharge.",
                "Zero online customer care dependency; direct call to the local executive for instant resolution."
            ],
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh har mahine ka hidden rental kat raha hai aapka. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (sirf ₹99/₹149 LTV ke hisab se). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota. PhonePe par humara system bilkul alag hai. Humne aapke Kanpur ke isi market area mein ek dedicated Sector Incharge bitha rakha hai. Koi online ticket-vicket raising ka jhamela nahi hai. Ek call ghumao, humara ladka turant aapki dukaan par hazir hoga. Agar daily target hit kar lete ho, toh rental bhi zero aur service bhi top class!"
        },
        "BharatPe": {
            "points": [
                "Leverage the fact that 70% to 80% of local consumers natively use PhonePe.",
                "Explain how routing PhonePe users through a third-party QR delays settlements.",
                "Pitch the reliable on-ground network: Local Sector Incharges stationed in every specific market zone.",
                "Emphasize fast, direct human support over automated, slow online complaint portals."
            ],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se 70% se 80% log PhonePe use karte hain. Jab consumer hi PhonePe ka hai, toh aap BharatPe ke QR par ghumakar settlement kyun delay kar rahe ho? Seedha PhonePe ka Smart Speaker lagao. Customers ke liye bhi frictionless payment hoga aur isi transaction volume ke basis par aapka loan offer bhi raat-o-raat active ho jayega. Rahi baat service ki—toh BharatPe ka na toh koi on-ground aadmi milta hai aur na hi unka support system local hai. Humara Sector Incharge har waqt isi market mein rehta hai. Kal ko network ka ya payment ka koi bhi issue aaye, aapko kisi app par jaakar shikayat nahi darj karni. Aapke paas humare local team ka number hoga, direct phone milao aur on-the-spot tension saaf!"
        },
        "Google Pay": {
            "points": [
                "Position the speaker as a gateway to the merchant ecosystem, not just an audio box.",
                "Explain how device deployment pushes the merchant into top-priority lending brackets.",
                "Frame GPay as a distant tech platform with zero local human service architecture.",
                "Highlight PhonePe's hyper-local team backup ensuring 100% counter uptime."
            ],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha. PhonePe ka Smart Speaker lagane ka matlab hai ki aapka business humare system mein top priority par aa jata hai. Iske lagte hi aapka business loan jald approve ho jata hai, aur aane wale time mein jo shop insurance aur retail health benefits hum de rahe hain, uski facilities bhi sabse pehle aapko milengi. Aur sabse matted baat bataun? Google Pay ka koi local office ya on-ground team nahi hai Kanpur mein. Kuch dikkat aayi toh mail likhte reh jaoge. PhonePe ka hamara local Sector Incharge hamesha aapke area mein round par rehta hai. Humara maqsad hai ki aapka counter kabhi band na ho. Bina kisi online ticketing ke, hand-to-hand aur reliable service sirf PhonePe par milti hai."
        },
        "Banks": {
            "points": [
                "Expose that bank QRs dump every single transaction directly into the bank account, making it tedious to track and verify daily business in the ledger.",
                "Highlight PhonePe’s unified end-of-day (EOD) single settlement that makes daily tracking effortless.",
                "Contrast slow, institutional bank compliance with PhonePe's 1-2 hour physical device replacement guarantee.",
                "Eliminate bank manager visits with direct Sector Incharge direct-line access."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. PhonePe par aisa kachra nahi hota! Hum din bhar ka poora collection ek sath, single settlement mein aapke bank mein bhejte hain, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ek transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka 1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega. Hum dhandha rukne nahi dete!"
        }
    },
    "Merchant Lending": {
        "Paytm": {
            "points": [
                "Expose Paytm’s true Annual Percentage Rate (APR) of 36%–37% hidden under processing fees and GST.",
                "Pitch PhonePe’s clear, low monthly entry-level interest rates of 1.25%–1.5%.",
                "Highlight the security of having an active on-ground Sector Incharge to assist with any payment queries during the loan tenure.",
                "Avoid cold automated fintech systems with localized human relationship managers."
            ],
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye. Woh upar se bolte hain 2% mahina, par hidden charges, processing fees aur GST milakar saal ka 36% se 37% tak baithta hai. Aap loot rahe ho wahan! Ek baar PhonePe ka loan banner check kariye, hum aapko pehli dafa mein hi 1.25% se 1.5% ke clear interest rate par loan de rahe hain. Koi hidden jhamela nahi hai. Aur sabse badhiya baat, Paytm par loan lene ke baad agar collection ya deduction ka koi confusion ho, toh aap chatbot se sarr marte reh jaoge. PhonePe par aapka bhai, humara local Sector Incharge hamesha aapke sath khada hai. Kuch bhi baat ho, direct usko phone lagao, woh aakar table par baith kar aapka hisab clear karega. Jab local support ka bharosa ho, toh dhandha fikar-mukt chalta hai."
        },
        "BharatPe": {
            "points": [
                "Pitch PhonePe's 'Continuous Eligibility' model allowing active Top-Ups without full closure.",
                "Guarantee new repeat loan banners within 1 week of closing a current loan block.",
                "Position the local Sector Incharge as an advocate who monitors your QR health to unlock bigger limits.",
                "Emphasize that reliable, human ground-support is unmatched by corporate apps."
            ],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko 'Continuous Eligibility' deta hai. Iska matlab yeh hai ki agar aapka loan chal raha hai aur aapko beech mein paise ki zaroorat padi, toh aapko live Top-Up ka option mil jata hai. Aur jaise hi aap purana loan close karte ho, within 1 week aapko naya repeat loan ka banner mil jata hai. Itna hi nahi, jab aap humare sath 3-4 loan cycle poori kar lete ho, toh aapki processing fee bhi bilkul zero ho jaati hai. Sabse bada fayda pata hai kya hai? BharatPe mein sab kuch digital machine par chalta hai, unka koi local chehra nahi hai aapse baat karne ke liye. PhonePe par humara Sector Incharge aapke touch mein rehta hai. Woh aapke QR ka health aur volume track karke system se aapki limit badhwane mein khud madad karta hai. Yeh machine ka nahi, bharose aur asli insani service ka rishta hai."
        },
        "Google Pay": {
            "points": [
                "Highlight 100% collateral-free, paperless lending backed purely by QR volume.",
                "Explain the lightning-fast 24 to 48-hour direct bank account capital disbursal.",
                "Contrast GPay's complicated third-party NBFC approvals with PhonePe's streamlined processing.",
                "Emphasize that the local Sector Incharge can expedite and verify any glitch on the spot."
            ],
            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge. PhonePe par agar aapka loan offer aaya hai, toh aapko koi collateral ya paperwork nahi chahiye. Sirf basic Aadhaar aur PAN card verify karna hai screen par, aur 24 se 48 ghante ke andar paisa seedha aapke linked bank account mein credit! Google Pay par teesri party ka jhamela rehta hai, unka customer care kabhi phone nahi uthata. Humare yahan agar aapka loan process hote waqt koi technical glitch aa bhi gaya, toh aapko pareshan nahi hona hai. Aap seedha humare area ke Sector Incharge ko batayiye, woh piche system par baat karke aapka temporary block turant clear karwayega. Fast capital ke sath fast aur reliable ground service sirf humare paas hai."
        },
        "Banks": {
            "points": [
                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of tedious entries that ruin credit assessments.",
                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",
                "Highlight that local financiers attack a merchant's local reputation if collections dip.",
                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."
            ],
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious ho jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. KYC Verification documentation checks verification checks verify track entries. Jab bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko sirf ek single unified settlement entry ke roop mein bank mein jata hai. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se jab aap paisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai! PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi karega. Aur kisi bhi tarah ke manual verification ya madad ke liye humara area Sector Incharge hamesha available hai. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!"
        }
    }
}

TECHNICAL_ERRORS = {
    "enacht_failed": {"title": "Unable to Process Your E-NACH Mandate", "reason": "Bank Details, IFSC, Account Type या E-NACH Consent में Problem है।", "actions": ["Bank Details दोबारा Check करें।", "सही Account Type (Savings) और IFSC चुनें।"]},
    "pan_mismatch": {"title": "PAN Name Mismatch", "reason": "PAN Card और Aadhaar Card में नाम अलग है।", "actions": ["सही नाम अपडेट कराएं।", "PAN में नाम सुधारकर फिर से KYC करें।"]},
    "kyc_incomplete": {"title": "Unable to Verify Your KYC", "reason": "KYC Process बीच में रुक गया / पूरा नहीं हो पाया।", "actions": ["कुछ समय (TAT) इंतजार करें।", "TAT पूरा होने के बाद भी Issue रहे तो War Room में Raise करें।"]},
    "face_match_failed": {"title": "Face Match Failed", "reason": "Selfie और Aadhaar/PAN Photo Match नहीं हुई।", "actions": ["Bright Light में Clear Selfie लें।", "चश्मा/कैप हटाकर Try करें।"]}
}

COUNTER_OBJECTIONS = {
    "eligibility": {"title": "PhonePe QR है, पर Loan के लिए Eligible कैसे बनूँ?", "reason": "मर्चेंट द्वारा नियमित व्यवहार बढ़ाना आवश्यक है।", "actions": ["रोजाना PhonePe QR पर ज्यादा से ज्यादा UPI Payments लें।", "आपकी लगातार Transaction History ही आपको Loan के लिए Eligible बनाती है।"]},
    "higher_offer": {"title": "मुझे Higher Loan Offer कैसे मिलेगा?", "reason": "लोन की राशि मुख्य रूप से लेनदेन और सिबिल पर आधारित है।", "actions": ["Loan Amount मुख्य रूप से आपके PhonePe QR Transactions और CIBIL Score पर निर्भर करता है।", "समय पर EDI Repayment करने से आपका CIBIL सुधरता है।"]},
    "edi_vs_emi": {"title": "मैं EMI की बजाय EDI क्यों लूँ?", "reason": "व्यवसाय के कैशफ्लो पर बिना दबाव डाले आसान दैनिक अदायगी।", "actions": ["EMI में हर महीने बड़ी Fixed Amount देनी पड़ती है।", "EDI में आपकी Daily Sales से छोटी-छोटी Amount कटती है, जिससे Repayment आसान हो जाता है।"]}
}

# 4. APP BOUNDARY SURFACE HEADERS
st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Lending Army Active Workspace</div>', unsafe_allow_html=True)

# 5. RESTORED NATIVE DESIGN MODULE BUTTONS (Only Modules 1 and 2 remain)
cols = st.columns(2)

with cols[0]:
    st.markdown("**MODULE 01**")
    if st.button("📊 ECB\n\nExternal commercial settlement configurations.", key="mod_ecb"):
        st.session_state.selected_module = "Smart Speaker"
        st.session_state.selected_competitor = None

with cols[1]:
    st.markdown("**MODULE 02**")
    if st.button("💼 LENDING\n\nMerchant evaluation profiles & pitch scripts.", key="mod_lending"):
        st.session_state.selected_module = "Merchant Lending"
        st.session_state.selected_competitor = None

st.markdown("<hr/>", unsafe_allow_html=True)

# 6. HISTORICAL DATA MATRIX EXTRACTION FLOW
if st.session_state.selected_module:
    current_mod = st.session_state.selected_module
    st.markdown(f'<div class="meta-label">Selected Track: {current_mod}</div>', unsafe_allow_html=True)
    
    # Target Dropdown Selector
    comp_choice = st.selectbox(
        "Select Target Competition / Outlet Specific Profile:",
        options=["Select Competition...", "Paytm", "BharatPe", "Google Pay", "Banks"]
    )
    
    if comp_choice != "Select Competition...":
        node = DATA_FLOW_MATRIX[current_mod][comp_choice]
        points_list_html = "".join([f"<li><span class='check-icon'>✓</span> {pt}</li>" for pt in node["points"]])
        
        # UI Premium Content Block Container
        st.markdown(f"""
            <div class="solution-popup-card flow-border">
                <div class="status-pill flow-color">🔥 COMPETITIVE OUTLET PLAYBOOK: {comp_choice.upper()}</div>
                <div class="popup-title">{current_mod} Strategy vs {comp_choice}</div>
                
                <div class="meta-label">Actual Points to Discuss / मुख्य बातें</div>
                <div class="action-steps-box" style="background: #F0FDF4; border-color: #DCFCE7; margin-bottom: 20px;">
                    <ul>{points_list_html}</ul>
                </div>
                
                <div class="meta-label">Hinglish Sales Pitch / मर्चेंट काउंटर पर क्या बोलें</div>
                <div class="diagnostic-reason-text" style="background: #FAFAFA; border: 1px solid #E4E4E7; font-size: 14.5px; line-height: 1.5; color: #27272A;">
                    🗣️ "{node['pitch']}"
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Audio Interface Component Implementation
        st.write("")
        st.markdown('<div class="meta-label">Interactive Pitch Training Audio:</div>', unsafe_allow_html=True)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# 7. UNCHANGED DIRECT TROUBLESHOOTING TECHNICAL SECTIONS (As per image_6.png)
st.markdown("<div style='margin-top: 40px;'></div>", unsafe_allow_html=True)
st.markdown('<div class="app-brand-tag">Instant Assistance Portals</div>', unsafe_allow_html=True)

col_err, col_obj = st.columns(2)

with col_err:
    selected_err = st.selectbox(
        "Troubleshoot Technical Errors",
        options=["None"] + list(TECHNICAL_ERRORS.keys()),
        format_func=lambda x: "Select Merchant Error..." if x == "None" else TECHNICAL_ERRORS[x]["title"]
    )

with col_obj:
    selected_obj = st.selectbox(
        "Resolve Counter Objections",
        options=["None"] + list(COUNTER_OBJECTIONS.keys()),
        format_func=lambda x: "Select Merchant Objection..." if x == "None" else COUNTER_OBJECTIONS[x]["title"]
    )

# Render Diagnostic Section Card matching choice (image_6.png Style)
if selected_err != "None":
    node = TECHNICAL_ERRORS[selected_err]
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
    node = COUNTER_OBJECTIONS[selected_obj]
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
