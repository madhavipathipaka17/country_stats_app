import streamlit as st
import plotly.express as px
from db.connection import run_query
from data.queries import GET_COUNTRY_STATS
from utils.helpers import segment_colors

df = run_query(GET_COUNTRY_STATS)

st.title("🌍 Global Overview Dashboard")

# ---------------- KPI CARDS ----------------
avg_income = df["income"].mean()
avg_life = df["life_expec"].mean()
avg_child_mort = df["child_mort"].mean()

high_risk = df[(df["child_mort"] > 80) & (df["income"] < 5000)].shape[0]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Income", f"{avg_income:.2f}")
col2.metric("Life Expectancy", f"{avg_life:.2f}")
col3.metric("Child Mortality", f"{avg_child_mort:.2f}")
col4.metric("High-Risk Countries", high_risk)

# ---------------- WORLD MAP ----------------
st.subheader("🌎 World Map by Segment")

fig_map = px.choropleth(
    df,
    locations="country",
    locationmode="country names",
    color="segment",
    color_discrete_map=segment_colors,
    title="Country Segments"
)

st.plotly_chart(fig_map, use_container_width=True)

# ---------------- SCATTER ----------------
st.subheader("📊 Income vs Life Expectancy")

fig_scatter = px.scatter(
    df,
    x="income",
    y="life_expec",
    color="segment",
    color_discrete_map=segment_colors,
    hover_name="country"
)

st.plotly_chart(fig_scatter, use_container_width=True)
st.caption("Countries with higher income generally demonstrate longer life expectancy, indicating strong links between economic prosperity and healthcare quality.")