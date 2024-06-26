from django.shortcuts import render
from ML_Model.url_feature_extraction import featureExtraction
from joblib import load
from .forms import ReviewForm
from .models import Review
from django.shortcuts import redirect
import os

# Construct the full path to the model
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'ML_Model', 'xgboost_model.joblib')

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

def review_page(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user  # Assuming user is logged in
            new_review.save()
            return redirect('review_page')  # Redirect to the same page after submission
    else:
        form = ReviewForm()

   # Fetch reviews from database (assuming Review model exists)
    reviews = Review.objects.all()

    # Prepare star icons data
    for review in reviews:
        review.star_icons = range(review.stars)  # List of filled stars
        review.empty_star_icons = range(5 - review.stars)  # List of empty stars

    context = {
        'form': form,
        'reviews': reviews,
    }
    return render(request, 'review.html', context)