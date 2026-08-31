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


tab1,tab2, tab3, tab4 = st.tabs(["Current Year Utility Data Analysis", "Year On Year Utility Data Analysis", "Current Year Expense Dashboard Analysis", "Year On Year Profit Analysis"])

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

with tab2:
    st.subheader("Year On Year Utility Data Analysis")

    with st.expander("**Metric #1: Total Utility Spend (2024-2026)**", expanded=True):
            st.markdown(
                """
            *	**Total Utility Spend** showed an average increase of **Php 2,627.23** per year.
            *   Other notable insights point to the start of the year (January) as a month marked by a high utility spend. 
            *   This is followed by the months of April to May. 
            *   All three years showed a marked spending increase during these months. 

        """)

    with st.expander("**Metric #2: Total Electricity Spend (2024-2026)**", expanded=True):
        st.markdown(
            """
            *	Total Electricity Spend increased by **Php 773.20** per year.
            *    Like the total utility spend, the months of April to May were also marked by a spending increase. 
            *    The month of July also showed a marked spending increase for all three years.

    """)

    with st.expander("**Metric #3: Total Water Bill Spend (2024-2026)**", expanded=True):
        st.markdown(
            """
        *   Total Water Bill Spend increased by **Php 1,854.03** per year
        *   Besides notable exceptions seen in the year 2025, the common trend shared by all three years was an increase in spend during the early months of the year (January and February) respectively. 


    """)

    with st.expander("**Metric #4: Utility Cost as Percentage of Revenue (2024-2026)**", expanded=True):
        st.markdown(
            """
        *  An examination of the utility cost as percentage of total revenue showed a worrying continual elevation in utility spending. 
        *  **Two** out of the three years showed elevated percentages (10%) that already ate into gross margins, while all three years averaged at least five months where utility cost percentage was above the acceptable rate. 
        *  Thankfully, the latest data shows the least number of months **(3)** where utility cost percentage reached an elevated rate. 

    """)

    with st.expander("**Metric #5: Effective Rate (2024-2026)**", expanded=True):
        st.markdown(
            """
            * The electricity rate data for the period specified showed an average increase of **Php 2.44 per kwh** for the years 2024-2026
            * The water rate data for the period specified showed an average increase of **Php 47.55 per cubic meter** for the years 2024-2026
    """)

    with st.expander("**Metric #6: Consumption Volume (2024-2026)**", expanded=True):
        st.markdown(
            """
            * The consumption volume data for the specified period showed a visible **decrease** for both water and electricity consumption.
            * Average Electricity Consumption: (-251.33)
            * Average Water Consumption:(-11.33)
    """)

    with st.expander("**Metric #7: Variance Data (2024-2026)**", expanded=True):
        st.markdown(
            """
            * **Electricity Variance Data** unearthed the following insights: 
                1.	Cost increases in the year 2024 were driven primarily by **rate hikes**. 
                2.	The year 2025 saw positive numbers which pointed to low variance for both price and quantity. 
                3.	For 2026, **both price and quantity variance** served as equal factors which led to electricity cost increases. 
            * **Water Variance Data** unearthed the following insights:
                1.	2025 was primarily driven by an increase in **consumption**, while both succeeding and preceding years saw no questionable variance jumps. 
    """)

    with st.expander("**Metric #8:Revenue vs Total Orders, Utility Cost Per Order and Average Order Value**", expanded=True):
        st.markdown(
            """
            *   Revenue data for the period specified showed an average increase of **Php 30,632.11** per year. 
            *   **2026** recorded the highest total revenue for the months of January-July.
            *   **2024** recorded the lowest total revenue for the months of January-July. 
            *   The highest (or one of the highest revenues recorded) for each year all coincide with similar months: **March, May and July**.
            *	2026 is the only year where the breakeven point was reached **twice**. 
            *	The lowest recorded revenue month is **February 2025** 
            *	The highest recorded revenue month is **May 2026**. 
            *	Total order data also showed an increase of **13.90**
            ---
            **Utility Cost Per Order showed a decrease of -82.55, however, so did Average Order Value, which went down to -1018.45 per year covered.** 
            #### KEY TAKEAWAYS
            *   Strong Operational Efficiency: Scaling total order volume allowed you to spread fixed or semi-variable utility costs across more transactions, driving down your utility cost per order.
            *	Changing Customer Purchasing Habits: A declining Average Order Value (AOV) means customers are buying fewer items per order, switching to cheaper options, or benefiting from larger discounts.
            *	Overall Growth: Increasing total revenue alongside rising order volume proves that the gains from sheer order volume are outpacing the revenue drop from smaller order sizes.
            
            ####  STRATEGIC RECOMMENDATIONS
            *   Protect Your Margins from Delivery/Labor Costs: Lower AOV means higher operational strain per dollar earned. Ensure that packing, transaction fees, and labor costs per order aren't eating into the savings gained from reduced utility costs.
            *	Focus on Upselling & Cross-Selling: Implement subtle basket-building strategies (e.g., minimum order thresholds for perks, bundled items, or targeted add-ons at checkout) to nudge AOV back up.
            *   Analyze Product Mix: Check if customers are shifting toward lower-margin items or if aggressive discounting over the three-year period systematically lowered the spend per ticket.


    """)

with tab3:
    st.subheader("Current Year Expense Dashboard Analysis")


    with st.expander("**Table #1: Operating Income and Operating Margin**", expanded=True):
        st.markdown(
            """
        * Table 1 displays the final operating income from the months of January- July 2026. 
        
        * Operating income is defined as the efficiency and sustainability level of the business to generate money from products before interests and taxes. 
        
        * Based on the computation, the months surveyed showed a mostly ideal and positive margin percentage. 
        
        * May 2026 is listed as the month with the highest operating margin, with July at a close second.
        
        * April 2026 is listed as the month with the lowest operating income and margin, notably displaying negative results for both. 

    """)

    with st.expander("**Table #2: Cost Spend Tables**", expanded=True):
        st.markdown(
        """
        * Table 2 looks at the two main branches of expenses which are used to calculate profit, cost of goods and operating expenses.
        The table displays the total amounts spent for the listed months, and the percentage each amount is of the total revenue earned during that period.	 
        The COG percentage for all months are at alarming levels, while the OPEX percentages display no anomalies.
	    The next few charts might be of help in order to diagnose the cost surge seen in the COG category.             
    """)

    with st.expander("**Table #3: Cost of Goods Table**", expanded=True):
        st.markdown(
            """
        * Table 3 breaks down the specific expenses included in the cost of goods computation. 
        
        * These include petty cash marketing, regular salaries, extra helper salaries, chicken leg quarter, cooking gas, cooking oil, dry goods, fish fillet, groceries and plastic goods for packaging.
        
        * Petty cash marketing and salaries compose the highest percentage of the expense, exceeding the ideal 40-50% of COGs. 
        
        * Possible issues include overstaffing, excessive overtime and inefficient procedures. 

            
    """)

    with st.expander("**Table #4: OPEX Chart Table**", expanded=True):
        st.markdown(
            """
        * Table 4 breaks down the specific operating expenses included in the operating expense computation for the months of January-July 2026
        
        * Electricity comprises the highest expense for all months, followed by the water bill. 
        
        * There were no anomalies spotted in the numbers listed. 

    """)

    with st.expander("**Takeaways**", expanded=True):
        st.markdown(
            """
        * A more detailed examination of the expenses which comprised the profit computation yielded the following insights:
        
        * Petty cash marketing comprises the largest cost of good among all listed costs. 
        
        * Unlike the other expenses listed this is all paid in cash and is a likely explanation for possible cashflow issues that arose in succeeding months. 
        
        * There is a need to establish a possible credit line for future expenses that will lessen the need to pay cash down for future costs and allow for better budgeting opportunities. 
        
        * Examining the numbers further also gave more insight into just how bad the April 2026 cost increases affected the health of the business. 
        
        * Hurdles encountered during preparation of the report included analyzing where certain expenses would be classified given the context of the business’ work. These are still concerns after the report has been completed, as they affect the computations greatly. 

    """)

with tab4:
    st.subheader("Year On Year Profit Analysis")

    with st.expander("**Gross Profit Takeaways**", expanded=True):
        st.markdown(
            """
        * A year-on-year comparison shows marked improvements in all months, except April 2026.	
          However, three out of the seven months displayed a decrease in gross profit margin compared to 2025.	
	      These months were January, March and April of 2026.	
	      Despite a marked improvement in gross profit, the gross profit margin percentages tell the real story.	
	      All figures are below the 50% threshold, meaning that raw ingredients consume half of sales and make it impossible to break even.		
	      The closest month that reached the 50% was May, which is also the month which reached the breakeven revenue of 810,000.00.	

    """)

    with st.expander("**Net Profit Takeaways**", expanded=True):
      st.markdown(
            """
        * A year-on-year comparison shows marked improvements in all months, except April.		
          The same cannot be said for net profit margins, which went down in 2026 for the following months: January, March and April 2026.	
	      Despite these comparisons pointing to decreases, the percentage values of net profit margin in 2026 all well within the high to ideal net profit margin percentage.		
	      Again, April 2026 is the exception in this regard, as seen in its negative net profit margin of -4.94%.	       
    """)

    with st.expander("**Insight #1: Decrease in Gross Profit Margin**", expanded=True):
        st.markdown(
            """
        • Examination of the data showed a marked decrease in gross profit margins year-on-year
        
        • This is dangerous given that even if sales showed an increase, this would continue to erode net profits
        
        • Some possible causes of gross profit margin erosion include: ingredient and packaging cost increases, a shift in sales mix (ordering more low margin food vs high margin), inventory waste, spoilage or portion deviation, heavy discounting or promos, and an increase in third party or packaging overhead
        
        • Action points for this include:
        
          -	Examining menu layout and adding more high margin food
          
          -	Renegotiating rates with suppliers and/or adjusting menu prices
          
          -	Auditing portion sizes


    """)

    with st.expander("**Insight #2: Negative gross profit margin but good net profit margin**", expanded=True):
        st.markdown(
            """
        • Examination of the data presented here showed that despite negative gross profit margin percentages, net profit percentages still fell under ideal or healthy values
        
        • This could be due to dangerously high raw materials costs but low overhead costs
        
        • Interestingly, the business falls under common business models which fit this: owner operated/high unpaid labor, ghost/cloud kitchens, caterings, or subsidized/low rent spaces 
        
        • This model is not sustainable in the long run as it carries risks which are harmful to the business, namely an inability to scale, a vulnerability to ingredient inflation and burnout. 
        
        • Some action points which may aid in solving this issue include protecting net margin while fixing cost of goods (aiming for an ideal 30-35% ingredient cost, the business currently is at a 40% raw material cost), and normalizing labor for true valuation (including the owner’s salary under operating expenses in order to gain a more accurate net value).
        
    """)




st.sidebar.button("Logout", on_click=logout)




