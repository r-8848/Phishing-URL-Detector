from django.shortcuts import render
from ML_Model.url_feature_extraction import featureExtraction
from joblib import load
import os

# Construct the full path to the model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'ML_Model', 'xgboost_model_joblib.joblib')

# Load the saved model
xgb_model = load(model_path)

def index(request):
    return render(request, 'index.html')

def detect_phishing(request):
    if request.method == 'POST':
        url = request.POST.get('url', '')

        # Preprocess the URL using the feature extraction function
        features = featureExtraction(url)

        # Make predictions using the loaded model
        prediction = xgb_model.predict([features])

        # Determine if the URL is phishing or not
        is_phishing = bool(prediction[0])

        return render(request, 'result.html', {'url': url, 'is_phishing': is_phishing})
    else:
        return render(request, 'index.html')
