import requests

host = 'http://jisutqybmf.market.alicloudapi.com'
path = '/weather/query'
appcode = '09983cef0485484ea7a2e88561521e80'


r = requests.get(host)
print(r.headers)

r.headers['Authorization'] = 'APPCODE ' + appcode

#requests.headers.add_header('Authorization', 'APPCODE ' + appcode)
#requests.add_header('Authorization', 'APPCODE ' + appcode)
url = 'http://jisutqybmf.market.alicloudapi.com/weather/query?city=北京'

r = requests.get(url, headers = r.headers)
print(r.headers)
print(r.text)
