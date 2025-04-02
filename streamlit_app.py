import streamlit as st
import pandas as pd
import time
import base64

# Set up page configuration
st.set_page_config(
    page_title='VAP -Varashakti Analytics Platform',
    page_icon=':house:',
    layout='wide'
)

# Custom styling
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            color: #2E86C1;
            margin-top: 20px;
        }
        .description {
            text-align: center;
            font-size: 18px;
            color: #5D6D7E;
        }
        .dashboard-card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
            text-align: center;
            transition: transform 0.2s;
        }
        .dashboard-card:hover {
            transform: scale(1.05);
        }
        .dashboard-link {
            font-size: 20px;
            font-weight: bold;
            color: #154360;
            text-decoration: none;
        }
        .dashboard-link:hover {
            color: #1ABC9C;
        }
        .logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 200px;
            margin-bottom: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Load Logo
logo_path = "Logo.png"
try:
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()
        st.markdown(f'<img src="data:image/png;base64,{encoded_logo}" class="logo">', unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("Logo not found. Please upload the logo to display it.")

# Title Section
st.markdown('<p class="title">Varashakti Analytics Platform</p>', unsafe_allow_html=True)

# Center-aligned description
st.markdown('<p class="description">Explore key insights and trends in housing loans.</p>', unsafe_allow_html=True)

# Spacing
st.markdown("---")

# Dashboard Links with Cards
dashboards = {
    "Disbursement Dashboard": "https://app.powerbi.com/reportEmbed?reportId=d8df3fd1-6e71-4489-923d-a2aa6a19ff44&autoAuth=true&ctid=a89b94f6-5056-46b5-9bb5-c8c1fc71d057",
    "HR Attrition": "https://bit.ly/VHF_HR_Attrition_Dashboard",
    "CXO Dashboard": "https://tinyurl.com/LmsPortfolioVhf",
    "DPD Analysis": "https://app.powerbi.com/reportEmbed?reportId=44180f4f-1398-4e20-a56a-3b5af447640b&autoAuth=true&ctid=a89b94f6-5056-46b5-9bb5-c8c1fc71d057"
}

cols = st.columns(2)
for i, (name, link) in enumerate(dashboards.items()):
    col = cols[i % 2]
    with col:
        st.markdown(
            f'<div class="dashboard-card">'
            f'<a class="dashboard-link" href="{link}" target="_blank">{name} ➜</a>'
            f'</div>',
            unsafe_allow_html=True
        )

# Loading animation for UX
with st.spinner('Loading dashboard insights...'):
    time.sleep(2)

# Footer
st.markdown("""
    ---
    <p style='text-align: center; color: grey;'>© 2025 Varashakti Analytics Platform - Housing Pvt Limited</p>
    """, unsafe_allow_html=True)
