'''
@Description: 统一地图显示多个职业数据
@Author: Jkonel
@Date: 2020-06-23 20:45:42
@LastEditors: jkonel
@LastEditTime: 2020-06-24 10:56:42
'''
from pyecharts.charts import Map
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line


##原始数据结构例子
data = [
    {
        'job':'java',
        'data': [
            {"province": "广东", "value": 2222},
            {"province": "江苏", "value": 2555},
            {"province": "山东", "value": 5000},
            #.............#
            {"province": "宁夏", "value": 2200},
            {"province": "西藏", "value": 3000}
            ]
    },
    {
        'job':'python',
        'data': [
            {"province": "广东", "value": 2222},
            {"province": "江苏", "value": 2555},
            {"province": "山东", "value": 5000},
            #.............#
            {"province": "宁夏", "value": 2200},
            {"province": "西藏", "value": 3000}
            ]
    },
]


'''
@description: 得到名字列表特定名字下标
@param : list,name
@return: index
'''
def get_list_index(list, str):
    index = 0
    for stri in list:
        if stri is str:
            return index
        else:
            index += 1
    return None

'''
@description: 
@param : job_name:'java';a:规范化数据;name:规范化名字列表
@return: grid_chart
'''
def get_chart(job_name, a, name):
    index = get_list_index(name, job_name)
    da = a[index]
    maxNum = max([x[1] for x in da])
    minNum = min([x[1] for x in da])

    map_chart = (
        Map()
        .add(
            series_name="",
            data_pair=da,
            zoom=1,
            center=[119.5, 34.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title = job_name,###
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                formatter=JsCode(
                    """function(params) {
                    if ('value' in params.data) {
                        return params.data.value[2] + ': ' + params.data.value[0];
                    }
                }"""
                ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="30",
                pos_top="center",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=10,
                max_=2000,
            ),
        )
    )
    bar_x_data = [x[0] for x in da]
    bar_y_data = [{"name": x[0], "value": x[1]} for x in da]
    bar = (
        Bar()
        .add_xaxis(xaxis_data=bar_x_data)
        .add_yaxis(
            series_name="",#job_name,##
            yaxis_data=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
        .reversal_axis()
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(
                max_=maxNum, axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                range_color=["lightskyblue", "yellow", "orangered"],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=minNum,
                max_=maxNum,
            ),
        )
    )

    pie = (
        Pie()
        .add(
            series_name = "",#job_name,##
            data_pair = da,###
            radius=["15%", "35%"],
            center=["80%", "82%"],
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    
    grid_chart = (
        Grid()
            .add(
                bar,
                grid_opts=opts.GridOpts(
                    pos_left="10", pos_right="85%", pos_top="90%", pos_bottom="5"
                ),
            )
        .add(map_chart, grid_opts=opts.GridOpts())
        .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
    )
    return grid_chart


'''
@description: 地图主输出函数
@param : 规范原始数据
@return: 地图输出
'''
def multicolorful_map(data):
    #有多少name就有多少个a元素
    name = [x['job'] for x in data]
    a = [ [[x['province'],x['value']] for x in d['data'] ] for d in data]
    #a =[[x['province'],x['value']] for x in data]

    timeline = Timeline(
        init_opts=opts.InitOpts(width="960px", height="480px", theme=ThemeType.DARK)
    )
    indexs = 0
    for job_name in name:
        timeline.add(get_chart(job_name, a, name), time_point=indexs)
        indexs+=1

    timeline.add_schema(
        orient="vertical",
        is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    return timeline

timelines = multicolorful_map(data)
timelines.render_notebook()
