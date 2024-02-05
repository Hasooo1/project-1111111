import streamlit as st
from setings.EDA_Setings import *

def eda():
    st.set_page_config(page_title="تحليل البيانات", layout="wide", initial_sidebar_state="auto")

    st.dataframe(All_Data())

    st.write("### Basic Statistics")
    st.write("Number of rows: ", Number_rows())
    st.write("Number of columns: ", Number_columns())
   
    st.write("Columns: ")
    st.dataframe(Columns())

    st.write("### All Citys And Districts")
    st.bar_chart(citys_chart())
    st.bar_chart(district_chart())

    st.write("### Districts in the city")
    city = st.selectbox("Enter the city", All_Citys())
    st.selectbox("Available Districts",district_of_city(city))

    st.markdown(" --- ")

    st.markdown("# البيانات التصويرية")

    vizuals = st.sidebar.selectbox("اختار الاشكال التي تريد رويتها", all_vizuals())
    if 'توزيع الأعمدة العددية' in vizuals:
        selected_num_cols = sidebar_multiselect_container('Choose columns for Distribution plots:', Numerical_Column(), 'Distribution')
        st.subheader('توزيع الأعمدة العددية')
        i = 0
        while (i < len(selected_num_cols)):
            c1, c2, c3= st.columns(3)
            for j in [c1, c2, c3]:
                if (i >= len(selected_num_cols)):
                    break    
                fig = px.histogram(df, x = selected_num_cols[i])
                j.plotly_chart(fig, use_container_width = True)
                i += 1
         
    if 'أعمدة البيانات الفئوية' in vizuals:
        selected_cat_cols = sidebar_multiselect_container('Choose columns for Count plots:', categorical_Column(), 'Count')
        st.subheader('أعمدة البيانات الفئوية')
        i = 0
        while (i < len(selected_cat_cols)):
            c1, c2 = st.columns(2)
            for j in [c1, c2]:
                if (i >= len(selected_cat_cols)):
                    break
                fig = px.histogram(df, x = selected_cat_cols[i], color_discrete_sequence=['indianred'])
                j.plotly_chart(fig, use_container_width = True)
                i += 1
    
    if 'Box Plots' in vizuals:
        selected_num_cols = sidebar_multiselect_container('Choose columns for Box plots:', Numerical_Column(), 'Box')
        st.subheader('Box plots')
        i = 0
        while (i < len(selected_num_cols)):
            c1, c2, c3= st.columns(3)
            for j in [c1, c2, c3]:
                if (i >= len(selected_num_cols)):
                    break
                fig = px.box(df, y = selected_num_cols[i])
                j.plotly_chart(fig, use_container_width = True)
                i += 1
    
    if 'Variance of Target with Categorical Columns' in vizuals:
        high_cardi_columns = []
        normal_cardi_columns = []
        for i in categorical_Column():
            if (df[i].nunique() > df.shape[0] / 10):
                high_cardi_columns.append(i)
            else:
                normal_cardi_columns.append(i)
        if len(normal_cardi_columns) == 0:
            st.write('There is no categorical columns with normal cardinality in the data.')
        else:
            st.subheader('Variance of target variable with categorical columns')
            model_type = st.radio('Select Problem Type:', ('Regression', 'Classification'), key = 'model_type')
            selected_cat_cols = sidebar_multiselect_container('Choose columns for Category Colored plots:', normal_cardi_columns, 'Category')
            if 'Target Analysis' not in vizuals:   
                target_column = st.selectbox("Select target column:", df.columns, index = len(df.columns) - 1)
            i = 0
            while (i < len(selected_cat_cols)):
                if model_type == 'Regression':
                    fig = px.box(df, y = target_column, color = selected_cat_cols[i])
                else:
                    fig = px.histogram(df, color = selected_cat_cols[i], x = target_column)
                st.plotly_chart(fig, use_container_width = True)
                i += 1
            if high_cardi_columns:
                if len(high_cardi_columns) == 1:
                    st.subheader('The following column has high cardinality, that is why its boxplot was not plotted:')
                else:
                    st.subheader('The following columns have high cardinality, that is why its boxplot was not plotted:')
                for i in high_cardi_columns:
                    st.write(i)
                st.write('<p style="font-size:140%">Do you want to plot anyway?</p>', unsafe_allow_html=True)    
                answer = st.selectbox("", ('No', 'Yes'))
                if answer == 'Yes':
                    for i in high_cardi_columns:
                        fig = px.box(df, y = target_column, color = i)
                        st.plotly_chart(fig, use_container_width = True)
            
eda()