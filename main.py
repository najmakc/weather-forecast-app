from fileinput import filename

import streamlit as st
import plotly.express as px
from backend import get_data


#Stramlit app heading
st.title("Weather Forecast for the Next days")

#input box for entering place
place = st.text_input("Place:")

#weather for the 5 days
days = st.slider("Forecast Days" ,min_value=1 ,max_value=5 , help="select the number of forecast days")

#choose which data you want to know
option = st.selectbox("Select the data to view",
                      options=("Temperature","sky"),index=None)

#Reading Temperature and sky data
if place and option:
    try :
        # subheading
        st.subheader(f"{option} for the next {days} in {place}")
        filtered_data = get_data(place,days)
        if option == "Temperature" :
            temperature = [dict["main"]["temp"] for dict in filtered_data]
            temperature = [temp-273.15 for temp in temperature]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x = dates , y = temperature ,labels= {"x":"Dates" , "y":"Temperature(c)"})
            st.plotly_chart(figure)
        if option == "sky":
            #dictionary of image path for each sky condition
            images = {"Clear":"images/clear.png" ,"Clouds":"images/cloud.png" ,"Rain":"images/rain.png" ,"Snow" :"images/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            #list of image filepath of each sky condition
            image_paths = [images[condition] for condition in sky_condition]
            st.image(image_paths , width=150)
    except KeyError:
        st.info("Invalid input ! Please enter valid input")




