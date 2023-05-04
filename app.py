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
# url='https://api.device-specs.io/api/laptops?populate=*&pagination[page]=1'
# data=requests.get(url,headers={'Authorization':'Bearer 65ff876523a821ccf99ed356e2236bcc525b53c67fc353f4642cfe1c75c72bd8eab6dd9fcd7173f3c0c5a8fc092b9296dfc5703d8f2e007b2b1e38e519803273dde5a64752fcc89a5d650fd524319c2539c4ad2691e0f1bb0fe4ce6b4f36a94aaf8b02b5583864e5164f639ea2bcbe374164d2b3f264f1fb9b66f29f14936dc2'})

list2=[
    {
        'name': 'Msi Katana GF76 11UC-655NL',
        'image':'https://devices-api-prd.s3.eu-west-3.amazonaws.com/baeaa801abbf0e5f3101eec2a2616a74.jpg',
        'price':1271,
        'currency':'EUR',
        'url':'https://www.bol.com/be/nl/p/msi-katana-gf76-11uc-655nl-gaming-laptop-17-3-inch/9300000075189520/',
        'info':'Intel Core i7 - i7-11800H - 8 cores - 17.3 inch - 16GB - 512GB SSD - Black - 9S7-17L212-655'
    },
    {
        'name': 'Apple Macbook Pro',
        'image':'https://devices-api-prd.s3.eu-west-3.amazonaws.com/57413871ce598d16ad7467cfd4a8696b.jpg',
        'price':1599,
        'currency':'EUR',
        'url':'https://www.bestbuy.com/site/macbook-pro-14-laptop-apple-m1-pro-chip-16gb-memory-512gb-ssd-latest-model-silver/6450856.p?skuId=6450856',
        'info':'2021 - Apple M1 Pro - Apple M1 Pro - 8 cores - 14.2 inch - 16GB - 512GB SSD - Silver - MKGR3LL/A'
    },
    {
        'name': 'Medion Akoya E15413',
        'image':'https://devices-api-prd.s3.eu-west-3.amazonaws.com/2d5bfd639ba38ab709bca66f45612aa7.jpg',
        'price':758.54,
        'currency':'EUR',
        'url':'https://azerty.nl/product/e15413-i5-512f8-qwerty/5089957',
        'info':'Intel® Core™ i5 - i5-1235U - 10 cores - 15.6 inch - 8GB - 512GB SSD - Metallic - 30034235'
    },
    {
        'name': 'Microsoft Surface Book 3',
        'image':'https://devices-api-prd.s3.eu-west-3.amazonaws.com/3e6d19881a3cecc045ba50ed684867b5.jpg',
        'price':2519.99,
        'currency':'EUR',
        'url':'https://www.bestbuy.com/site/microsoft-surface-book-3-15-touch-screen-pixelsense-2-in-1-laptop-intel-core-i7-32gb-memory-512gb-ssd-platinum/6408385.p?skuId=6408385',
        'info': '2020 - Intel 10th Generation Core i7 - 1065G7 - 4 cores - 15 inch - 32GB - 512GB SSD - Platinum - SMN-00001'
    },
    {
        'name': 'Asus Rog Zephyrus G14 GA402RJ-L8018W 6900HSL',
        'image':'https://devices-api-prd.s3.eu-west-3.amazonaws.com/52a82d5610a9293c3efbb7668f256503.jpg',
        'price':2114,
        'currency':'EUR',
        'url':'https://www.bol.com/be/nl/p/asus-rog-zephyrus-g14-ga402rj-l8018w-6900hs-notebook-35-6-cm-wqxga-amd-ryzen-9-16-gb-ddr5-sdram-1000-gb-ssd-amd-radeon-rx-6700s-wi-fi-6e-windows-11-home-zwart-grijs/9300000071777997/',
        'info': 'AMD Ryzen™ 9 - 6900HS - 8 cores - 14 inch - 16GB - 1000GB SSD - Eclipse Gray AniMe Matrix version - 90NR09T4-M00430'
    }
]
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
    # d=json.loads(data.content.decode('utf-8'))
    # main_data=d['data']
    # count=0
    # print(len(main_data..))
    # st.write(main_data)
    for i in list2:
        # st.write(main_data[i])
        # print(main_data[i])
        name=i['name']
        info=i['info']
        img=i['image']
        price=i['price']
        currency=i['currency']
        url=i['url']
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