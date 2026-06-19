import streamlit as st
import pandas as pd
import plotly.express as px

# Load cleaned dataset
df = pd.read_csv("zomato_cleaned.csv")

st.set_page_config(page_title="Zomato Dashboard", layout="wide")
st.title("Zomato Data Analysis Dashboard")

# Filters
city = st.selectbox("Select City", df["city"].unique())
rating = st.slider("Minimum Rating", 0.0, 5.0, 3.5)

# Filtered data
filtered = df[(df["city"] == city) & (df["aggregate_rating"] >= rating)]

# Metrics
col1, col2 = st.columns(2)
with col1:
    st.metric("Average Cost", round(filtered["average_cost_for_two"].mean(), 2))
    st.metric("Total Restaurants", len(filtered))
with col2:
    fig = px.bar(filtered.groupby("cuisines")["aggregate_rating"].mean().sort_values(ascending=False))
    st.plotly_chart(fig, use_container_width=True)
