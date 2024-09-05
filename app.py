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
fig_1.show()

df_sorted = df.sort_values(by=['price','model_year'])
df_loc = df_sorted[25000:26500]
st.header('Compare price distribution between model year and odometer')
fig_2 = px.scatter(df_loc, x='model_year', y= 'price', color= 'odometer', marginal_x= "box", marginal_y= "violin")
fig_2.show()
