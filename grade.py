import streamlit as st
st.title("grade")
project=st.number_input("enter your project score")
internal=st.number_input("enter your internal score")
external=st.number_input("enter your external score")
if st.button("total"):
    if(project>50 and internal>50 and external>50):
        total=((70/100)*project)+((10/100)*internal)+((20/100)*external)
        st.text(total)
        if(total>90):
           st.success("A grade")
        elif(80<total<90):
            st.success("B grade")
        else:
           st.success("C grade")
    else:
        if(external<50):
            st.error("student failed in external",external)
        if( internal<50 ):
           st.error("student failed in internal",internal)
        if(project<50):
            st.error("student failed in project",project)