import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("Marks.csv")
fig=ff.create_distplot([df["In Percentage"].tolist()],["Percent"],show_hist=True)
fig.show()