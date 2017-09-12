"""\
输入城市名，查询该城市的天气；
输入 help，获取帮助；
输入 history， 获取查询历史；
输入 quit，退出天气查询系统；\
"""
import requests

def get_city_weather(cityname):
    '''
    @input cityname
    @return cityweather
    '''

    urlbase = 'http://jisutqybmf.market.alicloudapi.com/weather/query'
    appcode = '09983cef0485484ea7a2e88561521e80'

    url = urlbase + '?city=%s' %cityname
    add_headers = {'Authorization': 'APPCODE ' + appcode}

    result = requests.get(url, headers = add_headers)

    weather_json = result.json()

    #print("%s现在天气：%s" %(cityname, weather_json['result']['weather']))

    weather_data = "天气：" + weather_json['result']['weather'] + "\n" + \
        "气温：" + weather_json['result']['templow'] +"℃ - " + weather_json['result']['temphigh'] + "℃\n" + \
        "更新时间：" + weather_json['result']['updatetime']
    return weather_data



def main():
    """程序主入口
    """
    list_history = list()

    while True:
        inputstr = input("请输入指令或您要查询的城市名：")
        if inputstr == 'help':
            print(__doc__)
        elif inputstr == 'history':
            for items in list_history:
                print(items)
        elif inputstr == 'quit':
            exit(0)
        else:
            result = ""

            try:
                result = get_city_weather(inputstr)
            except:
                result = "未找到该城市的天气数据！"

            print(result)
            list_history.append("%s\n%s" %(inputstr, result))


if __name__ == "__main__":
    # execute only if run as a script
    main()
