import pandas as pd
import plotly.express as px
import streamlit as st
import os


st.set_page_config (page_title = "Utilities Dashboard", page_icon ="🍽", layout="wide")

def logout():
    st.session_state.authenticated = False
    st.session_state.clear()  # Optional: wipes all saved state variables safely

# 2. AUTH GUARD: Check authentication at the VERY TOP of your page script
if not st.session_state.get("authenticated", False):
    st.warning("Please log in to access this page.")
    st.switch_page("Home_Page.py")  # 👈 Replace "app.py" with the filename of your Main/Login page
    st.stop()




st.title("Utilities Dashboard 🍽")

st.sidebar.image("White Logo.png")

st.sidebar.header("Dashboard Menu")

st.sidebar.page_link("Home_Page.py", label="Home Page")
st.sidebar.page_link("pages/Current_Year_Dashboard.py", label="Current Year Dashboard")
st.sidebar.page_link ("pages/Year_On_Year_Dashboard.py", label ="Year On Year Dashboard")
st.sidebar.page_link ("pages/Historical_Dashboard.py", label="Historical Dashboard")
st.sidebar.page_link ("pages/Utilities_Dashboard.py", label = "Utilities Dashboard")
st.sidebar.page_link("pages/Dashboard_Analysis.py", label="Dashboard Analysis Page")

st.sidebar.header("Filter By Month:")

utilityspend_df = pd.read_csv("UtilitySpend.csv", index_col=False)
consumptionvol_df = pd.read_csv("ConsumptionVolume.csv", index_col=False)
effectiverates_df = pd.read_csv("EffectiveRates.csv", index_col=False)
utilitysplitratio_df = pd.read_csv("UtilitySplitRatio.csv", index_col=False)
utilitycostpercent_df = pd.read_csv ("UtilityCostPercent.csv", index_col=False)
watervariance_df = pd.read_csv("WaterVariance26.csv", index_col=False)
elecvariance_df = pd.read_csv ("ElecVariance26.csv", index_col = False)
costperorders_df = pd.read_csv("CostPerOrders.csv", index_col = False)

selected_month = st.sidebar.selectbox("Select Month", utilityspend_df["Month"].unique())
utilityspend_df = utilityspend_df[utilityspend_df["Month"] == selected_month].iloc[0]
consumptionvol_df = consumptionvol_df[consumptionvol_df["Month"] == selected_month].iloc[0]
effectiverates_df = effectiverates_df[effectiverates_df["Month"] == selected_month].iloc[0]
watervariance_df = watervariance_df[watervariance_df["Month"] == selected_month].iloc[0]
elecvariance_df = elecvariance_df [elecvariance_df ["Month"] == selected_month].iloc[0]
utilitycostpercent_df = utilitycostpercent_df[utilitycostpercent_df ["Month"]  == selected_month].iloc[0]
costperorders_df = costperorders_df [costperorders_df ["Month"] == selected_month].iloc[0]

st.subheader("General Information")
with st.container(border=True):
    col1,col2,col3 = st.columns(3)
    #Total Utility Spend
    Total_Spend = utilityspend_df["TotalSpend26"]
    col1.metric(label="Total Utility Spend:", value=f"₱{Total_Spend}",delta="Total Spent for the Month", delta_arrow="off", delta_color="yellow")

    #Electricity Total
    Electricity_Bill = utilityspend_df["ElecSpend26"]
    Electricity_Consumption = consumptionvol_df["ElConsumption26"]

    col2.metric(label="Total Electric Bill:", value=f"₱{Electricity_Bill}", delta=f"{Electricity_Consumption} kwh", delta_arrow="off", delta_color="yellow")

    #Water Total
    Water_Bill = utilityspend_df ["WatSpend26"]
    Water_Consumption = consumptionvol_df ["WatConsumption26"]

    col3.metric(label="Total Water Bill:", value=f"₱{Water_Bill}", delta=f"{Water_Consumption} cu m",delta_arrow="off", delta_color="yellow" )


st.subheader("Utility Rates")
with st.container(border=True):
    col1,col2 = st.columns(2)

    #Electricity Effective Rates

    Electricity_Rate = effectiverates_df ["ElecRate26"]


    col1.metric(label="Electricity Rate", value=f"₱{Electricity_Rate} per kwh")

    #Water Effective Rates

    Water_Rate = effectiverates_df["WatRate26"]

    col2.metric (label="Water Rate", value =f"₱{Water_Rate} per cubic meter")


st.subheader("Utility Cost Breakdown")

with st.container(border=True):
    col1,col2 = st.columns(2)
    with col1:
            # --- DEBUG HELPER (Temporary: shows exact values in your dashboard) ---
            # st.write(f"Selected Month: `{selected_month}`")
            # st.write("CSV Months:", utilitysplitratio_df["Month"].tolist())

            # 1. Clean user selection down to first 3 lowercase letters (e.g., 'January' -> 'jan', 'Mar' -> 'mar')
            clean_selected = str(selected_month).strip().lower()[:3]

            # 2. Slice the CSV's Month column to 3 letters as well before comparing
            filtered_ratio = utilitysplitratio_df[
                utilitysplitratio_df["Month"].astype(str).str.strip().str.lower().str[:3] == clean_selected
            ]

            # 3. Build chart if matched
            if not filtered_ratio.empty:
                elec_val = filtered_ratio["ElecPercent26"].iloc[0]
                wat_val = filtered_ratio["WatPercent26"].iloc[0]

                pie_data = pd.DataFrame({
                    "Type": ["Electricity Spend", "Water Spend"],
                    "Count": [elec_val, wat_val]
                })

                fig = px.pie(
                    pie_data,
                    names="Type",
                    values="Count",
                    title=f"Utility Split Ratio",
                    hole=0.4,
                    color_discrete_sequence=["#047d28", "#ccc60e"]
                )

                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning(f"No utility split ratio data found for '{selected_month}'.")
                st.info(f"Available months in CSV: {', '.join(utilitysplitratio_df['Month'].astype(str).unique())}")

    with col2:
                st.write ("**Utility vs Total Costs**")

                Utility_Percent = utilitycostpercent_df ["UtilityPercent26"]
                CostPercent = utilitycostpercent_df ["CostPercentLevel"]
                st.metric(label ="Utility As Percentage of Total Cost",value = f"{Utility_Percent}% of Total Cost", delta=f"{CostPercent} for total cost", delta_arrow="off", delta_color="blue")

                UtilityCostPerOrder = costperorders_df ["CostOrder26"]
                st.metric(label ="Utility Cost Per Order", value =f"₱{UtilityCostPerOrder} per order")

                OrderValue = costperorders_df ["AOV26"]
                st.metric(label ="Average Order Value Per Month", value=f"₱{OrderValue}")

                UtilityBurden = costperorders_df ["UtilityBurdenPercent26"]
                UtilityBurdenQual = costperorders_df ["UtilityBurdenQuality"]
                st.metric (label ="Utility Burden Percentage", value= f"{UtilityBurden}%", delta =f"{UtilityBurdenQual} Utility Burden Level", delta_arrow="off", delta_color="yellow")

st.subheader("Utility Price vs Quantity Variance")
st.write("If **Price Variance** is higher than the Quantity variance, this means that the costs were influenced by a rate increase.")
st.write("If the **Quantity Variance** was higher, the costs were influenced by an increase in consumption.")

st.subheader("ELECTRICITY")
with st.container(border=True):
    col1,col2, col3 = st.columns(3)

    with col1:
        ElectricityPriceVariance = elecvariance_df ["ElecPriceVar26"]
        col1.metric(label ="Electricity Price Variance Level", value =f"{ElectricityPriceVariance}")
    with col2:
        ElectricityQuantityVariance = elecvariance_df ["ElecQuanVar26"]
        col2.metric (label = "Electricity Quantity Variance Level", value = f"{ElectricityQuantityVariance}")
    with col3:
        ElectricityVarianceResult = elecvariance_df ["ElecVarianceResult"]
        col3.metric (label = "Electricity Variance Outcome", value =f"{ElectricityVarianceResult}")

st.subheader("WATER")
with st.container(border=True):
    col1,col2, col3 = st.columns(3)

    with col1:
        WaterPriceVariance = watervariance_df ["WatPriceVar26"]
        col1.metric(label ="Water Price Variance Level", value =f"{WaterPriceVariance}")
    with col2:
        WaterQuantityVariance = watervariance_df ["WatQuanVar26"]
        col2.metric (label = "Water Quantity Variance Level", value = f"{WaterQuantityVariance}")
    with col3:
        WaterVarianceResult = watervariance_df ["WatVarianceResult"]
        col3.metric (label = "Water Variance Outcome", value =f"{WaterVarianceResult}")





st.sidebar.button("Logout", on_click=logout)




