import pandas as pd
import plotly.express as px
import streamlit as st
import os

st.set_page_config(page_title="Year On Year Dashboard", page_icon="🍽", layout="wide")


def logout():
    st.session_state.authenticated = False
    # Optional: force a rerun so it immediately jumps to the login screen


st.title("Year on Year Dashboard 🍽")

st.sidebar.image("White Logo.png")

st.sidebar.header("Dashboard Menu")

st.sidebar.page_link("Home_Page.py", label="Home Page")
st.sidebar.page_link("pages/Current_Year_Dashboard.py", label="Current Year Dashboard")
st.sidebar.page_link ("pages/Year_On_Year_Dashboard.py", label ="Year On Year Dashboard")
st.sidebar.page_link ("pages/Historical_Dashboard.py", label="Historical Dashboard")

st.sidebar.header("Filter By Month:")

#DataFrame References
revenue_df = pd.read_csv("Revenue_Comparison.csv", index_col=False)
revtargetcomparison_df = pd.read_csv("RevvsTargetComparison.csv", index_col=False)
totalordercomparison_df = pd.read_csv("TotalOrderComparison.csv", index_col=False)
avgordercomparison_df = pd.read_csv ("AvgOrderComparison.csv", index_col = False)


#Selectbox
selected_month = st.sidebar.selectbox("Select Month", revenue_df["Month"].unique())
revenue_df = revenue_df[revenue_df["Month"] == selected_month].iloc[0]
revtargetcomparison_df = revtargetcomparison_df[revtargetcomparison_df["Month"] == selected_month].iloc[0]
totalordercomparison_df = totalordercomparison_df[totalordercomparison_df["Month"] == selected_month].iloc[0]
avgordercomparison_df = avgordercomparison_df[avgordercomparison_df ["Month"] == selected_month].iloc[0]



with st.container(border=True):
    col1, col2 = st.columns(2)
    #REVENUECOMPARISON
    Revenue_2026 = revenue_df["Revenue2026"]
    Revenue_2025 = revenue_df ["Revenue2025"]
    Percentage = revenue_df["VsPrevYear"]
    col1.metric(label="Revenue Comparison", value=f"₱{Revenue_2026} vs. ₱{Revenue_2025}", delta = f"{Percentage} vs. 2025")

    #REVENUEVSTARGET
    Percent2025 = revtargetcomparison_df ["%off_2025"]
    Percent2026 = revtargetcomparison_df ["%off_2026"]
    AmtPercent = revtargetcomparison_df ["PercentAmt"]
    col2.metric(label="Revenue vs Target Comparison", value=f"{Percent2026} vs.{Percent2025}", delta=f"{AmtPercent} vs.2025")


with st.container (border=True):
        col1, col2 = st.columns(2)
        with col1:
                #TotalOrderConsumption
                Old_Total = totalordercomparison_df ["Total_2025"]
                New_Total = totalordercomparison_df ["Total_2026"]
                Increase = totalordercomparison_df ["Order_Amount"]
                col1.metric (label = "Total Order Comparison", value = f"{New_Total} vs. {Old_Total}", delta =f"{Increase} vs. 2025", delta_arrow ="off", delta_color ="off")

        with col2:
                #AverageOrderValue
                AverageOrder2025 = avgordercomparison_df ["2025_AOV"]
                AverageOrder2026 = avgordercomparison_df ["2026_AOV"]
                AOVIncrease = avgordercomparison_df ["AOV_Increase"]
                col2.metric (label = "Average Order Value Comparison", value = f"₱{AverageOrder2026} vs. ₱ {AverageOrder2025}", delta = f"{AOVIncrease} vs 2025", delta_arrow ="off", delta_color = "off")

st.subheader("Gross vs.Net Profit Comparison (2025 vs 2026)")

df = pd.read_csv("NetGrossComparison.csv")
df.columns = df.columns.str.strip()

st.dataframe(df.style.format({
    "GrossProfit": "₱{:,.2f}",
    "NetProfit": "₱{:,.2f}"
}))

st.sidebar.button("Logout", on_click=logout)

