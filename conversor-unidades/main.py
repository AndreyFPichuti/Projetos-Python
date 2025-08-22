import streamlit as st
from calculos import *

st.title('Conversor de unidades')

aba1, aba2, aba3 = st.tabs(['Comprimento', 'Peso', 'Temperatura'])

with aba1:
    st.subheader('Conversor de Comprimento')
    comprimento = st.number_input('Digite o comprimento para converter')
    da_unidade = st.radio('De qual unidade?', options=
    ['mm', 'cm', 'm', 'km', 'inches', 'ft', 'yard', 'miles'])

    para_unidade = st.radio('Para qual unidade?', options=
    ['mm', 'cm', 'm', 'km', 'inches', 'ft', 'yard', 'miles'])

    if st.button('Converter comprimento'): 
        st.write('Resultado')
        st.markdown(calcular_comprimento(comprimento, da_unidade, para_unidade))
        st.button('Reiniciar')
    
with aba2:
    st.subheader('Conversor de Peso')
    peso = st.number_input('Digite o peso para converter')
    da_unidade = st.radio('De qual unidade?', options=
    ['mg', 'g', 'kg', 'ounce', 'pound'])

    para_unidade = st.radio('Para qual unidade?', options=
    ['mg', 'g', 'kg', 'ounce', 'pound'])

    if st.button('Converter peso'): 
        st.write('Resultado')
        st.markdown(calcular_peso(peso, da_unidade, para_unidade))
        st.button('Reiniciar')

with aba3:
    st.subheader('Conversor de Temperatura')
    temperatura = st.number_input('Digite a temperatura para converter')
    da_unidade = st.radio('De qual unidade?', options=
    ['Celsius', 'Fahrenheit', 'Kelvin'])

    para_unidade = st.radio('Para qual unidade?', options=
    ['Celsius', 'Fahrenheit', 'Kelvin'])

    if st.button('Converter temperatura'): 
        st.write('Resultado')
        st.markdown(calcular_temperatura(temperatura, da_unidade, para_unidade))
        st.button('Reiniciar')
