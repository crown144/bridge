import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import pickle
from sklearn.preprocessing import LabelEncoder



train = pd.read_csv('bridge_train.csv')
target='桥梁评级'
IDcol = '桥梁id+上下行+检查时间'
le = LabelEncoder()
train[target] = le.fit_transform(train[target])

'''训练集预处理'''
for col in train.columns:
    if col not in ['桥梁id+上下行+检查时间','桥梁评级','定期检查时间','工作时间','年日均交通量','建成时间','上下行','是否预应力桥梁']:
        for x in train.index:
            if(train[col][x]!=train[col][x]):
                train.loc[x,col]=0
aver={}
for col in ['定期检查时间','工作时间','年日均交通量','建成时间','上下行','是否预应力桥梁']:
    cnt=0
    sum=0
    for x in train.index:
        if(train[col][x]!=train[col][x]):
            continue
        sum=sum+train[col][x]
        cnt=cnt+1
    aver[col]=sum/cnt
for col in ['定期检查时间','工作时间','年日均交通量','建成时间','上下行','是否预应力桥梁']:
    for x in train.index:
        if (train[col][x] != train[col][x]):
            train.loc[x,col]=aver[col]


x_columns = [x for x in train.columns if x not in [target, IDcol]]
X_train = train[x_columns]
y_train = train['桥梁评级']
dtrain = xgb.DMatrix(X_train, label=y_train)


# booster:
params = {'booster': 'gbtree',
          'objective': 'multi:softmax',
          'num_class':3,
          'eval_metric': 'auc',
          'max_depth': 10,
          'lambda': 10,
          'subsample': 0.75,
          'colsample_bytree': 0.75,
          'min_child_weight': 2,
          'eta': 0.025,
          'seed': 0,
          'nthread': 8,
          'gamma': 0.3,
          'learning_rate': 0.2}

num_rounds = 200
bst = xgb.train(params, dtrain,num_rounds)
# 假设您希望保存模型为'model.pkl'文件
with open('model.pkl', 'wb') as f:
    pickle.dump(bst, f)

# y_pred = bst.predict(dtest)

# print(classification_report(y_test, y_pred))
# print(metrics.accuracy_score(y_test, y_pred, normalize=True))