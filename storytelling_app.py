import streamlit as st
from streamlit.components.v1 import html
import pandas as pd
from ipyvizzu import Chart, Data, Config, Style, DisplayTarget

st.title('Storytelling Data App')


def cria_grafico():
    chart = Chart(width='640px', height='360px', display=DisplayTarget.MANUAL)
    data = Data()
    df = pd.read_csv("data/titanic.csv")
    data.add_df(df)
    chart.animate(data)

    # Configurações

    chart.animate(
        Config(
            {
                "x": "Count", "y": "Sex",
                "label": "Count",
                "title": "Passageiros Titanic"
            }
        )
    )

    chart.animate(
        Config(
            {
                "x": ["Count", "Survived"],
                "label": ["Count", "Survived"],
                "color": "Survived"
            }
        )
    )

    chart.animate(
        Config(
            {
                "x": "Count",
                "y": ["Sex", "Survived"]
            }
        )
    )

    # Style

    chart.animate(
        Style(
            {
                "title": {"fontSize": 35}
            }
        )
    )

    return chart._repr_html_()


GRAFICO = cria_grafico()
html(GRAFICO, width=640, height=360)
