import requests


def extractNaptans(urls):
    array = []
    naptan_ids = set()  # A set to track the naptan_ids that have been added

    for service_name, api_url in urls.items():
        # Make the API request
        response = requests.get(api_url)
        data = response.json()

        # Extract the NaPTAN IDs, hub NaPTAN codes, and common names
        for station in data["stopPoints"]:
            common_name = station["commonName"]

            if "stationNaptan" in station:
                naptan_id = station["stationNaptan"].strip()
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

    return array


# TfL Stop Points API endpoints
stopPointsDict = {
    "tube_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Tube",
    "overground_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Overground",
    "elizabethLine_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Elizabeth-Line",
    "tram_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/Tram",
    "DLR_stopPoints": "https://api.tfl.gov.uk/StopPoint/Mode/DLR",
}

# Print the unique station details
for x in extractNaptans(stopPointsDict):
    print(x)
