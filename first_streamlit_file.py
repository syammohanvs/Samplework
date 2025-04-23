import streamlit as st
import pandas as pd


# Set the title of the Streamlit app
st.title("Auto EDA with Streamlit")
st.header("Explore your dataset with ease!")
st.subheader("Upload your CSV file below:")
st.markdown("This app uses various libraries for *automated Exploratory* **Data Analysis** (EDA).")
st.code("""
import pandas as pd
""",language='python')