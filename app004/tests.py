from django.test import TestCase
import  requests,json
from django.http import JsonResponse
# Create your tests here.
def get_info(request):
    url = f'http://127.0.0.1:8000/student/3/'
    response = requests.get(url=url)
    return JsonResponse(response.text,safe= False)
# def requests_url_key(url):
#     try:
#         r = requests.get(url = url,timeout= 30 )
#         print("R",r)
#         if r.status_code == 200:
#             return r.text
#     except EOFError as e:
#         print("请求错误",e)
def requests_url_key(url):
    payload = dict(key1='value1', key2='value2')
    try:
        r = requests.patch(url = url,data=payload )
        print("R",r)
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

    index_rul = f'http://127.0.0.1:8000/jsons/'
    index_res = requset_api(index_rul)
    print(index_res)


def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + int(myDict[i])

    return sum

def runs_get():
    paydata =     {
    "name": '80',
    "sid": '802',
    }
    # 身份认证令牌 https://www.cnblogs.com/xuxinstyle/p/9675541.html
    headers = {'Authorizations': 'token 26f153854049bd835f6fb971c9128e2f1f1af33e'}
    r = requests.post(f'http://127.0.0.1:8000/student/', data=paydata,headers = headers)

def runs_gets():
    paydata = {
        "name": '80',
        "sid": '802',
    }
    headers = {'Authorization': 'token 26f153854049bd835f6fb971c9128e2f1f1af33e'}    # 身份认证令牌
    r = requests.post(f'http://127.0.0.1:8000/student/', data=paydata,headers = headers)
    r_text = json.loads(r.text)
    print((r_text))
    sums = returnSum(r_text)
    return sums
if __name__ == '__main__':
    a = runs_gets()
    print(a)
