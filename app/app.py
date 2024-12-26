from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and scaler
model = pickle.load(open("model.pkl", "rb"))  # Load the trained model
scaler = pickle.load(open("scaler.pkl", "rb"))  # Load the scaler used during training

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    try:
        # Get the uploaded file
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            # Read the CSV file
            df = pd.read_csv(file)
            
            # Check if the CSV contains the correct number of features
            if df.shape[1] == 20:  # Updated feature count
                # Convert the DataFrame to a NumPy array for prediction
                features = df.values.reshape(1, -1)
                
                # Apply the scaler (preprocessing) to the features
                scaled_features = scaler.transform(features)
                
                # Get the prediction from the model
                prediction = model.predict(scaled_features)
                
                # Interpret the prediction
                classification_text = "Malignant" if prediction[0] == 1 else "Benign"
                
                # Dynamic health tips based on the prediction and feature values
                tips = []
                if prediction[0] == 1:  # Malignant
                    if df['radius_mean'].iloc[0] > 15:
                        tips.append("Consider adding cruciferous vegetables like broccoli and cauliflower to your meals.")
                    if df['smoothness_mean'].iloc[0] > 0.1:
                        tips.append("Stay hydrated and focus on balanced meals with whole grains and lean proteins.")
                    tips.append("Schedule a follow-up consultation with your healthcare provider for further evaluation.")
                else:  # Benign
                    if df['texture_mean'].iloc[0] > 18:
                        tips.append("Continue with regular health check-ups to monitor overall wellness.")
                    if df['smoothness_mean'].iloc[0] > 0.1:
                        tips.append("Incorporate antioxidant-rich foods like berries, spinach, and green tea into your diet.")
                    tips.append("Maintain a healthy lifestyle with regular self-care and wellness routines.")
                tips.append("Include omega-3-rich foods like salmon, walnuts, and flaxseeds in your meals.")
                tips.append("Engage in regular physical activity to promote overall health and reduce inflammation.")

                # Render the results with health tips
                return render_template('index.html', 
                                       classification_text=f"Prediction: {classification_text}",
                                       health_tips=tips)
            else:
                return render_template('index.html', classification_text="Error: The CSV file must have 22 features.")
        else:
            return render_template('index.html', classification_text="Error: Invalid file format. Please upload a CSV file.")
    except Exception as e:
        return render_template('index.html', classification_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
