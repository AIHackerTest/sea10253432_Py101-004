"""\
输入城市名，查询该城市的天气；
输入 help，获取帮助；
输入 history， 获取查询历史；
输入 quit，退出天气查询系统；\
"""

def prepare_weather_data():
    filepath = "../resource/weather_info.txt"
#    print(filepath)
    dict_weather = dict()
    with open(filepath) as f:
        for line in f:
            key, value = line.strip().split(',')
            dict_weather[key] = value

    return dict_weather

list_history = list()
def add_history(city, result):
    list_history.append("%s:%s" %(city, result))


#        print(dict_weather)

dict_weather = prepare_weather_data()

while True:
    inputstr = input("请输入指令或您要查询的城市名：")
    if inputstr == 'help':
        print(__doc__)
    elif inputstr == 'history':
        for l in list_history:
            print(l)
    elif inputstr == 'quit':
        exit(0)
    else:
        result = ""

        try:
            result = dict_weather[inputstr]
        except Exception as e:
            result = "未找到该城市的天气数据！"

        print(result)
        add_history(inputstr,result)
