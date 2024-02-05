import os
import pandas as pd
import plotly.express as px
import streamlit as st

file = "/DataSet/Data.csv"
path = os.getcwd() + file
data = pd.read_csv(path)
df = data.copy()

def all_vizuals():
    vizuals = [ 
        'توزيع الأعمدة العددية', 'أعمدة البيانات الفئوية', 
        'Box Plots', 'Variance of Target with Categorical Columns'
        ]
    return vizuals

def All_Data():
    Data_head = df.head()
    return Data_head

def Number_rows():
    Data_rows = df.shape[0]
    return Data_rows

def Number_columns():
    Data_columns = df.shape[1]
    return Data_columns

def Columns():
    column = df.columns.to_frame().T
    return column

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

def citys_chart():
    Citys = df.groupby("city").size()
    return Citys

def district_chart():
    district = df.groupby("district").size()
    return district

def Numerical_Column():
    numerical = df.select_dtypes(exclude = 'object').columns
    return numerical

def categorical_Column():
    categorical = df.select_dtypes(include = 'object').columns
    return categorical

def sidebar_multiselect_container(massage, arr, key):
    container = st.sidebar.container()
    select_all_button = st.sidebar.checkbox("Select all for " + key + " plots")
    if select_all_button:
        selected_num_cols = container.multiselect(massage, arr, default = list(arr))
    else:
        selected_num_cols = container.multiselect(massage, arr, default = arr[0])
    return selected_num_cols  