import streamlit as st

def show_qualification():
    # CSS for qualification cards
    st.markdown("""
    <style>
    .qual-card {
        background: rgba(64,224,208,0.08);
        border-radius: 15px;
        padding: 20px 25px;
        margin: 12px 0;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        transition: 0.3s;
        position: relative;
    }
    .qual-card:hover {
        transform: scale(1.03);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.35);
    }
    .qual-title {
        font-size: 17px;
        font-weight: 700;
        color: #40E0D0;
        margin-bottom: 5px;
    }
    .qual-subtitle {
        font-size: 14px;
        font-weight: 500;
        color: #f0f0f0;
        margin-bottom: 8px;
    }
    .qual-duration {
        font-size: 13px;
        color: #b0b0b0;
        margin-bottom: 10px;
    }
    .qual-percent {
        font-size: 14px;
        color: #f0f0f0;
    }
    .qual-section {
        margin-top: 20px;
        margin-bottom: 20px;
    }
                /* Media queries for responsiveness */
    @media (max-width: 600px) {  /* Mobile */
        .qual-card {
            padding: 15px 20px;
            margin: 10px 0;
        }
        .qual-title {
            font-size: 15px;
        }
        .qual-subtitle, .qual-percent {
            font-size: 12px;
        }
        .qual-duration {
            font-size: 11px;
        }
        .qual-section {
            margin-top: 15px;
            margin-bottom: 15px;
        }
    }
    @media (min-width: 601px) and (max-width: 1024px) {  /* Tablet */
        .qual-card {
            padding: 18px 22px;
            margin: 11px 0;
        }
        .qual-title {
            font-size: 16px;
        }
        .qual-subtitle, .qual-percent {
            font-size: 13px;
        }
        .qual-duration {
            font-size: 12px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Section title
    st.subheader("🎓 Education & Qualifications")

    # Mysuru Royal Institute of Technology
    st.markdown("""
    <div class="qual-section">
        <div class="qual-card">
            <div class="qual-title">Mysuru Royal Institute of Technology</div>
            <div class="qual-subtitle">Bachelor of Engineering in Computer Science and Engineering</div>
            <div class="qual-duration">2023</div>
            <div class="qual-percent">Percentage: 82%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # St. Philomena's PU College
    st.markdown("""
    <div class="qual-section">
        <div class="qual-card">
            <div class="qual-title">St. Philomena's PU College</div>
            <div class="qual-duration">2019</div>
            <div class="qual-percent">Percentage: 74.2%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # St. Philomena's High School
    st.markdown("""
    <div class="qual-section">
        <div class="qual-card">
            <div class="qual-title">St. Philomena's High School</div>
            <div class="qual-duration">2017</div>
            <div class="qual-percent">Percentage: 84.16%</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
