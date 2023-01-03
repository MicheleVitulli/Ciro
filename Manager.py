import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
	cred = credentials.Certificate('ciro-key.json')
	firebase_admin.initialize_app(cred)
db = firestore.client()


st.set_page_config(page_title='Ciro', layout = 'wide', page_icon = '🍝', initial_sidebar_state = 'auto')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown('# 🍝 Ciro')

numero_tavolo = st.number_input('Numero del tavolo', min_value=0, step=1)
operatore = st.text_input('Nome Operatore')
capienza = st.number_input('Capienza tavolo', min_value=1, step=1)
button = st.button('Aggiungi operatore')


doc_ref = db.collection('tavoli').document(str(numero_tavolo))
if button:
    doc_ref.set({
        'operatore': (operatore.lower()).capitalize(),
        'capienza': capienza
        })
    doc = doc_ref.get()
    st.success(f'L\' operatore del tavolo {doc.id} è {doc.to_dict()["operatore"]}')