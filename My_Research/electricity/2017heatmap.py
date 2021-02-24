from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
import ElectricityData

c = (

    Geo()

        .add_schema(maptype = "china")
        .add(
        "geo",
        [list(z) for z in zip(ElectricityData.provinces, ElectricityData.GWP2017heatmapvalues)],
        type_ = ChartType.HEATMAP,
    )
        .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        .set_global_opts(
        visualmap_opts = opts.VisualMapOpts(min_ = 0,
                                            max_ = 1.2, ),
        title_opts = opts.TitleOpts(title = "Geo-HeatMap"),
    ).render("GWP2017heatmap.html")
)
