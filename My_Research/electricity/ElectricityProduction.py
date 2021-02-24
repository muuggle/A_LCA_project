# from pyecharts import options as opts
# from pyecharts.charts import Geo
# from pyecharts.globals import ChartType
# import Data2017

# c = (
#     Geo()
#         .add_schema(maptype = "china")
#         .add(
#         "geo",
#         [list(z) for z in zip(Data2017.provinces, Data2017.values)],
#         type_ = ChartType.HEATMAP,
#     )
#         .set_series_opts(label_opts = opts.LabelOpts(is_show = True))
#         .set_global_opts(
#         visualmap_opts = opts.VisualMapOpts(),
#         title_opts = opts.TitleOpts(title = "Geo-HeatMap"),
#     ).render("ElectricityProduction2017.html")
# )
from pyecharts import options as opts
from pyecharts.charts import Map
import ElectricityData

c2017 = (
    Map()
        .add("Electricity Production （亿千瓦时）",
             [list(z) for z in zip(ElectricityData.provinces, ElectricityData.values2017)], "china")
        .set_global_opts(
        title_opts = opts.TitleOpts(title = "Electricity Production 2017"),
        visualmap_opts = opts.VisualMapOpts(min_ = 0,
                                            max_ = 5000,
                                            range_text = ["High", "Low"],
                                            is_calculable = True,
                                            range_color = ["lightskyblue", "yellow", "orangered"],
                                            is_piecewise = True
                                            # 设置为分段形式
                                            ),
    ).set_series_opts(label_opts = opts.LabelOpts(is_show = False)).render("ElectricityProduction2017.html")
)

c2016 = (
    Map()
        .add("电力生产（亿千瓦时）", [list(z) for z in zip(ElectricityData.provinces, ElectricityData.values2016)], "china")
        .set_global_opts(
        title_opts = opts.TitleOpts(title = "Electricity Production 2016"),
        visualmap_opts = opts.VisualMapOpts(min_ = 0,
                                            max_ = 5000,
                                            range_text = ["High", "Low"],
                                            is_calculable = True,
                                            range_color = ["lightskyblue", "yellow", "orangered"],
                                            is_piecewise = True
                                            # 设置为分段形式
                                            ),
    ).set_series_opts(label_opts = opts.LabelOpts(is_show = False)).render("ElectricityProduction2016.html")
)

c2015 = (
    Map()
        .add("电力生产（亿千瓦时）", [list(z) for z in zip(ElectricityData.provinces, ElectricityData.values2015)], "china")
        .set_global_opts(
        title_opts = opts.TitleOpts(title = "Electricity Production 2015"),
        visualmap_opts = opts.VisualMapOpts(min_ = 0,
                                            max_ = 5000,
                                            range_text = ["High", "Low"],
                                            is_calculable = True,
                                            range_color = ["lightskyblue", "yellow", "orangered"],
                                            is_piecewise = True
                                            # 设置为分段形式
                                            ),
    ).set_series_opts(label_opts = opts.LabelOpts(is_show = False)).render("ElectricityProduction2015.html")
)

c2014 = (
    Map()
        .add("电力生产（亿千瓦时）", [list(z) for z in zip(ElectricityData.provinces, ElectricityData.values2014)], "china")
        .set_global_opts(
        title_opts = opts.TitleOpts(title = "Electricity Production 2014"),
        visualmap_opts = opts.VisualMapOpts(min_ = 0,
                                            max_ = 5000,
                                            range_text = ["High", "Low"],
                                            is_calculable = True,
                                            range_color = ["lightskyblue", "yellow", "orangered"],
                                            is_piecewise = True
                                            # 设置为分段形式
                                            ),
    ).set_series_opts(label_opts = opts.LabelOpts(is_show = False)).render("ElectricityProduction2014.html")
)
