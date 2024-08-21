import requests

# TfL Tube Stations API endpoint
stopPoints_API = "https://api.tfl.gov.uk/StopPoint/Mode/Tube"

# Make the API request
response = requests.get(stopPoints_API)
data = response.json()

array = []
naptan_ids = set()  # A set to track the naptan_ids that have been added

# Extract the NaPTAN IDs, hub NaPTAN codes, and common names
for station in data["stopPoints"]:
    common_name = station["commonName"]

    if "stationNaptan" in station:
        naptan_id = station["stationNaptan"]
    else:
        naptan_id = "N/A"
    
    if "hubNaptanCode" in station:
        hub_naptan = station["hubNaptanCode"]
    else:
        hub_naptan = "N/A"

    # Only add to array if naptan_id is not already present
    if naptan_id != "N/A" and naptan_id not in naptan_ids:
        naptan_ids.add(naptan_id)  # Add the naptan_id to the set
        array.append(f"{common_name}, {naptan_id}, {hub_naptan}")

# Print the unique station details
for x in array: print(x)
