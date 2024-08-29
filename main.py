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

#subheading
st.subheader(f"{option} for the next {days} in {place}")
# def get_data(days):
#     dates = ["2022-25-10" ,"2022-26-10","2022-27-10"]
#     temperature = [10,11,15]
#     temperature = [i * days for i in temperature]
#     return dates ,temperature


data = get_data(place , days , option)


#Create the graph

figure = px.line(x = d,y = t, labels={"x":"Date" ,"y":"Temperature(c)"})

# showing the graph

st.plotly_chart(figure)

