from django.shortcuts import render,HttpResponse
import jwt
from app01 import models
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime,timedelta
from bridge import settings
from django.forms.models import model_to_dict
from django.apps import apps

#增加条目
def insert_data_from_json(json_data):
    for model_name, data_list in json_data.items():
        try:
            model_class = apps.get_model(app_label='app01', model_name=model_name)
        except LookupError:
            print(f"Model {model_name} not found.")
            continue
        
        for data in data_list:
            instance = model_class()
            for key, value in data.items():
                setattr(instance, key, value)
            instance.save()


#jwt token加密
def encode_jwt_token(username):
    payload = {
        'exp': datetime.utcnow() + timedelta(seconds=3600),  # 单位秒
        'iat': datetime.utcnow(),
        'data': {'username': username}
        }
    JWT_SECRET_KEY = settings.SECRET_KEY
    encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm='HS256')
    return encoded_jwt

#jwt token解密
def decode_jwt_token(token):
    JWT_SECRET_KEY = settings.SECRET_KEY
    username = jwt.decode(token, JWT_SECRET_KEY, algorithms=['HS256'])
    return username


# Create your views here.
def index(request):
    return HttpResponse('hello')

### 登录传递一个json，包含username和password
### 形如{'username':'xxx','password':'xxx'} 
@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        try:
            user = models.user_info.objects.get(username = username)
            # userinfo_dict=dict(models.user_info.Permission_CHOICES)
            if user:
                if user.password == password:
                    encoded_jwt = encode_jwt_token(user.username)
                    return HttpResponse(json.dumps({'status':'登陆成功','token':encoded_jwt}),content_type="application/json")
                    #return HttpResponse(json.dumps('登陆成功'))
                else:
                    return HttpResponse(json.dumps({'status':'密码错误'}),content_type="application/json")
        except:
            return HttpResponse(json.dumps({'status':'账号不存在'}),content_type="application/json")

@csrf_exempt
def register(request):
    # 获取客户端通过get请求发送过来的数据
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password = data['password']
        enterprise_name = data['enterprise_name']
        permission = data['permission']
    # phone = request.GET.get('phone')
    # insert into
    # user = User(username ='xiaoming',password = '123456')
        result = '注册失败'
    #try:
        user = models.user_info.objects.filter(username=username)
        if user:
            result = '用户已存在'
        else:
            models.user_info.objects.create(username=username, password=password,enterprise_name=enterprise_name,permission=permission)
            result = '注册成功'
    #except:
        #pass
        return HttpResponse(result)

### 在请求头里Authorization里加jwt token
@csrf_exempt
def datalist(request):
    if request.method == 'POST':
        http_authori = request.META.get('HTTP_AUTHORIZATION')
        decoded_jwt = decode_jwt_token(http_authori)
        username = decoded_jwt['data']['username']
        user = models.user_info.objects.get(username = username)
        userinfo_dict=dict(models.user_info.Permission_CHOICES)
        permission = userinfo_dict[user.permission]
        if(permission == 'Enterprise'):
            try:
                bridge = models.App01BasicInfo.objects.get(上传用户=username)
                result= model_to_dict(bridge)
                return HttpResponse(json.dumps(result), content_type="application/json")
                #return HttpResponse('Yes')
            except:
                return HttpResponse(json.dumps('未查询到相关数据'))
        elif(permission == 'Admin'):
            return HttpResponse('1')
        return HttpResponse('OK')

'''
{
'basic_info':{'桥梁id','定期检查时间','工作时间','年日均交通量','建成时间','上下行','是否预应力桥梁','上传用户'}





}
'''
@csrf_exempt
def add_datalist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        insert_data_from_json(data)
        return HttpResponse('1')