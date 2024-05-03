import streamlit as st

st.set_page_config(
    page_title="Morgan Streamlit",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This platform is a demonstration of the skills I learnt with the Streamlit Library 

    **👈 Select a demo from the sidebar** to see some examples
    of the Streamlit tool I have created!
    ### Want to learn more about me?
    - [My website](https://morgancab.github.io/)
    - [My linkedin](https://www.linkedin.com/in/morgancab/?locale=en_US)
    - [My github](https://github.com/morgancab)
"""
)

