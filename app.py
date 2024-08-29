#Importing packages
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
    
st.header('Data viewer')
st.dataframe(df)

checkbox = st.checkbox('Type', value=True)
if checkbox:
    type = 'type'
else:
    type = None
st.header('Compare price distribution between condition and type')
fig_1 = px.histogram(df, x= 'condition', y= 'price', color= type)
st.write(fig_1)

st.header('Compare price distribution between model year and odometer')
fig_2 = px.scatter(df, x='model_year', y= 'odometer', color= 'condition', marginal_x= "box", marginal_y= "violin")
st.write(fig_2)
