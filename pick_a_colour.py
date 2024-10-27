import streamlit as st

color = st.color_picker("Pick A Color", "#F90004")
st.write("The current color is", color)