"import streamlit as st

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

    /* Base Engine UI Configuration */

    html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"] {

        background-color: #0A0A0C !important;

        color: #FFFFFF !important;

        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;

    }

    

    /* Clean Top Header Space Clearances */

    header, [data-testid="stHeader"], footer { background: transparent !important; visibility: hidden; }

    

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

        font-size: 26px;

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

    

    /* Fixed Symmetrical Card Framework */

    div.stButton > button {

        background-color: #1C1C1E !important;

        border: 1px solid rgba(255,255,255,0.08) !important;

        border-radius: 18px !important;

        padding: 24px 20px !important;

        text-align: left !important;

        width: 100% !important;

        min-height: 142px !important; 

        display: flex !important;

        flex-direction: column !important;

        justify-content: flex-start !important;

        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;

    }

    div.stButton > button:hover {

        border-color: rgba(255,255,255,0.25) !important;

        background-color: #242426 !important;

        transform: translateY(-2px);

    }

    

    /* Typography formatting for main module lists */

    div.stButton > button p {

        color: #FFFFFF !important;

        text-align: left !important;

        line-height: 1.5 !important;

        font-size: 13px !important;

        font-weight: 400 !important;

        opacity: 0.7 !important;

        white-space: normal !important;

    }

    div.stButton > button p::first-line {

        font-size: 18px !important;

        font-weight: 800 !important;

        color: #FFFFFF !important;

        opacity: 1 !important;

    }

    

    /* Illuminated Triage Troubleshooting Section Card */

    .illuminated-triage-panel {

        background: linear-gradient(180deg, #121215 0%, #0A0A0C 100%);

        border: 1px solid rgba(255, 255, 255, 0.15);

        box-shadow: 0 0 25px rgba(255, 255, 255, 0.03);

        border-radius: 24px;

        padding: 24px;

        margin-top: 10px;

    }

    

    /* Pitch CTA Accent Button elements */

    div.pitch-trigger-box button {

        background-color: #00CD52 !important;

        border: none !important;

        text-align: center !important;

        min-height: auto !important;

        padding: 14px 20px !important;

    }

    div.pitch-trigger-box button p {

        color: #000000 !important;

        text-align: center !important;

        font-weight: 700 !important;

        opacity: 1 !important;

    }

    div.pitch-trigger-box button p::first-line {

        font-size: 14px !important;

        color: #000000 !important;

    }

    

    /* Selection Fields Inside Diagnostics */

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

    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"] {

        color: white !important;

    }

    

    /* Output Data Interface Modals */

    .solution-popup-card {

        background: #FFFFFF;

        border-radius: 24px;

        padding: 26px;

        margin-top: 16px;

        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);

    }

    .solution-popup-card.err-border { border-left: 6px solid #FF3B30; }

    .solution-popup-card.obj-border { border-left: 6px solid #5856D6; }

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

    .status-pill.obj-color { background: #E8EAF6; color: #3F51B5; }

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

    

    hr { border-color: rgba(255,255,255,0.08) !important; margin: 24px 0 !important; }

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

    time.sleep(2.1)

    splash_placeholder.empty()

    st.session_state.splash_done = True



# 4. ACTIVE DATA STRUCTURAL ENTITIES

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

                "Expose that bank QRs dump every single transaction directly into the bank account, making it tedious to track and verify daily dhandha entries.",

                "Highlight unified end-of-day (EOD) single settlement that keeps passbooks perfectly clean.",

                "Contrast institutional banking delays with lightning fast 1-2 hour physical device swap deployment.",

                "Eliminate structural bank branch operational visits with direct-line field engineering tools."

            ],

            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. PhonePe par aisa kachra nahi hota! Hum din bhar ka poora collection ek sath, single settlement mein aapke bank mein bhejte hain, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ek transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka 1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega. Hum dhandha rukne nahi dete!"

        }

    },

    "Merchant Lending": {

        "Paytm": {

            "points": [

                "Expose true Annual Percentage Rate (APR) of 36%–37% hidden under processing blocks and processing premiums.",

                "Pitch clear, low monthly entry level interest matrix rates of 1.25%–1.5%.",

                "Highlight the physical security of having an active ground layout asset checking processing parameters.",

                "Avoid cold automated digital loops via dedicated human verification channels."

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

            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge. PhonePe par agar aapka loan offer aaya hai, toh aapko koi collateral ya paperwork nahi chahiye. Sirf basic Aadhaar aur PAN card verify karna hai screen par, aur 24 se 48 ghante ke andar paise seedha aapke linked bank account mein credit! Google Pay par teesri party ka jhamela rehta hai, unka customer care kabhi phone nahi uthata. Humare yahan agar aapka loan process hote waqt koi technical glitch aa bhi gaya, toh aapko pareshan nahi hona hai. Aap seedha humare area ke Sector Incharge ko batayiye, woh piche system par baat karke aapka temporary block turant clear karwayega. Fast capital ke sath fast aur reliable ground service sirf humare paas hai."

        },

        "Banks": {

            "points": [

                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of tedious entries that ruin credit assessments.",

                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",

                "Highlight that local financiers attack a merchant's local reputation if collections dip.",

                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."

            ],

            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious ho jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. Jag bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko sirf ek single unified settlement entry ke roop mein bank mein jata hai. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se jab aap paisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai! PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi karega. Aur kisi bhi tarah ke manual verification ya madad ke liye humara area Sector Incharge hamesha available hai. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!"

        }

    }

}



TECHNICAL_ERRORS = {

    "pan_mismatch": {"title": "PAN Name Mismatch", "reason": "PAN Card aur Aadhaar Card mein naam alag hai.", "actions": ["Sahi naam update karayen.", "PAN mein naam sudharkar fir se KYC karen."]},

    "kyc_failed_link": {"title": "KYC Verification Failed", "reason": "PAN aur Aadhaar aapas mein Link nahi hai.", "actions": ["PAN ko Aadhaar se Link karwaen (NSDL/UTI Portal ya Bank/CSC ke madhyam se).", "Link hone ke baad 24 ghante baad Retry karen."]},

    "kyc_incomplete": {"title": "Unable to Verify Your KYC", "reason": "KYC Process beech mein ruk gaya / poora nahi ho paya.", "actions": ["Kuch samay (TAT) intezar karen.", "TAT poora hone ke baad bhi issue rahe toh War Room mein Raise karen."]},

    "face_match_failed": {"title": "Face Match Failed", "reason": "Selfie aur Aadhaar/PAN Photo Match nahi hui.", "actions": ["Bright Light mein Clear Selfie le.", "Chashma/Cap hatakar try kare.", "Chehra Frame mein Proper rakhe aur dobara Retry kare."]},

    "kyc_failed_docs": {"title": "KYC Failed", "reason": "Di gayi Details Verification Document se Match nahi hui.", "actions": ["Di gayi jankari (Name, DOB, Address, aadi) sahi bhare.", "Documents sahi aur Clear Upload kare.", "Fir bhi Fail ho toh yeh Terminal Error hai - Next Merchant par Move kare."]},

    "digilocker_error": {"title": "DigiLocker Error", "reason": "UIDAI/DigiLocker ki taraf se Technical Issue hai.", "actions": ["2 ghante Wait kare aur fir se Try kare.", "Issue hone par War Room mein Raise kare."]},

    "unable_process_request": {"title": "Unable to Process Your Request", "reason": "System / Server Problem ya Lending Partner ki taraf se Temporary Issue hai.", "actions": ["Kuch samay baad Retry kare.", "Baar-baar Issue aane par War Room mein Raise kare."]},

    "enacht_failed": {"title": "Unable to Process Your E-NACH Mandate", "reason": "Bank Details, IFSC, Account Type ya E-NACH Consent mein Problem hai.", "actions": ["Bank Details dobara Check kare.", "Sahi Account Type (Savings) aur IFSC chune.", "Dobara Mandate Setup kare."]},

    "upi_mandate_failed": {"title": "UPI Mandate Setup Failed", "reason": "UPI ID ya Bank se Mandate Setup nahi ho paya.", "actions": ["UPI ID Active aur Same Bank ki ho.", "Bank App/UPI App mein Mandate Approve kare."]},

    "disbursement_failed": {"title": "Loan Disbursement Failed", "reason": "Bank Account, IFSC, KYC ya System issue ke karan Disbursement nahi ho paya.", "actions": ["Bank Details aur IFSC Verify kare.", "KYC Complete aur Approved hai ya nahi Check kare.", "Issue rahe toh War Room mein Raise kare."]}

}



COUNTER_OBJECTIONS = {

    "eligibility": {"title": "Mere paas PhonePe QR hai, par Loan ke liye Eligible kaise banu?", "reason": "Merchant dwara niyamit aur sahi vyavahar badhana aavashyak hai.", "actions": ["Rojana PhonePe QR par jyada se jyada UPI Payments le.", "Aapki lagatar Transaction History hi aapko Loan ke liye Eligible banati hai.", "Jitna jyada aur Regular istemal, utni jaldi Loan Offer!"]},

    "higher_offer": {"title": "Mujhe Higher Loan Offer kaise milega?", "reason": "Loan ki rashi mukhya roop se lenden aur cibil par aadharit hai.", "actions": ["Loan Amount mukhya roop se aapke PhonePe QR Transactions aur CIBIL Score par nirbhar karta hai.", "Samay par EDI Repayment karne se aapka CIBIL sudharta hai aur agla Higher Loan Slab swatah khul jata hai.", "Acche Business Performance se Loan Offer badhta hai."]},

    "edi_miss": {"title": "Agar mein EDI Miss kar du toh kya hoga?", "reason": "E-NACH bounce hone par credit score aur future metrics par bura asar padta hai.", "actions": ["Hum E-NACH ke madhyam se Due aur Overdue Amount ko aapke Bank Account se Auto-Debit kar sakte hain.", "Baar-baar Default karne se aapka CIBIL Score kharab hota hai.", "Isse bhavishya mein Loan milna mushkil ho sakta hai."]},

    "loan_reject": {"title": "Loan Banner dikha, fir bhi mera Loan Reject kyun ho gaya?", "reason": "Banner eligible criteria dikhata hai par final approval partner assessment par hota hai.", "actions": ["Loan Offer Eligibility aapki Activity ke aadhar par hoti hai.", "Lekin Final Approval Lending Partner dwara kiya jata hai.", "Kuch Internal Parameters mein kami hone par Loan Reject ho sakta hai.", "Aap QR Usage jaari rakhe aur CIBIL sudhare, fir dobara koshish kare."]},

    "competitor_more_offer": {"title": "Doosre Merchant ko mujhse jyada Loan Amount kyun offer hua?", "reason": "Lending risk assessment engines multiple variable parameters par matrix evaluation karte hain.", "actions": ["Lending Company aapke Business ko kareeb 20 alag-alag Parameters par Evaluate karti hai.", "Jaise: Transaction Volume, Consistency, Business Vintage, Ticket Size, Refund Ratio, CIBIL Score, KYC Quality aadi.", "Har Merchant ke yeh Parameters alag hote hain, isliye Offer bhi alag hota hai."]},

    "loan_benefit": {"title": "Loan lene ka mere liye kya fayda hai?", "reason": "Business scaling capital metrics validation.", "actions": ["Loan se aap Inventory bada sakte hain, Business Expand kar sakte hain.", "Jyada Stock = Jyada Sales aur jyada Profit kama sakte hain.", "Samay par Repayment karne se CIBIL Score improve hota hai.", "Bhavishya mein aapko Higher Loan Amount kam Interest Rate par milega."]},

    "edi_vs_emi": {"title": "Main EMI ki bajay EDI kyun lu?", "reason": "Vyavasay ke cashflow par bina dabav dale aasan dainik adayegi framework.", "actions": ["EMI mein har mahine badi Fixed Amount deni padti hai.", "EDI mein aapki Daily Sales se chhoti-chhoti Amount katti hai, jisse Repayment aasan ho jata hai.", "Business Cash Flow mein koi dabav nahi padta."]}

}



# 5. CORE WORKSPACE SURFACE INTERFACES

st.markdown('<div class="active-workspace-surface">', unsafe_allow_html=True)



st.markdown('<div class="app-brand-tag">Kanpur Division Module</div>', unsafe_allow_html=True)

st.markdown('<div class="app-main-title">Pitch Pro</div>', unsafe_allow_html=True)



# THE LANDING TELEMETRY PANEL: Disappears automatically when a workspace module is selected.

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



# Symmetrical Card Grid Generation Systems (Clean line breaks, original short names)

row1_cols = st.columns(2)

with row1_cols[0]:

    st.markdown("<div class='app-brand-tag' style='font-size:10px;'>Module 01</div>", unsafe_allow_html=True)

    if st.button("ECB\nExternal commercial settlement configurations.", key="mod_ecb"):

        reset_pitch_flow("Smart Speaker")



with row1_cols[1]:

    st.markdown("<div class='app-brand-tag' style='font-size:10px;'>Module 02</div>", unsafe_allow_html=True)

    if st.button("LENDING\nMerchant evaluation profiles and pitch scripts.", key="mod_lending"):

        reset_pitch_flow("Merchant Lending")



row2_cols = st.columns(2)

with row2_cols[0]:

    st.markdown("<div class='app-brand-tag' style='font-size:10px;'>Module 03</div>", unsafe_allow_html=True)

    if st.button("GATE MEETING RITUALS\nMorning optimization and attendance routines.", key="mod_gate"):

        reset_pitch_flow("Gate Meeting Rituals")



with row2_cols[1]:

    st.markdown("<div class='app-brand-tag' style='font-size:10px;'>Module 04</div>", unsafe_allow_html=True)

    if st.button("MERCHANT VISIT RITUALS\nGround deployment checklist and merchant journey.", key="mod_visit"):

        reset_pitch_flow("Merchant Visit Rituals")



st.markdown("<hr/>", unsafe_allow_html=True)



# 6. DYNAMIC DRILL-DOWN SUB WORKSPACES

if st.session_state.selected_module:

    current_mod = st.session_state.selected_module

    

    # SYSTEM INTERACTION 1: STRATEGIC PLAYBOOKS (Upgraded with clean Dropdown Design System)

    if current_mod in ["Smart Speaker", "Merchant Lending"]:

        st.markdown('<div class="app-brand-tag" style="margin-bottom:6px;">Target Competition Matrices</div>', unsafe_allow_html=True)

        

        comp_options = ["Select Competitor...", "Paytm", "BharatPe", "Google Pay", "Banks"]

        

        # Clean Premium High Contrast SelectBox replacement

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

                            {"".join([f"<li style='color: #1B5E20; font-size:14px; margin-bottom:8px;'>✅ {pt}</li>" for pt in
