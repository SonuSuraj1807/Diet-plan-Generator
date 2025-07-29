# app.py

import streamlit as st
from generate_diet import generate_diet # Import your diet generation function

st.title('Diet Generator') # Sets the main title of your web app

# Input fields for user data
gender = st.selectbox('What is your Gender?', ['Male', 'Female'])
age = st.number_input('What is your Age?', min_value=1, max_value=120)
body_comp = st.selectbox("What is your Body Composition?", ["Lean", "Average",
                                                           "Overweight", "Obese"])
activity = st.selectbox("What is your Activity Level?", ["Sedentary", "Light",
                                                         "Moderate", "Active", "Athlete"])

generate_button = st.button('Generate') # This creates the clickable button

# Logic to run when the button is clicked
if generate_button:
    print('Generating Diet...') # This prints to your Terminal where you run Streamlit
    st.write('Generating Diet...') # This displays a message in the Streamlit web app

    # Call your generate_diet function from generate_diet.py with the collected user inputs
    diet = generate_diet(age=age, body_comp=body_comp, activity_level=activity,
                         gender=gender)

    # Display the actual diet recommendation content from the LLM in the web app
    st.write(diet.content) # .content extracts the text from the LLM's response object
