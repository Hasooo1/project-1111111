import os
import numpy as np
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.simplefilter("ignore")

file = "/DataSet/Data.csv"
XGB_model = "/Saved_model/XGBmodel.sav"
LGBM_model = "/Saved_model/LGBMmodel.sav"
LR_model = "/Saved_model/LRmodel.sav"
#   RF_model = "/Saved_model/RFmodel.sav"

path = os.getcwd() + file
path_XGB = os.getcwd() + XGB_model
path_LGBM = os.getcwd() + LGBM_model
path_LR = os.getcwd() + LR_model
#   path_RF = os.getcwd() + RF_model

XGB = pickle.load(open(path_XGB, 'rb'))
LGBM = pickle.load(open(path_LGBM, 'rb'))
LR = pickle.load(open(path_LR, 'rb'))
#   RF = pickle.load(open(path_RF, 'rb'))

df = pd.read_csv(path)

def LGBM_predict(data):
    Arr = np.array(data)
    ress = Arr.reshape(1,-1)
    return LGBM.predict(ress)

def XGB_predict(data):
    Arr = np.array(data)
    ress = Arr.reshape(1,-1)
    return int(XGB.predict(ress))

def LR_predict(data):
    Arr = np.array(data)
    ress = Arr.reshape(1,-1)
    return int(LR.predict(ress)) 

#def RF_predict(data):
#    Arr = np.array(data)
#    ress = Arr.reshape(1,-1)
#    return int(RF.predict(ress)) 

def All_Citys():
    city_options = df['city'].unique()
    city_options = city_options.tolist()
    return city_options

def district_of_city(City):
    grouped_data = df.groupby('city')
    city_name = City
    districts = grouped_data.get_group(city_name)['district']
    districts = districts.drop_duplicates()
    district_options = districts.tolist()
    return district_options

def All_front():
    front_options = df['front'].unique()
    front_options = front_options.tolist()
    return front_options

def True_and_False_option():
    True_and_False_options = ['يوجد' , 'لا يوجد']
    return True_and_False_options

def True_and_False(choice):
    if choice == 'يوجد':
        return 1
    else:
        return 0

def City_value(City):
    Encoded_df = df.copy()
    le = LabelEncoder()
    le.fit(Encoded_df['city'])
    Encoded_df['city'] = le.transform(Encoded_df['city'])
    city_name = City
    encoded_value = le.transform([city_name])
    return int(encoded_value)

def district_value(district):
    Encoded_df = df.copy()
    le = LabelEncoder()
    le.fit(Encoded_df['district'])
    Encoded_df['district'] = le.transform(Encoded_df['district'])
    district_name = district
    encoded_value = le.transform([district_name])
    return int(encoded_value)

def front_value(front):
    Encoded_df = df.copy()
    le = LabelEncoder()
    le.fit(Encoded_df['front'])
    Encoded_df['front'] = le.transform(Encoded_df['front'])
    front_name = front
    encoded_value = le.transform([front_name])
    return int(encoded_value)