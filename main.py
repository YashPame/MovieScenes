import streamlit as st
from Data import Data

if 'count' not in st.session_state:
    st.session_state.count = 0

st.title(Data[st.session_state.count]['Movie Name'])
st.image(Data[st.session_state.count]['image'], width=400)
st.subheader(Data[st.session_state.count]['Context'])

col1, col2 = st.columns(2)


with col1:
    if st.button("Previous"):
        if st.session_state.count > 0:
            st.session_state.count -= 1
        else:
            st.session_state.count = len(Data) - 1

with col2:
    if st.button("Next"):
        if st.session_state.count < len(Data) - 1:
            st.session_state.count += 1
        else:
            st.session_state.count = 0
