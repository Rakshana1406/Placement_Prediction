import streamlit as st

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

/* =========================
BUTTON
========================= */

.stButton button{

    width: 100%;

    height: 55px;

    border-radius: 14px;

    border: none;

    font-size: 20px;

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
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Placement Guide",
    page_icon="🎯",
    layout="wide"
)

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div style="
background: linear-gradient(135deg,#ec4899,#c026d3,#7c3aed);
padding:40px;
border-radius:25px;
text-align:center;
color:white;
margin-bottom:20px;
">

<h1>🎯 Placement Awareness </h1>

<p style="font-size:20px;">
Helping Students Prepare for Successful Career Opportunities
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# WHAT IS PLACEMENT
# =========================

st.markdown("## 🎓 What is Placement?")

st.info("""
Placement is the process through which students obtain job opportunities
from companies through campus recruitment drives and hiring programs.

A successful placement depends on academic performance, technical skills,
communication abilities, internships, projects, aptitude, and interview performance.

Campus placements help students begin their professional careers immediately
after graduation.
""")

# =========================
# IMPORTANCE OF PLACEMENT
# =========================

st.markdown("## 💼 Importance of Placement")

st.success("""
• Provides career opportunities after graduation.

• Helps students gain industry exposure.

• Improves professional growth and confidence.

• Bridges the gap between academics and industry requirements.

• Creates financial stability and career development opportunities.
""")

# =========================
# FACTORS AFFECTING PLACEMENT
# =========================

st.markdown("## 📊 Factors Affecting Placement")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎓 CGPA", "Important")

with col2:
    st.metric("💻 Projects", "Very Important")

with col3:
    st.metric("💼 Internships", "Highly Preferred")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("🗣 Communication", "Critical")

with col5:
    st.metric("🧠 Aptitude", "Important")

with col6:
    st.metric("🤝 Soft Skills", "Essential")

# =========================
# PLACEMENT ROADMAP
# =========================

st.markdown("## 🚀 Placement Preparation Roadmap")

st.warning("""
📍 First Year

• Focus on communication skills.

• Learn programming fundamentals.

• Improve academic performance.

--------------------------------------------

📍 Second Year

• Learn Python, Java, or Web Development.

• Start building mini projects.

• Participate in technical events.

--------------------------------------------

📍 Third Year

• Complete internships.

• Earn certifications.

• Build real-world projects.

• Improve coding skills.

--------------------------------------------

📍 Final Year

• Practice aptitude and reasoning.

• Prepare for technical interviews.

• Attend mock interviews.

• Build a strong resume and LinkedIn profile.
""")

# =========================
# TOP CAREER DOMAINS
# =========================

st.markdown("## 🌟 Popular Career Opportunities")

col1, col2 = st.columns(2)

with col1:

    st.success("💻 Software Developer")

    st.success("📊 Data Analyst")

    st.success("🤖 Machine Learning Engineer")

    st.success("🧠 AI Engineer")

with col2:

    st.success("🌐 Web Developer")

    st.success("☁️ Cloud Engineer")

    st.success("🔒 Cyber Security Analyst")

    st.success("📈 Business Analyst")

# =========================
# SKILLS COMPANIES EXPECT
# =========================

st.markdown("## 🏢 Skills Expected by Companies")

st.info("""
✅ Problem Solving Skills

✅ Communication Skills

✅ Teamwork and Collaboration

✅ Programming Knowledge

✅ Technical Project Experience

✅ Internship Experience

✅ Aptitude and Logical Reasoning

✅ Leadership and Time Management
""")

# =========================
# PLACEMENT TIPS
# =========================

st.markdown("## 💡 Placement Success Tips")

st.success("""
✅ Maintain a good CGPA.

✅ Complete internships regularly.

✅ Build real-world projects.

✅ Improve communication skills.

✅ Practice aptitude and coding questions.

✅ Keep LinkedIn and resume updated.

✅ Attend mock interviews.

✅ Earn industry-relevant certifications.

✅ Participate in hackathons and workshops.

✅ Stay consistent with learning.
""")

# =========================
# MOTIVATIONAL SECTION
# =========================

st.markdown("""
<div style="
background: linear-gradient(135deg,#ec4899,#7c3aed);
padding:40px;
border-radius:25px;
text-align:center;
color:white;
margin-top:30px;
">

<h1>✨ Success Comes to Those Who Prepare</h1>

<p style="font-size:22px; line-height:2;">

Keep Learning • Keep Building • Keep Growing 🚀

</p>

</div>
""", unsafe_allow_html=True)

# =========================
# NAVIGATION
# =========================

st.markdown("---")

col1, col2 = st.columns([8,1])

with col1:
    if st.button("⬅ Previous"):
        st.switch_page("pages/5_Career_Guidance.py")

with col2:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.markdown("""
<div style="text-align:center;">

<h3>💜 AI Powered Placement Prediction System</h3>

<p>
Designed & Developed By Muthu Rakshana R
</p>

</div>
""", unsafe_allow_html=True)