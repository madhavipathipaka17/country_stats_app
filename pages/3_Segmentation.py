import streamlit as st
import plotly.express as px
from db.connection import run_query
from utils.helpers import segment_colors

st.header("📊 Page 3: 🧩Segmentation Insights")

# -------------------------------
# 🔎 FILTERS (SQL BASED)
# -------------------------------
st.sidebar.header("🔎 Filters - Page 3")

base_df = run_query("SELECT * FROM country_stats")

segment = st.sidebar.selectbox(
    "Segment",
    ["All"] + list(base_df["segment"].unique())
)

income_range = st.sidebar.slider(
    "Income Range",
    int(base_df["income"].min()),
    int(base_df["income"].max()),
    (int(base_df["income"].min()), int(base_df["income"].max()))
)

inflation_range = st.sidebar.slider(
    "Inflation Range",
    float(base_df["inflation"].min()),
    float(base_df["inflation"].max()),
    (float(base_df["inflation"].min()), float(base_df["inflation"].max()))
)

fertility_range = st.sidebar.slider(
    "Fertility Rate (total_fer)",
    float(base_df["total_fer"].min()),
    float(base_df["total_fer"].max()),
    (float(base_df["total_fer"].min()), float(base_df["total_fer"].max()))
)

# -------------------------------
# 🔥 SQL QUERY (ALL FILTERING HERE)
# -------------------------------
query = f"""
SELECT *
FROM country_stats
WHERE income BETWEEN {income_range[0]} AND {income_range[1]}
AND inflation BETWEEN {inflation_range[0]} AND {inflation_range[1]}
AND total_fer BETWEEN {fertility_range[0]} AND {fertility_range[1]}
"""

if segment != "All":
    query += f" AND segment = '{segment}'"

df = run_query(query)

# -------------------------------
# 1. SEGMENT DISTRIBUTION
# -------------------------------
st.subheader("📊 Segment Distribution")

segment_counts = df["segment"].value_counts().reset_index()
segment_counts.columns = ["segment", "count"]

fig1 = px.pie(
    segment_counts,
    names="segment",
    values="count",
    color="segment",
    color_discrete_map=segment_colors,
    title="Country Distribution by Segment"
    
)

st.plotly_chart(fig1)



# -------------------------------
# 2. INCOME BY SEGMENT
# -------------------------------
st.subheader("💰 Income by Segment")

fig2 = px.box(
    df,
    x="segment",
    y="income",
    color="segment",
    color_discrete_map=segment_colors,
    title="Income Distribution Across Segments"
)

st.plotly_chart(fig2)

# -------------------------------
# 3. GDP BY SEGMENT
# -------------------------------
st.subheader("🌍 GDP by Segment")

fig3 = px.box(
    df,
    x="segment",
    y="gdpp",
    color="segment",
    color_discrete_map=segment_colors,
    title="GDP Distribution Across Segments"
)

st.plotly_chart(fig3)