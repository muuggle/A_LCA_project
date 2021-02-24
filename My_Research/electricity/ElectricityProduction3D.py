from pyecharts import options as opts
from pyecharts.charts import Map3D
from pyecharts.globals import ChartType
from pyecharts.commons.utils import JsCode

from My_Research.electricity import ElectricityData

# example_data = [
#     ("黑龙江", [127.9688, 45.368, 100]),
#     ("内蒙古", [110.3467, 41.4899, 300]),
#     ("吉林", [125.8154, 44.2584, 300]),
#     ("辽宁", [123.1238, 42.1216, 300]),
#     ("河北", [114.4995, 38.1006, 300]),
#     ("天津", [117.4219, 39.4189, 300]),
#     ("山西", [112.3352, 37.9413, 300]),
#     ("陕西", [109.1162, 34.2004, 300]),
#     ("甘肃", [103.5901, 36.3043, 300]),
#     ("宁夏", [106.3586, 38.1775, 300]),
#     ("青海", [101.4038, 36.8207, 300]),
#     ("新疆", [87.9236, 43.5883, 300]),
#     ("西藏", [91.11, 29.97, 300]),
#     ("四川", [103.9526, 30.7617, 300]),
#     ("重庆", [108.384366, 30.439702, 300]),
#     ("山东", [117.1582, 36.8701, 300]),
#     ("河南", [113.4668, 34.6234, 300]),
#     ("江苏", [118.8062, 31.9208, 300]),
#     ("安徽", [117.29, 32.0581, 300]),
#     ("湖北", [114.3896, 30.6628, 300]),
#     ("浙江", [119.5313, 29.8773, 300]),
#     ("福建", [119.4543, 25.9222, 300]),
#     ("江西", [116.0046, 28.6633, 300]),
#     ("湖南", [113.0823, 28.2568, 300]),
#     ("贵州", [106.6992, 26.7682, 300]),
#     ("广西", [108.479, 23.1152, 300]),
#     ("海南", [110.3893, 19.8516, 300]),
#     ("上海", [121.4648, 31.2891, 1300]),
# ]

c = (
    Map3D()
        .add_schema(
        box_height = 15,
        region_height = 2,
        # is_show_ground = True,
        shading = "lambert",
        itemstyle_opts = opts.ItemStyleOpts(
            color = "rgb(169,169,169)",
            opacity = 1,
            border_width = 0.8,
            border_color = "rgb(245,245,245)",
        ),
        map3d_label = opts.Map3DLabelOpts(
            is_show = False,
            formatter = JsCode("function(data){return data.name + " " + data.value[2];}"),
        ),
        emphasis_label_opts = opts.LabelOpts(
            is_show = False,
            color = "#fff",
            font_size = 10,
            background_color = "rgba(0,23,11,0)",
        ),
        light_opts = opts.Map3DLightOpts(
            main_color = "#fff",
            main_intensity = 1.2,
            main_shadow_quality = "high",
            is_main_shadow = False,
            main_beta = 10,
            ambient_intensity = 0.3,
        ),
    )
        .add(
        series_name = "bar3D",
        data_pair = [list(z) for z in zip(ElectricityData.provinces, ElectricityData.Geo2017)],
        type_ = ChartType.BAR3D,
        is_map_symbol_show = True,
        bar_size = 1.5,
        shading = "lambert",
        bevel_size = 0.2,
        label_opts = opts.LabelOpts(
            is_show = True,
            formatter = JsCode("function(data){return data.value[2];}"),
            font_size = 1,
        ),
        min_height = 0.5,

    )
        .set_global_opts(title_opts = opts.TitleOpts(title = "ElectricityProduction"),
                         visualmap_opts = opts.VisualMapOpts(
                             max_ = 5000,
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
                         ))
        .render("2017_3D.html")
)
