import yfinance as yf
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt

apple = yf.Ticker("AAPL")


# URL of the JSON file to download
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content of the response to a file
    with open("apple.json", "wb") as file:
        file.write(response.content)
        
    print("File 'apple.json' has been downloaded successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)

with open('apple.json',"r") as json_file:
    apple_info = json.load(json_file)
    
print(apple_info)
print(apple_info["country"])

apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())

apple_share_price_data.reset_index(inplace=True)

#apple_share_price_data.plot(x="Date", y="Open") this code is used only in jupyter notebook for showing charts

# Create a line plot
plt.plot(apple_share_price_data["Date"], apple_share_price_data["Open"])

# Customize the plot (if needed)
plt.title("Apple Share Price")
plt.xlabel("Date")
plt.ylabel("Open Price")

# Show the plot (this will display the plot in a separate window)
plt.show()


print(apple.dividends)

