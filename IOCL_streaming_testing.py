import time                       # to simulate a real time data, time loop
import numpy as np                # np mean, np random
import pandas as pd               # read csv, df manipulation
import plotly.express as px       # interactive charts
import streamlit as st            # 🎈 data web app development

st.set_page_config(page_title="Data Dashboard", page_icon="✅", initial_sidebar_state="auto", layout="wide")

# Read csv
# dataset_url = "E:\\GUI\\GUI\\Dataset\\IOCL\\vibration\\compressors\\"
dataset_url = "C:\\Users\\KuldeepRana\\Downloads\\Python-NSE-Option-Chain-Analyzer-master\\Python-NSE-Option-Chain-Analyzer-master"
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)
# Dashboard title
st.title("CSV Data to Dashboard")
job_filter = st.selectbox("Select the Equipment", ["NSE-OCA-BANKNIFTY-08-Dec-2022", "NSE-OCA-NIFTY-08-Dec-2022"])
df = pd.read_csv(dataset_url+"\\"+job_filter+".csv")

# creating a single-element container
placeholder = st.empty()
# near real-time / live feed simulation
for seconds in range(len(df)):

    df = pd.read_csv(dataset_url+"\\"+job_filter+".csv")
    with placeholder.container():

        # create three columns
        kpi3, kpi1, kpi2 = st.columns(3)
        kpi5, kpi6, kpi7 = st.columns(3)
        kpi8, kpi9, kpi10 = st.columns(3)
        kpi4, = st.columns(1)
# fill in those three columns with respective metrics or KPIs
        kpi1.metric(
            label="time ⏳",
            value=df["Time"][seconds]
        )

        kpi2.metric(
            label="Call Sum 💍",
            value=df['Call Sum'][seconds]
        )
        kpi3.metric(
            label="Put Sum ☢",
            value=np.mean(df["Put Sum"][seconds-10:seconds])
        )
        kpi4.metric(
            label="Value ☢",
            value=np.mean(df["Value"][seconds-10:seconds])
        )
        kpi5.metric(
            label="Call1 ☢",
            value=np.mean(df["Call1"][seconds-10:seconds])
        )
        kpi6.metric(
            label="Call2 ☢",
            value=np.mean(df["Call2"][seconds-10:seconds])
        )
        kpi7.metric(
            label="Call3 ☢",
            value=np.mean(df["Call3"][seconds-10:seconds])
        )
        kpi8.metric(
            label="Put1 ☢",
            value=np.mean(df["Put1"][seconds-10:seconds])
        )
        kpi9.metric(
            label="Put2 ☢",
            value=np.mean(df["Put2"][seconds-10:seconds])
        )
        kpi10.metric(
            label="Put3 ☢",
            value=np.mean(df["Put3"][seconds-10:seconds])
        )
# create two columns for charts
        fig_col3, fig_col1,fig_col2 = st.columns(3)
        fig_col5, fig_col6, fig_col7 = st.columns(3)
        fig_col8, fig_col9, fig_col10 = st.columns(3)
        fig_col4, = st.columns(1)
        with fig_col4:
            st.markdown("Value")
            fig = px.line(data_frame=df[:seconds], y="Value", x="Time")
            st.write(fig)

        with fig_col1:
            st.markdown("Call Sum")
            fig2 = px.line(data_frame=df[:seconds], x="Time", y="Call Sum")
            st.write(fig2)

        with fig_col2:
            st.markdown("Put Sum")
            fig3 = px.line(data_frame=df[:seconds], x="Time", y="Put Sum",color='Put Sum')
            st.write(fig3)

        with fig_col3:
            st.markdown("Difference")
            fig4 = px.line(data_frame=df[:seconds], x="Time", y="Difference",color= 'Difference')
            st.write(fig4)
        with fig_col5:
            st.markdown("Call1")
            fig5 = px.line(data_frame=df[:seconds], y="Call1", x="Time",color= 'Call1')
            st.write(fig5)

        with fig_col6:
            st.markdown("Call2")
            fig6 = px.line(data_frame=df[:seconds], x="Time", y="Call2",color= 'Call2')
            st.write(fig6)

        with fig_col7:
            st.markdown("Call3")
            fig7 = px.line(data_frame=df[:seconds], x="Time", y="Call3",color= 'Call3')
            st.write(fig7)
        with fig_col8:
            st.markdown("Put1")
            fig8 = px.line(data_frame=df[:seconds], y="Put1", x="Time",color= 'Put1')
            st.write(fig8)

        with fig_col9:
            st.markdown("Put2 ")
            fig9 = px.line(data_frame=df[:seconds], x="Time", y="Put2",color= 'Put2')
            st.write(fig9)

        with fig_col10:
            st.markdown("Put3")
            fig10 = px.line(data_frame=df[:seconds], x="Time", y="Put3",color= 'Put3')
            st.write(fig10)
        st.markdown("Detailed Data View")
        element = st.dataframe(df)
# element.add_rows(df)
        with st.echo():
         st.write('Code executed and data printed')
        time.sleep(1)
