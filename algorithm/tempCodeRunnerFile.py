
# gdbt = joblib.load('gdbt.pkl')
# def predict(input_dict):
#     input_df = pd.DataFrame(data=input_dict, index=[0])
#     probabilities = gdbt.predict_proba(input_df)
#     #概率改成百分比，百分比保留两位小数
#     probabilities = [f'{prob*100:.2f}%' for prob in probabilities[0]]
#     return probabilities
