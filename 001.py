import streamlit as st

st.title("🥤 Drink Order App")
st.write("Welcome! Please fill out your preferences below.")

# Contact Information Section
st.header("Contact Information")
contact_options = ('Email', 'Table phone', 'Mobile phone')
selected_contact = st.selectbox('Select your preferred contact method:', contact_options)
st.write(f'**Contact method:** {selected_contact}')

agree = st.checkbox('I agree to the terms and conditions')
if agree:
    st.success('Thank you for agreeing!')

age = st.slider('Select your age:', 0, 100, 25)
st.write(f"**Age:** {age}")

text_content = 'This is some text for download.'
st.download_button('⬇️ Download Info', text_content)

st.markdown("---")

# Drink Order Section
st.header("Order Your Drink")
with st.form('order_drink'):
    col1, col2 = st.columns(2)
    with col1:
        drinks = ('Tea', 'Coffee', 'Water')
        selected_drink = st.selectbox('What drink do you want?', drinks)
        sizes = ('Small', 'Medium', 'Large')
        selected_size = st.selectbox('What size do you want?', sizes)
    with col2:
        toppings = ('Jelly', 'Pearls', 'Pudding')
        selected_topping = st.selectbox('What toppings do you want?', toppings)
        quantity = st.slider('How many drinks do you want?', 1, 5, 1)
    submitted = st.form_submit_button('Submit Order')

    if submitted:
        st.success('✅ Order submitted!')
        order_summary = {
            'Drink': selected_drink,
            'Size': selected_size,
            'Topping': selected_topping,
            'Quantity': quantity
        }
        st.write("### Your Order Summary")
        st.table(order_summary)
