from pyecharts import options as opts
from pyecharts.charts import Map, Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType

data = [['杭州市', 200], ['宁波市', 200], ['温州市', 30],
        ['嘉兴市', 40], ['湖州市', 50], ['绍兴市', 60],
        ['金华市', 70], ['衢州市', 8], ['舟山市', 90],
        ['台州市', 10], ['丽水市', 110]]

# map = (Map().add("CO2 emission", data, "浙江", zoom = 1).set_global_opts(
#     title_opts = opts.TitleOpts(title = "Map-浙江地图"),
#     visualmap_opts = opts.VisualMapOpts(max_ = 300, is_piecewise = True)
# ).render("map_Zhejiang.html"))
# def map_yunnan() -> Map:
#     c = (
#         Map()
#             .add("CO2 emission", data, "浙江", zoom = 1,maptype="zhejiang" )
#             .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
#             .set_global_opts(
#             title_opts = opts.TitleOpts(title = "浙江碳排放"),
#             visualmap_opts = opts.VisualMapOpts(max_ = 300, is_pziecewise = True
#                                                 # pieces = [{"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
#                                                 #           {"max": 9, "min": 1, "label": "0-9", "color": "#FFE4E1"},
#                                                 #           {"max": 99, "min": 10, "label": "10-99", "color": "#FF7F50"},
#                                                 #           {"max": 499, "min": 100, "label": "100-499",
#                                                 #            "color": "#F08080"},
#                                                 #           {"max": 999, "min": 500, "label": "500-999",
#                                                 #            "color": "#CD5C5C"},
#                                                 #           {"max": 9999, "min": 1000, "label": ">=1000",
#                                                 #            "color": "#8B0000"}]
#                                                 ),
#         )
#     )
#
#     return c
#
#
# d_map = map_yunnan()
# d_map.render("map_zhejiang.html")


citys = ['杭州市', '宁波市', '温州市',
         '嘉兴市', '湖州市', '绍兴市',
         '金华市', '衢州市', '舟山市',
         '台州市', '丽水市']
values = [365, 656, 524, 455, 411, 174, 125, 121, 666, 123, 444]
c = (
    Geo().add_schema(maptype = "浙江")
     .add("CO2 emission", [list(z) for z in zip(citys, values)], type_ = ChartType.SCATTER)
     .set_global_opts(visualmap_opts = opts.VisualMapOpts(), title_opts = opts.TitleOpts(title = "Geo-浙江地图"))
     .set_series_opts(label_opts = opts.LabelOpts(is_show = True)).render("zj.html")
     )
# c = (
#     Geo()
#         .add_schema(maptype = "china")
#         .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
#         .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
#         .set_global_opts(
#         visualmap_opts = opts.VisualMapOpts(), title_opts = opts.TitleOpts(title = "Geo-基本示例")
#     )
#         .render("geo_base.html")
# )
