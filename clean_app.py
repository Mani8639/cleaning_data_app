import streamlit as st
import pandas as pd
import numpy as np

st.title("🔧 Data Cleaning App")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview", df.head())

    st.write("### Missing Values")
    st.write(df.isnull().sum())

    method = st.selectbox("Handle Missing Values", ["None", "Drop Rows", "Fill Mean", "Fill Median", "Fill Mode"])

    if method == "Drop Rows":
        df.dropna(inplace=True)
    elif method == "Fill Mean":
        df.fillna(df.mean(numeric_only=True), inplace=True)
    elif method == "Fill Median":
        df.fillna(df.median(numeric_only=True), inplace=True)
    elif method == "Fill Mode":
        for col in df.columns:
            df[col].fillna(df[col].mode()[0], inplace=True)

    st.write("### After Handling Missing Values")
    st.write(df.head())

    # Download cleaned CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Cleaned Data", csv, "cleaned_data.csv", "text/csv")
