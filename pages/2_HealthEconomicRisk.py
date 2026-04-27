import streamlit as st
import plotly.express as px
from db.connection import run_query
from data.queries import GET_COUNTRY_STATS
from utils.helpers import segment_colors

df = run_query(GET_COUNTRY_STATS)

st.title("⚕️ Health & Economic Risk")

# ---------------- CHILD MORTALITY ----------------
st.subheader("1. Child Mortality by Country")

fig1 = px.bar(
    df.sort_values("child_mort", ascending=False),
    x="country",
    y="child_mort",
    color="segment",
    color_discrete_map=segment_colors,
    custom_data=["income", "gdpp"]   # Extra country details
)

# Hover details
fig1.update_traces(
    hovertemplate=
    "<b>Country:</b> %{x}<br>" +
    "<b>Child Mortality:</b> %{y}<br>" +
    "<b>Income:</b> %{customdata[0]}<br>" +
    "<b>GDP:</b> %{customdata[1]}<extra></extra>"
)

# Layout improvements
fig1.update_layout(
    xaxis_title="Country",
    yaxis_title="Child Mortality Rate",
    xaxis_tickangle=-60,
    height=400
)

st.plotly_chart(fig1, use_container_width=True)
st.caption("High Child Mortality usually occurs when:Low income + Low gdpp + Low health")

# ---------------- HEALTH VS MORTALITY ----------------
st.subheader("2.Health vs Child Mortality")

fig2 = px.scatter(
    df,
    x="health",
    y="child_mort",
    size="income",
    color="segment",
    color_discrete_map=segment_colors,
    hover_name="country",
    trendline="ols"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------------- INFLATION ----------------
st.subheader("3.Inflation Risk Analysis")

fig3 = px.box(
    df,
    x="segment",
    y="inflation",
    color="segment",
    color_discrete_map=segment_colors,
)

st.plotly_chart(fig3, use_container_width=True)
st.caption("""An Inflation Risk Chart is an early warning tool for economic pressure.
It helps reveal where rising costs may undermine development, increase vulnerability, and reduce quality of life.""")

# -------------------------------
# FERTILITY vs GDP VISUALIZATION
# -------------------------------
st.subheader("4.📊 Fertility vs GDP")

fig_fert_gdp = px.scatter(
    df,
    x="gdpp",
    y="total_fer",
    color="segment",  
    color_discrete_map=segment_colors,
    hover_name="country",
    title="Fertility vs GDP per Capita"
)

st.plotly_chart(fig_fert_gdp)
