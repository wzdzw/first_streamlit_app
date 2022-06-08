
"""
# My first app
ESS-DABW course learning:
"""

import streamlit as st
import pandas as pd
#df = pd.DataFrame({
 # 'first column': [1, 2, 3, 4],
  #'second column': [10, 20, 30, 40]
#})

#df

st.title('My parents new healthy diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3 & BlueberryOatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-boiled free range egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
