import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import io
from PIL import Image

st.title("Analysis of students scores")
uploaded_file = st.file_uploader("Choose an Excel file(which has a column named 'scores')", type=["xlsx"])

def calculate_average(scores):
    return sum(scores) / len(scores)

def percentage_distribution(scores):
    bins = {'<=10': 0, '10-13.5': 0, '14-17.5': 0, '>17.5': 0}
    for score in scores:
        if score <= 10:
            bins['<=10'] += 1
        elif score <= 13.5:
            bins['10-13.5'] += 1
        elif score <= 17.5:
            bins['14-17.5'] += 1
        else:
            bins['>17.5'] += 1
    return bins
if uploaded_file:    
    df = pd.read_excel(uploaded_file)
    scores = df['Scores'].dropna().astype(float).tolist()

    if scores:
        st.write("Total students:", len(scores))
        st.write("Average score:", calculate_average(scores))

        dist = percentage_distribution(scores)
        labels = list(dist.keys())
        values = list(dist.values())

        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis("equal")

        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=300)

        buf.seek(0)

        st.markdown("Score distribution.")
        img = Image.open(buf)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(img, width=300)
            st.markdown("The pie chart above shows the percentage distribution of students' scores across different score ranges. This visualization helps to understand how the scores are distributed among the students, indicating which score ranges are more common and which are less frequent.")
