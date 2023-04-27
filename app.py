import streamlit as st 
import pickle
import numpy as np

# importig the 
predict_model=pickle.load(open('static/model_final.pkl','rb'))
drop_down=pickle.load(open('static/data-dropdown_final.pkl','rb'))
st.title('Laptop Price Predictor')


# core
no_of_core=st.selectbox("No of Cores",drop_down['cpu_number_of_cores_1'].unique())

# display in each
display_size=st.selectbox("Display size",drop_down['display_size__inch_1'].unique())

# RAM
ram=st.selectbox("RAM(in GB)",drop_down['memory_ram__gb_1'].unique())

# Storage type
Storage_type=st.selectbox("Storage Type",drop_down['storage_type_1'].unique())

# storage capacity
Storage_capacity=st.selectbox("Storage_capacity(in GB)",drop_down['storage_capacity__gb_1'].unique())

# laptop color
color=st.selectbox("Laptop body color",drop_down['design_color_name_1'].unique())

# company
company=st.selectbox("Company Name:",drop_down['company'].unique())

# laptop type
type_company=st.selectbox("Laptop Type:",drop_down['type'].unique())

# cpu type
cpu_type=st.selectbox("Cpu Type:",drop_down['cpu_type'].unique())

# cpu_implementation
cpu_implementation=st.selectbox("Cpu implemented",drop_down['cpu_implementation'].unique())

if st.button('Predict Price'): 
    query=np.array([no_of_core, display_size, ram, Storage_type, Storage_capacity, color, company,type_company, cpu_type, cpu_implementation])
    query=query.reshape(1,10)
    st.title(int(np.exp(predict_model.predict(query))[0]))