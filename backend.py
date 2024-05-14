import requests

key = "76ccde622bcdeddc80f698c98af82bb3"


def get_data(place="Delhi", forecast_days=2, kind="Temperature"):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    values = 8 * forecast_days
    filtered_data = filtered_data[:values]
    return filtered_data


if __name__ == "__main__":
    print(get_data())
