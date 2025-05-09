# SkySight 🌤️🌦️🌍 - Real-time Weather Insights at Your Fingertips 🌡️☁️


**SkySight** is your ultimate weather dashboard, delivering accurate, real-time weather updates for any city worldwide. Built with simplicity and functionality in mind, SkySight provides user-friendly access to weather details using the reliable [WeatherAPI](https://www.weatherapi.com/).

---

## Features:
- **Real-Time Weather Updates**: Instantly access temperature, humidity, and atmospheric conditions for any location.
- **Search by City**: Input a city name to get the latest weather insights.
- **Intuitive Design**: An easy-to-navigate interface that prioritizes usability.
- **Powered by WeatherAPI**: Trusted, accurate weather data for a seamless user experience.

---

## Tech Stack:
- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Python, Flask
- **API**: [WeatherAPI](https://www.weatherapi.com/)
- **Deployment**: Local (future plans for cloud deployment)

---

## Project Structure:

```
SkySight/
│
├── app.py              # Main Flask application
├── config.py           # API key configuration
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
│   └── index.html      # Main UI template
└── static/             # Static assets (CSS, images, etc.)
    └── style.css       # Custom styles
```
## Image
![SkySight ](https://github.com/Kirankumarvel/SkySight/blob/main/static/SkySight.png)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Kirankumarvel/SkySight.git
   cd SkySight
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your API Key**:
   - Sign up at [WeatherAPI](https://www.weatherapi.com/) and get your API key.
   - Create a file named `config.py` in the root directory and add the following:
     ```python
     WEATHER_API_KEY = "your_weather_api_key"
     ```

6. **Run the application**:
   ```bash
   python app.py
   ```

   - Open your browser and navigate to `http://127.0.0.1:5000` to explore SkySight.

---


---

## Contributing

Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests to enhance SkySight.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

Created by **Kiran Kumar**  
- **GitHub**: [github.com/Kirankumarvel](https://github.com/Kirankumarvel)  
- **LinkedIn**: [linkedin.com/in/kirankumarvel](https://www.linkedin.com/in/kirankumarvel/)
```
