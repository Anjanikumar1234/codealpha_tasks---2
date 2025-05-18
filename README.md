IP Geolocation Tracker
📌 Description
This Python-based tool fetches and displays detailed geolocation information of any given IP address — or your own IP if none is provided. It shows location details such as city, region, country, timezone, and ISP. It also fetches real-time weather data for that location using the OpenWeatherMap API. Finally, it generates an interactive map with all the information shown via popup markers.

🛠 Installation
To run this project, ensure you have Python installed. You can download it from:
🔗 Python Official Website

Install the required dependencies using pip:

bash
Copy
Edit
pip install requests folium
🚀 How to Run
Run the script using the command:

bash
Copy
Edit
python geolocation_tracker.py
You will be prompted to enter an IP address or press Enter to automatically detect your current IP.

📊 Example Run

yaml
Copy
Edit
🌐 IP Geolocation Tracker

🔎 Enter IP address (or press Enter if you don't know your IP): 8.8.8.8

📍 Fetching location...
✅ Location found:
Ip: 8.8.8.8
City: Mountain View
Region: California
Country: United States
Timezone: America/Los_Angeles
Isp: Google LLC

☁️ Getting current weather...
🌦️ Weather Info:
Description: Clear sky
Temperature: 20.5
Humidity: 60
Wind speed: 3.6

🗺️ Generating interactive map...
The interactive map will open automatically in your default web browser showing location and weather info.

⚙ Configuration
You must obtain a free API key from OpenWeatherMap and replace the placeholder in the script:

python
Copy
Edit
OPENWEATHER_API_KEY = "your_valid_api_key_here"  # Replace with your key
⏳ Key Features
✅ Detects geolocation by IP or auto-detects your own IP
✅ Shows detailed location info: city, region, country, timezone, ISP
✅ Fetches current weather info: temperature, humidity, wind speed
✅ Generates interactive map with markers and info popups
✅ Opens map automatically in default web browser

🤝 Contributing
Want to improve this project? Feel free to:
🔹 Fork the repository
🔹 Create a new branch
🔹 Submit a pull request

Your contributions are always welcome! 😊
