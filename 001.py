import streamlit as st

options = ('Email', 'Table phone', 'Mobile phone')

options = st.selectbox('Select your preferred contact method:', options)

st.write('You selected:', options)

agree = st.checkbox('I agree')

if agree:
    st.write('Great! You agreed.')

age = st.slider('Select your age:', 0, 100, 25)
st.write("I'm", age, 'years old')

text_content = 'this is some text'
st.download_button('download', text_content)

with st.form('order drink'):
    drink = ('Tea', 'Coffee', 'Water')
    option_drink = st.selectbox('What drink do you want?', drink)
    size = ('Small', 'Medium', 'Large')
    option_size = st.selectbox('What size do you want?', size)
    toppings = ('jelly', 'pearls', 'pudding')
    option_toppings = st.selectbox('What toppings do you want?', toppings)
    numbers = st.slider('How many drink do you want?', 1, 5, 1)
    submitted = st.form_submit_button('Submit')
    bill = {'Drink:': option_drink, 'Size:': option_size, 'Toppings:': option_toppings, 'How many:': numbers}
    if submitted:
        st.write('You ordered:', option_drink, option_size, option_toppings, numbers)
        for x, y in bill.items():
            st.write(x, y)