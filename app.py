import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as com 
import pickle
import requests
import json
import numpy as np
import webbrowser

# importig the 
predict_model=pickle.load(open('static/model_final.pkl','rb'))
drop_down=pickle.load(open('static/data-dropdown_final.pkl','rb'))


# this is api connection
url='https://api.device-specs.io/api/laptops?populate=*&pagination[page]=1'
data=requests.get(url,headers={'Authorization':'Bearer 65ff876523a821ccf99ed356e2236bcc525b53c67fc353f4642cfe1c75c72bd8eab6dd9fcd7173f3c0c5a8fc092b9296dfc5703d8f2e007b2b1e38e519803273dde5a64752fcc89a5d650fd524319c2539c4ad2691e0f1bb0fe4ce6b4f36a94aaf8b02b5583864e5164f639ea2bcbe374164d2b3f264f1fb9b66f29f14936dc2'})

with st.sidebar:
    selected=option_menu(
        menu_title="Main Menu",
        options=['Laptop Price Prediction','Latest Laptops Available']

    )

# for Price Prediction
if selected=='Laptop Price Prediction':
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
        st.title("Approximated price : {}₹".format(int(np.exp(predict_model.predict(query))[0])))
        st.write("(According to given configuration)")

# Define CSS style for container
container_style = '''
    border-radius: 10px;
    border: 1px solid black;
    background-color: #262730;
    padding: 10px;
'''
def display_laptop_details(laptop):
        container=st.container()
        container.style=container_style
        with container:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(laptop['image'], use_column_width=True)
            with col2:
                st.write(f"{laptop['name']}")
                st.write(f"{laptop['info']}")
                st.write(f"Price:{laptop['price']} {laptop['currency']} ")
                if st.button("View Product",key=f"{laptop['key']}"):
                    webbrowser.open_new_tab(laptop['url'])
            # container = st.empty()
        # container.markdown(f'<div style="{container_style}">{container}</div>', unsafe_allow_html=True)

if selected=='Latest Laptops Available':
    st.title("Latest Laptops are here")
    # st.write(data)
    d=json.loads(data.content.decode('utf-8'))
    main_data=d['data']
    count=0
    # print(len(main_data..))
    # st.write(main_data)
    for i in range(5):
        # st.write(main_data[i])
        print(main_data[i])
        name=main_data[i]['name']
        info=main_data[i]['info']
        img=main_data[i]['images'][0]['url']
        price=main_data[i]['prices'][0]['price']
        currency=main_data[i]['prices'][0]['currency']
        url=main_data[i]['prices'][0]['url']
        laptop={
            'name':name,
            'info':info,
            'image':img,
            'price':price,
            'currency':currency,
            'key':i,
            'url':url
        }
        container=st.container()
        container.style=container_style
        with container:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(laptop['image'], use_column_width=True)
            with col2:
                st.write(f"{laptop['name']}")
                st.write(f"{laptop['info']}")
                st.write(f"Price:{laptop['price']} {laptop['currency']} ")
                if st.button("View Product",key=f"{laptop['key']}"):
                    webbrowser.open_new_tab(laptop['url'])
        # display_laptop_details(laptop)
    # display_laptop_details(laptop)
#     {'id': 2881,
#   'name': 'Msi Katana GF76 11UC-655NL',
#   'mpn': '9S7-17L212-655',
#   'images': [{'url': 'https://devices-api-prd.s3.eu-west-3.amazonaws.com/baeaa801abbf0e5f3101eec2a2616a74.jpg'}],
#   'prices': [{'price': 1271,
#     'old_price': 999,
#     'currency': 'EUR',
#     'url': 'https://www.bol.com/be/nl/p/msi-katana-gf76-11uc-655nl-gaming-laptop-17-3-inch/9300000075189520/'}],
#   'info': 'Intel Core i7 - i7-11800H - 8 cores - 17.3 inch - 16GB - 512GB SSD - Black - 9S7-17L212-655',
#   'main': {'cpu_type': 'Intel Core i7',
#    'cpu_implementation': 'i7-11800H',
#    'cpu_number_of_cores': 8,
#    'display_size__inch': 17.3,
#    'memory_ram__gb': 16,
#    'storage_type': 'SSD',
#    'storage_capacity__gb': 512,
#    'design_color_name': 'Black'}}


# 65ff876523a821ccf99ed356e2236bcc525b53c67fc353f4642cfe1c75c72bd8eab6dd9fcd7173f3c0c5a8fc092b9296dfc5703d8f2e007b2b1e38e519803273dde5a64752fcc89a5d650fd524319c2539c4ad2691e0f1bb0fe4ce6b4f36a94aaf8b02b5583864e5164f639ea2bcbe374164d2b3f264f1fb9b66f29f14936dc2