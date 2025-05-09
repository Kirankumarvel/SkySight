from flask import Flask, render_template, request, flash
import requests
from config import WEATHER_API_KEY
import os
app = Flask(__name__)


app.secret_key = os.getenv('SECRET_KEY', 'default_secret_key')  # Use environment variable or fallback

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if not city:
            flash('City name is required!', 'error')
        else:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
                
                # Print for debugging
                print(f"Request URL: {url}")
                print(f"Response Status Code: {response.status_code}")
                
                weather_data = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                weather_data = {'error': 'City not found or API issue!'}
            except ValueError:
                print("Invalid JSON response")
                weather_data = {'error': 'Invalid response from weather API!'}

    return render_template('index.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
