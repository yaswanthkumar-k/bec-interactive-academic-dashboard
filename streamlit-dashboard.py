
# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# --------- Page Configuration ---------
st.set_page_config(page_title="Interactive Academic Dashboard", layout="wide")
st.title("Bapatla Engineering College")

# --------- Data Preparation ---------
# CIE Marks Data
cie_data = {
    'CIE Component': ['Term Exams', 'AAT', 'Attendance'],
    'R20 Credits': [20, 10, 0],
    'R24 Credits': [20, 15, 5]
}
df_cie = pd.DataFrame(cie_data)

# Course Credits Comparison
course_data = {
    'Category': ['HMSC', 'BSC', 'ESC', 'PCC', 'PE', 'JOE','PRJ','SO','OE', 'MC'],
    'R20 Credits': [10.5, 18, 22.5, 48, 12, 13.5, 16.5, 16, 3, 0],
    'R24 Credits': [11, 20, 22, 51.5, 15, 13.5, 16, 8, 3, 0]
}
df_course = pd

# Department-wise Credits
dept_data = {
    'Category': ['HMSC', 'BSC', 'ESC', 'PCC', 'PE', 'JOE','PRJ','SO','OE', 'MC'],
    'IT': [10.5, 18, 22.5, 48, 12, 13.5, 16.5, 16, 3, 0],
    'CSE': [10.5, 21, 24, 51, 18, 16.5, 16, 12, 10,0],
    'AIML': [25, 6, 1, 2, 4, 4, 6, 4, 5,0],
    'CBDS': [10.5, 18, 22.5, 48, 12, 16.5, 0, 16.5, 16,0],
    'DS': [8, 18, 22.5, 48, 12, 16.5, 0, 16.5, 16,0]
}
df_dept = pd.DataFrame(dept_data)

# --------- Sidebar Navigation ---------
st.sidebar.title("")
tab_choice = st.sidebar.radio("Select Section", ["CIE Marks", "Course Credits", "Department Credits", "Department Pie Chart"])

# --------- Tabbed Content ---------
if tab_choice == "CIE Marks":
    cie_year = st.sidebar.selectbox("Select Regulation", ['R20 Credits', 'R24 Credits'])
    tab1, tab2 = st.tabs(["📊 Pie Chart", "📄 Data Table"])

    with tab1:
        st.subheader(f"CIE Marks Distribution - {cie_year}")
        fig_cie = px.pie(df_cie, values=cie_year, names='CIE Component',
                         color_discrete_sequence=px.colors.qualitative.Plotly)
        st.plotly_chart(fig_cie, use_container_width=True)

    with tab2:
        st.subheader("CIE Data Table")
        st.dataframe(df_cie)

elif tab_choice == "Course Credits":
    tab1, tab2 = st.tabs(["📊 Bar Chart", "📄 Data Table"])

    with tab1:
        st.subheader("Course Credits Comparison (R20 vs R24)")
        fig_course = px.bar(df_course, x='Category', y=['R20 Credits', 'R24 Credits'],
                            barmode='group',
                            color_discrete_sequence=['#636EFA', '#00CC96'])
        st.plotly_chart(fig_course, use_container_width=True)

    with tab2:
        st.subheader("Course Credits Data Table")
        st.dataframe(df_course)

elif tab_choice == "Department Credits":
    tab1, tab2 = st.tabs(["📊 Department Comparison", "📄 Data Table"])

    with tab1:
        st.subheader("Department-wise Course Credits")
        fig_dept = px.bar(df_dept, x='Category', y=['IT', 'CSE', 'AIML', 'CBDS', 'DS'],
                          barmode='group',
                          color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_dept, use_container_width=True)

    with tab2:
        st.subheader("Department Credits Data Table")
        st.dataframe(df_dept)

elif tab_choice == "Department Pie Chart":
    dept_selected = st.sidebar.selectbox("Select Department", ['IT', 'CSE', 'AIML', 'CBDS', 'DS'])
    tab1, tab2 = st.tabs(["📊 Pie Chart", "📄 Data Table"])

    with tab1:
        st.subheader(f"{dept_selected} Department Course Distribution")
        fig_dept_pie = px.pie(df_dept, values=dept_selected, names=df_dept['Category'],
                              color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig_dept_pie, use_container_width=True)

    with tab2:
        st.subheader("Department Credits Data Table")
        st.dataframe(df_dept)