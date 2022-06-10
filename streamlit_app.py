
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
my_fruit_list = my_fruit_list.set_index('Fruit')

# put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show = my_fruit_list.loc[fruits_selected]

# display fruit table on the page
st.dataframe(fruit_to_show)

# new section to display fruitvice API response
import requests
st.header('Fruityvice fruit advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
st.text(fruityvice_response.json())
