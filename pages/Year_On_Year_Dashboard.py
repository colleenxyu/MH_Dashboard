import pandas as pd
import plotly.express as px
import streamlit as st
import os
import io

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
st.sidebar.page_link ("pages/Utilities_Dashboard.py", label = "Utilities Dashboard")
st.sidebar.page_link("pages/Dashboard_Analysis.py", label="Dashboard Analysis Page")

st.sidebar.header("Filter By Month:")

#DataFrame References
revenue_df = pd.read_csv("Revenue_Comparison.csv", index_col=False)
revtargetcomparison_df = pd.read_csv("RevvsTargetComparison.csv", index_col=False)
totalordercomparison_df = pd.read_csv("TotalOrderComparison.csv", index_col=False)
avgordercomparison_df = pd.read_csv ("AvgOrderComparison.csv", index_col = False)
consumptionvol2426_df = pd.read_csv ("ConsumptionVol2426.csv", index_col = False)
effectiverates2426_df = pd.read_csv ("EffectiveRates2426.csv", index_col = False)
totalelecspend2426_df = pd.read_csv ("TotalElecSpend2426.csv", index_col = False)
toutilitycostper2426_df = pd.read_csv ("TotalUtilityCostPercent2426.csv", index_col = False)
utilityspend2426_df = pd.read_csv ("TotalUtilitySpend2426.csv", index_col=False)
totalwaterspend2426_df = pd.read_csv ("TotalWaterSpend2426.csv", index_col=False)
utilityorderdata2426_df = pd.read_csv ("UtilityOrderData2426.csv", index_col = False)
variance2426_df = pd.read_csv ("VarianceTable2426.csv", index_col = False)
pricevsquantity2426_df = pd.read_csv ("PriceVsQuantity2426.csv", index_col = False)


#Selectbox
selected_month = st.sidebar.selectbox("Select Month", revenue_df["Month"].unique())
revenue_df = revenue_df[revenue_df["Month"] == selected_month].iloc[0]
revtargetcomparison_df = revtargetcomparison_df[revtargetcomparison_df["Month"] == selected_month].iloc[0]
totalordercomparison_df = totalordercomparison_df[totalordercomparison_df["Month"] == selected_month].iloc[0]
avgordercomparison_df = avgordercomparison_df[avgordercomparison_df ["Month"] == selected_month].iloc[0]
consumptionvol2426_df = consumptionvol2426_df [consumptionvol2426_df ["Month"] == selected_month].iloc[0]
effectiverates2426_df = effectiverates2426_df [effectiverates2426_df ["Month"] == selected_month].iloc[0]
totalelecspend2426_df = totalelecspend2426_df [totalelecspend2426_df ["Month"] == selected_month].iloc[0]
toutilitycostper2426_df = toutilitycostper2426_df [toutilitycostper2426_df ["Month"] == selected_month].iloc[0]
utilityspend2426_df = utilityspend2426_df [utilityspend2426_df ["Month"] == selected_month].iloc[0]
totalwaterspend2426_df = totalwaterspend2426_df [totalwaterspend2426_df ["Month"] == selected_month].iloc[0]
utilityorderdata2426_df = utilityorderdata2426_df [utilityorderdata2426_df ["Month"] == selected_month].iloc[0]
variance2426_df = variance2426_df [variance2426_df ["Month"] == selected_month].iloc[0]
pricevsquantity2426_df = pricevsquantity2426_df [pricevsquantity2426_df ["Month"] == selected_month].iloc[0]

tab1,tab2 = st.tabs(["General Business Year On Year Dashboard", "Utility Year On Year Dashboard"])

with tab1:
    st.subheader("General Business Dashboard")
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

    df = pd.read_csv("GrossvsNetComparison2526.csv")

    # Unpivot the DataFrame from wide to long format
    df_long = df.melt(
        id_vars=["Month"],
        value_vars=["Gross_Profit25", "Net_Profit25", "Gross_Profit26", "Net_Profit26"],
        var_name="Metric",
        value_name="Amount"
    )

    # Now 'Metric' exists as a column in df_long!
    fig = px.bar(
        df_long,
        x="Month",
        y="Amount",
        color="Metric",
        barmode="group",
        title="Year-over-Year Gross vs Net Profit Comparison",
        text_auto="$,.0f"
    )

    fig.update_layout(template="plotly_white")
    st.plotly_chart(fig)

    df = pd.read_csv ("GrossvsNetComparison2526.csv")
    st.dataframe(df)



with tab2:
    st.subheader("Utility Dashboard")
    with st.container(border=True):
        st.subheader("General Information")
            #TotalSpendComparison
        TotalSpend25 = utilityspend2426_df ["Spend2025"]
        TotalSpend26 = utilityspend2426_df ["Spend2026"]
        st.metric(label="Total Utility Spend:", value=f"₱ {TotalSpend25} vs ₱ {TotalSpend26}", delta ="2025 vs 2026", delta_color ="blue",delta_arrow ="off")
        col1,col2 = st.columns(2)
        with col1:
                #TotalElectricitySpend
                ElecSpend25 = totalelecspend2426_df ["ElecSpend2025"]
                ElecSpend26 = totalelecspend2426_df ["ElecSpend2026"]
                ElecKWH25 = consumptionvol2426_df["KWHAmt25"]
                ElecKWH26 = consumptionvol2426_df["KWHAmt26"]
                col1.metric (label="Total Electric Bill: ", value =f"₱ {ElecSpend25} vs ₱ {ElecSpend26}",delta =f"{ElecKWH25} kwh vs {ElecKWH26} kwh", delta_color ="blue", delta_arrow ="off" )
        with col2:
                #TotalWaterBill
                WatSpend25 = totalwaterspend2426_df ["WaterSpend2025"]
                WatSpend26 = totalwaterspend2426_df ["WaterSpend2026"]
                WatAmt25 = consumptionvol2426_df ["CUAmt25"]
                WatAmt26 = consumptionvol2426_df ["CUAmt26"]
                col2.metric(label = "Total Water Bill: ", value = f"₱ {WatSpend25} vs ₱ {WatSpend26}", delta =f"{WatAmt25} cu m vs {WatAmt26} cu m", delta_color = "blue", delta_arrow ="off")
    with st.container(border=True):
        st.subheader("Consumption Data")
        with st.container(border=True):
            st.subheader("Utility Rates")
            #ElectricityRate
            ElecRate25 = effectiverates2426_df ["ElecAmt25"]
            ElecRate26 = effectiverates2426_df ["ElecAmt26"]
            st.metric(label = "Electricity Rate", value = f"₱ {ElecRate25} per kwh vs ₱ {ElecRate26} per kwh", delta_color = "violet",delta ="2025 vs 2026", delta_arrow ="off")
            #WaterRate
            WaterRate25 = effectiverates2426_df ["WaterAmt25"]
            WaterRate26 = effectiverates2426_df ["WaterAmt26"]
            st.metric (label = "Water Rate", value =f"₱ {WaterRate25} per cubic meter vs ₱ {WaterRate26} per cubic meter", delta_color = "violet",delta ="2025 vs 2026", delta_arrow ="off")

        with st.container(border=True):
            st.subheader("Utility Variance")

            col1, col2 = st.columns(2)
            with col1:
            # ElectricityVariance
                ElVar25 = pricevsquantity2426_df["ElecVar25"]
                ElVar26 = pricevsquantity2426_df["ElecVar26"]
                st.metric(label="Electricity Variance Type", value=f"{ElVar25} vs {ElVar26}", delta_color="violet",
                          delta="2025 vs 2026", delta_arrow="off")

            with col2:
            #WaterVariance

                WatVar25 = pricevsquantity2426_df ["WaterVar25"]
                WatVar26 = pricevsquantity2426_df ["WaterVar26"]
                st.metric(label="Water Variance Type", value=f"{WatVar25} vs {WatVar26}", delta_color="violet",
                          delta="2025 vs 2026", delta_arrow="off")


        with st.container(border=True):
            st.subheader("Utility Cost Breakdown")
            #UtilityCostPercentage
            CostPercent25 = toutilitycostper2426_df ["UtilityCent25"]
            CostPercent26 = toutilitycostper2426_df ["UtilityCent26"]
            st.metric (label ="Utility As Percentage of Total Revenue", value = f"{CostPercent25}% vs {CostPercent26}% of Total Cost", delta = "2025 vs 2026", delta_color = "violet", delta_arrow ="off")


            col1, col2 = st.columns(2)
            with col1:
            #UtilityCostPerOrder
                UtilityCOP25 = utilityorderdata2426_df ["CostPerOrder25"]
                UtilityCOP26 = utilityorderdata2426_df ["CostPerOrder26"]
                st.metric(label = "Utility Cost Per Order", value =f"₱ {UtilityCOP25} vs ₱ {UtilityCOP26}", delta_color = "violet",delta ="2025 vs 2026", delta_arrow ="off")
            with col2:
            #AverageOrderValue
                avgvalue25 = utilityorderdata2426_df ["AOV25"]
                avgvalue26 = utilityorderdata2426_df ["AOV26"]
                st.metric(label="Average Order Value", value=f"₱ {avgvalue25} vs ₱ {avgvalue26}",
                          delta_color="violet", delta="2025 vs 2026", delta_arrow="off")




st.sidebar.button("Logout", on_click=logout)

