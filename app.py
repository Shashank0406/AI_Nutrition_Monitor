import streamlit as st
from dotenv import load_dotenv, find_dotenv
import os
import google.generativeai as genai
from PIL import Image
import datetime
import sqlite3
import json
import re

load_dotenv(find_dotenv())
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



def extract_ingredients(analysis_text):
    ingredients = []
    lines = analysis_text.split('\n')
    for line in lines:
        if re.match(r'^\d+\.\s+', line):  # Match numbered list items
            ingredient = line.split('-')[0].strip()
            ingredient = re.sub(r'^\d+\.\s+', '', ingredient)  # Remove numbering
            ingredients.append(ingredient)
    return ingredients

def get_refined_analysis(ingredients_with_quantities):
    prompt = f"""
    As a nutritionist, provide a detailed analysis of this meal with the following ingredients and quantities:
    {ingredients_with_quantities}
    if no ingredientrs quantities are provided take approx values
    
    Please provide:
    1. Total calories
    2. Macronutrient breakdown (protein, carbs, fats in %)
    3. Fiber content
    4. Detailed breakdown of calories per ingredient
    5. Any health considerations or recommendations
    
    Format the response clearly with sections and numbers.
    """
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.set_page_config(page_title="My AI Nutrition Monitor")
#init_db()

st.header("AI Nutrition Monitor")

uploaded_file = st.file_uploader("Choose an image", type=['jpg','jpeg','png'])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    initial_prompt = """
    List all visible ingredients in this food image.
    Format as a numbered list without quantities or calories.
    """
    
    analyze_button = st.button("Identify Ingredients")
    
    if analyze_button:
        with st.spinner("Identifying ingredients..."):
            image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]
            model = genai.GenerativeModel("gemini-1.5-flash")
            initial_response = model.generate_content([initial_prompt, image_data[0]])
            
            ingredients = extract_ingredients(initial_response.text)
            
            st.subheader("Enter Quantities")
            
            # Create input fields for quantities
    
quantities = {}
for ingredient in ingredients:
                quantities[ingredient] = st.text_input(f"Enter quantity for {ingredient} (e.g., 100g, 2 cups)",
                    key=ingredient
                )          
if st.button("Calculate Nutrition"):
    # Format ingredients with quantities
    ingredients_with_quantities = "\n".join([f"{ingredient}: {qty}" for ingredient, qty in quantities.items() if qty])
    with st.spinner("Calculating detailed nutrition..."):
        refined_analysis = get_refined_analysis(ingredients_with_quantities)
        #save_analysis(quantities, refined_analysis, image)
        st.success("Analysis complete!")
        st.subheader("Detailed Nutrition Analysis")
        st.write(refined_analysis)
                    