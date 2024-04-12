from django.shortcuts import render,HttpResponse
import jwt
from app01 import models
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime,timedelta
from bridge import settings
from django.forms.models import model_to_dict
from django.apps import apps
import os,sys
sys.path.append("..")
from algorithm import gdbt

#增加条目
def insert_data_from_json(json_data,username):
    #print(type(json_data))
    #print(json_data)
    for model_name, data_dict in json_data.items():
        try:
            model_class = apps.get_model(app_label='app01', model_name=model_name)
        except LookupError:
            print(f"Model {model_name} not found.")
            continue
        data_dict['上传用户'] = username
        instance = model_class()
        for key, value in data_dict.items():
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
    # phone = request.GET.get('phone')
    # insert into
    # user = User(username ='xiaoming',password = '123456')
        result = '注册失败'
    #try:
        user = models.user_info.objects.filter(username=username)
        if user:
            result = '用户已存在'
        else:
            models.user_info.objects.create(username=username, password=password,enterprise_name=enterprise_name,permission="E")
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
        #print(username)
        user = models.user_info.objects.get(username = username)
        userinfo_dict=dict(models.user_info.Permission_CHOICES)
        permission = userinfo_dict[user.permission]
        if(permission == 'Enterprise'):
            try:
                #多条查询要用filter
                bridge_list = models.App01BasicInfo.objects.filter(上传用户 = username)
                results_list = []
                for bridge in bridge_list:
                    result = model_to_dict(bridge)
                    results_list.append(result)
                json_response = json.dumps(results_list)
                return HttpResponse(json_response, content_type="application/json")
                #return HttpResponse('Yes')
            except:
                return HttpResponse(json.dumps('未查询到相关数据'))
        elif(permission == 'Admin'):
            try:
                bridge = models.App01BasicInfo.objects.all()
                result = []
                for i in bridge:
                    result.append(model_to_dict(i))
                return HttpResponse(json.dumps(result), content_type="application/json")
            except:
                return HttpResponse(json.dumps('未查询到相关数据'))
        elif(permission == 'Client'):
            return HttpResponse(json.dumps('权限不足'))

'''
header里Authorization里加jwt token
body:
{
'App01BasicInfo':{'桥梁id','定期检查时间','工作时间','年日均交通量','建成时间','上下行','是否预应力桥梁'},
‘BeamBaseplateConcreteCracking’:{'bridge_id','梁体底板混凝土破损跨径','平均数量','平均面积_m2_field','总面积_m2_field','数量','最大面积_m2_field'},
'BeamBaseplateXCracking':{'bridge_id','梁体底板横向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度占比','每延米数量','长度总和_cm_field'},
'BeamBaseplateYCracking':{'bridge_id','梁体底板纵向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度占比','长度总和_cm_field'},
'BeamSteelCorrosion':{'bridge_id','梁体钢筋锈蚀跨径','平均数量','平均长度_m_field','数量','最大长度_m_field','长度总和_m_field'},
'BeamWebplateConcreteCracking':{'bridge_id','梁体腹板混凝土破损跨径','平均数量','平均面积_m2_field','总面积_m2_field','数量','最大面积_m2_field'},
'BeamWebplateZCracking':{'bridge_id','梁体腹板竖向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度占比','长度总和_cm_field'},
'BeamWingplateXCracking':{'bridge_id','梁体翼板横向裂缝跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','平均间距','数量','最大宽度_mm_field','最大长度_cm_field','长度总和_cm_field'},
'BearingCracking':{'bridge_id','支座开裂跨径','宽度总和_mm_field','平均宽度_mm_field','平均数量','平均长度_cm_field','数量','最大宽度_mm_field','最大长度_cm_field','长度总和_cm_field'},
'BearingDeformation':{'bridge_id','支座变形跨径','平均数量','数量'},
'BearingHanging':{'bridge_id','支座脱空跨径','平均数量','数量'},
'BridgeGrading':{'bridge_id','桥梁等级'},
'ConcreteBreakage':{'bridge_id','缩缝混凝土开裂跨径','平均数量','平均面积_m2_field','总面积_m2_field','数量','最大面积_m2_field'},
'PierCracking':{'bridge_id','墩台裂缝跨径','宽度总和_m_field','平均宽度_m_field','平均数量','平均长度_cm_field','数量','最大宽度_m_field','最大长度_cm_field','长度总和_cm_field'},
'PierSteelCorrosion':{'bridge_id','墩台钢筋腐蚀跨径','平均数量','平均长度_m_field','数量','最大长度_m_field','长度总和_m_field'}
}
'''
@csrf_exempt
def add_datalist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        http_authori = request.META.get('HTTP_AUTHORIZATION')
        decoded_jwt = decode_jwt_token(http_authori)
        username = decoded_jwt['data']['username']
        insert_data_from_json(data,username)
        return HttpResponse(json.dumps({'status':'success'}))
    
### 在请求头里Authorization里加jwt token
### body:
### {
###     'bridge_id': 'xxx'}
### }
@csrf_exempt
def delete_datalist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        http_authori = request.META.get('HTTP_AUTHORIZATION')
        decoded_jwt = decode_jwt_token(http_authori)
        username = decoded_jwt['data']['username']
        userinfo = models.user_info.objects.get(username = username)
        bridgeinfo = models.App01BasicInfo.objects.get(桥梁id = data['bridge_id'])
        
        userinfo_dict=dict(models.user_info.Permission_CHOICES)
        permission = userinfo_dict[userinfo.permission]
        if(permission == 'Admin' or username == bridgeinfo.上传用户):
            models.App01BasicInfo.objects.filter(桥梁id = data['bridge_id']).delete()
            return HttpResponse(json.dumps({'status':'success'}))
        else:
            return HttpResponse(json.dumps({'status':'无权执行此操作'},ensure_ascii=False))
        

### 在请求头里Authorization里加jwt token
### body:
### {
###     'bridge_id': 'xxx',
###     '要修改的数据表名':{'要修改的字段名':'要修改的值'}
### }
@csrf_exempt
def update_datalist(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        http_authori = request.META.get('HTTP_AUTHORIZATION')
        decoded_jwt = decode_jwt_token(http_authori)
        username = decoded_jwt['data']['username']
        userinfo = models.user_info.objects.get(username = username)
        userinfo_dict=dict(models.user_info.Permission_CHOICES)
        permission = userinfo_dict[userinfo.permission]
        bridgeinfo = models.App01BasicInfo.objects.get(桥梁id = data['bridge_id'])
        if(permission == 'Admin' or username == bridgeinfo.上传用户):
            for model_name, data_dict in data.items():
                print(data_dict)
                try:
                    model_class = apps.get_model(app_label='app01', model_name=model_name)
                except LookupError:
                    print(f"Model {model_name} not found.")
                    continue
                #获取要修改的数据表的实例,不止是app01basicinfo
                try:
                    revise_table = model_class.objects.get(桥梁id = data['bridge_id'])
                    print(revise_table)
                except:
                    revise_table = model_class.objects.get(bridge_id = data['bridge_id'])
                    print(revise_table)
                for key, value in data_dict.items():
                    setattr(revise_table, key, value)
                revise_table.save()
            return HttpResponse(json.dumps({'status':'success'}))
        else:
            return HttpResponse(json.dumps({'status':'无权执行此操作'},ensure_ascii=False))
        
#传入机器算法模型
#从request.body中获取json数据转化为一个dict，将这个dict传入算法模型
#json格式见test.json
@csrf_exempt
def assess(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        #print(data)
        result = gdbt.predict(data)
        return HttpResponse(json.dumps(result))