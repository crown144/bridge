import pickle
import pandas as pd
import xgboost as xgb
from sklearn.metrics import classification_report
import os
import joblib
# test = pd.read_csv('F:/study/大创/桥梁/bridge_testrevised.csv',encoding='gbk')
# target='桥梁评级'
# IDcol = '桥梁id+上下行+检查时间'
# #test去掉target和IDcol列
# test = test.drop([target,IDcol],axis=1)
# #把test第一条数据转换成dict
# test_dict = test.iloc[0].to_dict()
# #把这个dict转换成json,格式为utf-8
# import json
# test_json = json.dumps(test_dict,ensure_ascii=False)
# #将json存储到txt文件中
# with open('test.json','w',encoding='utf-8') as f:
#     f.write(test_json)

def predict(input_dict):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'gdbt.pkl')
    gdbt = joblib.load(model_path)
    input_df = pd.DataFrame(data=input_dict, index=[0])
    probabilities = gdbt.predict_proba(input_df)
    #概率改成百分比，百分比保留两位小数
    probabilities = [f'{prob*100:.2f}%' for prob in probabilities[0]]
    return probabilities
