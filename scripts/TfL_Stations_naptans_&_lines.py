import requests
from time import sleep
import random
import json


def extractNaptans(urls):
    array = []
    naptan_ids = set()  # A set to track the naptan_ids that have been added

    for service_name, api_url in urls.items():
        try:
            # Make the API request
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from {api_url}: {e}")
            continue

        # Extract the NaPTAN IDs, hub NaPTAN codes, and common names
        for station in data.get("stopPoints", []):
            common_name = station.get("commonName", "N/A")
            naptan_id = station.get("stationNaptan", "N/A").strip()
            hub_naptan = station.get("hubNaptanCode", "N/A")

            # Only add to array if naptan_id is not already present
            if naptan_id != "N/A" and naptan_id not in naptan_ids:
                naptan_ids.add(naptan_id)  # Add the naptan_id to the set
                array.append({
                    "common_name": common_name,
                    "naptan_id": naptan_id,
                    "hub_naptan": hub_naptan
                })

    return array


def extractLines(stop_point, max_retries=5):
    stopPoint_API = f"https://api.tfl.gov.uk/StopPoint/{stop_point}"
    desired_lines = {
        "Bakerloo", "Central", "Circle", "District", "DLR", "Elizabeth line",
        "Hammersmith & City", "Jubilee", "London Overground", "Metropolitan",
        "Northern", "Piccadilly", "Tram", "Victoria", "Waterloo & City"
    }

    retry_count = 0
    while retry_count < max_retries:
        try:
            response = requests.get(stopPoint_API)
            if response.status_code == 429:  # Too Many Requests
                retry_after = int(response.headers.get('Retry-After', 1))
                # Sleep for the amount of time specified in Retry-After header plus a random jitter
                sleep(retry_after + random.uniform(0, 2))
                retry_count += 1
                continue
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            lines = [line.get("name") for line in data.get(
                "lines", []) if line.get("name") in desired_lines]
            return lines
        except requests.RequestException as e:
            retry_count += 1
            # Exponential backoff with jitter
            sleep(2 ** retry_count + random.uniform(0, 2))
    return []


# TfL Stop Points API endpoints
stopPointsDict = {
    "tube_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Tube",
    "overground_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Overground",
    "elizabethLine_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Elizabeth-Line",
    "tram_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Tram",
    "DLR_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/DLR",
}

# Fetch station details
stations = extractNaptans(stopPointsDict)

# Prepare list for DataFrame
data_for_json = []

# Print CSV header
print("Station Name, NaPTAN ID, Hub NaPTAN, Lines")

# Fetch and format lines for each station
for station in stations:
    naptan_id = station["naptan_id"]
    lines = extractLines(naptan_id)
    # Prepare the station information
    station_data = {
        "Station Name": station["common_name"],
        "NaPTAN ID": naptan_id,
        "Hub NaPTAN": station["hub_naptan"],
        "Lines": lines  # Store lines as a list
    }
    data_for_json.append(station_data)
    # Print the station information in CSV format
    lines_str = ", ".join(lines) if lines else "No lines data available"
    print(
        f"{station['common_name']}, {naptan_id}, {station['hub_naptan']}, [{lines_str}]")
    sleep(0.1)  # Sleep to prevent hitting rate limits

# Write the data to a JSON file
with open("Station_NaPTANs.json", "w") as json_file:
    json.dump(data_for_json, json_file, indent=4)

print("Data has been written to Station_NaPTANs.json")
