from get_weather import get_weather

#Add a function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32 

def display_weather_info(weather_data):
    if not weather_data:
        print("Unable to retrieve weather data.")
        return

    location = weather_data["name"]
    main = weather_data["main"]
    weather = weather_data["weather"][0]

    print("The temperatures in Celsius:")
    print(f"The current temperature in {location} is {main['temp']}°C with {weather['description']}.")
    print(f"High: {main['temp_max']}°C, Low: {main['temp_min']}°C")

    print("The temperatures in Fahrenheit:")
    print(f"The current temperature in {location} is {celsius_to_fahrenheit(main['temp']):.2f}°F with {weather['description']}.")
    print(f"High: {celsius_to_fahrenheit(main['temp_max']):.2f}°F, Low: {celsius_to_fahrenheit(main['temp_min']):.2f}°F")

def main():
    location = input("Enter location: ").strip()
    if not location:
        print("Please enter a valid location.")
        return

    weather_data = get_weather(location)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
