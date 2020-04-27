import  requests,math
import  json
#
# def read_key():
#     """  持久化key,便于读取 """
#     key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'user-key')
#     print(key_path)
#     with open(key_path, 'r', encoding='utf-8') as f:
#         key = f.read()
#         print(key)
#     return key
# #
# def request_url_get(url):
#     """ 请求url方法get方法 """
#     try:
#         r = requests.get(url=url, timeout=30)
#         if r.status_code == 200:
#             return r.text
#         return None
#     except RequestException:
#         print('请求url返回错误异常')
#         return None

import  os



def read_key():
    # 读取本地的key
    key_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'user_key')
    print(key_path)
    with open(key_path,'r', encoding= 'utf-8') as f:
        key = f.read()
        print("key",key)
    return  key
def requests_url_key(url):
    try:
        r = requests.get(url = url,timeout= 30 )
        if r.status_code == 200:
            return r.text
    except EOFError as e:
        print("请求错误",e)


def  pare_json(content_json):
    result = json.loads(content_json)
    return result


def requset_api(url):
    result=   requests_url_key(url= url)
    result_json = pare_json(result)
    return  result_json



def run():
    # keywords="成都理工大学"
    # city = 'chengdu'
    origin = "116.481028,39.989643"
    destination = "116.434446,39.90816"
    key = read_key()
    offset = 20

    index_url  = f'https://restapi.amap.com/v3/direction/walking?key={key}&origin={origin}&destination={destination}'
    index_result = requset_api(index_url)
    pages = math .ceil(int(index_result['count'])/offset)

    for page  in range(1, pages +1):
        url =f'https://restapi.amap.com/v3/direction/walking?key={key}&origin={origin}&destination={destination}&limit =2&offset = 2'
        result = requset_api(url)
        print('result',result)
        with open('read.josn','w') as f:
            f.write(str(result))

if __name__ == '__main__':
    a = run()
    print(a)
