import easyocr
import streamlit as st

upload = st.file_uploader("Choose a file",type=["png","jpg","jpeg"])
if upload is not None:
    byte = upload.getvalue()
    reader = easyocr.Reader(['fa','en'],gpu=False)
    result = reader.readtext(byte,detail=0,paragraph=True,decoder='beamsearch')
    for i in result:
        st.info(i)

