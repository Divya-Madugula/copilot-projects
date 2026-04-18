from get_weather import get_weather

# Convert a temperature from Celsius to Fahrenheit.
# This is used to display both units to the user.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Print weather information in a human-friendly format.
# If the API request failed, this function outputs an error message.
def display_weather_info(weather_data):
    if not weather_data:
        print("Unable to retrieve weather data.")
        return

    # Extract common fields from the API response.
    location = weather_data["name"]
    main = weather_data["main"]
    weather = weather_data["weather"][0]

    print("The temperatures in Celsius:")
    print(f"The current temperature in {location} is {main['temp']}°C with {weather['description']}.")
    print(f"High: {main['temp_max']}°C, Low: {main['temp_min']}°C")

    print("The temperatures in Fahrenheit:")
    print(f"The current temperature in {location} is {celsius_to_fahrenheit(main['temp']):.2f}°F with {weather['description']}.")
    print(f"High: {celsius_to_fahrenheit(main['temp_max']):.2f}°F, Low: {celsius_to_fahrenheit(main['temp_min']):.2f}°F")

# Main script entry point.
# It asks the user for a location, fetches the weather, then displays the results.
def main():
    location = input("Enter location: ").strip()
    if not location:
        print("Please enter a valid location.")
        return

    weather_data = get_weather(location)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
