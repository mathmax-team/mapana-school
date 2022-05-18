import streamlit as st

st.title('Test App')

def afunc(x):
var1=[]
var1=[]
# raise(ValueError, "parar2")
# print(var1[0])
try:
    print(var1[0])
except Exception:
    pass
return x**2

starter=st.sidebar.radio('Selection',['Bulbasaur','Charmander','Squirtle'])
st.text(f'{starter} is a good choice!')

st.write(afunc(4))
st.write(afunc(5))
st.write(afunc(5))
st.write(afunc(4))
