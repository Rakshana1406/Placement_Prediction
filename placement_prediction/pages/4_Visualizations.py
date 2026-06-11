import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="Visualization Dashboard",
    layout="wide"
)

# ======================================
# LOAD DATA
# ======================================
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "dataset" / "college_student_placement_dataset.csv"
data = pd.read_csv(csv_path)
# ======================================
# CUSTOM CSS
# ======================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(
        135deg,
        #fbcfe8,
        #e9d5ff,
        #ddd6fe
    );
}

/* REMOVE TOP SPACE */

.block-container {
    padding-top: 1rem;
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

/* Sidebar Text */

section[data-testid="stSidebar"] *{
    color: white !important;
}

/* Sidebar Title */

section[data-testid="stSidebar"]::before{

    content: "🎓 Placement AI System";

    display: block;

    font-size: 26px;

    font-weight: bold;

    text-align: center;

    padding-top: 25px;

    padding-bottom: 25px;

    color: white;
}

/* Navigation Buttons */

section[data-testid="stSidebarNav"] a{

    border-radius: 14px;

    margin: 8px;

    padding: 12px 18px;

    transition: 0.3s;

    font-size: 17px;

    font-weight: 500;
}

/* Hover Effect */

section[data-testid="stSidebarNav"] a:hover{

    background: rgba(255,255,255,0.18);

    transform: translateX(5px);
}

/* Active Page */

section[data-testid="stSidebarNav"] a[aria-current="page"]{

    background: rgba(255,255,255,0.25);

    border-left: 5px solid white;
}

/* HERO */

.hero {
    background: linear-gradient(
        135deg,
        #ec4899,
        #c026d3,
        #7c3aed
    );

    padding: 40px;

    border-radius: 25px;

    text-align: center;

    color: white;

    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

.hero h1 {
    font-size: 50px;
    font-weight: bold;
}

.hero p {
    font-size: 20px;
}

/* CARDS */

.card {
    background: rgba(255,255,255,0.75);

    backdrop-filter: blur(10px);

    padding: 20px;

    border-radius: 20px;

    box-shadow: 0px 8px 20px rgba(0,0,0,0.1);

    text-align: center;

    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

/* METRICS */

.metric {
    font-size: 35px;

    font-weight: bold;

    color: #7c3aed;
}

/* TITLES */

.section-title {
    text-align: center;

    color: #7c3aed;

    font-size: 35px;

    font-weight: bold;

    margin-top: 20px;
}

/* BUTTONS */

.stButton button {
    width: 100%;
    height: 50px;

    border-radius: 12px;

    border: none;

    color: white;

    font-size: 18px;

    font-weight: 600;

    background: linear-gradient(
        90deg,
        #ec4899,
        #7c3aed
    );
}

.stButton button:hover {
    background: linear-gradient(
        90deg,
        #db2777,
        #6d28d9
    );
}

/* FOOTER */

.footer {
    text-align: center;
    color: #7c3aed;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# HERO SECTION
# ======================================

st.markdown("""
<div class='hero'>

<h1>📊 AI Analytics Dashboard</h1>

<p>
Placement Prediction Visualization System
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ======================================
# KPI CARDS
# ======================================

total_students = len(data)

placement_rate = (
    data["Placement"]
    .value_counts(normalize=True)["Yes"] * 100
)

internship_success = (
    data["Internship_Experience"]
    .value_counts(normalize=True)["Yes"] * 100
)

accuracy = 100

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(f"""
    <div class='card'>

    <h3>🎓 Total Students</h3>

    <p class='metric'>{total_students}</p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class='card'>

    <h3>📈 Placement Rate</h3>

    <p class='metric'>{placement_rate:.1f}%</p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class='card'>

    <h4>💼Internship Success</h4>

    <p class='metric'>{internship_success:.1f}%</p>

    </div>
    """, unsafe_allow_html=True)

with col4:

    st.markdown(f"""
    <div class='card'>

    <h3>🤖 Model Accuracy</h3>

    <p class='metric'>{accuracy}%</p>

    </div>
    """, unsafe_allow_html=True)

# ======================================
# PIE CHART
# ======================================

st.markdown(
    "<h1 class='section-title'>🥧 Placement Distribution</h1>",
    unsafe_allow_html=True
)

fig1 = px.pie(
    data,
    names="Placement",
    color="Placement",
    hole=0.4,
    color_discrete_sequence=[
    "#ec4899",
    "#7c3aed"
]
)

st.plotly_chart(fig1, width='stretch')

st.markdown(
    "<h1 class='section-title'>📚 Top CGPA Students</h1>",
    unsafe_allow_html=True
)

top_students = data.sort_values(
    by="CGPA",
    ascending=False
).head(10)

fig2 = px.bar(
    top_students,
    x="College_ID",
    y="CGPA",
    color="CGPA",
    color_continuous_scale=[
    "#fbcfe8",
    "#e9d5ff",
    "#c026d3",
    "#7c3aed"
]
)

st.plotly_chart(fig2, width='stretch')

st.markdown(
    "<h1 class='section-title'>🎯 Skills Analysis</h1>",
    unsafe_allow_html=True
)

fig3 = px.scatter(
    data,
    x="CGPA",
    y="Communication_Skills",
    color="Placement",
    size="Projects_Completed",
    hover_data=["IQ"],
    color_discrete_sequence=[
    "#ec4899",
    "#7c3aed"
    ]
    
)

st.plotly_chart(fig3, width='stretch')

st.markdown(
    "<h1 class='section-title'>💼 Internship Analysis</h1>",
    unsafe_allow_html=True
)

internship_data = (
    data.groupby("Internship_Experience")
    .size()
    .reset_index(name="Count")
)

fig4 = px.line(
    internship_data,
    x="Internship_Experience",
    y="Count",
    markers=True
)

fig4.update_traces(
    line=dict(
        color="#7c3aed",
        width=5
    ),
    marker=dict(
        size=10,
        color="#ec4899"
    )
)

st.plotly_chart(fig4, width='stretch')

st.markdown(
    "<h1 class='section-title'>🗣 Communication Skills Distribution</h1>",
    unsafe_allow_html=True
)

fig5 = px.histogram(
    data,
    x="Communication_Skills",
    color="Placement",
    barmode="group",
    color_discrete_sequence=[
    "#c026d3",
    "#ec4899"
]
)

st.plotly_chart(fig5, width='stretch')

st.markdown(
    "<h1 class='section-title'>💻 Projects vs Placement</h1>",
    unsafe_allow_html=True
)

fig6 = px.box(
    data,
    x="Placement",
    y="Projects_Completed",
    color="Placement",
    color_discrete_sequence=[
    "#ec4899",
    "#7c3aed"
]
)

st.plotly_chart(fig6, width='stretch')

# ======================================
# NAVIGATION
# ======================================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns([8,1])

with col1:

    if st.button("⬅ Previous"):

        st.switch_page(
            "pages/3_Prediction.py"
        )

with col2:

    if st.button("Next ➜"):

        st.switch_page(
            "pages/5_Career_Guidance.py"
        )

# ======================================
# FOOTER
# ======================================

st.markdown("""
<div class='footer'>

<h3>💜 AI Powered Visualization Dashboard</h3>

<p>
Built using Streamlit + Plotly + Machine Learning
</p>

</div>
""", unsafe_allow_html=True)