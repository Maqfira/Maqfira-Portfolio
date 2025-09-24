import streamlit as st
import os
from home import show_home
from skills import show_skills
from experience import show_experience
from qualification import show_qualification
from projects import show_projects

# --- Page settings ---
st.set_page_config(
    page_title="Maqfira Sarwar — Portfolio",
    page_icon="✒️",
    layout="wide"
)

# --- Global CSS (background, sidebar, buttons, fonts) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    /* Main background */
    .stApp {
        background-image: linear-gradient(
            90deg,
            transparent 0%, transparent 88%,
            rgba(200, 200, 200,0.07) 88%, rgba(200, 200, 200,0.07) 93%,
            transparent 93%, transparent 100%
        ),
        linear-gradient(90deg, rgb(0,0,0), rgb(0,0,0));
    }

    /* Sidebar background */
    section[data-testid="stSidebar"] {
        background-color: rgba(0,0,0,0.9);
    }

    /* Text color */
    .stApp, .stMarkdown, .stText, .stTitle {
        color: #40E0D0;
    }

    /* Buttons */
        .stButton>button {
        background-color: black !important;  /* Force black background */
        color: #40E0D0 !important;           /* Turquoise text */
        border: 2px solid #40E0D0 !important;
        border-radius: 10px;
        padding: 8px 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: rgba(64,224,208,0.1);
        border-color: white;
        transform: scale(1.05);
    }
    .stButton>button:active,
    .stButton>button:focus {
        color: #40E0D0 !important;
        border-color: #40E0D0 !important;
        box-shadow: 0 0 5px #40E0D0;
        outline: none !important;
    }

    /* Sidebar text */
    .sidebar-title {
        color:white;
        font-weight:800;
        margin-bottom:15px;
        font-size:28px;
    }
    .sidebar-link {
        display:block;
        font-size:20px;
        color:#40E0D0;
        text-decoration:none;
        padding:8px 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .sidebar-link:hover {
        color:#00BFFF;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar Navigation ---
st.sidebar.markdown("<h class='sidebar-title'>More About Me</h>", unsafe_allow_html=True)

if "section" not in st.session_state:
    st.session_state.section = "Home"

if st.sidebar.button("Home", key="home_btn"):
    st.session_state.section = "Home"
if st.sidebar.button("Qualification", key="qual_btn"):
    st.session_state.section = "Qualification"
if st.sidebar.button("Skills", key="skills_btn"):
    st.session_state.section = "Skills"
if st.sidebar.button("Experience", key="exp_btn"):
    st.session_state.section = "Experience"
if st.sidebar.button("Projects", key="proj_btn"):
    st.session_state.section = "Projects"

# --- Render selected section ---
if st.session_state.section == "Home":
    show_home()
elif st.session_state.section == "Skills":
    show_skills()
elif st.session_state.section == "Experience":
    show_experience()
elif st.session_state.section == "Qualification":
    show_qualification()
elif st.session_state.section == "Projects":
    show_projects()
