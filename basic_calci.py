import streamlit as st
st.title("basic clauclator")
num=st.number_input("enter a number",min_value=1,step=1)
num2=st.number_input("enter a number2",min_value=1,step=1)
if st.button("add"):
    st.text(num+num2)
    st.success("added")