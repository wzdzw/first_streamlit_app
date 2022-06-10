
"""
# My first app
ESS-DABW course learning:
"""

import streamlit as st
import pandas as pd
import requests as rqt
import snowflake.connector
from urllib.error import URLError 

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
st.header('Fruityvice fruit advice!')
try:
  fruit_choice = st.text_input('what fruit would like information about?')
  if not fruit_choice:
    st.error("please select a fruit to get information.")
  else: 
    fruityvice_response = rqt.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    st.dataframe(fruityvice_normalized)
except URLError as e:
  st.error()

# do not run anything past here
st.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows)

# allow user to add fruit to the list
fruit_new = st.text_input('what fruit would like to add?','Jackfruit')
st.write('Thanks for adding ', fruit_new)

my_cur.execute("Insert into fruit_load_list values('from_streamlit')")
