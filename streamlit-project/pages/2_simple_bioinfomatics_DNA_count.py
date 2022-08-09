import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('./dna-logo.jpg')

st.image(image, use_column_width=True)
st.write("""
***
""")
st.write("""
    ## DNA Nucleotide Count Web App
    This app counts the nucleotide composition of query DNA!
    ***
""")


