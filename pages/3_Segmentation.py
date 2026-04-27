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
st.subheader("1.Country Segmentation Distribution")
# Equal weight for visibility
df["count"] = 1
# Sunburst Plot
fig_sunburst = px.sunburst(
    df,
    path=["segment", "country"],
    values="count",
    color="segment",
    color_discrete_map=segment_colors,
    custom_data=["income", "gdpp", "child_mort", "life_expec"],
    
)

# Get all labels
labels = fig_sunburst.data[0]["labels"]
parents = fig_sunburst.data[0]["parents"]

# Custom hover text
hover_templates = []

for label, parent in zip(labels, parents):
    # Segment level (parent is empty)
    if parent == "":
        hover_templates.append(
            "<b>Segment:</b> %{label}<br>" +
            "<b>Percentage:</b> %{percentRoot}<extra></extra>"
        )
    # Country level
    else:
        hover_templates.append(
            "<b>Country:</b> %{label}<br>" +
            "<b>Income:</b> %{customdata[0]}<br>" +
            "<b>GDP:</b> %{customdata[1]}<br>" +
            "<b>Child Mortality:</b> %{customdata[2]}<br>" +
            "<b>Life Expectancy:</b> %{customdata[3]}<extra></extra>"
        )

# Apply hover templates
fig_sunburst.data[0].hovertemplate = hover_templates

# Text inside chart
fig_sunburst.update_traces(
    textinfo="label+percent parent",
    insidetextorientation="radial"
)

# Layout
fig_sunburst.update_layout(
    title_text="",
    title_x=0.5,
    height=450,
    margin=dict(t=60, l=20, r=20, b=20)
)

# Display chart
st.plotly_chart(fig_sunburst, use_container_width=True)

# -------------------------------
# 2. INCOME BY SEGMENT
# -------------------------------
st.subheader("2.💰 Income by Segment")

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
st.subheader("3.🌍 GDP by Segment")

fig3 = px.box(
    df,
    x="segment",
    y="gdpp",
    color="segment",
    color_discrete_map=segment_colors,
    title="GDP Distribution Across Segments"
)

st.plotly_chart(fig3)
st.caption("""GDP by Segment reveals which country groups have economic strength versus structural vulnerability.
It is a key indicator for understanding development inequality, resource allocation, and long-term growth potential.""")