 #import 
import pandas as pd 
import seaborn as sns 
import streamlit as st
import numpy as np 

## title and subheader 
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")


##upload Dataset 
upload = st.file_uploader("Upload Your Data Set (IN CSV FORMAT) ")
if  upload is not None:
    data=pd.read_csv(upload)
    
#show Dataset 
if upload is not  None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head(5))
        if st.button("Tail"):
            st.write(data.tail(5))
        if st.button("Column"):
            st.write(data.columns)
        if st.button("Shape"):
            st.write("Shape of yout data is --" ,data.shape)
## Check data type of Each Colummns:
if upload is not None:
    if st.checkbox("DataType of Each Columns"):
        st.text("DataTypes")
        st.write(data.dtypes)
#Find the shape our DataSet Number of Riws and Number of Columns 
if upload is not None:
    data_shape=st.radio("What dimension do you want to check ?" , ('Rows' , 'Columns'))
    
    if  data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])

## finding the null value present in data set 
if upload is not None:
    test=data.isnull().values.any()
    if test == True:
        if st.checkbox("Null Values in the Data Set"):
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
            st.success("Congratulation!!! ,No Missing Value are Present  ")
    
    
# Find Duplicate values in the data Set 
if upload is not None:
    test1=data.duplicated().any()
    if test1==True:
        st.warning("This DataSet Contains Some Duplicated Value")
        dup=st.selectbox("Do you want to remove duplicated value ",\
            ("Select one" , "Yes" , "No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.write("Yahoo!! Duplicated Values are Removed ")
        if dup=="No":
            st.text("Ok No Problem")

#Get Overall Statistics 
if upload is not None:
    if st.checkbox("Summary Of The DataSet"):
        st.write(data.describe(include='all'))
        
### About Selection 
if st.button("About App"):
    st.write("Build  with StreamLit")
    st.write("Thanks to StreamLit ") 

##By 
if st.checkbox("By"):
    st.success("Shailendra Singh....... ")
            
        
        