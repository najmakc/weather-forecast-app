import streamlit as st

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

