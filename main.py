import streamlit as st
import requests

def get_weather(city, units='metric', api_key='e170cf5a92b4797f093bb94ca1fbbdf3'):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units={units}"
    r = requests.get(url)
    content = r.json()
    return content

st.title("Weather Forecast App")

# Input for city name
city_name = st.text_input("Enter city name:", "Washington")

if st.button("Get Weather Forecast"):
    st.write(f"Weather forecast for {city_name}:")

    try:
        weather_data = get_weather(city=city_name)
        with open('data.txt', 'a') as file:
            for dicty in weather_data['list']:
                file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")

        # Display weather data
        for forecast in weather_data['list']:
            st.write(f"Date and Time: {forecast['dt_txt']}")
            st.write(f"Temperature: {forecast['main']['temp']} °C")
            st.write(f"Description: {forecast['weather'][0]['description']}")
            st.write("---")

    except Exception as e:
        st.error("An error occurred. Please check the city name or try again later.")