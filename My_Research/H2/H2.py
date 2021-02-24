import pyecharts.options as opts
from pyecharts.charts import Bar3D

H2_kinds_X = [
    "PEM(质子交换膜)", "AE（碱性）"]

Indicator_Y = ["ecosystem quality", "human health", "resources", "total"]
Data_Z = [
    [0, 0, 0.044],
    [0, 1, 0.125],
    [0, 2, 0.300],
    [0, 3, 0.469],
    [1, 0, 0.043],
    [1, 1, 0.122],
    [1, 2, 0.296],
    [1, 3, 0.461],
]
data = [[d[1], d[0], d[2]] for d in Data_Z]
(
    Bar3D(init_opts = opts.InitOpts(width = "1600px", height = "800px"))
        .add(
        series_name = "",
        data = data,
        xaxis3d_opts = opts.Axis3DOpts(type_ = "category", data = Indicator_Y,
                                       name = "Indicator type"),
        yaxis3d_opts = opts.Axis3DOpts(type_ = "category", data = H2_kinds_X, name = "Electrolyzer type ",
                                       name_gap = 30),
        zaxis3d_opts = opts.Axis3DOpts(type_ = "value", name = "Points"),
        label_opts = opts.LabelOpts(is_show = True)
        # 数据标签显示

    )
        .set_global_opts(
        visualmap_opts = opts.VisualMapOpts(
            max_ = 0.5,
            range_color = [
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
        )
    )
        .render("H2endpoint1.html")
)
