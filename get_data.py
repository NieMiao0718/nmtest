#只需要传入test_case对应的function name，即可获取request data，返回字典格式
import json
#打开case文件同名的json文件
#模块、接口名称、接口参数，模块先不管，接口名称使用case名切片，接口参数使用case名对应
f = open("test_login.json")
data = json.load(f)
def get_data(func):
