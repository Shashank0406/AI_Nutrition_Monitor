# AI Nutrition Monitor 🍴🤖

AI Nutrition Monitor is a Streamlit-based application designed to analyze food items in images using generative AI. It identifies the meal, lists ingredients, estimates calorie counts, and provides a nutritional breakdown.

---

## Features
- **Upload Food Images**: Users can upload images of food items for analysis.
- **AI-Powered Analysis**: Utilizes Google's generative AI (Gemini model) to identify food ingredients and estimate calorie content.
- **Nutritional Insights**: Provides a detailed report, including:
  - Meal name
  - Ingredient list with calorie estimates
  - Total calorie count
  - Protein, carbs, and fats percentage
  - Fiber content and health recommendations
- **Streamlit Interface**: User-friendly interface for seamless interaction.

---

## Installation

### Prerequisites
1. Python 3.9 or higher
2. Required libraries (install using the steps below)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/shashank04/ai-nutrition-monitor.git
   cd ai-nutrition-monitor
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment:
   - Create a `.env` file in the project root.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

---

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run nutrition_app.py
   ```

2. Open the app in your browser (default URL: `http://localhost:8501`).

3. Upload an image of food in the sidebar and click **"Analyse this food"**.

4. View the detailed nutritional analysis displayed on the page.

---

## Code Structure

```plaintext
ai-nutrition-monitor/
│
├── nutrition_app.py     # Main Streamlit application
├── requirements.txt     # Required Python libraries
├── .env                 # environment file
└── README.md            # Project documentation (this file)
```

### Key Functions
- **`get_gemini_response(input, image)`**:
  - Sends input prompt and image data to the Gemini model for content generation.
- **`input_image_setup(uploaded_file)`**:
  - Prepares the uploaded image file for API processing.

---

## Example Output

### Input:
A food image (e.g., a bowl of Chicken Tikka Masala with Rice and Naan).

### Output:
```
Food Analysis
Meal Name: Chicken Tikka Masala with Rice and Naan

Chicken Tikka Masala (approx. 300g) - 500 calories (estimated based on typical recipe and serving size. Calorie count varies based on ingredients used and portion size)
Basmati Rice (approx. 150g) - 225 calories (estimated based on cooked basmati rice)
Naan bread (approx. 100g) - 200 calories (estimated based on a typical serving of naan bread)
Total estimated calories: 925

The healthiness of this meal depends on the specific recipe and ingredients used. A homemade version with less oil and added vegetables would be healthier than a restaurant version. This example meal is moderately healthy as it includes protein from chicken, carbohydrates from rice and naan, and some potential micronutrients depending on the spices used. However, it is relatively high in calories and fat, depending on the preparation method.

Nutritional Percentage Split (Approximate, varies significantly by preparation):

Protein: 25% (Primarily from chicken)
Carbohydrates: 60% (Primarily from rice and naan)
Fats: 15% (From chicken and cooking oil)
Fiber Content: Moderate (the exact amount depends on the amount of rice and naan, as well as the spices used in the curry).

Important Details:

Sodium content can be high due to the spices and potential added salt.
The calorie count is an estimate and can vary greatly depending on portion sizes and cooking methods. A restaurant serving is likely to have significantly more calories.
To improve the healthiness of this meal, consider adding more vegetables to the curry and choosing whole-wheat naan. Reducing the amount of oil used in the cooking will also reduce the fat and calorie content.
```

---

## Requirements
The following Python libraries are used in the project:
- **Streamlit**: For the web application interface
- **Pillow**: For image processing
- **python-dotenv**: For managing environment variables
- **google-generativeai**: To integrate with Google's Gemini AI

---

## Contributing

Feel free to submit issues and pull requests to improve the project. For major changes, please discuss with the maintainers via issue threads.

---

## Acknowledgments
- Google Generative AI for the powerful Gemini model
- Streamlit for the intuitive web app framework
