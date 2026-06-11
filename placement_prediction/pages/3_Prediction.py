import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime
import plotly.express as px

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Placement Prediction",
    page_icon="🎯",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "model",
    "placement_model.pkl"
)

model = joblib.load(model_path)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* GLOBAL */

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

/* BACKGROUND */

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
    color: white !important;
}

section[data-testid="stSidebar"]::before{

    content: "🎓 Placement AI System";

    display:block;

    text-align:center;

    font-size:28px;

    font-weight:bold;

    padding-top:30px;

    padding-bottom:30px;
            
    color:white;
}

/* NAVIGATION */

section[data-testid="stSidebarNav"] a{

    border-radius:14px;

    margin:8px;

    padding:12px 18px;

    transition:0.3s;

    font-size:17px;
}

section[data-testid="stSidebarNav"] a:hover{

    background: rgba(255,255,255,0.2);

    transform: translateX(5px);
}

section[data-testid="stSidebarNav"] a[aria-current="page"]{

    background: rgba(255,255,255,0.25);

    border-left:5px solid white;
}

/* HERO */

.hero{

    background: linear-gradient(
        135deg,
        #ec4899,
        #7c3aed
    );

    padding:50px;

    border-radius:30px;

    color:white;

    text-align:center;

    box-shadow:0 10px 30px rgba(0,0,0,0.15);

    margin-bottom:30px;
}

/* SECTION TITLE */

.section-title{

    text-align:center;

    color:#7c3aed;

    font-size:40px;

    font-weight:bold;

    margin-top:30px;

    margin-bottom:30px;
}

/* GLASS CARD */

.card{

    background: rgba(255,255,255,0.55);

    backdrop-filter: blur(12px);

    padding:30px;

    border-radius:25px;

    box-shadow:0 8px 20px rgba(0,0,0,0.1);

    margin-bottom:20px;
}

/* METRICS */

div[data-testid="metric-container"]{

    background: rgba(255,255,255,0.55);

    border-radius:20px;

    padding:15px;

    box-shadow:0 8px 20px rgba(0,0,0,0.1);
}

/* BUTTON */

.stButton button{

    width:100%;

    height:55px;

    border:none;

    border-radius:14px;

    color:white;

    font-size:20px;

    font-weight:bold;

    background: linear-gradient(
        90deg,
        #ec4899,
        #7c3aed
    );

    transition:0.3s;
}

.stButton button:hover{

    transform: scale(1.02);

    background: linear-gradient(
        90deg,
        #db2777,
        #6d28d9
    );
}

/* FLOAT ANIMATION */

@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(-10px);
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

    text-align:center;

    margin-top:40px;

    color:#7c3aed;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# CHECK SESSION DATA
# ==========================================

if "student_data" not in st.session_state:

    st.warning("⚠ Please Fill Student Details First")

    st.stop()

data = st.session_state["student_data"]

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class='hero float'>

<h1 style='font-size:60px;'>

🎯 Placement Prediction Result

</h1>

<br>

<p style='font-size:24px; line-height:2;'>

AI Based Student Placement Analysis Dashboard

</p>

</div>
""", unsafe_allow_html=True)


# ==========================================
# SCORE CALCULATION
# ==========================================

total_projects = (
    data["academic_projects"] +
    data["internship_projects"]
)

score = (
    data["cgpa"] * 10 +
    data["communication"] * 5 +
    total_projects * 5 +
    data["extracurricular"] * 3 +
    data["iq"] * 0.2
)

score = int(score / 2)

# ==========================================
# STUDENT DETAILS
# ==========================================

st.markdown(
    "<h1 class='section-title'>👨‍🎓 Student Details</h1>",
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🎓 CGPA", data["cgpa"])

with col2:
    st.metric("🧠 IQ", data["iq"])

with col3:
    st.metric(
        "💻 Total Projects",
        data["academic_projects"] +
        data["internship_projects"]
    )

with col4:
    st.metric("🗣 Communication", data["communication"])

# ==========================================
# PREDICTION RESULT
# ==========================================

st.markdown(
    "<h1 class='section-title'>🤖 AI Prediction</h1>",
    unsafe_allow_html=True
)

if score < 75:

    st.error("❌ NOT PLACED")

    st.markdown("""
    <div class='card'>

    <h2 style='color:#dc2626;'>

    ❌ Reasons For Not Getting Placed

    </h2>
    """, unsafe_allow_html=True)

    reasons = []

    if data["cgpa"] < 6:
        reasons.append("⚠ Low CGPA")

    if data["communication"] < 5:
        reasons.append("⚠ Poor Communication Skills")

    if (
    data["academic_projects"] +
    data["internship_projects"]
    ) < 3:
        reasons.append(
        "⚠ Less Project Experience"
    )

    if data["internship"] == "No":
        reasons.append("⚠ No Internship Experience")

    if data["iq"] < 70:
        reasons.append("⚠ Low IQ Score")

    if len(reasons) == 0:
        reasons.append("⚠ Overall Performance Needs Improvement")

    for reason in reasons:
        st.warning(reason)

    st.markdown("</div>", unsafe_allow_html=True)

    # IMPROVEMENTS

    st.markdown("""
    <div class='card'>

    <h2 style='color:#7c3aed;'>

    📈 Things To Improve

    </h2>
    """, unsafe_allow_html=True)

    improvements = [

        "✅ Improve Communication Skills",

        "✅ Build More Real-Time Projects",

        "✅ Practice Aptitude Questions",

        "✅ Complete Internship Programs",

        "✅ Improve Resume & LinkedIn",

        "✅ Attend Mock Interviews"
    ]

    for item in improvements:
        st.success(item)

    st.markdown("</div>", unsafe_allow_html=True)



else:

    st.success("🎉 PLACED")

st.markdown("""
<div class='card' style='text-align:center;'>

<h1 style='font-size:90px;'>🏆</h1>

<h1 style='color:#16a34a;'>
Congratulations!
</h1>

<p style='font-size:24px;'>
You are Placement Ready.
</p>

</div>
""", unsafe_allow_html=True)

st.metric(
    "📈 Placement Probability",
    f"{min(round((score / 120) * 100), 100)}%"
)
st.info(
    f"💰 Desired Salary Package: {data['expected_package']} LPA"
)

st.success("🌟 Placement Readiness: Excellent")
# ==========================================
# PERFORMANCE GRAPH
# ==========================================

st.markdown(
    "<h1 class='section-title'>📊 Performance Analysis</h1>",
    unsafe_allow_html=True
)

performance_data = pd.DataFrame({

    "Category":[
        "CGPA",
        "Communication",
        "Projects",
        "Extra Curricular",
        "IQ Score"
    ],

    "Score":[
        data["cgpa"] * 10,
        data["communication"] * 10,
        (
            data["academic_projects"] +
            data["internship_projects"]
        ) * 10,
        data["extracurricular"] * 10,
        data["iq"] / 2
    ]
})

fig = px.bar(

    performance_data,

    x="Category",

    y="Score",

    color="Category",

    text="Score",

    color_discrete_sequence=[
    "#2563EB",  # CGPA - Blue
    "#10B981",  # Communication - Green
    "#F59E0B",  # Projects - Orange
    "#EF4444",  # Extra Curricular - Red
    "#8B5CF6"   # IQ - Purple
]
)

fig.update_layout(

    height=500,

    plot_bgcolor="white",

    paper_bgcolor="rgba(0,0,0,0)",

    font=dict(size=16)
)

st.plotly_chart(fig, width='stretch')

# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.markdown(
    "<h1 class='section-title'>📄 Download Report</h1>",
    unsafe_allow_html=True
)

report = f"""

PLACEMENT PREDICTION REPORT
===========================

Generated On:
{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

-----------------------------------

Student Name:
{data["name"]}

CGPA:
{data["cgpa"]}

IQ Score:
{data["iq"]}

Communication Skills:
{data["communication"]}

Academic Projects:
{data["academic_projects"]}

Internship Projects:
{data["internship_projects"]}

Total Projects:
{data["academic_projects"] + data["internship_projects"]}

Internship:
{data["internship"]}

-----------------------------------

Placement Status:

{"PLACED" if score >= 75 else "NOT PLACED"}

"""

st.download_button(

    label="⬇ Download Report",

    data=report,

    file_name="placement_report.txt",

    mime="text/plain"
)

# ==========================================
# NAVIGATION
# ==========================================

st.markdown("<br>", unsafe_allow_html=True)

b1, b2 = st.columns([8,1])

with b1:

    if st.button("⬅ Previous"):

        st.switch_page(
            "pages/2_Student_Details.py"
        )

with b2:

    if st.button("Next ➡"):

        st.switch_page(
            "pages/4_Visualizations.py"
        )

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class='footer'>

<h2>

💜 AI Powered Placement Prediction System

</h2>

<p>

Designed & Developed By Rakshana R

</p>

</div>
""", unsafe_allow_html=True)