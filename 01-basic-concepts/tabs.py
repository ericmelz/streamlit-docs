import streamlit as st

tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("Welcome to Tab 1")
    st.write("You can put anything here—charts, text, widgets, etc.")

with tab2:
    st.header("This is Tab 2")
    st.write("Still going strong.")

with tab3:
    st.header("And finally Tab 3")
    st.write("You're a tab pro now.")
