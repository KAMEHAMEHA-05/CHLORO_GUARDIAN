# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 01:01:24 2023

@author: Admin
"""


import streamlit as st
from annotated_text import annotated_text

st.set_page_config(page_title='ChloroGaurdian', page_icon='https://lh6.googleusercontent.com/HLD2JXwK52tt965RS9UZFen52lpSUHyNOyOODuAlFdjbxyoD7v0ul3JgTZLkBzL2cgOWvfH5f20M5kmKnDc8yTU',menu_items={'About' : "Consider me to be Ishaan's blessing for you"})
st.markdown(
    """
    <style>
@font-face {
  font-family: 'Comfortaa', cursive;
  font-style: bold;
  font-weight: 750;
  src: url("https://fonts.googleapis.com/css2?family=Cinzel&display=swap") format('woff2');
  unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02BB-02BC, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2122, U+2191, U+2193, U+2212, U+2215, U+FEFF, U+FFFD;
}

html, body, [class*="css"]  {
font-family: 'Comfortaa', cursive;
font-size: 23px;
}
</style>

    """, 
    unsafe_allow_html=True,
)

st.markdown(
     f"""
     <style>
     .stApp {{
         background: url("https://i.postimg.cc/tgy7wv1s/bacggron-overlay.png");
         background-size: cover
     }}
     </style>
     """,
     unsafe_allow_html=True
 )

st.image('https://i.postimg.cc/1zGf0tbR/yay-stealing-but-white.png', width = 50)
st.image("https://i.postimg.cc/wjSN7BRm/chloroguardian-clean-Dirty-Yellow.png")
st.write('')
st.write('')
txt = "As the manual analyzation and hours of intense study for the detection of infections becomes quite cumbersome, the best way to save time and human resources is to instead produce an artificial intelligence capable of studying thousands of plant diseases and be able to instantly detect one. Our website has been equipped with machine learning to be able to detect plant diseases that show morphological symptoms in their leaves and diagnose them so as to quickly cull the spread of this disease further."
st.write(txt)
