import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* GOOGLE FONT */

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* GLOBAL */

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */

.stApp{
    background: linear-gradient(
        135deg,
        #fbcfe8,
        #e9d5ff,
        #ddd6fe
    );
}

/* =========================
SIDEBAR
========================= */

section[data-testid="stSidebar"]{

    background: linear-gradient(
        180deg,
        #ec4899,
        #c026d3,
        #7c3aed
    );

    color: white;
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] *{
    color: white !important;
}

/* SIDEBAR TITLE */

section[data-testid="stSidebar"]::before{

    content: "🎓 Placement AI System";

    display: block;

    font-size: 28px;

    font-weight: bold;

    text-align: center;

    padding-top: 30px;

    padding-bottom: 30px;
}

/* NAVIGATION */

section[data-testid="stSidebarNav"] a{

    border-radius: 14px;

    margin: 8px;

    padding: 12px 18px;

    transition: 0.3s;

    font-size: 17px;

    font-weight: 500;
}

/* HOVER */

section[data-testid="stSidebarNav"] a:hover{

    background: rgba(255,255,255,0.18);

    transform: translateX(5px);
}

/* ACTIVE PAGE */

section[data-testid="stSidebarNav"] a[aria-current="page"]{

    background: rgba(255,255,255,0.25);

    border-left: 5px solid white;
}

/* =========================
METRICS
========================= */

div[data-testid="metric-container"]{

    background: rgba(255,255,255,0.45);

    border-radius: 20px;

    padding: 15px;

    box-shadow: 0 8px 20px rgba(0,0,0,0.1);

    backdrop-filter: blur(10px);
}

/* =========================
CARD
========================= */

.card{

    background: rgba(255,255,255,0.55);

    backdrop-filter: blur(12px);

    padding: 30px;

    border-radius: 25px;

    text-align: center;

    box-shadow: 0 8px 20px rgba(0,0,0,0.1);

    transition: 0.4s;

    margin-bottom: 20px;

    min-height: 280px;
}

/* CARD HOVER */

.card:hover{

    transform: translateY(-10px);

    box-shadow: 0 15px 30px rgba(0,0,0,0.2);
}

/* =========================
SECTION TITLE
========================= */

.section-title{

    text-align: center;

    color: #7c3aed;

    font-size: 42px;

    font-weight: bold;

    margin-top: 40px;

    margin-bottom: 30px;
}

/* HERO GLOW EFFECT */

.hero-glow{
    animation: glow 2s infinite alternate;
}

@keyframes glow{

    from{
        box-shadow:0 0 20px rgba(236,72,153,0.4);
    }

    to{
        box-shadow:0 0 40px rgba(124,58,237,0.8);
    }
}

/* CARD FADE IN */

@keyframes fadeIn {

    from{
        opacity:0;
        transform:translateY(25px);
    }

    to{
        opacity:1;
        transform:translateY(0px);
    }
}

.card{
    animation: fadeIn 1s ease;
}
            
/* =========================
BUTTON
========================= */

.stButton button{

    width: 100%;

    height: 55px;

    border-radius: 14px;

    border: none;

    font-size: 60px;

    font-weight: bold;

    color: white;

    background: linear-gradient(
        90deg,
        #ec4899,
        #7c3aed
    );

    transition: 0.3s;
}

/* BUTTON HOVER */

.stButton button:hover{

    transform: scale(1.03);

    background: linear-gradient(
        90deg,
        #db2777,
        #6d28d9
    );
}

/* =========================
FLOAT ANIMATION
========================= */

@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(-12px);
}

100%{
transform:translateY(0px);
}

}

.float{

animation: float 4s ease-in-out infinite;
}

/* FOOTER */

.footer{

    text-align: center;

    margin-top: 40px;

    color: #7c3aed;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================

col1, col2 = st.columns([1.5,1])

with col1:

    st.markdown("""
    <div style="
    background: linear-gradient(135deg,#ec4899,#7c3aed);
    padding:30px;
    border-radius:30px;
    color:white;
    text-align:center;
    margin-top:40px;
    box-shadow:0 10px 30px rgba(0,0,0,0.15);
    " class="float hero-glow">

    <h1 style='font-size:55px;'>

    🤖 Welcome

    </h1>
                
    <h3 style="font-size:40px; font-weight:bold;">

    🤖 AI Placement Prediction

    </h3>

    <br>

    <p style="font-size:28px; line-height:2;">

    Analyze student performance and predict placement chances
    using Machine Learning & Artificial Intelligence.

    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div style="text-align:center; margin-top:70px;">

    <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=800"
    class="float"
    style="
    width:360px;
    height:360px;
    border-radius:50%;
    object-fit:cover;
    border:10px solid rgba(255,255,255,0.4);
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
    ">

    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<marquee
behavior="scroll"
direction="left"
scrollamount="8"
style="
font-size:22px;
font-weight:bold;
color:#7c3aed;
margin-top:20px;
margin-bottom:20px;
">

🚀 AI Powered Placement Prediction System •
📊 Smart Analytics Dashboard •
🎯 Career Guidance Platform •
🤖 Machine Learning Based Predictions •
💼 Placement Readiness Analysis •
📈 Student Performance Tracking •

</marquee>
""", unsafe_allow_html=True)

# =========================
# METRICS
# =========================

st.markdown("<br><br>", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric("🎓 Students", "1200+")

with m2:
    st.metric("📈 Accuracy", "95%")

with m3:
    st.metric("🤖 Predictions", "500+")

with m4:
    st.metric("🏆 Placements", "850+")

# =========================
# FEATURES
# =========================

st.markdown(
    "<h1 class='section-title'>🚀 Platform Features</h1>",
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class='card'>

    <h1>🤖</h1>

    <h2 style="color:#7c3aed;">
    AI Prediction
    </h2>

    <p style="font-size:18px; line-height:1.8;">

    Predict placement chances using Machine Learning algorithms.

    </p>

    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class='card'>

    <h1>📊</h1>

    <h2 style="color:#7c3aed;">
    Analytics Dashboard
    </h2>

    <p style="font-size:18px; line-height:1.8;">

    Interactive charts and student performance analysis.

    </p>

    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class='card'>

    <h1>🎯</h1>

    <h2 style="color:#7c3aed;">
    Career Guidance
    </h2>

    <p style="font-size:18px; line-height:1.8;">

    Get smart AI suggestions to improve placement opportunities.

    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================
# WHY CHOOSE US
# =========================

st.markdown(
    "<h1 class='section-title'>🌟 Why Choose Our Platform?</h1>",
    unsafe_allow_html=True
)

w1, w2, w3 = st.columns(3)

with w1:

    st.markdown("""
    <div class='card'>

    <h1>⚡</h1>

    <h2>Fast Prediction</h2>

    <p>
    Instant AI-based placement analysis system.
    </p>

    </div>
    """, unsafe_allow_html=True)

with w2:

    st.markdown("""
    <div class='card'>

    <h1>🧠</h1>

    <h2>Smart AI</h2>

    <p>
    Intelligent Machine Learning prediction engine.
    </p>

    </div>
    """, unsafe_allow_html=True)

with w3:

    st.markdown("""
    <div class='card'>

    <h1>🚀</h1>

    <h2>Career Growth</h2>

    <p>
    Improve placement opportunities with AI guidance.
    </p>

    </div>
    """, unsafe_allow_html=True)

# =========================
# QUOTE SECTION
# =========================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(135deg,#ec4899,#7c3aed);
padding:45px;
border-radius:30px;
text-align:center;
color:white;
box-shadow:0 10px 30px rgba(0,0,0,0.15);
">

<h1 style="font-size:45px;">

✨ Success Begins With Smart Preparation

</h1>

<p style="font-size:24px; line-height:2;">

AI Powered Placement Prediction & Career Guidance Platform

</p>

</div>
""", unsafe_allow_html=True)

# =========================
# START BUTTON
# =========================

st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    if st.button("🚀 Click here to start prediction "):
        st.switch_page(
            "pages/2_Student_Details.py"
        )
    

# =========================
# FOOTER
# =========================

st.markdown("""
<div class='footer'>

<h2>

💜 AI Powered Placement Prediction System

</h2>

<p style="font-size:18px;">

Designed & Developed By Rakshana R

</p>

</div>
""", unsafe_allow_html=True)