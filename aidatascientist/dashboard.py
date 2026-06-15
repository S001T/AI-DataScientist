import streamlit as st

from aidatascientist import DataAgent


st.title(
    "AI Data Scientist"
)

file = st.file_uploader(
    "Upload CSV"
)

if file:

    with open(
        "uploaded.csv",
        "wb"
    ) as f:

        f.write(
            file.read()
        )

    agent = DataAgent()

    agent.load(
        "uploaded.csv"
    )

    stats = agent.analyze()

    st.json(stats)

    if st.button(
        "Generate Charts"
    ):

        charts = (
            agent.visualize()
        )

        for chart in charts:

            st.image(chart)