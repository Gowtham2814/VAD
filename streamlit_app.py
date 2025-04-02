import streamlit as st

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='VAP - Varashakti Analytics Platform',
    page_icon=':bar_chart:',
)

# -----------------------------------------------------------------------------
# Draw the actual page

# Set the title that appears at the top of the page.
'''
# :bar_chart: VAP - Varashakti Analytics Platform

Explore various analytics dashboards available in our platform.
'''

# Add some spacing
''
''

st.header('Available Dashboards', divider='gray')

# Dashboard Links
dashboards = {
    "Disbursement Dashboard": "https://app.powerbi.com/reportEmbed?reportId=d8df3fd1-6e71-4489-923d-a2aa6a19ff44&autoAuth=true&ctid=a89b94f6-5056-46b5-9bb5-c8c1fc71d057",
    "HR Attrition Dashboard": "https://bit.ly/VHF_HR_Attrition_Dashboard",
    "CXO Dashboard": "https://tinyurl.com/LmsPortfolioVhf",
    "DPD Dashboard": "https://app.powerbi.com/reportEmbed?reportId=44180f4f-1398-4e20-a56a-3b5af447640b&autoAuth=true&ctid=a89b94f6-5056-46b5-9bb5-c8c1fc71d057"
}

cols = st.columns(2)
for i, (name, link) in enumerate(dashboards.items()):
    col = cols[i % len(cols)]
    with col:
        st.markdown(f"### [{name}]({link})", unsafe_allow_html=True)

# Footer
st.write("\n---\n© 2025 Varashakti Analytics Platform")

