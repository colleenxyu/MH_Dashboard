import pandas as pd
import plotly.express as px
import streamlit as st
import os


st.set_page_config (page_title = "Dashboard Analysis", page_icon ="🍽", layout="wide")

def logout():
    st.session_state.authenticated = False
    st.session_state.clear()  # Optional: wipes all saved state variables safely

# 2. AUTH GUARD: Check authentication at the VERY TOP of your page script
if not st.session_state.get("authenticated", False):
    st.warning("Please log in to access this page.")
    st.switch_page("Home_Page.py")  # 👈 Replace "app.py" with the filename of your Main/Login page
    st.stop()




st.title("Dashboard Analysis Page 🍽")

st.sidebar.image("White Logo.png")

st.sidebar.header("Dashboard Menu")

st.sidebar.page_link("Home_Page.py", label="Home Page")
st.sidebar.page_link("pages/Current_Year_Dashboard.py", label="Current Year Dashboard")
st.sidebar.page_link ("pages/Year_On_Year_Dashboard.py", label ="Year On Year Dashboard")
st.sidebar.page_link ("pages/Historical_Dashboard.py", label="Historical Dashboard")
st.sidebar.page_link ("pages/Utilities_Dashboard.py", label = "Utilities Dashboard")
st.sidebar.page_link("pages/Dashboard_Analysis.py", label="Dashboard Analysis Page")


tab1,tab2 = st.tabs(["Current Year Utility Data Analysis", "Year On Year Utility Data Analysis"])

with tab1:
    st.subheader("Current Year Utility Data Analysis")

    with st.expander("**Metric #1: Utility as Cost (%) of Total Revenue**", expanded=True):
        st.markdown(
        """
    The months **January, April and June** saw elevated increases in utility spending as a percentage of total revenue.
January only saw a slight increase in utility spending (6%), however the months of April and June saw worrying percentages (approaching and at the 10% mark) which could already point to utility spending eating into the company’s gross margins.
#### Analysis:
---
To determine the possible factors that led to worrying spending percentages, other metrics were examined. Findings are listed below.
*	**Electricity Effective Rates** increased by Php 0.55 from March to April (going from 15.09 to 15.64 per kwh). A further increase of Php 0.2 per kwh was seen from June to April (May not being counted due to an anomaly).
*	**Consumption Volume** showed an increase of 135 kwh from March to April, further increasing by 202 kwh from April to June (May not being counted due to an anomaly).
*	Both **Electricity Price** and **Electricity Quantity Variances** appeared positive in April, pointing to a collective squeeze/increase in both. Due to an anomaly in the previous month, June showed an over-the-top price variance amount.
*	However, **Quantity Variance** was much higher in comparison (988.35 vs 2111.4) in April.
---

#### Conclusion:
*	An increase in consumption coupled with an increase in price during the month of April led to an increase in utility spending.
*	An increase in electricity rate led to the increase in price during the month of June
""")

    with st.expander("**Metric #2: Utility Split Ratio**", expanded=True):
        st.markdown("""
        The months of **January-July 2026** saw some slightly elevated **split ratios**. These were only seen in water bill spending. 
The months of January and July saw a slight percentage increase (35 and 31% respectively), while the anomalous percentage split seen in May can be attributed to an anomaly due to the refund amount of the electricity bill for the month at that time. 

        
        """)

    with st.expander("**Metric #3: Effective Rates**", expanded=True):
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("Electricity Rates: Examined")
            st.markdown("""
            A collective analysis of the electricity rates uncovered the following insights:
    *	The rates average about **1 peso per kwh** more when compared to the average residential rate data available from Meralco.
    *	The months **March, April and July** showed an increase in electricity rates. 
    *	No baseline data is available for March 2026, but a marked increase is seen in the average rates when comparing January 2026  (12.95 per kwh average) and April 2026 (14.35 per kwh average). 
    *	The business’ data shows an increase of **Php 0.55 per kwh** from March to April 2026. 
    *	Meralco data also indicates that April 2026 marked a record high increase in electricity rates due to generation charges. 
    *	Examining the months of June to July 2026 showed that the business’ rate increase closely matches the average rate increase found in the baseline data from Meralco (Php 0.32 and Php 0.35 increase respectively). 
    
            """)
        with col2:
            st.subheader("Water Rates: Examined")
            st.markdown("""
            A collective analysis of the water rates uncovered the following insights:
    * Maynilad has an average basic charge of **Php 52.86 per cubic meter**
    * The business’ water bill rates all fall at relatively close values, except for a marked **Php 1.75 peso** increase from January to February 2026 (142.50 in January 2026 vs 144.25 in February 2026). Examination of external data showed no scheduled base charge increase during this time. 
    * Unfortunately, the water rates calculated are not an accurate representation of cost per cubic meter because the final rate indicated in the water bill is inclusive of other charges not related to consumption. 

            """)

    with st.expander("**Metric #4: Total Consumption Volume**", expanded=True):
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("**Electricity Consumption: Explained**")
            st.markdown("""
            *	Average energy consumption volume for the months of Jan-July: **1805.71 kwh**
            *	The highest consumption volume recorded was in May: **2035 kwh**
            *	This corresponded to the month with the highest revenue: **Php 821,319.00**
            *	Aside from May 2026, no other anomalous values were spotted in the data

            """)
        with col2:
            st.subheader("**Water Rates: Explained**")
            st.markdown("""
            *	Average water consumption volume for the months of Jan-July: **67.14 cubic meters**
            *   The highest consumption volume recorded was in January: **96 cubic meters**
            *	This corresponded to the meter reading dates from the previous month (December)
            *	Besides that, consumption rates were relatively stable 

            
            """)

    with st.expander("**Metric #5: Variance Table**", expanded=True):
        st.markdown("""
        When analyzing variance, take note of the following:
        * When **Price** is higher than **Quantity Variance**: external hikes are a possible cause, and repricing menus are an ideal action point.
        * When **Quantity** is higher than **Price Variance**: kitchen waste or production spikes are a possible cause. Internal audits are an ideal action point.
        * When **both** are equal or close in value: this is called a combined squeeze, and both factors must be examined in greater detail. 
        """)

        col1,col2 = st.columns(2)
        with col1:
            st.subheader("**Water Bill: Price Vs Quantity**")
            st.markdown("""
            * The months of **January and February 2026** both pointed to an increase in price as primary cause for cost increase.
            * This was substantiated by water increases from December 2025 to January 2026 (17.29) and January 2026 to February 2026 (1.76). 
            * Meanwhile, the months of **April and May 2026** pointed to quantity consumption increase as cause for cost increase.
            * This was substantiated by the consumption volume increase seen from March to April (58 to 61 cubic meter consumption), and from April to May 2026 (61 to 62 cubic meter consumption).
            * Meanwhile, the months of March, June and July both reflected either 0 or negative values, which are likely caused by a low rate and reduced usage. This is the ideal best result to achieve in order to maximize cost savings and expand profit margins.

            """
            )
        with col2:
            st.subheader("**Electricity Bill: Price Vs Quantity**")
            st.markdown("""
            * The months of March, April and May all point to quantity variance as a cause for cost increase.
            * This was substantiated by the gradual consumption volume increase for each month (1662,1797 and 2035 kwh respectively). 
            * Meanwhile, the months of February and July reflect price variance as a cause for cost increase.
            * This was substantiated by visible rate increases seen from January to February and June to July (from 14.22 to 14.43, and from 15.8 to 16.12 per kwh respectively). 
            * Only the month of January reflected either zero or negative values, representing the ideal result to achieve in order to maximize cost savings and expand profit margins. 

            
            """)

    with st.expander("**Metric #6: Utility Consumption Cost Per Order & Average Order Value**", expanded =True):
        st.subheader("**Utility Cost Per Order vs Average Order Value: Examined**")
        st.markdown("""
        * The ideal ratio is a low utility cost per order and a high order value 
        * The months of **January, April, June and July 2026** all have a high utility cost per order.
        * Due to a cost anomaly in May, the month’s unusually low utility cost per order cannot be considered here. 
        * **July** is an example of a month with max profitability as it has a low utility cost per order (381.68) and a high order value (7951). 
        * **April** is an example of a month that is in a ‘danger zone’, as it has a high utility cost per order (392.78) and a high average order value (3935.55). 

        
        
        """)


st.sidebar.button("Logout", on_click=logout)




