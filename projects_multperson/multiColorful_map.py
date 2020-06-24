'''
@Description: 统一地图显示多个职业数据
@Author: Jkonel
@Date: 2020-06-23 20:45:42
@LastEditors: jkonel
@LastEditTime: 2020-06-24 16:50:39
'''
from pyecharts.charts import Map
from typing import List
import pyecharts.options as opts
from pyecharts.globals import ThemeType
from pyecharts.commons.utils import JsCode
from pyecharts.charts import Timeline, Grid, Bar, Map, Pie, Line


##原始数据结构例子
data1 = [
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
data = [
    {
        'job':'省总职位数',
        'data': [
            {'province': '上海市', 'value': 36987},
             {'province': '云南省', 'value': 1220},
             {'province': '内蒙古自治区', 'value': 140},
             {'province': '北京市', 'value': 19852},
             {'province': '吉林省', 'value': 486},
             {'province': '四川省', 'value': 10155},
             {'province': '天津市', 'value': 1486},
             {'province': '宁夏回族自治区', 'value': 139},
             {'province': '安徽省', 'value': 3609},
             {'province': '山东省', 'value': 3938},
             {'province': '山西省', 'value': 226},
             {'province': '广东省', 'value': 62244},
             {'province': '广西壮族自治区', 'value': 1043},
             {'province': '新疆维吾尔自治区', 'value': 238},
             {'province': '江苏省', 'value': 21811},
             {'province': '江西省', 'value': 1286},
             {'province': '河北省', 'value': 817},
             {'province': '河南省', 'value': 1888},
             {'province': '浙江省', 'value': 15811},
             {'province': '海南省', 'value': 313},
             {'province': '湖北省', 'value': 9495},
             {'province': '湖南省', 'value': 4292},
             {'province': '甘肃省', 'value': 221},
             {'province': '福建省', 'value': 3272},
             {'province': '西藏自治区', 'value': 33},
             {'province': '贵州省', 'value': 359},
             {'province': '辽宁省', 'value': 4003},
             {'province': '重庆市', 'value': 2918},
             {'province': '陕西省', 'value': 4999},
             {'province': '青海省', 'value': 116},
             {'province': '黑龙江省', 'value': 534}]
    },
    {
        'job':'平均薪资',
        'data': [
            {'province': '上海市', 'value': 21733},
             {'province': '云南省', 'value': 9581},
             {'province': '内蒙古自治区', 'value': 8616},
             {'province': '北京市', 'value': 19090},
             {'province': '吉林省', 'value': 8385},
             {'province': '四川省', 'value': 12605},
             {'province': '天津市', 'value': 11359},
             {'province': '宁夏回族自治区', 'value': 7993},
             {'province': '安徽省', 'value': 11381},
             {'province': '山东省', 'value': 10049},
             {'province': '山西省', 'value': 8638},
             {'province': '广东省', 'value': 15687},
             {'province': '广西壮族自治区', 'value': 8558},
             {'province': '新疆维吾尔自治区', 'value': 9180},
             {'province': '江苏省', 'value': 13370},
             {'province': '江西省', 'value': 10127},
             {'province': '河北省', 'value': 8549},
             {'province': '河南省', 'value': 10383},
             {'province': '浙江省', 'value': 15048},
             {'province': '海南省', 'value': 9327},
             {'province': '湖北省', 'value': 11874},
             {'province': '湖南省', 'value': 11501},
             {'province': '甘肃省', 'value': 8451},
             {'province': '福建省', 'value': 15142},
             {'province': '西藏自治区', 'value': 8741},
             {'province': '贵州省', 'value': 9156},
             {'province': '辽宁省', 'value': 10280},
             {'province': '重庆市', 'value': 10788},
             {'province': '陕西省', 'value': 12151},
             {'province': '青海省', 'value': 8492},
             {'province': '黑龙江省', 'value': 7400}]
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
