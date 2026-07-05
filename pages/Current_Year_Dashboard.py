import pandas as pd
import plotly.express as px
import streamlit as st
import os


st.set_page_config (page_title = "Current Year Dashboard", page_icon ="🍽", layout="wide")

def logout():
    st.session_state.authenticated = False
    # Optional: force a rerun so it immediately jumps to the login screen





st.title("2026 Dashboard 🍽")

st.sidebar.image("White Logo.png")

st.sidebar.header("Dashboard Menu")

st.sidebar.page_link("Home_Page.py", label="Home Page")
st.sidebar.page_link("pages/Current_Year_Dashboard.py", label="Current Year Dashboard")
st.sidebar.page_link ("pages/Year_On_Year_Dashboard.py", label ="Year On Year Dashboard")
st.sidebar.page_link ("pages/Historical_Dashboard.py", label="Historical Dashboard")

st.sidebar.header("Filter By Month:")

revenue_df = pd.read_csv("Total_Revenue.csv", index_col=False)
retargeting_df = pd.read_csv("Rev_vs_Target.csv", index_col=False)
ordertotal_df = pd.read_csv("Total_Orders.csv", index_col=False)
newcustomers_df = pd.read_csv("New_Customers.csv", index_col=False)
repeatcustomerrate_df = pd.read_csv("Repeat_Customer_Rate.csv", index_col=False)

selected_month = st.sidebar.selectbox("Select Month", revenue_df["Month"].unique())
revenue_df = revenue_df[revenue_df["Month"] == selected_month].iloc[0]
retargeting_df = retargeting_df[retargeting_df["Month"] == selected_month].iloc[0]
ordertotal_df = ordertotal_df[ordertotal_df["Month"] == selected_month].iloc[0]
newcustomers_df = newcustomers_df[newcustomers_df["Month"] == selected_month].iloc[0]
repeatcustomerrate_df = repeatcustomerrate_df[repeatcustomerrate_df["Month"] == selected_month].iloc[0]

with st.container(border=True):
    col1, col2, col3, col4, col5 = st.columns(5)

    Total_Revenue = revenue_df["Total_Revenue"]
    Percentage = revenue_df["Percentage"]
    col1.metric(label="Total Revenue:", value=f"₱{Total_Revenue}", delta=f"{Percentage} vs. previous month")

    Total_Revenue = retargeting_df["Total_Revenue"]
    Percent = retargeting_df["Percent"]

    col2.metric(label="Revenue vs Target", value=f"{Percent}", delta="off breakeven point")

    Total_Orders = ordertotal_df["Total_Orders"]
    Amount_Quantity = ordertotal_df["Amount_Quantity"]
    col3.metric(label="Total Orders", value=f"{Total_Orders}", delta=f"{Amount_Quantity} vs. previous month",
                delta_arrow="off", delta_color="off")

    New_Customers = newcustomers_df["New_Customers"]
    Amount = newcustomers_df["Amount"]
    col4.metric(label="New Customers", value=f"{New_Customers}", delta=f"{Amount} vs. previous month",
                delta_arrow="off", delta_color="off")

    RCR = repeatcustomerrate_df["RCR"]
    Growth = repeatcustomerrate_df["Growth"]
    col5.metric(label="Repeat Customer Rate", value=f"{RCR}%", delta=f"{Growth} vs. previous month", delta_arrow="off",
                delta_color="off")

col1, col2 = st.columns(2)
with col1:
    st.subheader("2026 Revenue Trend")
    revenueinfo_df = pd.read_csv("Revenue_Data.csv")

    fig = px.line(
        revenueinfo_df,
        x="Month",
        y="Revenue",
        markers=True
    )

    fig.update_layout(
        yaxis_title="Revenue",
        xaxis_title="Month",
        height=400
    )

    fig.update_traces(line_color="#c71b08")

    st.plotly_chart(fig)

df = pd.read_csv("New_vs_Returning_Customers.csv")
selected_month = st.sidebar.selectbox("Select Month", df["Month"].unique(), key="new_vs_old_customers")

filtered_df = df[df["Month"] == selected_month].iloc[0]

with col2:
    st.subheader("Customer Breakdown")
    pie_data = pd.DataFrame({
        "Type": ["New_Customers", "Returning_Customers"],
        "Count": [
            filtered_df["New_Customers"],
            filtered_df["Returning_Customers"]
        ]
    })

    # 👇 build chart from filtered data (THIS is what makes it dynamic)
    fig = px.pie(
        pie_data,
        names="Type",
        values="Count",
        title=f"New Vs. Returning Customers",
        hole=0.4,
        color_discrete_sequence=["#047d28", "#ccc60e"]
    )

    st.plotly_chart(fig, width="stretch")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Gross vs.Net Profit")
    df = pd.read_csv("Gross_Net_Profit.csv")

    selected_month = st.sidebar.selectbox(
        "Select Month",
        df["Month"].unique(),
        key="month_filter"
    )

    # Filter data
    filtered_df = df[df["Month"] == selected_month]

    # Convert to "long format" for grouped bar chart
    df_melted = filtered_df.melt(
        id_vars=["Month"],
        value_vars=["Gross_Profit", "Net_Profit"],
        var_name="Profit_Type",
        value_name="Amount"
    )

    # Bar chart
    fig = px.bar(
        df_melted,
        x="Profit_Type",
        y="Amount",
        color="Profit_Type",
        text="Amount",
        color_discrete_map={
            "Revenue": "#c71b08",
            "Cost": "#080707",
            "Profit": "#ccc60e"
        }
    )

    st.plotly_chart(fig, width="stretch")

with col2:
    df = pd.read_csv("Customer_By_Type_File.csv")

    # Sidebar filter
    selected_month = st.sidebar.selectbox("Select Month", df["Month"].unique(), key="customer_type_filter")

    # Filter data
    filtered_df = df[df["Month"] == selected_month]

    # Convert wide → long format
    pie_df = filtered_df.melt(
        id_vars="Month",
        value_vars=["Corporate", "Catering", "Individual"],
        var_name="Type",
        value_name="Count"
    )

    # Donut chart
    fig = px.pie(
        pie_df,
        names="Type",
        values="Count",
        title=f"Customers by Type",
        hole=0.5,
        color_discrete_sequence=["#c71b08", "#047d28", "#ccc60e"]
    )

    # Display in Streamlit
    st.plotly_chart(fig, width="stretch")

    st.sidebar.button("Logout", on_click=logout)




