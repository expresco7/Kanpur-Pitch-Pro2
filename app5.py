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

# 2. CRED DESIGN SYSTEM & HIGH-CONTRAST INTERACTION ENGINE
st.markdown("""
    <style>
    /* Base Engine UI Configuration */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {
        background-color: #0A0A0C !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* FIX: Remove extra space at top of page and reduce bottom scrolling deadspace */
    [data-testid="stAppViewContainer"] .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 46rem !important;
    }
    
    /* Clean Top Header Space Clearances */
    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; display: none !important; }
    
    /* Premium CRED Intro Transition Graphics Engine */
    @keyframes credTracking {
        0% { letter-spacing: -0.2em; opacity: 0; filter: blur(12px); }
        40% { opacity: 1; filter: blur(0px); }
        70% { letter-spacing: 0.15em; opacity: 1; }
        100% { opacity: 0; letter-spacing: 0.2em; filter: blur(4px); }
    }
    @keyframes workspaceFadeUp {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
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
    
    .active-workspace-surface {
        animation: workspaceFadeUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) normal forwards;
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
    
    /* Symmetrical Carousel Architecture */
    .stHorizontalBlock {
        display: flex !important;
        flex-wrap: nowrap !important;
        overflow-x: auto !important;
        padding: 4px 4px 16px 4px;
        gap: 16px;
    }
    .stHorizontalBlock::-webkit-scrollbar { height: 6px; }
    .stHorizontalBlock::-webkit-scrollbar-track { background: rgba(255, 255, 255, 0.02); border-radius: 10px; }
    .stHorizontalBlock::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); border-radius: 10px; }
    
    .carousel-card-shell {
        background-color: #1C1C1E;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 20px;
        height: 190px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .carousel-card-shell:hover {
        border-color: rgba(255,255,255,0.25);
        background-color: #242426;
        transform: translateY(-2px);
    }
    .carousel-card-title {
        font-size: 15px;
        font-weight: 800;
        color: #FFFFFF;
        line-height: 1.3;
        margin-top: 4px;
    }
    
    /* Fix floating buttons on landing carousel */
    .carousel-card-shell div.stButton > button {
        background-color: rgba(255,255,255,0.05) !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        border-radius: 10px !important;
        padding: 6px 12px !important;
        min-height: 32px !important;
        width: 100% !important;
    }
    .carousel-card-shell div.stButton > button:hover { background-color: #FFFFFF !important; border-color: #FFFFFF !important; }
    .carousel-card-shell div.stButton > button p {
        color: #FFFFFF !important; font-size: 11px !important; font-weight: 700 !important;
        text-transform: uppercase !important; letter-spacing: 0.05em !important; margin: 0 auto !important;
    }
    .carousel-card-shell div.stButton > button:hover p { color: #000000 !important; }

    /* --- ENHANCED HIGH-HIGHLIGHT TRIAGE SECTION CHASSIS --- */
    .illuminated-triage-panel {
        background: linear-gradient(145deg, #111115 0%, #1A1A22 100%) !important;
        border: 1px solid rgba(255, 149, 0, 0.25) !important;
        box-shadow: 0 20px 45px rgba(0, 0, 0, 0.5), 0 0 30px rgba(255, 149, 0, 0.03) !important;
        border-radius: 24px !important;
        padding: 24px !important;
        margin-top: 30px !important;
        margin-bottom: 20px !important;
    }
    
    .terminal-main-header {
        font-size: 14px !important;
        font-weight: 800 !important;
        letter-spacing: 0.1em !important;
        text-transform: uppercase !important;
        color: #FF9500 !important;
        display: block !important;
        margin-bottom: 20px !important;
    }
    
    div.pitch-trigger-box button { background-color: #00CD52 !important; border: none !important; padding: 14px 20px !important; width: 100%; }
    div.pitch-trigger-box button p { color: #000000 !important; font-weight: 700 !important; font-size: 14px !important; }

    /* Fixed Floating Corner Back Button Interface Styles */
    div.floating-back-container { position: fixed; bottom: 24px; left: 24px; z-index: 9999; }
    div.floating-back-container button {
        background-color: #1C1C1E !important; border: 1px solid rgba(255,255,255,0.15) !important;
        border-radius: 30px !important; padding: 8px 18px !important; box-shadow: 0 8px 24px rgba(0,0,0,0.5) !important;
    }
    div.floating-back-container button:hover { background-color: #FFFFFF !important; border-color: #FFFFFF !important; }
    div.floating-back-container button p { color: #FFFFFF !important; font-size: 11px !important; font-weight: 700 !important; text-transform: uppercase !important; }
    div.floating-back-container button:hover p { color: #000000 !important; }
    
    .custom-input-heading {
        color: #8E8E93 !important;
        font-size: 10px !important;
        text-transform: uppercase !important;
        letter-spacing: 0.08em !important;
        font-weight: 700 !important;
        margin-bottom: 8px !important;
        display: block !important;
        text-align: left !important;
    }
    
    div[data-testid="stSelectbox"] > div { background-color: #0A0A0C !important; border: 1px solid rgba(255,255,255,0.06) !important; border-radius: 12px !important; }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] { color: white !important; }
    
    /* Output Data Interface Modals */
    .solution-popup-card { background: #FFFFFF; border-radius: 24px; padding: 26px; margin-top: 16px; box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3); }
    .solution-popup-card.err-border { border-left: 6px solid #FF3B30; }
    .solution-popup-card.obj-border { border-left: 6px solid #5856D6; }
    .solution-popup-card.flow-border { border-left: 6px solid #00CD52; }
    .solution-popup-card.ritual-border { border-left: 6px solid #FF9500; }
    
    .status-pill { display: inline-block; font-size: 10px; font-weight: 800; letter-spacing: 0.05em; padding: 5px 12px; border-radius: 50px; margin-bottom: 14px; }
    .status-pill.err-color { background: #FFEBEE; color: #D32F2F; }
    .status-pill.obj-color { background: #E8EAF6; color: #3F51B5; }
    .status-pill.flow-color { background: #E8F9EE; color: #007A31; }
    .status-pill.ritual-color { background: #FFF3E0; color: #E65100; }
    
    .popup-title { color: #1C1C1E; font-size: 22px; font-weight: 800; margin: 0 0 16px 0; }
    .meta-label { font-size: 11px; color: #71717A; text-transform: uppercase; font-weight: 700; letter-spacing: 0.04em; margin-bottom: 6px; margin-top: 14px; }
    .diagnostic-reason-text { background: #F4F4F5; color: #1C1C1E; padding: 14px 16px; border-radius: 14px; font-size: 15px; font-weight: 500; margin-bottom: 10px; }
    .action-steps-box { background: #E8F5E9; border: 1px solid #C8E6C9; border-radius: 14px; padding: 16px; }
    
    .ritual-table { width: 100%; border-collapse: collapse; margin-top: 10px; color: #1C1C1E; }
    .ritual-table th { background: #F4F4F5; text-align: left; padding: 10px; font-size: 12px; text-transform: uppercase; font-weight: 700; color: #71717A; border-bottom: 2px solid #E4E4E7; }
    .ritual-table td { padding: 12px 10px; font-size: 14px; border-bottom: 1px solid #E4E4E7; vertical-align: top; }
    .ritual-table tr:last-child td { border-bottom: none; }
    .step-highlight { font-weight: 700; color: #000000; }
    
    hr { border-color: rgba(255,255,255,0.06) !important; margin: 20px 0 !important; }
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

# 4. DATA MATRIX - COMPREHENSIVE REPOSITORY SYNCHRONIZED ARCHITECTURE
DATA_FLOW_MATRIX = {
    "Smart Speaker": {
        "Paytm": {
            "points": [
                "Expose the hidden monthly device rentals via the Paytm Business App filter history.",
                "Highlight the current PhonePe special retention discount (₹99/₹149 setup fee).",
                "Contrast Paytm's frustrating online ticket/chatbot support with PhonePe's dedicated Area Sector Incharge.",
                "Zero online customer care dependency; direct call to the local executive for instant resolution."
            ],
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh har mahine ka hidden rental kat raha hai aapka. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (sirf ₹99/₹149 LTV ke hisab se). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota. PhonePe par humara system bilkul alag hai. Humne aapke Kanpur ke isi market area mein ek dedicated Sector Incharge bitha rakha hai. Koi online ticket-vicket raising ka jhamela nahi hai. Ek call ghumao, humara ladka turant aapki dukaan par hazir hoga. Agar daily target hit kar lete ho, toh rental bhi zero aur service bhi top class!",
            "audio": "loan_paytm.mp3"
        },
        "BharatPe": {
            "points": [
                "Leverage the fact that 70% to 80% of local consumers natively use PhonePe.",
                "Explain how routing PhonePe users through a third-party QR delays settlements.",
                "Pitch the reliable on-ground network: Local Sector Incharges stationed in every specific market zone.",
                "Emphasize fast, direct human support over automated, slow online complaint portals."
            ],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se 70% se 80% log PhonePe use karte hain. Jab consumer hi PhonePe ka hai, toh aap BharatPe ke QR par ghumakar settlement kyun delay kar rahe ho? Seedha PhonePe ka Smart Speaker lagao. Customers ke liye bhi frictionless payment hoga aur isi transaction volume ke basis par aapka loan offer bhi raat-o-raat active ho jayega. Rahi baat service ki—toh BharatPe ka na toh koi on-ground aadmi milta hai aur na hi unka support system local hai. Humara Sector Incharge har waqt isi market mein rehta hai. Kal ko network ka ya payment ka koi bhi issue aaye, aapko kisi app par jaakar shikayat nahi darj karni. Aapke paas humare local team ka number hoga, direct phone milao aur on-the-spot tension saaf!",
            "audio": "loan_bharatpe.mp3"
        },
        "Google Pay": {
            "points": [
                "Position the speaker as a gateway to the merchant ecosystem, not just an audio box.",
                "Explain how device deployment pushes the merchant into top-priority lending brackets.",
                "Frame GPay as a distant tech platform with zero local human service architecture.",
                "Highlight PhonePe's hyper-local team backup ensuring 100% counter uptime."
            ],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha. PhonePe ka Smart Speaker lagane ka matlab hai ki aapka business humare system mein top priority par aa jata hai. Iske lagte hi aapka business loan jald approve ho jata hai, aur aane wale time mein jo shop insurance aur retail health benefits hum de rahe hain, uski facilities bhi sabse pehle aapko milengi. Aur sabse matted baat bataun? Google Pay ka koi local office ya on-ground team nahi hai Kanpur mein. Kuch dikkat aayi toh mail likhte reh jaoge. PhonePe ka hamara local Sector Incharge hamesha aapke area mein round par rehta hai. Humara maqsad hai ki aapka counter kabhi band na ho. Bina kisi online ticketing ke, hand-to-hand aur reliable service sirf PhonePe par milti hai.",
            "audio": "loan_gpay.mp3"
        },
        "Banks": {
            "points": [
                "Expose that bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of tedious entries.",
                "Highlight unified end-of-day (EOD) single settlement that keeps passbooks perfectly clean.",
                "Contrast institutional banking delays with lightning fast 1-2 hour physical device swap deployment.",
                "Eliminate structural bank branch operational visits with direct-line field engineering tools."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. PhonePe par aisa kachra nahi hota! Hum din bhar ka poora collection ek sath, single settlement mein aapke bank mein bhejte hain, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ein transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka 1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega. Hum dhandha rukne nahi dete!",
            "audio": "loan_bank.mp3"
        }
    },
    "Merchant Lending": {
        "Paytm": {
            "points": [
                "Expose true Annual Percentage Rate (APR) of 36%–37% hidden under processing blocks and processing premiums.",
                "Pitch clear, low monthly interest matrix rates of 1.25%–1.5%.",
                "Highlight the physical security of having an active ground layout asset checking processing parameters.",
                "Avoid cold automated digital loops via dedicated human verification channels."
            ],
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye. Woh upar se bolte hain 2% mahina, par hidden charges, processing fees aur GST milakar saal ka 36% se 37% tak baithta hai. Aap loot rahe ho wahan! Ek baar PhonePe ka loan banner check kariye, hum aapko pehli dafa mein hi 1.25% se 1.5% ke clear interest rate par loan de rahe hain. Koi hidden jhamela nahi hai. Aur sabse badhiya baat, Paytm par loan lene ke baad agar collection ya deduction ka koi confusion ho, toh aap chatbot se sarr marte reh jaoge. PhonePe par aapka bhai, humara local Sector Incharge hamesha aapke sath khada hai. Kuch bhi baat ho, direct usko phone lagao, woh aakar table par baith kar aapka hisab clear karega. Jag local support ka bharosa ho, toh dhandha fikar-mukt chalta hai.",
            "audio": "loan_paytm.mp3"
        },
        "BharatPe": {
            "points": [
                "Pitch PhonePe's 'Continuous Eligibility' model allowing active Top-Ups without full closure.",
                "Guarantee new repeat loan banners within 1 week of closing a current loan block.",
                "Position the local Sector Incharge as an advocate who monitors your QR health to unlock bigger limits.",
                "Emphasize that reliable, human ground-support is unmatched by corporate apps."
            ],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko 'Continuous Eligibility' deta hai. Iska matlab yeh hai ki agar aapka loan chal raha hai aur aapko beech mein paise ki zaroorat padi, toh aapko live Top-Up ka option mil jata hai. Aur jaise hi aap purana loan close karte ho, within 1 week aapko naya repeat loan ka banner mil jata hai. Itna hi nahi, jab aap humare sath 3-4 loan cycle poori kar lete ho, toh aapki processing fee bhi bilkul zero ho jaati hai. Sabse bada fayda pata hai kya hai? BharatPe mein sab kuch digital machine par chalta hai, unka koi local chehra nahi hai aapse baat karne ke liye. PhonePe par humara Sector Incharge aapke touch mein rehta hai. Woh aapke QR ka health aur volume track karke system se aapki limit badhwane mein khud madad karta hai. Yeh machine ka nahi, bharose aur asli insani service ka rishta hai.",
            "audio": "loan_bharatpe.mp3"
        },
        "Google Pay": {
            "points": [
                "Highlight 100% collateral-free, paperless lending backed purely by QR volume.",
                "Explain the lightning-fast 24 to 48-hour direct bank account capital disbursal.",
                "Contrast GPay's complicated third-party NBFC approvals with PhonePe's streamlined processing.",
                "Emphasize that the local Sector Incharge can expedite and verify any glitch on the spot."
            ],
            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge. PhonePe par agar aapka loan offer aaya hai, toh aapko koi collateral ya paperwork nahi chahiye. Sirf basic Aadhaar aur PAN card verify karna hai screen par, aur 24 se 48 ghante ke andar paise seedha aapke linked bank account mein credit! Google Pay par teesri party ka jhamela rehta hai, unka customer care kabhi phone nahi uthata. Humare yahan agar aapka loan process hote waqt koi technical glitch aa bhi gaya, toh aapko pareshan nahi hona hai. Aap seedha humare area ke Sector Incharge ko batayiye, woh piche system par baat karke aapka temporary block turant clear karwayega. Fast capital ke sath fast aur reliable ground service sirf humare paas hai.",
            "audio": "loan_gpay.mp3"
        },
        "Banks": {
            "points": [
                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of tedious entries.",
                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",
                "Highlight that local financiers attack a merchant's local reputation if collections dip.",
                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."
            ],
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious ho jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. Jab bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko sirf ek single unified settlement entry ke roop mein bank mein jata hai. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se jab aap kaisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai! PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi korega. Aur kisi bhi tarah ke manual verification ya madad ke liye humara area Sector Incharge hamesha available hai. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!",
            "audio": "loan_bank.mp3"
        }
    }
}

TECHNICAL_ERRORS = {
    "pan_mismatch": {"title": "PAN Name Mismatch", "reason": "PAN Card aur Aadhaar Card mein naam alag hai.", "actions": ["Sahi naam update karayen.", "PAN mein naam sudharkar fir se KYC karen."]},
    "kyc_failed_link": {"title": "KYC Verification Failed", "reason": "PAN aur Aadhaar aapas mein Link nahi hai.", "actions": ["PAN ko Aadhaar se Link karwaen (NSDL/UTI Portal ya Bank/CSC ke madhyam se).", "Link hone ke baad 24 ghante baad Retry karen."]}
}

COUNTER_OBJECTIONS = {
    "eligibility": {"title": "Mere paas PhonePe QR hai, par Loan ke liye Eligible kaise banu?", "reason": "Merchant dwara niyamit aur sahi vyavahar badhana aavashyak hai.", "actions": ["Rojana PhonePe QR par jyada se jyada UPI Payments le."]}
}

# 5. CORE WORKSPACE SURFACE INTERFACES
st.markdown('<div class="active-workspace-surface">', unsafe_allow_html=True)

st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)
st.markdown('<div class="app-main-title">Pitch Pro Terminal</div>', unsafe_allow_html=True)

# The Landing Telemetry Panel
if not st.session_state.selected_module:
    st.markdown("""
        <div class="telemetry-card">
            <div class="app-brand-tag" style="font-size:10px; margin-bottom:12px; color:rgba(255,255,255,0.4);">Territory Market Share Snapshot</div>
            <div class="telemetry-grid">
                <div class="telemetry-item">
                    <div class="telemetry-val leader-color">38.6%</div>
                    <div class="telemetry-lbl">🟢 PhonePe</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">37.6%</div>
                    <div class="telemetry-lbl">Paytm</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">9.6%</div>
                    <div class="telemetry-lbl">BharatPe</div>
                </div>
                <div class="telemetry-item">
                    <div class="telemetry-val">5.8%</div>
                    <div class="telemetry-lbl">Google Pay</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Carousel columns loop processing framework
carousel_cols = st.columns(4)
modules = ["Smart Speaker", "Merchant Lending", "Gate Meeting Rituals", "Merchant Visit Rituals"]
keys = ["mod_ecb", "mod_lending", "mod_gate", "mod_visit"]

for i, col in enumerate(carousel_cols):
    with col:
        st.markdown(f"""
            <div class="carousel-card-shell">
                <div>
                    <div class="app-brand-tag" style="font-size:9px; margin-bottom:0px;">Module 0{i+1}</div>
                    <div class="carousel-card-title">{modules[i].upper()}</div>
                </div>
        """, unsafe_allow_html=True)
        if st.button("Open", key=keys[i]):
            reset_pitch_flow(modules[i])
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # End active-workspace-surface
st.markdown("<hr/>", unsafe_allow_html=True)

# 6. DYNAMIC DRILL-DOWN SUB WORKSPACES
if st.session_state.selected_module:
    current_mod = st.session_state.selected_module
    
    # System Interaction 1 & 2: Strategic Playbooks
    if current_mod in ["Smart Speaker", "Merchant Lending"]:
        st.markdown('<div class="app-brand-tag" style="margin-bottom:6px;">Target Competition Matrices</div>', unsafe_allow_html=True)
        
        comp_options = ["Select Competitor...", "Paytm", "BharatPe", "Google Pay", "Banks"]
        
        selected_dropdown = st.selectbox(
            "Choose a target competitor to open tactical playbook",
            options=comp_options,
            index=comp_options.index(st.session_state.selected_competitor) if st.session_state.selected_competitor in comp_options else 0,
            key="competitor_dropdown_matrix"
        )
        
        if selected_dropdown != "Select Competitor...":
            st.session_state.selected_competitor = selected_dropdown
            comp_choice = st.session_state.selected_competitor
            node = DATA_FLOW_MATRIX[current_mod][comp_choice]
            
            st.markdown(f"""
                <div class="solution-popup-card flow-border">
                    <div class="status-pill flow-color">COMPETITIVE OUTLET PLAYBOOK: {comp_choice.upper()}</div>
                    <div class="popup-title">{current_mod} Strategy vs {comp_choice}</div>
                    <div class="meta-label">Actual Points to Discuss / मुख्य बातें</div>
                </div>
            """, unsafe_allow_html=True)
            
            with st.container():
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
            if st.button(f"Customize Active Pitch Script vs {comp_choice}", key="generate_pitch_btn"):
                st.session_state.pitch_customized = True
            st.markdown('</div>', unsafe_allow_html=True)
            
            if st.session_state.pitch_customized:
                st.markdown(f"""
                    <div class="solution-popup-card flow-border" style="margin-top:16px;">
                        <div class="meta-label" style="margin-top:0px;">Hinglish Sales Pitch / मर्चेंट काउंटर पर क्या बोलें</div>
                        <div class="diagnostic-reason-text" style="background: #FAFAFA; border: 1px solid #E4E4E7; line-height:1.5; font-size:14.5px; color:#1C1C1E; font-weight:400;">
                            "{node['pitch']}"
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.write("")
                st.markdown('<div class="app-brand-tag" style="margin-bottom:8px;">🎙️ Training Audio Player:</div>', unsafe_allow_html=True)
                
                base_dir = os.path.dirname(os.path.abspath(__file__))
                absolute_audio_path = os.path.join(base_dir, node["audio"])
                
                try:
                    with open(absolute_audio_path, "rb") as audio_file:
                        st.audio(audio_file.read(), format="audio/mp3")
                except FileNotFoundError:
                    st.error(f"⚠️ Audio asset missing: '{node['audio']}' could not be matched at root destination.")

    # System Interaction 3: Gate Meetings
    elif current_mod == "Gate Meeting Rituals":
        st.markdown("""
            <div class="solution-popup-card ritual-border">
                <div class="status-pill ritual-color">GATE MEETING GUIDELINES</div>
                <div class="popup-title">10 KA DUM</div>
                <table class="ritual-table">
                    <tr><th>Gate Meeting</th><th>Description</th></tr>
                    <tr><td><span class="step-highlight">1. Attendance</span></td><td>1-QR Generation/Scanning<br>2-Selfie with Code (Mention AOP, Count of Active, Location)<br>3-Virtual GM Form</td></tr>
                    <tr><td><span class="step-highlight">2. Team Grooming</span></td><td>Basic Hygiene - Dress, Bags, Helmet, Mobile Cover, Mobile Screen Guard, Torn Shoes or Slippers.</td></tr>
                    <tr><td><span class="step-highlight">3. SKH</span></td><td>In-depth Discussion with help of Agent Activity & Tracker</td></tr>
                    <tr><td><span class="step-highlight">4. DSR</span></td><td>1-Take Appointment during Morning calling activity<br>2-Visit Mx and Mark tasks with final remarks</td></tr>
                    <tr><td><span class="step-highlight">5. Salary Discussion</span></td><td>Daily Salary Discussion with format to be done and Signed by Manager i.e. TSM, ASM, CSM.</td></tr>
                    <tr><td><span class="step-highlight">6. TOD</span></td><td>1-Task of the Day Discussion<br>2-Open Smart Squad<br>3-Perform Ace Activities<br>4-TP Commitment for the Day on Sales Academy</td></tr>
                    <tr><td><span class="step-highlight">7. Manager Inputs</span></td><td>How to Drive task of the Day, share inputs and create innovative drives.</td></tr>
                    <tr><td><span class="step-highlight">8. Collateral Dist.</span></td><td>QR, A4, SS, RVP collection, distribution and submission.</td></tr>
                    <tr><td><span class="step-highlight">9. Telecalling Activity</span></td><td>15 Appointments to be Booked before leaving.</td></tr>
                    <tr><td><span class="step-highlight">11. Support Required</span></td><td>One on One support requirement discussion with Manager.</td></tr>
                </table>
            </div>
        """, unsafe_allow_html=True)

    # System Interaction 4: Visitation Rituals
    elif current_mod == "Merchant Visit Rituals":
        st.markdown("""
            <div class="solution-popup-card ritual-border">
                <div class="status-pill ritual-color">STEP-BY-STEP GUIDE FOR SUCCESS</div>
                <div class="popup-title">5 KA PUNCH</div>
                <table class="ritual-table">
                    <tr><th>Step</th><th>Task Objective</th><th>Action Roadmap</th></tr>
                    <tr><td><span class="step-highlight">1</span></td><td><b>QR Deployment & Test Transaction</b></td><td>Deploy minimum 3 QR codes and perform a small test transaction to confirm tracking ecosystem health.</td></tr>
                    <tr><td><span class="step-highlight">2</span></td><td><b>Tag Competition QR</b></td><td>Locate and tag the specific competition QR active on counter inside analytics environment.</td></tr>
                    <tr><td><span class="step-highlight">3</span></td><td><b>Show Transaction in App</b></td><td>Verify test transaction inside the PhonePe Business App. Click all visible structural banners and request Photo QR if available.</td></tr>
                    <tr><td><span class="step-highlight">4</span></td><td><b>Complete Merchant KYC</b></td><td>Collect valid verification documentation details. Securely verify account identity instruments (PAN, Aadhaar) on workspace dashboard.</td></tr>
                    <tr><td><span class="step-highlight">5</span></td><td><b>Smartspeaker Activation</b></td><td>Plug in and charge smartspeaker. Share complete support line coordinates and localized contact details with the merchant.</td></tr>
                </table>
            </div>
        """, unsafe_allow_html=True)

    # Floating Back Button Action
    st.markdown('<div class="floating-back-container">', unsafe_allow_html=True)
    if st.button("← Back to Dashboard", key="floating_back_nav_action"):
        st.session_state.selected_module = None
        st.session_state.selected_competitor = "Select Competitor..."
        st.session_state.pitch_customized = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# 7. HIGHLY HIGHLIGHTED STANDALONE VERTICAL TRIAGE TERMINAL ENGINE
if not st.session_state.selected_module:
    st.markdown("""
        <div class="illuminated-triage-panel">
            <span class="terminal-main-header">⚡ INSTANT TROUBLESHOOTING TERMINAL</span>
    """, unsafe_allow_html=True)

    # Item Container Block 01: Technical Errors Selector Dropdown
    st.markdown('<span class="custom-input-heading">Troubleshoot Technical Errors</span>', unsafe_allow_html=True)
    selected_err = st.selectbox(
        "Technical Error Form Selector Tool",
        options=["None"] + list(TECHNICAL_ERRORS.keys()),
        format_func=lambda x: "Select Merchant Error..." if x == "None" else TECHNICAL_ERRORS[x]["title"],
        key="tech_errors_aligned_dropdown",
        label_visibility="collapsed"
    )
    
    st.markdown('<div style="margin-bottom: 24px;"></div>', unsafe_allow_html=True)
    
    # Item Container Block 02: Counter Objections Selector Dropdown
    st.markdown('<span class="custom-input-heading">Resolve Counter Objections</span>', unsafe_allow_html=True)
    selected_obj = st.selectbox(
        "Counter Objection Form Selector Tool",
        options=["None"] + list(COUNTER_OBJECTIONS.keys()),
        format_func=lambda x: "Select Merchant Objection..." if x == "None" else COUNTER_OBJECTIONS[x]["title"],
        key="counter_objections_aligned_dropdown",
        label_visibility="collapsed"
    )
    
    st.markdown('</div>', unsafe_allow_html=True) # Safe terminal container seal close
    
    # Action result metrics outputs cards processing
    if selected_err != "None":
        node = TECHNICAL_ERRORS[selected_err]
        actions_html = "".join([f"<li style='color:#721c24; margin-bottom:6px;'>📍 {act}</li>" for act in node["actions"]])
        st.markdown(f"""
            <div class="solution-popup-card err-border">
                <div class="status-pill err-color">LENDING ERROR DIAGNOSTIC</div>
                <div class="popup-title">{node['title']}</div>
                <div class="meta-label">Reason / क्यों होता hai</div>
                <div class="diagnostic-reason-text">{node['reason']}</div>
                <div class="meta-label">Immediate Solution / क्या करें</div>
                <div class="action-steps-box" style="background:#FFF0F2; border-color:#FFD2D7;"><ul>{actions_html}</ul></div>
            </div>
        """, unsafe_allow_html=True)
        
    elif selected_obj != "None":
        node = COUNTER_OBJECTIONS[selected_obj]
        actions_html = "".join([f"<li style='color:#1a2556; margin-bottom:6px;'>📍 {act}</li>" for act in node["actions"]])
        st.markdown(f"""
            <div class="solution-popup-card obj-border">
                <div class="status-pill obj-color">OBJECTION RESOLUTION ENGINE</div>
                <div class="popup-title">{node['title']}</div>
                <div class="meta-label">Reason / क्यों होता hai</div>
                <div class="diagnostic-reason-text">{node['reason']}</div>
                <div class="meta-label">Immediate Action / क्या करें</div>
                <div class="action-steps-box" style="background:#EEF0FC; border-color:#D2D7FA;"><ul>{actions_html}</ul></div>
            </div>
        """, unsafe_allow_html=True)
