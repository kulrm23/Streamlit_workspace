import time  # to simulate a real time data, time loop
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  # interactive charts
import streamlit as st  # 🎈 data web app development

st.set_page_config(
    page_title="Real-Time Data Dashboard",
    page_icon="✅",
    layout="wide",)

# Read csv
dataset_url = "E:\\GUI\\GUI\\Dataset\\IOCL\\vibration\\compressors\\"
def get_data() -> pd.DataFrame:

    return pd.read_csv(dataset_url)
# Dashboard title
st.title("Real-Time / Live Data to Dashboard")
# top-level filters
job_filter = st.selectbox("Select the Equipment", ["NSE-OCA-BANKNIFTY-08-Dec-2022"])

df = pd.read_csv(dataset_url+"\\"+job_filter+".csv")

# # creating a single-element container
placeholder = st.empty()
# near real-time / live feed simulation
for seconds in range(len(df)):
    with placeholder.container():
        
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

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
            value = np.mean(df["Put Sum"][seconds-10:seconds])
        )
        # create two columns for charts
        fig_col1, fig_col2, fig_col3 = st.columns(3)
        with fig_col1:
            st.markdown("### Heatmap based condition inferencing")
            fig = px.density_heatmap(
                data_frame=df[:seconds], y="Call Sum", x="Put Sum")
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Live-Streaming "+job_filter)
            fig2 = px.scatter(data_frame=df[:seconds], x="Time", y="Call Sum")
            st.write(fig2)

        with fig_col2:
            st.markdown("### Live-Streaming "+job_filter)
            fig3 = px.scatter(data_frame=df[:seconds], x="Time", y="Put Sum")
            st.write(fig3)

        with fig_col3:
            st.markdown("### Live-Streaming "+job_filter)
            fig4 = px.scatter(data_frame=df[:seconds], x="Time", y="Difference")
            st.write(fig4)
        st.markdown("### Detailed Data View")
        st.dataframe(df, 1)
        
        time.sleep(3)