import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Career Guidance",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

.stApp{
    background: linear-gradient(
        135deg,
        #fbcfe8,
        #e9d5ff,
        #ddd6fe
    );
}

/* SIDEBAR */

section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #ec4899,
        #c026d3,
        #7c3aed
    );
}

section[data-testid="stSidebar"] *{
    color:white !important;
}

section[data-testid="stSidebar"]::before{
    content:"🎓 Placement AI System";
    display:block;
    text-align:center;
    font-size:28px;
    font-weight:bold;
    padding-top:25px;
    padding-bottom:25px;
    color:white;
}

/* HERO */

.hero{
    background: linear-gradient(
        135deg,
        #ec4899,
        #7c3aed
    );

    padding:40px;
    border-radius:25px;
    text-align:center;
    color:white;
    margin-bottom:25px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.15);
}

.hero h1{
    font-size:50px;
    font-weight:bold;
}

.hero p{
    font-size:20px;
}

/* CARD */

.card{
    background:rgba(255,255,255,0.7);
    backdrop-filter:blur(10px);
    padding:25px;
    border-radius:20px;
    box-shadow:0px 8px 20px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

.section-title{
    text-align:center;
    color:#7c3aed;
    font-size:36px;
    font-weight:bold;
    margin-top:20px;
    margin-bottom:20px;
}

/* BUTTON */

.stButton button{
    width:100%;
    height:50px;
    border:none;
    border-radius:12px;
    color:white;
    font-size:18px;
    font-weight:bold;
    background:linear-gradient(
        90deg,
        #ec4899,
        #7c3aed
    );
}

.footer{
    text-align:center;
    margin-top:40px;
    color:#7c3aed;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================

st.markdown("""
<div class="hero">

<h1>🤖 Career Guidance Assistant</h1>

<p>
Get AI Inspired Career Advice For Placements & Interviews
</p>

</div>
""", unsafe_allow_html=True)

# =========================
# INTRO
# =========================

st.markdown("""
<div class="card">

<h2 style="color:#7c3aed;">
🎯 Placement Success Guide
</h2>

<p>

This assistant helps students understand:

✅ Placement Preparation

✅ Interview Readiness

✅ Internship Importance

✅ Software Development Skills

✅ Machine Learning Career Path

✅ Communication Skills Improvement

</p>

</div>
""", unsafe_allow_html=True)

# =========================
# CAREER ASSISTANT
# =========================

st.markdown(
    "<h1 class='section-title'>💡 Ask Career Questions</h1>",
    unsafe_allow_html=True
)

selected_question = st.selectbox(
    "Choose a Question",
    [
        "Select a Question",
        "How can I improve my placement chances?",
        "Why is CGPA important?",
        "Why are internships important?",
        "How can I improve communication skills?",
        "How many projects should I complete?",
        "Skills required for Software Developer?",
        "Skills required for Machine Learning Engineer?",
        "How should I prepare for interviews?"
    ]
)

if selected_question == "How can I improve my placement chances?":

    st.success("""
✅ Improve CGPA

✅ Complete internships

✅ Build quality projects

✅ Practice coding

✅ Improve communication skills

✅ Attend mock interviews
""")

elif selected_question == "Why is CGPA important?":

    st.success("""
📚 CGPA is used by many companies for initial screening.

🎯 A CGPA above 7.5 increases placement opportunities.

🚀 Higher CGPA improves eligibility.
""")

elif selected_question == "Why are internships important?":

    st.success("""
💼 Internships provide industry exposure.

📈 Improve practical skills.

🚀 Strengthen your resume.
""")

elif selected_question == "How can I improve communication skills?":

    st.success("""
🗣 Public Speaking

👥 Group Discussions

🎤 Presentations

🎯 Mock Interviews

👂 Active Listening
""")

elif selected_question == "How many projects should I complete?":

    st.success("""
💻 Build 3-5 quality projects.

🚀 Focus on real-world problems.

📂 Upload projects to GitHub.
""")

elif selected_question == "Skills required for Software Developer?":

    st.success("""
🐍 Python / Java

📚 Data Structures

🗄 SQL & DBMS

🌐 Web Development

⚡ Problem Solving
""")

elif selected_question == "Skills required for Machine Learning Engineer?":

    st.success("""
🤖 Machine Learning

🐍 Python

📊 Pandas

📈 Data Visualization

🧠 Statistics

⚙ Scikit-Learn
""")

elif selected_question == "How should I prepare for interviews?":

    st.success("""
✅ Self Introduction

✅ Technical Concepts

✅ Project Explanation

✅ Aptitude Questions

✅ HR Questions

✅ Mock Interviews
""")

else:
    st.info("👆 Select a question from the dropdown.")

# =========================
# QUICK TIPS
# =========================

st.markdown(
    "<h1 class='section-title'>🚀 Quick Success Tips</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">

⭐ Maintain CGPA Above 7.5

⭐ Complete At Least 2 Internships

⭐ Build 5+ Projects

⭐ Practice Coding Daily

⭐ Improve Communication Skills

⭐ Attend Mock Interviews

⭐ Maintain LinkedIn & GitHub Profiles

</div>
""", unsafe_allow_html=True)

# =========================
# NAVIGATION
# =========================

col1, col2 = st.columns([8,1])

with col1:
    if st.button("⬅ Previous"):
        st.switch_page("pages/4_Visualizations.py")

with col2:
    if st.button("Next ➡"):
        st.switch_page("pages/6_Placement Awareness.py")

# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

<h3>💜 AI Powered Career Guidance Assistant</h3>

<p>
Designed & Developed By Rakshana R
</p>

</div>
""", unsafe_allow_html=True)