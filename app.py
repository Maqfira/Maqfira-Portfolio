import streamlit as st
import os
import time
from PIL import Image, ImageOps, ImageDraw
import io
import base64
from home import show_home
from skills import show_skills
from experience import show_experience
from qualification import show_qualification
from projects import show_projects

st.set_page_config(page_title="Maqfira Sarwar — Portfolio", page_icon="✒️", layout="wide")
st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
        /* Main background */
        .stApp {
      
            background-image: linear-gradient(90deg, transparent 0%, transparent 88%,rgba(200, 200, 200,0.07) 88%, rgba(200, 200, 200,0.07) 93%,transparent 93%, transparent 100%),linear-gradient(135deg, transparent 0%, transparent 83%,rgba(200, 200, 200,0.07) 83%, rgba(200, 200, 200,0.07) 91%,transparent 91%, transparent 100%),linear-gradient(0deg, transparent 0%, transparent 43%,rgba(200, 200, 200,0.07) 43%, rgba(200, 200, 200,0.07) 50%,transparent 50%, transparent 100%),linear-gradient(135deg, transparent 0%, transparent 16%,rgba(200, 200, 200,0.07) 16%, rgba(200, 200, 200,0.07) 56%,transparent 56%, transparent 100%),linear-gradient(90deg, rgb(0,0,0),rgb(0,0,0));;
        # background-color:#121212
        }
        /* Sidebar background */
        section[data-testid="stSidebar"] {

                   
        background-image: linear-gradient(231deg, rgba(233, 233, 233, 0.01) 0%, rgba(233, 233, 233, 0.01) 25%,rgba(10, 10, 10, 0.01) 25%, rgba(10, 10, 10, 0.01) 50%,rgba(237, 237, 237, 0.01) 50%, rgba(237, 237, 237, 0.01) 75%,rgba(200, 200, 200, 0.01) 75%, rgba(200, 200, 200, 0.01) 100%),linear-gradient(344deg, rgba(2, 2, 2, 0.03) 0%, rgba(2, 2, 2, 0.03) 20%,rgba(10, 10, 10, 0.03) 20%, rgba(10, 10, 10, 0.03) 40%,rgba(100, 100, 100, 0.03) 40%, rgba(100, 100, 100, 0.03) 60%,rgba(60, 60, 60, 0.03) 60%, rgba(60, 60, 60, 0.03) 80%,rgba(135, 135, 135, 0.03) 80%, rgba(135, 135, 135, 0.03) 100%),linear-gradient(148deg, rgba(150, 150, 150, 0.03) 0%, rgba(150, 150, 150, 0.03) 14.286%,rgba(15, 15, 15, 0.03) 14.286%, rgba(15, 15, 15, 0.03) 28.572%,rgba(74, 74, 74, 0.03) 28.572%, rgba(74, 74, 74, 0.03) 42.858%,rgba(175, 175, 175, 0.03) 42.858%, rgba(175, 175, 175, 0.03) 57.144%,rgba(16, 16, 16, 0.03) 57.144%, rgba(16, 16, 16, 0.03) 71.42999999999999%,rgba(83, 83, 83, 0.03) 71.43%, rgba(83, 83, 83, 0.03) 85.71600000000001%,rgba(249, 249, 249, 0.03) 85.716%, rgba(249, 249, 249, 0.03) 100.002%),linear-gradient(122deg, rgba(150, 150, 150, 0.01) 0%, rgba(150, 150, 150, 0.01) 20%,rgba(252, 252, 252, 0.01) 20%, rgba(252, 252, 252, 0.01) 40%,rgba(226, 226, 226, 0.01) 40%, rgba(226, 226, 226, 0.01) 60%,rgba(49, 49, 49, 0.01) 60%, rgba(49, 49, 49, 0.01) 80%,rgba(94, 94, 94, 0.01) 80%, rgba(94, 94, 94, 0.01) 100%),linear-gradient(295deg, rgba(207, 207, 207, 0.02) 0%, rgba(207, 207, 207, 0.02) 25%,rgba(47, 47, 47, 0.02) 25%, rgba(47, 47, 47, 0.02) 50%,rgba(142, 142, 142, 0.02) 50%, rgba(142, 142, 142, 0.02) 75%,rgba(76, 76, 76, 0.02) 75%, rgba(76, 76, 76, 0.02) 100%),linear-gradient(73deg, rgba(81, 81, 81, 0.03) 0%, rgba(81, 81, 81, 0.03) 12.5%,rgba(158, 158, 158, 0.03) 12.5%, rgba(158, 158, 158, 0.03) 25%,rgba(136, 136, 136, 0.03) 25%, rgba(136, 136, 136, 0.03) 37.5%,rgba(209, 209, 209, 0.03) 37.5%, rgba(209, 209, 209, 0.03) 50%,rgba(152, 152, 152, 0.03) 50%, rgba(152, 152, 152, 0.03) 62.5%,rgba(97, 97, 97, 0.03) 62.5%, rgba(97, 97, 97, 0.03) 75%,rgba(167, 167, 167, 0.03) 75%, rgba(167, 167, 167, 0.03) 87.5%,rgba(22, 22, 22, 0.03) 87.5%, rgba(22, 22, 22, 0.03) 100%),linear-gradient(90deg, hsl(137,0%,23%),hsl(137,0%,23%));
        }
        /* Text color */
        .stApp, .stMarkdown, .stText, .stTitle {
            color: #40E0D0;
        }
        
#         }
        .stButton>button {
    background-color:black
    #   rgba(0,0,0,0); /* fully transparent */
    color: #40E0D0;                  /* text color */
    border: 2px solid #40E0D0;       /* optional border */
    border-radius: 10px;              /* rounded corners */
    padding: 8px 20px;
    transition: 0.3s;
}

/* Hover effect */
.stButton>button:hover {
    background-color:
    rgba(64,224,208,0.1); /* slightly visible on hover */
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

        </style>
        """,
        unsafe_allow_html=True
    )


# --- Sidebar CSS ---
st.sidebar.markdown(
    """
    
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
        .sidebar-title{
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
       /* Media queries for sidebar responsiveness */
        @media (max-width: 600px) {  /* Mobile */
            .sidebar-title {
                font-size: 24px;
            }
            .sidebar-link {
                font-size: 18px;
                padding: 6px 0;
            }
        }
        @media (min-width: 601px) and (max-width: 1024px) {  /* Tablet */
            .sidebar-title {
                font-size: 26px;
            }
            .sidebar-link {
                font-size: 19px;
                padding: 7px 0;
            }
        }
        /* Responsive adjustments */
    @media (max-width: 600px) {  /* Mobile */
        .sidebar-text {
            font-size: 24px;
            margin-bottom: 10px;
        }
        .sidebar-link {
            font-size: 18px;
            padding: 6px 0;
        }
    }
    @media (min-width: 601px) and (max-width: 1024px) {  /* Tablet */
        .sidebar-text {
            font-size: 26px;
            margin-bottom: 12px;
        }
        .sidebar-link {
            font-size: 19px;
            padding: 7px 0;
        }
    }
    </style>
    </style>
    <h class="sidebar-title">More About Me</h>
    """,
    unsafe_allow_html=True
)

# Initialize session state
if "section" not in st.session_state:
    st.session_state.section = "Home"


# Sidebar links as buttons (but styled as text)
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

# --- Render the selected section ---
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