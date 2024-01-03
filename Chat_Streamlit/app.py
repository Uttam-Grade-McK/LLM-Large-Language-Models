import streamlit as st
import google.generativeai as palm
from PIL import Image

st.set_page_config(
    page_title="PaLM Text Generation (LLM) API",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'About': "# This app shows you how to use PaLM Text Generator API"
    }
)

API_KEY = 'AIzaSyAptIc5Jn4Qoeh72oxByun0bZhyOB0BBCA' #API from GCP (Create new project in GCP account. > API & Services > Library > Search Generative Palm API and enable API > API & Services > Credencials > create credentials > API Key > API Key will create and paste here.)
palm.configure(api_key = API_KEY)

#Text Generation
model_id = 'models/text-bison-001'
prompt = """
    what is Deep Learning?
"""

def create_session_state():
    if 'temperature' not in st.session_state:
        st.session_state['temperature'] = 0.0
    if 'token_limit' not in st.session_state:
        st.session_state['token_limit'] = 256
    if 'top_k' not in st.session_state:
        st.session_state['top_k'] = 40
    if 'top_p' not in st.session_state:
        st.session_state['top_p'] = 0.8
    if 'debug_mode' not in st.session_state:
        st.session_state['debug_mode'] = False
    if 'prompt' not in st.session_state:
        st.session_state['prompt'] = []
    if 'response' not in st.session_state:
        st.session_state['response'] = []

#creating session states
create_session_state()

def reset_session() -> None:
    st.session_state['temperature'] = 0.0
    st.session_state['token_limit'] = 256
    st.session_state['top_k'] = 40
    st.session_state['top_p'] = 0.8
    st.session_state['debug_mode'] = False
    st.session_state['prompt'] = []
    st.session_state['response'] = []


image = Image.open('./image/palm_image.jpg')
st.image(image)
st.title(":red[PaLM ] :blue[LLM] Text Generation")

with st.sidebar:
    image = Image.open('./image/setting.jpg')
    st.image(image)
    st.markdown("<h2 style='text-align: center; color: red;'>Setting Tab</h2>", unsafe_allow_html=True)


    st.write("Model Settings:")

    #define the temeperature for the model
    temperature_value = st.slider('Temperature :', 0.0, 1.0, 0.2)
    st.session_state['temperature'] = temperature_value

    #define the temeperature for the model
    token_limit_value = st.slider('Token limit :', 1, 1024, 256)
    st.session_state['token_limit'] = token_limit_value

    #define the temeperature for the model
    top_k_value = st.slider('Top-K  :', 1,40,40)
    st.session_state['top_k'] = top_k_value

    #define the temeperature for the model
    top_p_value = st.slider('Top-P :', 0.0, 1.0, 0.8)
    st.session_state['top_p'] = top_p_value

    if st.button("Reset Session"):
        reset_session()


with st.container():
    st.write("Current Generator Settings: ")
    # if st.session_state['temperature'] or st.session_state['debug_mode'] or :
    st.write ("Temperature: ",st.session_state['temperature']," \t \t Token limit: ",st.session_state['token_limit']
                ," \t \t Top-K: ",st.session_state['top_k']
                ," \t \t Top-P: ",st.session_state['top_p']
                ," \t \t Debug Model: ",st.session_state['debug_mode'])


    prompt = st.text_area("Add your prompt: ",height = 100)
    if prompt:
        st.session_state['prompt'].append(prompt)
        st.markdown("<h3 style='text-align: center; color: blue;'>Generator Model Response</h3>", unsafe_allow_html=True)
        with st.spinner('PaLM is working to generate, wait.....'):
            response = palm.generate_text(model = model_id, prompt=prompt, temperature = st.session_state['temperature'],
                                max_output_tokens = st.session_state['token_limit'],
                                top_p = st.session_state['top_p'],
                                top_k = st.session_state['top_k'])
            
            st.markdown(response.candidates[0]['output'])
    