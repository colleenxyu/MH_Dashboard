import pandas as pd
import plotly.express as px
import streamlit as st
import os


st.set_page_config (page_title = "Historical Dashboard", page_icon ="🍽", layout="wide")
def logout():
    st.session_state.authenticated = False
    # Optional: force a rerun so it immediately jumps to the login screen


st.title("Historical Dashboard 🍽")

st.sidebar.image("White Logo.png")

st.sidebar.header("Dashboard Menu")

st.sidebar.page_link("Home_Page.py", label="Home Page")
st.sidebar.page_link("pages/Current_Year_Dashboard.py", label="Current Year Dashboard")
st.sidebar.page_link ("pages/Year_On_Year_Dashboard.py", label ="Year On Year Dashboard")
st.sidebar.page_link ("pages/Historical_Dashboard.py", label="Historical Dashboard")

st.sidebar.button("Logout", on_click=logout)

st.subheader("Historical Revenue Trend")

# 1. Load the data
revenuehistorical_df = pd.read_csv("Historical_Revenue_List.csv")

# 2. Keep ONLY the columns we care about (this throws away all those empty commas)
df_clean = revenuehistorical_df[["Year", "Month", "Total Revenue"]].dropna(subset=["Year"])

# 3. Clean the revenue column (remove commas, spaces, and make it a number)
df_clean["Total Revenue"] = (
    df_clean["Total Revenue"]
    .astype(str)
    .str.replace(",", "", regex=True)
    .str.replace(" ", "", regex=True)
)
df_clean["Total Revenue"] = pd.to_numeric(df_clean["Total Revenue"], errors="coerce")

# 4. Force Year to a string so the filter and colors treat them as distinct categories
df_clean["Year"] = df_clean["Year"].astype(int).astype(str)

# 5. Get our unique years for the dropdown filter
available_years = sorted(df_clean["Year"].unique())

selected_years = st.multiselect(
    "Select Years to Display:",
    options=available_years,
    default=available_years
)

# 6. Filter the data based on selection
filtered_df = df_clean[df_clean["Year"].isin(selected_years)]

# 7. Keep months in perfect chronological order
month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 8. Build the plot
fig = px.line(
    filtered_df,
    x="Month",
    y="Total Revenue",
    color="Year",
    category_orders={"Month": month_order},
    markers=True
)

fig.update_layout(
    yaxis_title="Revenue",
    xaxis_title="Month",
    height=500,
    legend_title="Year"
)

st.plotly_chart(fig)