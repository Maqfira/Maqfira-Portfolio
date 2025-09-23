import streamlit as st

def show_projects():
    # CSS for project cards and tech badges
    st.markdown("""
    <style>
    .proj-card {
        background: rgba(64,224,208,0.08);
        border-radius: 15px;
        padding: 20px 25px;
        margin: 15px 0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        transition: 0.3s;
        position: relative;
    }
    .proj-card:hover {
        transform: scale(1.03);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.35);
    }
    .proj-title {
        font-size: 18px;
        font-weight: 700;
        color: #40E0D0;
        margin-bottom: 5px;
    }
    .proj-description {
        font-size: 14px;
        color: #f0f0f0;
        line-height: 1.6;
        margin-bottom: 10px;
    }
    .tech-badge {
        display: inline-block;
        background: #0e1117;
        color: #40E0D0;
        border: 1px solid #40E0D0;
        border-radius: 12px;
        padding: 3px 10px;
        margin: 2px;
        font-size: 12px;
    }
                /* Media queries for responsiveness */
    @media (max-width: 600px) {  /* Mobile */
        .proj-card {
            padding: 15px 20px;
            margin: 10px 0;
        }
        .proj-title {
            font-size: 16px;
        }
        .proj-description {
            font-size: 12px;
        }
        .tech-badge {
            padding: 2px 8px;
            font-size: 10px;
            margin: 1px;
        }
    }
    @media (min-width: 601px) and (max-width: 1024px) {  /* Tablet */
        .proj-card {
            padding: 18px 22px;
            margin: 12px 0;
        }
        .proj-title {
            font-size: 17px;
        }
        .proj-description {
            font-size: 13px;
        }
        .tech-badge {
            padding: 3px 9px;
            font-size: 11px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("🖥️ Projects & Technical Work")

    # Online Car Rental System
    st.markdown("""
    <div class="proj-card">
        <div class="proj-title">Online Car Rental System</div>
        <div class="proj-description">
            Developed a **secure admin-based system** to manage car rentals, customer records, bookings, and payments efficiently.
            Integrated **user authentication** for administrator-only access.
        </div>
        <div class="tech-badge">HTML5</div>
        <div class="tech-badge">CSS</div>
        <div class="tech-badge">Bootstrap</div>
        <div class="tech-badge">SQL</div>
    </div>
    """, unsafe_allow_html=True)

    # AI Assistant using Python
    st.markdown("""
    <div class="proj-card">
        <div class="proj-title">AI Assistant using Python</div>
        <div class="proj-description">
            Built an **AI assistant** with **90% accuracy** in user query responses.
            Integrated **voice recognition** with an average response time of < 2 seconds.
        </div>
        <div class="tech-badge">Python</div>
    </div>
    """, unsafe_allow_html=True)

    # HR Management System
    st.markdown("""
    <div class="proj-card">
        <div class="proj-title">HR Management System</div>
        <div class="proj-description">
            Developed a **comprehensive employee management system** with dashboards that reduced record retrieval time by 30%.
            Enabled **efficient handling of employee records** with FastAPI and MySQL backend.
        </div>
        <div class="tech-badge">Python</div>
        <div class="tech-badge">FastAPI</div>
        <div class="tech-badge">MySQL</div>
        <div class="tech-badge">HTML5</div>
        <div class="tech-badge">CSS</div>
        <div class="tech-badge">Bootstrap</div>
        <div class="tech-badge">JavaScript</div>
    </div>
    """, unsafe_allow_html=True)

    # Hotel Booking Data Analysis
    st.markdown("""
    <div class="proj-card">
        <div class="proj-title">Hotel Booking Data Analysis</div>
        <div class="proj-description">
            Analyzed **40,000+ hotel booking records** to uncover patterns in cancellations, customer preferences, and seasonal trends.
            Performed **data cleaning & preprocessing** with Pandas and NumPy, and created **interactive visualizations** with Matplotlib and Seaborn.
        </div>
        <div class="tech-badge">Python</div>
        <div class="tech-badge">Pandas</div>
        <div class="tech-badge">NumPy</div>
        <div class="tech-badge">Matplotlib</div>
        <div class="tech-badge">Seaborn</div>
        <div class="tech-badge">MySQL</div>
    </div>
    """, unsafe_allow_html=True)
