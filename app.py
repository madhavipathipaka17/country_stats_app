import streamlit as st

st.title("🌍 Country Stats Dashboard")

st.write("Welcome! Use sidebar to navigate.")

st.page_link("pages/1_GlobalOverview.py", label="🌍 Global Overview")
st.page_link("pages/2_HealthEconomicRisk.py", label="⚕️ Health & Risk")
st.page_link("pages/3_Segmentation.py", label="🧩Segment_insights")