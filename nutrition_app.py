import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os
import google.generativeai as genai
from PIL import Image

load_dotenv(find_dotenv())

#page config

st.set_page_config(page_title="My AI Nutrition Monitor")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image):
    model=genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input,image[0]])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data,
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No image uploaded")
    

st.sidebar.title("Navigation")
st.sidebar.header("Upload Section")
uploaded_file = st.sidebar.file_uploader("choose an image", type=['jpg','jpeg','png'])

st.header("AI Nurtition Monitor")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption="uplaoded_image", use_container_width=True)

submit = st.button("Analyse this food")

input_prompt = """
You are an expert nutritionist analyzing the food items in the image.
Start by determining if the image contains food items. 
If the image does not contain any food items, 
clearly state "No food items detected in the image." 
and do not provide any calorie information. 
If food items are detected, 
start by naming the meal based on the image, 
identify and list every ingredient you can find in the image, 
and then estimate the total calories for each ingredient. 
Summarize the total calories based on the identified ingredients. 
Follow the format below:

If no food items are detected:
No food items detected in the image.

If food items are detected:
Meal Name: [Name of the meal]

1. Ingredient 1 - estimated calories
2. Ingredient 2 - estimated calories
----
Total estimated calories: X

Finally, mention whether the food is healthy or not, 
and provide the percentage split of protein, carbs, and fats in the food item. 
Also, mention the total fiber content in the food item and any other important details.

Note: Always identify ingredients and provide an estimated calorie count, 
even if some details are uncertain.
"""

if submit:
    with st.spinner("Processing....."):
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt,image_data)
    st.success("DONE!")
    st.subheader("Food Analysis")
    st.write(response)



