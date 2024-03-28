from xgb import predict
import pandas as pd

test = pd.read_csv('F:/study/大创/桥梁/bridge_testrevised.csv',encoding='gbk')

# 假设你想要使用第一行作为输入
input_data = test.iloc[0].to_dict()

# 将输入数据转换为 DataFrame
input_df = pd.DataFrame(data=input_data, index=[0])
#print(input_df)

input_df['桥梁id+上下行+检查时间'] = pd.to_numeric(input_df['桥梁id+上下行+检查时间'], errors='coerce')

input_dict = input_df.to_dict(orient='records')[0]
print(input_dict)

# # 使用 predict 函数进行预测
# probabilities = predict(input_dict)

# # 打印每个类别的置信度
# print(probabilities)