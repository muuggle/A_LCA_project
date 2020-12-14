import pyecharts.options as opts
from pyecharts.charts import Bar3D

Elec_kinds_X = [
    "photovoltaic3", "photovoltaic", "wind", "wind", "coal", "coal", "hydro", "hydro",
    "naturegas", "naturegas", "others", "others"]

Indicator_Y = ["ecosystem quality", "human health", "resources", "total"]
Data_Z = [
    [0, 0, 0.0015],
    [0, 1, 0.0038],
    [0, 2, 0.0043],
    [0, 3, 0.0096],
    [1, 0, 0.0020],
    [1, 1, 0.0049],
    [1, 2, 0.0056],
    [1, 3, 0.0124],
    [2, 0, 0.0008],
    [2, 1, 0.0024],
    [2, 2, 0.0058],
    [2, 3, 0.0090],
    [3, 0, 0.0008],
    [3, 1, 0.0024],
    [3, 2, 0.0058],
    [3, 3, 0.0090],
    [4, 0, 0.0238],
    [4, 1, 0.0541],
    [4, 2, 0.0352],
    [4, 3, 0.1131],
    [5, 0, 0.019],
    [5, 1, 0.0431],
    [5, 2, 0.0282],
    [5, 3, 0.0903],
    [6, 0, 0.0001],
    [6, 1, 0.0002],
    [6, 2, 0.0004],
    [6, 3, 0.0007],
    [7, 0, 0.0001],
    [7, 1, 0.0002],
    [7, 2, 0.0004],
    [7, 3, 0.0007],
    [8, 0, 0.0123],
    [8, 1, 0.0206],
    [8, 2, 0.0348],
    [8, 3, 0.0677],
    [9, 0, 0.0098],
    [9, 1, 0.0162],
    [9, 2, 0.0276],
    [9, 3, 0.0536],
    [10, 0, 0.0033],
    [10, 1, 0.0039],
    [10, 2, 0.0052],
    [10, 3, 0.0124],
    [11, 0, 0.0002],
    [11, 1, 0.001],
    [11, 2, 0.0006],
    [11, 3, 0.0018],

]
data = [[d[0], d[1], d[2]] for d in Data_Z]
(
    Bar3D(init_opts = opts.InitOpts(width = "1600px", height = "800px"))
        .add(
        series_name = "",
        data = data,
        xaxis3d_opts = opts.Axis3DOpts(type_ = "category", data = Elec_kinds_X,
                                       name = "Power type (left : XJ & right : ZJ)"),
        yaxis3d_opts = opts.Axis3DOpts(type_ = "category", data = Indicator_Y, name = "Indicator type",name_gap = 30),
        zaxis3d_opts = opts.Axis3DOpts(type_ = "value", name = "Points"),
        # label_opts = opts.LabelOpts(is_show = True)
        # 数据标签显示

    )
        .set_global_opts(
        visualmap_opts = opts.VisualMapOpts(
            max_ = 0.12,
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
        .render("endpoint1.html")
)
