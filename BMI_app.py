import streamlit as st
# Make center column wider
col1, col2, col3 = st.columns([1, 6, 1])

with col2:
    st.title("BMI_Checker")
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)

if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("Showing the widget")
status = st.radio("Select Gender: ", ('Male', 'Female'))
if status=='Male':
    st.success('Male')
else:
    st.success('Female')
height=st.number_input('enter the height in meter',min_value=1, max_value=3) 
if(st.button('Submit',key='submit_button2')):
    result1 = height
    st.success(result1)   
weight=st.number_input('enter the weight in kg',min_value=1, max_value=100) 
if(st.button('Submit',key='submit_button3')):
    result2 = weight
    st.success(result2)  
BMI = weight / (height ** 2)
st.success(f'The BMI of {name} is {BMI:.2f}')  
    