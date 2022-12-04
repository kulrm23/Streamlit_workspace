# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:54:33 2022

@author: abhijeet.ghosh
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----Title
st.title("REVIEW IOCL DATA")
st.markdown("The dashboard will help a researcher to get to know \
more about the available data before proceeding to model building pipeline")

# ----Sidebars
st.sidebar.title("Select Plot type")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

path_core = "E:\\GUI\\GUI\\Dataset\\IOCL\\"
path = "E:\\GUI\\GUI\\Dataset\\IOCL\\vibration\\compressors"
data = pd.read_csv(path + "\\Compressor_1_demo_Axial_Vel.csv")
data2 = pd.read_csv(path+"\\Compressor_1_demo_Horizontal_Vel.csv")
chart_visual = st.sidebar.selectbox('Select Charts/Plot type',
									('Line Chart', 'Bar Chart', 'Bubble Chart','Scatter'))

# ----Checkbox
st.sidebar.checkbox("Show Analysis by plotting against Time", True, key = 1)

selected_usecase = st.sidebar.selectbox('Select Usecase',
									options = ['Vibration',
												'Battery', 'Oil',
												'ESA'])
selected_eqp = st.sidebar.selectbox('Select Equipment Category',
									options = ['FireEngines',
												'Pumps',
												'Compressors'])

selected_eqp_name = st.sidebar.selectbox('Select Equipment Name',
									options = ['BBI_FIRE_ENGINE_1',
                                        'BBI_FIRE_ENGINE_2',
                                        'BBI_FIRE_ENGINE_3',
                                        'BBI_FIRE_ENGINE_4',
                                        'BBI_FIRE_ENGINE_5',
                                        'BBI_FIRE_ENGINE_6',
                                        'Compressor_1_demo_Axial_Vel',
                                        'Compressor_1_demo_Horizontal_Vel',
                                        'Compressor_1_demo_Vertical_Vel',
                                        'Compressor1_Axial_Velocity',
                                        'Compressor1_Horizontal_Velocity',
                                        'Compressor1_Vertical_Velocity',
                                        'Compressor2_Axial_Velocity',
                                        'Compressor2_Horizontal_Velocity',
                                        'Compressor2_Vertical_Velocity'])

path_final = path_core + "\\" + selected_usecase + "\\" + selected_eqp + "\\" + selected_eqp_name+".csv"
try:
    data=pd.read_csv(path_final)
    # ----Figure
    fig = go.Figure()
    
    
    if chart_visual == 'Line Chart':
    	if selected_eqp == 'Compressors':
    		fig.add_trace(go.Scatter(x = data.Time, y = data.rms,
    								mode = 'lines',
    								name = selected_usecase))
    
    	if selected_eqp == 'FireEngines':
    		fig.add_trace(go.Scatter(x = data.Time, y = data,
    								mode = 'lines', name = 'Smoked'))
    	# if selected_usecase == 'Oil':
    	# 	fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    	# 							mode = 'lines',
    	# 							name = 'Never_Smoked'))
    	# if selected_usecase == 'ESA':
    	# 	fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    	# 							mode='lines',
    	# 							name="Unknown"))
    
    elif chart_visual == 'Bar Chart':
    	if selected_usecase == 'Vibration':
    		fig.add_trace(go.Scatter(x = data.Time, y = data.rms,
    								name = selected_usecase))
    
    # 	if selected_usecase == 'Battery':
    # 		fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    # 								 name = 'Smoked'))
    # 	if selected_usecase == 'Oil':
    # 		fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    # 								name = 'Never_Smoked'))
    # 	if selected_usecase == 'ESA':
    # 		fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    # 								name="Unknown"))
    
    # elif chart_visual == 'Scatter':
    # 	if selected_usecase == 'Vibration':
    
    # 	if selected_usecase == 'Battery':
    # 		fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    # 								 name = 'Smoked'))
    # 	if selected_usecase == 'Oil':
    # 		fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    # 								name = 'Never_Smoked'))
    # 	if selected_usecase == 'ESA':
    # 		fig.add_trace(go.Scatter(x = data.rms, y = data.Time,
    # 								name="Unknown"))
    
    elif chart_visual == 'Bubble Chart':
    	if selected_usecase == 'Vibration':
    		fig.add_trace(go.Scatter(x=data.Time,
    								y=data.rms,
    								mode='markers',
    								marker_size=[40, 60, 80, 60, 40, 50],
    								name='Formerly_Smoked'))
    		
    # 	if selected_status == 'Smoked':
    # 		fig.add_trace(go.Scatter(x=data.Country, y=data.Smokes,
    # 								mode='markers',
    # 								marker_size=[40, 60, 80, 60, 40, 50],
    # 								name='Smoked'))
    # 		
    # 	if selected_status == 'Never_Smoked':
    # 		fig.add_trace(go.Scatter(x=data.Country,
    # 								y=data.Never_Smoked,
    # 								mode='markers',
    # 								marker_size=[40, 60, 80, 60, 40, 50],
    # 								name = 'Never_Smoked'))
    # 	if selected_status == 'Unknown':
    # 		fig.add_trace(go.Scatter(x=data.Country,
    # 								y=data.Unknown,
    # 								mode='markers',
    # 								marker_size=[40, 60, 80, 60, 40, 50],
    # 								name="Unknown"))
    
    st.plotly_chart(fig, use_container_width=True)

except:
    pass