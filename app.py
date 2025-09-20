# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata")

df = pd.read_csv("metadata_sample.csv", low_memory=False)
df.dropna(subset=["title", "abstract"], inplace=True)
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
df["year"] = df["publish_time"].dt.year

# Year filter
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
filtered = df[df["year"].between(year_range[0], year_range[1])]

# Publications per year
st.subheader("Publications Over Time")
st.bar_chart(filtered["year"].value_counts().sort_index())

# Top journals
st.subheader("Top Journals")
st.bar_chart(filtered["journal"].value_counts().head(10))

# Word cloud
st.subheader("Title Word Cloud")
title_text = " ".join(filtered["title"].dropna().astype(str))
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(title_text)
st.image(wordcloud.to_array())

# Sample data
st.subheader("Sample Data")
st.dataframe(filtered[["title", "journal", "publish_time"]].head(10))
