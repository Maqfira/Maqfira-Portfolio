import streamlit as st
import os
import time
from PIL import Image, ImageOps, ImageDraw
import io
import base64

def show_home():
    col1,col2 = st.columns([1,0.5])

    with col1:
            st.markdown("""
        <style>
        /* Reduce spacing between header, title, subheader, text */
        h1, h2, h3, p {
            margin: 1px;
            padding: 1px;
            color:white;
        }
        </style>
        """, unsafe_allow_html=True)
            st.header("Hello, It's Me")
            st.markdown(
                """
                <style>
                @keyframes typing {
                    from { width: 0 }
                    to { width: 13ch } /* number of characters in your name */
                }
                .animated-title {
                    font-family: Poppins, sans-serif;
                    font-size: 50px;
                    color: white;
                    white-space: nowrap;
                    overflow: hidden;
                    border-right: 4px solid #40E0D0;
                    width: 13ch; /* final width to prevent shrink */
                    animation: typing 2s steps(13) forwards; /* run once and stop */
                }
                </style>
                <h1 class="animated-title">Maqfira Sarwar!</h1>
                """,
                unsafe_allow_html=True
            )
            st.markdown("""
        <h3 style=""; font-weight:400;">
        I'm a <span class="animated-text"  ></span>
        </h3>

        <style>
        .animated-text {
        display: inline-block;
        color: #40E0D0;
        animation: textChange 3s infinite;
        }

        @keyframes textChange {
        0% { content: "Software Developer"; }
        50% { content: "Data Analyst"; }
        100% { content: "Software Developer"; }
        }

        /* workaround for changing text */
        .animated-text::after {
        content: "Software Developer";
        animation: changeText 3s infinite;
        }

        @keyframes changeText {
        0% { content: "Software Developer"; }
        50% { content: "Data Analyst"; }
        #   100% { content: "Software Developer"; }
        }
        </style>
        """, unsafe_allow_html=True)
            st.markdown("""
<h3 style='
    font-size: clamp(1rem, 2.5vw, 1.5rem);
    font-weight: 400;
    color: #ffffff;  /* change color if needed */
'>
Software Developer & Aspiring Data Analyst | Delivering Scalable Solutions and Actionable Insights
</h3>
""", unsafe_allow_html=True)
            social_icons_data = {
            "LinkedIn": ["https://www.linkedin.com/in/maqfirasarwar/", "https://cdn-icons-png.flaticon.com/128/3536/3536505.png"],
            "GitHub": ["https://github.com/Maqfira", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
            "WhatsApp": ["https://wa.me/916360656585", "https://cdn-icons-png.flaticon.com/128/4423/4423697.png"]
            }

            social_icons_html = [
            f"<a href='{social_icons_data[platform][0]}' target='_blank' style='margin-right: 20px;'>"
            f"<img class='social-icon' src='{social_icons_data[platform][1]}' alt='{platform}'"
            f" style='width: 25px; height: 25px;'></a>"
            for platform in social_icons_data
        ]
            st.write(f"""
            <div style="display: flex;  margin-bottom: 20px;">
            {''.join(social_icons_html)}
            </div>""", 
            unsafe_allow_html=True)
            con1,con2,con3,con4,con5 = st.columns([0.1,0.1,0.1,0.1,0.1])
            # st.button("Hire Me")

            with con1:
            
                gmail_link = "https://mail.google.com/mail/?view=cm&to=maqfirasarwar2302@gmail.com"

                st.markdown(
            f"""
            <a href="{gmail_link}" target="_blank">
                <button style="
                    background-color:#00BFFF;
                    color:white;
                    padding:10px 20px;
                    border:none;
                    border-radius:5px;
                    font-size:16px;
                    cursor:pointer;
                ">
                Hire Me
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )
            with con2:
                phone_number = "+916360656585"
                call_link = f"tel:{phone_number}"

                st.markdown(
                f"""
                <a href="{call_link}">
                    <button class='but' style="
                        background-color:#4CAF50;
                        color:white;
                        padding:10px 20px;
                        border:none;
                        border-radius:5px;
                        font-size:16px;
                        cursor:pointer;
                    ">
                    Call Me
                    </button>
                </a>
                <style>
                  @media (max-width: 600px) {{  /* Mobile */
                    .but {{
                        margin-top:8px;
                    }}
                }}
                </style>
                """,
                unsafe_allow_html=True
            )

    with col2:
            img = Image.open("assets/maqfi.png").convert("RGBA")
            # Make the image square (largest dimension)
            size = max(img.size)
            new_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            new_img.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
            # Create circular mask
            mask = Image.new("L", (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)
            # Apply circular mask
            circular_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
            circular_img.paste(new_img, (0, 0), mask=mask)
            # Convert to base64
            buffered = io.BytesIO()
            circular_img.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()

            # Display in Streamlit with glowing outline
            st.markdown(
                f"""
                <style>
                .profile-img-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }}
                .profile-img {{
                    width: 350px;
                    height: 350px;
                    border-radius: 50%;
                    object-fit: cover;
                }}
                /* Media queries for responsiveness */
                @media (max-width: 600px) {{  /* Mobile */
                    .profile-img {{
                        width: 250px;
                        height: 250px;
                    }}
                }}
                @media (min-width: 601px) and (max-width: 1024px) {{  /* Tablet */
                    .profile-img {{
                        width: 300px;
                        height: 300px;
                    }}
                }}
                @media (min-width: 601px) and (max-width: 1024px) {{  /* Tablet */
                    .animated-title {{
                        font-size:20px;

                        # height: 300px;
                    }}
                }}
                 @media (max-width: 600px) {{  /* Mobile */
                    .animated-title {{
                        font-size: 30px;
                        # height: 250px;
                    }}
                }}
                </style>
                <div class="profile-img-container">
                    <img class="profile-img" src="data:image/png;base64,{img_str}" 
                        >
                </div>
                """,
                unsafe_allow_html=True
            )
    col3,col31 = st.columns(2)
    with col3:
            st.write("")  # add one line
            st.write("") 
            resume_path = "assets/Maqfira Sarwar.pdf"

            with open(resume_path, "rb") as f:
                pdf_bytes = f.read()

            st.download_button(
                label="Get Resume",
                data=pdf_bytes,
                file_name="Maqfira_Sarwar.pdf",
                mime="application/pdf"
            )


