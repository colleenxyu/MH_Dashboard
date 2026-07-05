import pandas as pd
import plotly.express as px
import streamlit as st
import os


st.set_page_config (page_title = "Mey Han Dashboard", page_icon ="🍽", layout="wide")

PASSWORD = st.secrets["dashboard_password"]



# ----------------------------
# Session state (track login)
# ----------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ----------------------------
# LOGIN SCREEN
# ----------------------------
def login_screen():
    st.title("🔐 Login Required")

    password = st.text_input("Enter password", type="password")

    if st.button("Enter Dashboard"):
        if password == PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password")

# ----------------------------
# DASHBOARD
# ----------------------------
def dashboard():




    st.sidebar.image("White Logo.png")

    st.sidebar.header("Dashboard Menu")

    #Sidebar Details
    st.sidebar.page_link ("./Home_Page.py", label="Home Page")
    st.sidebar.page_link("pages/Current_Year_Dashboard.py", label="Current Year Dashboard")
    st.sidebar.page_link("pages/Year_On_Year_Dashboard.py", label="Year On Year Dashboard")
    st.sidebar.page_link("pages/Historical_Dashboard.py", label="Historical Dashboard")

    st.sidebar.button("Logout", on_click=logout)

    st.title("Mey Han Dashboard 🍽")

    st.markdown("<div style='padding: 15px;'></div>", unsafe_allow_html=True)

    #Main Page



    st.markdown("""
        <div style="font-size: 20px; line-height: 1.6;">
        Welcome to the Mey Han Company Dashboard.<br><br>
        This dashboard aims to offer a concise status update on the company's current status.
        It also offers a year to year and historical comparison analysis of the company revenue.<br><br>
        
        Feel free to browse accordingly. 
        
        
        If you have any questions or concerns, please contact the developer.<br><br>
        Thank You!
        </div>
        """,
                    unsafe_allow_html=True)





# ----------------------------
# LOGOUT FUNCTION
# ----------------------------
def logout():
    st.session_state.authenticated = False


# ----------------------------
# APP CONTROLLER
# ----------------------------
if st.session_state.authenticated:
    dashboard()
else:
    login_screen()









