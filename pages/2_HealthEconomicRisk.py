import streamlit as st
import plotly.express as px
from db.connection import run_query
from data.queries import GET_COUNTRY_STATS
from utils.helpers import segment_colors

df = run_query(GET_COUNTRY_STATS)

st.title("⚕️ Health & Economic Risk")

# ---------------- CHILD MORTALITY ----------------
st.subheader("1.Child Mortality by Country")

fig1 = px.bar(
    df.sort_values("child_mort", ascending=False),
    x="country",
    y="child_mort",
    color="child_mort"
)

st.plotly_chart(fig1, use_container_width=True)

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
