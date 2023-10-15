import pandas as pd

# Define the URL from which to read HTML data
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"

# Read HTML data from the URL and store it in a list of DataFrames
read_html_pandas_data = pd.read_html(url)

# Extract the first DataFrame from the list (assuming there's only one table)
netflix_dataframe = read_html_pandas_data[0]

# Print the first few rows of the DataFrame
print(netflix_dataframe.head())
