
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

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = rqt.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized

# new section to display fruitvice API response
st.header('Fruityvice fruit advice!')
try:
  fruit_choice = st.text_input('what fruit would like information about?')
  if not fruit_choice:
    st.error("please select a fruit to get information.")
  else: 
    back_from_funciton = get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_funciton)
except URLError as e:
  st.error()

# do not run anything past here


st.header("The fruit load list contains:")
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

# add a button to load the fruit
if st.button("Get Fruit Load List"):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  st.dataframe(my_data_rows)

#st.stop()
# allow user to add fruit to the list
def insert_row(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("Insert into fruit_load_list values('"+ new_fruit +"')")
    return "Thanks for adding " + new_fruit

add_my_fruit = st.text_input('what fruit would like to add?')
if st.button('Add a Fruit to the list'):
  my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
  back_from_function = insert_row(add_my_fruit)
  st.text(back_from_function)


