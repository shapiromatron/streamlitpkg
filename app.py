import streamlit as st

from streamlitpkg.work import super_add

a = st.slider("Value of A?", 0, 130, 25)
b = st.slider("Value of B?", 0, 130, 25)
st.write(f"Super Add: {a} + {b} = {super_add(a, b)}")
