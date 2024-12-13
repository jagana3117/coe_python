import streamlit as st
st.title("shopping bills")
salary=st.number_input("enter your salary: ")
s1=st.number_input("bill1:")
s2=st.number_input("bill2:")
s3=st.number_input("bill3:")
if st.button("total"):
    st.text(s1+s2+s3)
if st.button("percentage"):
    st.text(((s1+s2+s3)/salary)*100)