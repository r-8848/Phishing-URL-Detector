
# Phishing Website Detector

## Introduction

Url Scanner is a dynamic web application that analyzes URL obtained from the user and classifies them.. Built using Django, a high-level Python web framework, Url Scanner offers users a seamless and robust platform to stay updated with current affairs while understanding the sentiment behind each news piece.
safe in the today's era of increasing cyberattacks by proper classification.
## Features

- **User Input**:Allows user to input URL for phishing 
- **Detection**: Analyzes and categorizes URL as Legitimate and Phishing.
- **Feedback**: Allows users to give feedback based on their experience.
- **Responsive Design**: Ensures a seamless user experience across different devices.

## Live Demo


## Screenshots



### Home Page


### Phishing Url Detection Results


## Getting Started

Follow these steps to set up and run the NewsApp on your local machine.

1. Clone the github repository.

3. Go to Url Scanner and bash these commands
   ```bash
   pip install virtualenv
    ```
   ```bash
   python -m venv myenv
   ```
   ```bash
   cd myen
   ```
   ```bash
   cd Scripts
   ```
   ```bash
   .\activate
   ```
    ```bash
   cd ../..
    ```
     ```bash
   pip install -r requirements.txt
   ```
   ```bash
   python manage.py migrate
   ```
    ```bash
   python manage.py runserver
   ```


### Prerequisites

Ensure you have the following installed on your system:

- Python (version 3.6 or higher)
- pip (Python package installer)
- Git

### How It Works

1. **Url Feature Extraction**:From the url entered by user, total 16 different features categorized as Address Bar based Features, Domain based Features, HTML & Javascript based Features are extracted from url.   
2. **Detection**:Each url is analyzed based on feature extracted using one of the most popular machine learning algorithms  XGBoost( eXtreme Gradient Boosting) to determine whether is it is legitimate or phishing. 
3. **Classification**:Url are then categorized based on the value(Label) returned by the model:
   - **Label 0**:Url are classified as Legitimate.
   - **Label 1**: Url are classified as Phishing.
   

### Contributing
We welcome contributions to Url Scanner! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.




