import streamlit
import pandas as pd

streamlit.header('Breakfast Favorites')

streamlit.text(' 🍔 Omega 3 & Blueberry Oatmeal') 
streamlit. text ('03 Kale, Spinach & Rocket Smoothie') 
streamlit.text ('4 Hard-Boiled Free-Range Egg')
streamlit.text('1• Avocado Toast')
                 
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe (my_fruit_list)
