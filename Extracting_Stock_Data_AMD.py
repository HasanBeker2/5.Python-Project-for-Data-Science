import yfinance as yf
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt

amd = yf.Ticker("AMD")


# URL of the JSON file to download
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Save the content of the response to a file
    with open("amd.json", "wb") as file:
        file.write(response.content)
        
    print("File 'amd.json' has been downloaded successfully.")
else:
    print("Failed to download the file. Status code:", response.status_code)

with open('amd.json',"r") as json_file:
    amd_info = json.load(json_file)
    
print(amd_info)
print(amd_info["country"])
print(amd_info["sector"])

amd_share_price_data = amd.history(period="max")
print(amd_share_price_data.head())
print(amd_share_price_data.iloc[0])


amd_share_price_data.reset_index(inplace=True)

#amd_share_price_data.plot(x="Date", y="Open") this code is used only in jupyter notebook for showing charts

# Create a line plot
plt.plot(amd_share_price_data["Date"], amd_share_price_data["Open"])

# Customize the plot (if needed)
plt.title("amd Share Price")
plt.xlabel("Date")
plt.ylabel("Open Price")

# Show the plot (this will display the plot in a separate window)
plt.show()


print(amd.dividends)

