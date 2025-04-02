import streamlit as st
import pandas as pd
import time

# Set up page configuration
st.set_page_config(
    page_title='Housing Loan Dashboard - VAP',
    page_icon=':house:',
    layout='wide'
)

# Custom styling
st.markdown(
    """
    <style>
        .title {
            text-align: center;
            font-size: 42px;
            font-weight: bold;
            color: #2E86C1;
        }
        .dashboard-card {
            background-color: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: center;
        }
        .dashboard-link {
            font-size: 18px;
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
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo Section
st.markdown('<img src="data:image/png;base64,{0}" class="logo">'.format(open("/mnt/data/Logo.png", "rb").read().encode("base64").decode()), unsafe_allow_html=True)

# Title Section
st.markdown('<p class="title">🏡 Housing Loan Analytics Dashboard</p>', unsafe_allow_html=True)

st.write("Explore key insights and trends in housing loans.")

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
    <p style='text-align: center; color: grey;'>© 2025 Varashakti Analytics Platform - Housing Loan Division</p>
    """, unsafe_allow_html=True)
