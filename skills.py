import streamlit as st
import random

def show_skills():
    # st.set_page_config(page_title="Portfolio", layout="wide")

    # Background images
    images = [
        "https://cdn-icons-png.flaticon.com/128/5968/5968350.png",
        "https://cdn-icons-png.flaticon.com/128/174/174854.png",
        "https://cdn-icons-png.flaticon.com/128/17482/17482427.png",
        "https://cdn-icons-png.flaticon.com/128/9307/9307630.png",
        "https://cdn-icons-png.flaticon.com/128/18168/18168844.png",
        "https://cdn-icons-png.flaticon.com/128/9912/9912341.png",
        "https://cdn-icons-png.flaticon.com/128/6260/6260220.png",
        "https://cdn-icons-png.flaticon.com/128/11068/11068857.png"
        "https://cdn-icons-png.flaticon.com/128/10050/10050999.png",
        "https://cdn-icons-png.flaticon.com/128/13651/13651057.png",
        "https://cdn-icons-png.flaticon.com/128/13651/13651001.png",
        "https://cdn-icons-png.flaticon.com/128/10050/10050999.png",
        "https://cdn-icons-png.flaticon.com/128/18168/18168844.png",



    ]

    # CSS for background images and skills
    css = "<style>\n"
    css += "body, .stApp {background: #0e1117; color: #f0f0f0;}\n"
    css += """
    @keyframes float {
        0% { transform: translate(0px, 0px) rotate(0deg); }
        50% { transform: translate(20px, 20px) rotate(10deg); }
        100% { transform: translate(0px, 0px) rotate(0deg); }
    }
    """
    for i, img in enumerate(images):
        top = random.randint(0, 90)
        left = random.randint(0, 90)
        width = random.randint(50, 150)
        duration = random.randint(1,5) 
        css += f"""
        .bg-img-{i} {{
            position: fixed;
            top: {top}%;
            left: {left}%;
            width: {width}px;
            opacity: 0.4;
            z-index: 0;
            pointer-events: none;
            animation: float {duration}s ease-in-out infinite;
        }}
        """
        
    # Skills card CSS
    css += """
    .skill-card {
        background: rgba(64,224,208,0.08);
        border-radius: 15px;
        padding: 15px 20px;
        margin: 10px 0;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
        transition: 0.3s;
        z-index: 1;
        position: relative;
    }
    .skill-card:hover {
        transform: scale(1.03);
        box-shadow: 0px 6px 15px rgba(0,0,0,0.3);
    }
    .skill-title {
        font-size: 18px;
        font-weight: 600;
        color: #40E0D0;
        margin-bottom: 8px;
    }
    .skill-items {
        font-size: 15px;
        color: #f0f0f0;
        line-height: 1.6;
    }
    /* Media queries for responsiveness */
    @media (max-width: 600px) {  /* Mobile */
        .skill-card {
            padding: 10px 15px;
            margin: 8px 0;
        }
        .skill-title {
            font-size: 16px;
            margin-bottom: 6px;
        }
        .skill-items {
            font-size: 13px;
        }
        """
    for i in range(len(images)):
        css += f"""
        .bg-img-{i} {{
            width: {random.randint(30, 100)}px;  /* Smaller on mobile */
        }}
        """
    css += """
    }
    @media (min-width: 601px) and (max-width: 1024px) {  /* Tablet */
        .skill-card {
            padding: 12px 18px;
            margin: 9px 0;
        }
        .skill-title {
            font-size: 17px;
            margin-bottom: 7px;
        }
        .skill-items {
            font-size: 14px;
        }
        """
    for i in range(len(images)):
        css += f"""
        .bg-img-{i} {{
            width: {random.randint(40, 120)}px;  /* Adjusted for tablet */
        }}
        """
    css += """
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    # Display background images
    for i, img in enumerate(images):
        st.markdown(f'<img src="{img}" class="bg-img-{i}">', unsafe_allow_html=True)

    # Skills content
    st.subheader("🛠️ Skills")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">💻 Programming Languages</div>
            <div class="skill-items">Python</div>
        </div>
        <div class="skill-card">
            <div class="skill-title">⚙️ Frameworks & Tools</div>
            <div class="skill-items">Django, FastAPI</div>
        </div>
        <div class="skill-card">
            <div class="skill-title">🎨 Frontend Technologies</div>
            <div class="skill-items">HTML5, CSS3, Bootstrap, JavaScript</div>
        </div>
        <div class="skill-card">
            <div class="skill-title">📊 Libraries</div>
            <div class="skill-items">NumPy, Pandas, Matplotlib, Seaborn, Plotly</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="skill-card">
            <div class="skill-title">🗄️ Databases</div>
            <div class="skill-items">MySQL</div>
        </div>
        <div class="skill-card">
            <div class="skill-title">📑 Tools</div>
            <div class="skill-items">MS Office (Word, Excel, PowerPoint)</div>
        </div>
        <div class="skill-card">
            <div class="skill-title">🤝 Soft Skills</div>
            <div class="skill-items">Team Collaboration, Problem-Solving, Quick Learning</div>
        </div>
        """, unsafe_allow_html=True)
