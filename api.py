from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

api_key = '28ca67eb395740f46c2c9605df9d8339'

@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML page

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get the city name from the frontend input
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = f"{data['main']['temp']} °C"
        desc = data['weather'][0]['description']
        return jsonify({'temp': temp, 'desc': desc})  # Return the weather data as JSON
    else:
        return jsonify({'error': 'Error fetching weather data'}), 500  # Return error message if API call fails

if __name__ == '__main__':
    app.run(debug=True)
