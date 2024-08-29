import requests

API_KEY = "d32bee40f60e054b623af5d652d6b6d2"
def get_data(place , forcast_days = None, type = None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[0:nr_values]
    if type == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if type == "sky":
        filtered_data = [ dict["weather"][0]["main"] for dict in filtered_data]

    return filtered_data


if __name__=="__main__":
    get_data("Dubai")


