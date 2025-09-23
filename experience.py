# import streamlit as st

# def show_experience():
#     # CSS for experience cards
#     st.markdown("""
#     <style>
#     .exp-card {
#         background: rgba(64,224,208,0.08);
#         border-radius: 15px;
#         padding: 20px 25px;
#         margin: 15px 0;
#         box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
#         transition: 0.3s;
#         position: relative;
#     }
#     .exp-card:hover {
#         transform: scale(1.03);
#         box-shadow: 0px 8px 20px rgba(0,0,0,0.35);
#     }
#     .exp-title {
#         font-size: 18px;
#         font-weight: 700;
#         color: #40E0D0;
#         margin-bottom: 5px;
#     }
#     .exp-subtitle {
#         font-size: 15px;
#         font-weight: 500;
#         color: #f0f0f0;
#         margin-bottom: 10px;
#     }
#     .exp-duration {
#         font-size: 13px;
#         color: #b0b0b0;
#         margin-bottom: 12px;
#     }
#     .exp-points {
#         font-size: 14px;
#         color: #f0f0f0;
#         line-height: 1.6;
#         margin-left: 15px;
#     }
#     .exp-section {
#         margin-top: 25px;
#         margin-bottom: 25px;
#     }
#                 /* Media queries for responsiveness */
#     @media (max-width: 600px) {  /* Mobile */
#         .exp-card {
#             padding: 15px 20px;
#             margin: 10px 0;
#         }
#         .exp-title {
#             font-size: 16px;
#         }
#         .exp-subtitle {
#             font-size: 13px;
#         }
#         .exp-duration {
#             font-size: 11px;
#         }
#         .exp-points {
#             font-size: 12px;
#             margin-left: 10px;
#         }
#         .exp-section {
#             margin-top: 20px;
#             margin-bottom: 20px;
#         }
#     }
#     @media (min-width: 601px) and (max-width: 1024px) {  /* Tablet */
#         .exp-card {
#             padding: 18px 22px;
#             margin: 12px 0;
#         }
#         .exp-title {
#             font-size: 17px;
#         }
#         .exp-subtitle {
#             font-size: 14px;
#         }
#         .exp-duration {
#             font-size: 12px;
#         }
#         .exp-points {
#             font-size: 13px;
#         }
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Experience section title
#     st.subheader("💼 Professional Experience")
    
#     # Assistant Engineer – Stem Avishkar Pvt Ltd
#     st.markdown("""
#     <div class="exp-section">
#         <div class="exp-card">
#             <div class="exp-title">Assistant Engineer</div>
#             <div class="exp-subtitle">Stem Avishkar Pvt Ltd</div>
#             <div class="exp-duration">Dec 2024 – Present</div>
#             <ul class="exp-points">
#                 <li>Optimized backend processing with Python & FastAPI, improving speed by 20%.</li>
#                 <li>Resolved 95% of reported bugs within deadlines and participated actively in sprints & code reviews.</li>
#                 <li>Learned and applied new frameworks & tools to enhance project delivery.</li>
#             </ul>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Full Stack Developer Trainer – Encapsulation Infotech Pvt Ltd
#     st.markdown("""
#     <div class="exp-section">
#         <div class="exp-card">
#             <div class="exp-title">Full Stack Developer Trainer</div>
#             <div class="exp-subtitle">Encapsulation Infotech Pvt Ltd</div>
#             <div class="exp-duration">Nov 2023 – Oct 2024</div>
#             <ul class="exp-points">
#                 <li>Conducted hands-on training sessions in Python, Django, SQL, HTML, CSS, and JavaScript.</li>
#                 <li>Mentored 40+ students, with 85% successfully completing real-time projects.</li>
#                 <li>Designed and executed internship programs, enabling practical, project-based learning.</li>
#             </ul>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


import streamlit as st

def show_experience():
    # CSS for timeline (flow chart style)
    st.markdown("""
    <style>
    .timeline {
        position: relative;
        max-width: 800px;
        margin: 0 auto;
    }
    .timeline::after {
        content: '';
        position: absolute;
        width: 6px;
        background-color: #40E0D0;
        top: 0;
        bottom: 0;
        left: 50%;
        margin-left: -3px;
    }
    .timeline-container {
        padding: 20px 40px;
        position: relative;
        background-color: inherit;
        width: 50%;
    }
    .timeline-container::after {
        content: '';
        position: absolute;
        width: 20px;
        height: 20px;
        right: -10px;
        background-color: #40E0D0;
        border: 3px solid #fff;
        top: 15px;
        border-radius: 50%;
        z-index: 1;
    }
    .left {
        left: 0;
    }
    .right {
        left: 50%;
    }
    .right::after {
        left: -10px;
    }
    .content {
        padding: 20px;
        background: rgba(64,224,208,0.08);
        position: relative;
        border-radius: 10px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.25);
        transition: 0.3s;
    }
    .content:hover {
        transform: scale(1.03);
        box-shadow: 0px 8px 20px rgba(0,0,0,0.35);
    }
    .exp-title {
        font-size: 18px;
        font-weight: 700;
        color: #40E0D0;
        margin-bottom: 5px;
    }
    .exp-subtitle {
        font-size: 15px;
        font-weight: 500;
        color: #f0f0f0;
        margin-bottom: 10px;
    }
    .exp-duration {
        font-size: 13px;
        color: #b0b0b0;
        margin-bottom: 12px;
    }
    .exp-points {
        font-size: 14px;
        color: #f0f0f0;
        line-height: 1.6;
    }
    /* Responsive */
    @media screen and (max-width: 600px) {
        .timeline::after {
            left: 31px;
        }
        .timeline-container {
            width: 100%;
            padding-left: 70px;
            padding-right: 25px;
        }
        .timeline-container::after {
            left: 15px;
        }
        .right {
            left: 0%;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("💼 Professional Experience")

    # Timeline structure
    st.markdown("""
    <div class="timeline">

      <div class="timeline-container left">
        <div class="content">
          <div class="exp-title">Assistant Engineer</div>
          <div class="exp-subtitle">Stem Avishkar Pvt Ltd</div>
          <div class="exp-duration">Dec 2024 – Present</div>
          <ul class="exp-points">
            <li>Optimized backend processing with Python & FastAPI, improving speed by 20%.</li>
            <li>Resolved 95% of reported bugs within deadlines and participated actively in sprints & code reviews.</li>
            <li>Learned and applied new frameworks & tools to enhance project delivery.</li>
          </ul>
        </div>
      </div>

      <div class="timeline-container right">
        <div class="content">
          <div class="exp-title">Full Stack Developer Trainer</div>
          <div class="exp-subtitle">Encapsulation Infotech Pvt Ltd</div>
          <div class="exp-duration">Nov 2023 – Oct 2024</div>
          <ul class="exp-points">
            <li>Conducted hands-on training sessions in Python, Django, SQL, HTML, CSS, and JavaScript.</li>
            <li>Mentored 40+ students, with 85% successfully completing real-time projects.</li>
            <li>Designed and executed internship programs, enabling practical, project-based learning.</li>
          </ul>
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)
