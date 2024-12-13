import streamlit as st
# st.title("This is a simple App")
# st.header("this is heading")
# st.subheader("this is subheading")
# st.success("success message")
# st.error("error message")
st.title("even or odd")
num1=st.number_input("enter number",min_value=1,step=1)
if st.button("even/odd"):
    if num1%2==0:
        st.success("even number")
    else:
        st.error("odd number")