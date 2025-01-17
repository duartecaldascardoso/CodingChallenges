import streamlit as st

st.set_page_config(page_title="Home", page_icon=":rocket:", layout="wide")

st.title("Welcome to Coding Challenges!")

st.write(
    "This is a collection of coding challenges that will test your knowledge in one of the following programming languages: "
)

st.radio("Select a language", ["Python", "JavaScript", "Java", "C++"], horizontal=True)