import requests

def get_weather():
    print("=== BASIC WEATHER APP ===")
    city = input("Enter city name: ").strip()
    
    if not city:
        print("Error: City name cannot be empty.")
        return
    
    # Using wttr.in JSON API for seamless execution without requiring an API key
    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        print(f"Fetching weather for {city}...")
        response = requests.get(url, timeout=10)
        
        if response.status_code != 200:
            print("Error: Could not retrieve weather data. Please check the city name.")
            return
        
        data = response.json()
        current = data['current_condition'][0]
        
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        humidity = current['humidity']
        desc = current['weatherDesc'][0]['value']
        wind_speed = current['windspeedKmph']
        
        print(f"\n--- Weather in {city.capitalize()} ---")
        print(f"Condition: {desc}")
        print(f"Temperature: {temp_c}°C ({temp_f}°F)")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
        
    except requests.exceptions.RequestException:
        print("Error: Network connection failed or request timed out.")
    except (KeyError, IndexError):
        print("Error: Unexpected data format received from weather service.")

if __name__ == "__main__":
    get_weather()