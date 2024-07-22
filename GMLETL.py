import requests
import pandas as pd

# Step 1: Download the file
url = "https://gml.noaa.gov/webdata/ccgg/trends/ch4/ch4_mm_gl.txt"
response = requests.get(url)
data = response.text

# Step 2: Parse the file
lines = data.split('\n')

# Step 3: Extract the data starting from the line with the headers
start_line = 0
for i, line in enumerate(lines):
    if line.startswith("# year   month       decimal       average   average_unc         trend     trend_unc"):
        start_line = i
        break

# Extract the headers and data lines
headers = lines[start_line].strip("# ").split()
data_lines = lines[start_line + 1:]

# Parse the data into a list of dictionaries
parsed_data = []
for line in data_lines:
    if line.strip() == "":
        continue
    values = line.split()
    entry = {headers[j]: values[j] for j in range(len(headers))}
    parsed_data.append(entry)

# Step 4: Save to CSV using pandas
df = pd.DataFrame(parsed_data)
df.to_csv('methane_data.csv', index=False)

print("Data has been saved to methane_data.csv")
