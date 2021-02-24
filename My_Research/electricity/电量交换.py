from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

c = (
    Geo()
        .add_schema(maptype = "china",
                    # itemstyle_opts = opts.ItemStyleOpts(color = "#323c48", border_color = "#111"),
                    )
        .add(
        "",
        # 南方电网
        [("广东", 1), ("海南", 1), ("广西", 1), ("云南", 1), ("贵州", 1)],
        type_ = ChartType.EFFECT_SCATTER,
        color = "black",
        symbol_size = 10
    )
        .add(
        "",
        # 华北电网
        [("北京", 1), ("河北", 1), ("山东", 1), ("山西", 1), ("天津", 1), ("内蒙古", 1)],
        type_ = ChartType.EFFECT_SCATTER,
        color = "blue",
        symbol_size = 10
    )
        .add(
        "",
        # 华东电网
        [("上海", 1), ("浙江", 1), ("江苏", 1), ("福建", 1), ("安徽", 1)],
        type_ = ChartType.EFFECT_SCATTER,
        color = "green",
        symbol_size = 10
    )
        .add(
        "",
        # 华中电网
        [("河南", 1), ("湖北", 1), ("湖南", 1), ("江西", 1), ("重庆", 1), ("四川", 1)],
        type_ = ChartType.EFFECT_SCATTER,
        color = "red",
        symbol_size = 10
    )
        .add(
        "",
        # 东北电网
        [("黑龙江", 1), ("辽宁", 1), ("吉林", 1)],
        type_ = ChartType.EFFECT_SCATTER,
        color = "purple",
        symbol_size = 10
    )
        .add(
        "",
        # 西北电网
        [("新疆", 1), ("青海", 1), ("宁夏", 1), ("陕西", 1), ("甘肃", 1)],
        type_ = ChartType.EFFECT_SCATTER,
        color = "gray",
        symbol_size = 10
    )
        .add(
        "geo",
        [("上海", "广州")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = 0.2, width = 0.1, color = "red"),
        label_opts = opts.LabelOpts
    )
        .add(
        "geo",
        [("北京", "上海")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = 0.4, width = 2.6, color = "purple"),
    )
        .add(
        "geo",
        [("北京", "成都")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = 0.1, width = 0.3, color = "purple"),
    )
        .add(
        "geo",
        [("成都", "上海")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = -0.45, width = 8, color = "green"),
    )
        .add(
        "geo",
        [("广州", "成都")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = 0.6, width = 0.6, color = "gray"),
    )
        .add(
        "geo",

        [("哈尔滨", "北京")],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),

        linestyle_opts = opts.LineStyleOpts(curve = 0, width = 2.2, color = "blue"),
        label_opts = opts.LabelOpts(is_show = True)

    )
        .add(
        "geo",
        [("西宁", "上海")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = 0.1, width = 2, color = "black"),
    )
        .add(
        "geo",
        [("西宁", "北京")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = 0.2, width = 4.8, color = "black"),
    )
        .add(
        "geo",
        [("西宁", "成都")
         ],
        type_ = ChartType.LINES,
        effect_opts = opts.EffectOpts(
            # symbol = SymbolType.ARROW, symbol_size = 6, color = "blue"
            is_show = False,
        ),
        linestyle_opts = opts.LineStyleOpts(curve = -0.2, width = 5, color = "black"),
    )

        .set_series_opts(label_opts = opts.LabelOpts(is_show = False))
        .set_global_opts(title_opts = opts.TitleOpts(title = "Geo-Lines"))
        .render("电量交换.html")
)
