import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Student Details",
    page_icon="👨‍🎓",
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

/* SIDEBAR NAV */

section[data-testid="stSidebarNav"] a{

    border-radius:14px;

    margin:8px;

    padding:12px 18px;

    transition:0.3s;
}

section[data-testid="stSidebarNav"] a:hover{

    background: rgba(255,255,255,0.2);

    transform: translateX(5px);
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

    box-shadow:0 10px 30px rgba(0,0,0,0.15);

    margin-bottom:30px;
}

/* FORM CARD */

.form-card{

    background: rgba(255,255,255,0.55);

    backdrop-filter: blur(12px);

    padding:35px;

    border-radius:25px;

    box-shadow:0 8px 20px rgba(0,0,0,0.1);
}

/* INPUTS */

.stTextInput input,
.stNumberInput input,
.stSelectbox div,
.stSlider {

    border-radius:12px !important;
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
}

.stButton button:hover{

    background: linear-gradient(
        90deg,
        #db2777,
        #6d28d9
    );

    transform: scale(1.02);
}

/* FLOAT */

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

/* CARD */

.tip-card{

    background: rgba(255,255,255,0.5);

    padding:25px;

    border-radius:20px;

    margin-top:20px;

    box-shadow:0 8px 20px rgba(0,0,0,0.1);
}

/* FOOTER */

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

col1, col2 = st.columns([1.5,1])

with col1:

    st.markdown("""
    <div class='hero float'>

    <h1 style='font-size:55px;'>

    👨‍🎓 Student Details

    </h1>

    <br>

    <p style='font-size:24px; line-height:2;'>

    Enter academic and skill details for
    AI-based placement prediction analysis.

    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div style="text-align:center; margin-top:40px;">

    <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=800"
    class="float"
    style="
    width:320px;
    height:320px;
    border-radius:50%;
    object-fit:cover;
    border:10px solid rgba(255,255,255,0.4);
    box-shadow:0 10px 30px rgba(0,0,0,0.2);
    ">

    </div>
    """, unsafe_allow_html=True)

# =========================
# PROGRESS BAR
# =========================



# =========================
# FORM
# =========================

st.markdown("<br>", unsafe_allow_html=True)


st.markdown("""
<h1 style='text-align:center; color:#7c3aed;'>

📋 Fill Student Information

</h1>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    name = st.text_input(
        "👤 Student Name"
    )

    cgpa = st.slider(
        "🎓 CGPA",
        0.0,
        10.0,
        7.0
    )

    iq = st.slider(
        "🧠 IQ Score",
        50,
        150,
        90
    )

    communication = st.slider(
        "🗣 Communication Skills",
        1,
        10,
        6
    )

    extracurricular = st.slider(
        "🏆 Extra Curricular Score",
        1,
        10,
        5
    )

with col2:

    academic = st.selectbox(
        "📚 Academic Performance",
        [
            "Excellent",
            "Good",
            "Average",
            "Poor"
        ]
    )

    internship = st.selectbox(
        "💼 Internship Experience",
        [
            "Yes",
            "No"
        ]
    )

    academic_projects = st.number_input(
    "📚 Academic Projects Completed",
    min_value=0,
    value=0,
    step=1
    )

    internship_projects = st.number_input(
        "💼 Internship Projects Completed",
        min_value=0,
        value=0,
        step=1
    )


    expected_package = st.selectbox(
    "💰 Expected Salary Package (LPA)",
    [
        "Below 3 LPA",
        "3 - 5 LPA",
        "5 - 8 LPA",
        "8 - 12 LPA",
        "Above 12 LPA"
    ]
    )

# =========================
# SAVE DATA
# =========================

if st.button("🚀 Predict Placement"):

    st.session_state["student_data"] = {

        "name": name,

        "cgpa": cgpa,

        "iq": iq,

        "communication": communication,

        "academic": academic,

        "internship": internship,

        "academic_projects": academic_projects,

        "internship_projects": internship_projects,

        "extracurricular": extracurricular,

        "expected_package": expected_package,
    }

    st.success("✅ Student Details Saved Successfully")

    st.switch_page(
        "pages/3_Prediction.py"
    )

st.markdown("</div>", unsafe_allow_html=True)

# =========================
# TIPS SECTION
# =========================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div class='tip-card'>

<h2 style='color:#7c3aed;'>

💡 Placement Tips

</h2>

<p style='font-size:18px; line-height:2;'>

✅ Students with strong communication skills have better placement opportunities.

<br>

✅ Real-time projects improve technical knowledge and resume strength.

<br>

✅ Internship experience increases placement probability.

<br>

✅ Good aptitude and problem-solving skills help crack interviews.

</p>

</div>
""", unsafe_allow_html=True)

# =========================
# MOTIVATIONAL QUOTE
# =========================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background: linear-gradient(135deg,#ec4899,#7c3aed);
padding:40px;
border-radius:25px;
text-align:center;
color:white;
box-shadow:0 10px 30px rgba(0,0,0,0.15);
">

<h1>

✨ Your Future Starts With Your Skills

</h1>

<p style="font-size:22px; line-height:2;">

Keep Learning • Keep Building • Keep Growing 🚀

</p>

</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================

st.markdown("""
<div class='footer'>

<h3>

💜 AI Powered Placement Prediction System

</h3>

<p>

Designed & Developed By Rakshana R

</p>

</div>
""", unsafe_allow_html=True)