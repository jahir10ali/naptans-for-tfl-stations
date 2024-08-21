import requests


def extractLines(stop_point):
    # Define the API endpoint for the specific station
    stopPoint_API = f"https://api.tfl.gov.uk/StopPoint/{stop_point}"

    # Define the exact names of the services you're interested in
    desired_lines = {
        "Bakerloo", "Central", "Circle", "District", "DLR", "Elizabeth line",
        "Hammersmith & City", "Jubilee", "London Overground", "Metropolitan",
        "Northern", "Piccadilly", "Tram", "Victoria", "Waterloo & City"
    }

    # Make the API request to get the data for the specific station
    response = requests.get(stopPoint_API)
    data = response.json()

    # Initialize the list for services
    lines = []

    # Check for services that match the desired list
    for line in data.get("lines", []):
        line_name = line.get("name")
        if line_name in desired_lines:
            lines.append(line_name)

    return lines




