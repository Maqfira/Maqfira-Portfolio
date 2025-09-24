import streamlit as st
import os
from PIL import Image, ImageDraw
import io
import base64

BASE_DIR = os.path.dirname(__file__)

def show_home():
    st.markdown("""
    <style>
    /* Normal buttons */
    .stButton>button,
    .stDownloadButton>button {
        background-color: black !important;
        color: #40E0D0 !important;
        border: 2px solid #40E0D0 !important;
        border-radius: 10px;
        padding: 8px 20px;
        transition: 0.3s;
    }
    /* Hover effect */
    .stButton>button:hover,
    .stDownloadButton>button:hover {
        background-color: rgba(64,224,208,0.2) !important;
        border-color: white !important;
        transform: scale(1.05);
    }
    /* Active/focus */
    .stButton>button:active,
    .stDownloadButton>button:active,
    .stButton>button:focus,
    .stDownloadButton>button:focus {
        color: #40E0D0 !important;
        border-color: #40E0D0 !important;
        box-shadow: 0 0 5px #40E0D0;
        outline: none !important;
    }
                /* Remove default padding/margin for main container */
.css-18e3th9 {  /* main container class */
    padding-top: 0rem;
    padding-bottom: 0rem;
    padding-left: 0rem;
    padding-right: 0rem;
}

/* Remove extra spacing for title and sections */
.css-1d391kg { /* container for sections */
    padding: 0rem !important;
}

    </style>
""", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 0.5])

    # --- Left column (Intro + Buttons) ---
    with col1:
        st.markdown(
            """
            <style>
            h1, h2, h3, p {
                margin: 1px !important;
                padding: 1px !important;
                color:white;
            }
            .animated-title {
                font-family: Poppins, sans-serif;
                font-size: 50px;
                color: white;
                white-space: nowrap;
                overflow: hidden;
                border-right: 4px solid #40E0D0;
                width: 13ch;
                animation: typing 2s steps(13) forwards;
            }
            @keyframes typing {
                from { width: 0 }
                to { width: 13ch }
            }
            .animated-text {
                display: inline-block;
                color: #40E0D0;
                animation: changeText 3s infinite;
            }
            .animated-text::after {
                content: "Software Developer";
                animation: changeText 3s infinite;
            }
            @keyframes changeText {
                0% { content: "Software Developer"; }
                50% { content: "Data Analyst"; }
                100% { content: "Software Developer"; }
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.header("Hello, It's Me")
        st.markdown("""
<div style=" font-family:'Poppins', sans-serif; color:#ffffff;">
    <h1 class='animated-title' style="margin-bottom:5px;">Maqfira Sarwar!</h1>
    <h3 style="font-weight:400; margin-bottom:5px;">
        I'm a <span class="animated-text"></span>
    </h3>
    <h3 style="font-size: clamp(1rem, 2.5vw, 1.5rem); font-weight:400; color:#ffffff;">
        Software Developer & Aspiring Data Analyst | Delivering Scalable Solutions and Actionable Insights
    </h3>
</div>
""", unsafe_allow_html=True)

        # Social icons
        social_icons_data = {
            "LinkedIn": ["https://www.linkedin.com/in/maqfirasarwar/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
            "GitHub": ["https://github.com/Maqfira", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
            "WhatsApp": ["https://wa.me/916360656585", "https://cdn-icons-png.flaticon.com/128/4423/4423697.png"]
        }

        social_icons_html = [
            f"<a href='{url}' target='_blank' style='margin-right: 20px;'><img src='{icon}' style='width:25px;height:25px;'></a>"
            for url, icon in social_icons_data.values()
        ]
        st.markdown(f"<div style='display:flex;margin-bottom:20px;'>{''.join(social_icons_html)}</div>", unsafe_allow_html=True)

        # Contact buttons
        gmail_link = "https://mail.google.com/mail/?view=cm&to=maqfirasarwar2302@gmail.com"
        phone_number = "+916360656585"

        st.markdown(
            f"""
            <a href="{gmail_link}" target="_blank">
                <button style="background-color:#00BFFF;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;cursor:pointer;">
                    Hire Me
                </button>
            </a>
            <a href="tel:{phone_number}">
                <button style="background-color:#4CAF50;color:white;padding:10px 20px;border:none;border-radius:5px;font-size:16px;cursor:pointer;margin-left:10px;">
                    Call Me
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

    # --- Right column (Profile Image) ---
    with col2:
        img_path = os.path.join(BASE_DIR, "assets", "maqfi.png")
        img = Image.open(img_path).convert("RGBA")

        size = max(img.size)
        new_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        new_img.paste(img, ((size - img.width) // 2, (size - img.height) // 2))

        mask = Image.new("L", (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)

        circular_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        circular_img.paste(new_img, (0, 0), mask=mask)

        buffered = io.BytesIO()
        circular_img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        st.markdown(
            f"""
            <div style="display:flex;justify-content:center;align-items:center;">
                <img src="data:image/png;base64,{img_str}" style="width:350px;height:350px;border-radius:50%;object-fit:cover;">
            </div>
            """,
            unsafe_allow_html=True
        )

    # --- Resume download ---
    resume_path = os.path.join(BASE_DIR, "assets", "Maqfira Sarwar.pdf")
    with open(resume_path, "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Get Resume",
        data=pdf_bytes,
        file_name="Maqfira_Sarwar.pdf",
        mime="application/pdf"
    )
