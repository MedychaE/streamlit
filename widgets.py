### for interactive application

import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

## input menu
name=st.text_input("Enter your name:")

## slider menu
age=st.slider("Select your age:",0,100,25)

st.write(f"Your age is {age}.")

## Select box
options=["Python", "Java", "C++", "JavaScript"]
choice=st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name} how are you")

## use dataframe
data={
    "Name":["John", "Jane", "Jake", "Jill"],
    "Age":[28,24,35,40],
    "City":["New York", "Loss Angeles", "Chicago", "Houston"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

## Uplodad button
uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

## go to the streamlit.io to further tools