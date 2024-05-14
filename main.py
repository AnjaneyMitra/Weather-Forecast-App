import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast For the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days" , min_value=1 , max_value=5 , help="Select the number of days to view the forecast")
option = st.selectbox("Select the data to view" ,
                      ("Temperature" , "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures= [dict["main"]["temp"] for dict in filtered_data]
            fixed_temp = []
            for temp in temperatures:
                temp = temp/10
                fixed_temp.append(temp)
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=fixed_temp, labels={"x": "Date" , "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_icons = [images[condition] for condition in sky_conditions]
            st.image(image_icons , width=115)

    except KeyError:
        st.write("This place does not exist")
