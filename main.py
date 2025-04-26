import streamlit as st
# Make center column wider
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.title("Banasthali Vidyapith")
from PIL import Image
img = Image.open(r"C:\Users\LNMIIT\Downloads\Banasthali_Vidyapeeth_Logo.png")
# st.image(img,width=200)
# Create three columns
col1, col2, col3 = st.columns([1, 2, 1])

# Put the image in the center column
with col2:
    st.image(img, width=200)

# if st.checkbox("Show/Hide"):

#     # display the text if the checkbox returns True value
#     st.text("Showing the widget")
status = st.radio("Select Gender: ", ('Male', 'Female'))
if status=='Male':
    st.success('Male')
else:
    st.success('Female')
    
# first argument takes the title of the selection box
# second argument takes options
hobby = st.multiselect("Hobbies: ",
                      ['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)


name = st.text_input("Enter Your name", "Type Here ...")

# # display the name when the submit button is clicked
# # .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
# # first argument takes the title of the slider
# # second argument takes the starting of the slider
# # last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value 
# of a variable at a specific position
st.text('Selected: {}'.format(level))

# age = st.number_input("Enter your age", min_value=0, max_value=100)

# gender = st.radio("Select Gender", ["Male", "Female"])
# hobbies = st.multiselect("Select Hobbies", ["Coding", "Reading", "Gaming"])

# upload = st.file_uploader("Upload CSV", type="csv")
# clicked = st.button("Click Me")
# with st.form("my_form"):
#     name = st.text_input("Name")
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("Form submitted with", name)

