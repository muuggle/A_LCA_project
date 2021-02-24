import random

from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker
import pandas as pd
import numpy as np

df = pd.read_csv('different types end 2017.csv')
Indicators = df.iloc[0:, 0].tolist()
Type1 = df.columns.values.tolist()
Types = Type1[1:]
data = df.iloc[0:, 1:]
print(data)

value = [[i, j, data.iloc[i, j]] for i in range(20) for j in range(11)]
print(value)

c = (
    HeatMap()
    .add_xaxis(Indicators)
    .add_yaxis(
        "series0",
        Types,
        value,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="HeatMap-Label 显示"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("heatmap_with_label_show.html")
)
