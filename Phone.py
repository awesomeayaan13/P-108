import pandas as pd
import csv
import plotly.figure_factory as ff

df=pd.read_csv("Phone.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Brand"],show_hist=True)
fig.show()