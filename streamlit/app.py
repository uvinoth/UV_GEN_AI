import streamlit as st
import pandas as pd
import numpy as np

# Title of App
st.title("Welcome vinoth")

# 
st.write("Vinoth sons are Athiyan and Agran")

#  Simple dataframe
df = pd.DataFrame({
    "first colum" : [1,2,3,5],
    "second colum": [20,44,4,4]
})

st.write(df)

#  Line chart

chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
