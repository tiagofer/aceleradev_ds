import streamlit as st
import pandas as pd 


def main():
    df = pd.read_csv('iris.csv')
    st.title("hello")
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('This is a text')
    variavel = st.text_input('Texto')
    st.text(variavel)
    st.sidebar.text("Sidebar na área")
    botton = st.button("Clica ai porra")
    if botton:
        st.text("clicou sim.")
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('checkado')
    radio = st.radio('Escolha as opções',('opt 1','opt 2'))
    if radio == 'opt 1':
        st.markdown('opção 01')
    else:
        st.markdown('opção 02')
    slider = st.sidebar.slider("Tamanho Visual",min_value=1,max_value=df.shape[0])
    st.dataframe(df.head(slider))
if __name__ == '__main__':
    main()