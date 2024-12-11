import streamlit as st
import pandas as pd
import numpy as np

## 1. Title
st.title("AI-IndoJaya")

## 2. Description
st.write("Selamat datang di website Artificial Intelligence karya anak muda Indonesia. Kami ada untuk membantu Anda!")

## 3. Select box1
options=["None","Kesehatan", "Ekonomi"]
choice=st.selectbox("Pilih bidang permasalahan Anda:", options)
st.write(f"Oke Anda memilih bidang {choice}.")

## 4. Select box2
options=["None","Klasifikasi", "Regresi"]
choice=st.selectbox("Pilih tujuan dari permasalahan Anda:", options)
st.write(f"Oke Anda memilih tujuan {choice}.")

## 5. Upload file
file_upload=st.file_uploader("Unggah file dataset Anda (CSV):",type="csv")
if file_upload is not None:
    df=pd.read_csv(file_upload)
    st.write(df)