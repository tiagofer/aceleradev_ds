import streamlit as st

def main():
    st.title("hello")
    st.header('This is a header')
    st.subheader('This is a subheader')
    st.text('This is a text')
    variavel = st.text_input('Texto')
    st.text(variavel)
    st.sidebar.text("Sidebar na área")

if __name__ == '__main__':
    main()