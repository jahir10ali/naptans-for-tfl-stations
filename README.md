# NaPTAN ID's and Lines Operating for all TfL Stations (no Bus Stations)

## Table of Contents

- [What is a NaPTAN ID?](#what-is-a-naptan-id)
- [Usage of NaPTAN IDs](#usage-of-naptan-ids)
- [NaPTAN IDs for TfL](#naptan-ids-for-tfl)
- [Applications for TfL Services](#applications-for-tfl-services)
- [Example Usage of the TfL API](#example-usage-of-the-tfl-api)
  - [Fetch Station Arrivals](#fetch-station-arrivals)
  - [Plan Journeys Between Two Stations](#plan-journeys-between-two-stations)
- [Data Files](#data-files)
- [Python Scripts for NaPTAN Data Fetching](#python-scripts-for-naptan-data-fetching)
  - [Purpose of the Python Scripts](#purpose-of-the-python-scripts)
  - [Usage](#usage)
  - [Optional Use](#optional-use)
  - [How to Execute the Scripts](#how-to-execute-the-scripts)
- [Contributing](#contributing)
- [License](#license)


This repository contains comprehensive data and resources related to NaPTAN (National Public Transport Access Node) IDs for Transport for London (TfL) stations. It provides information on what NaPTAN IDs are, their general usage, and specific applications for TfL services. Additionally, it includes scripts and datasets to help you fetch and use NaPTAN IDs for various purposes.

## What is a NaPTAN ID?

A **NaPTAN ID** (National Public Transport Access Node ID) is a unique identifier used in the UK to represent every point of access to public transport. It is part of the NaPTAN schema, which is a national system that provides a consistent, unique reference for all public transport access points (such as bus stops, railway stations, tram stops, airports, ferry terminals, etc.) across the UK.

### Usage of NaPTAN IDs

NaPTAN IDs can be used to:

- Identify public transport locations uniquely.
- Fetch real-time transport data (e.g., arrivals and departures).
- Facilitate journey planning applications.
- Integrate and cross-reference data across various transport datasets.

## NaPTAN IDs for TfL

Within the Transport for London (TfL) network, NaPTAN IDs are assigned to each transport station, such as Tube stations, Overground stations, Tram stops, Docklands Light Railway (DLR) stations, and the Elizabeth Line stations.

### Applications for TfL Services

This repository leverages NaPTAN IDs for several purposes within the TfL network, including:

- **Fetching Station Names**: Use the NaPTAN IDs to fetch specific station names and mapping both together. This allows anyone to search for a station and retrieve the corresponding NaPTAN ID.
- **Retrieving Real-Time Arrivals**: Obtain real-time arrival information for each station by querying the TfL API with NaPTAN IDs.
- **Journey Planning**: Plan journeys between two stations by providing their respective NaPTAN IDs to get the most efficient routes, connections, and real-time updates.

### Example Usage of the TfL API

The NaPTAN IDs can be used with the Transport for London (TfL) API to perform various operations, such as retrieving station arrivals and planning journeys. Below are examples demonstrating how to use NaPTAN IDs with the TfL API.

#### 1. Fetch Station Arrivals

To get the latest arrival times for a specific station, use the NaPTAN ID of that station with the TfL API. 

**Example: Fetching Arrivals for King's Cross St. Pancras Station**

- **Station NaPTAN ID**: `940GZZLUKSX` (King's Cross St. Pancras)

API Endpoint: https://api.tfl.gov.uk/StopPoint/{id}/Arrivals

Replace `{id}` with the NaPTAN ID of the station:

- Arrivals for King's Cross St. Pancras - https://api.tfl.gov.uk/StopPoint/940GZZLUKSX/Arrivals

#### 2. Plan Journeys Between Two Stations

To plan a journey between two stations, use their respective NaPTAN IDs with the TfL API. 

**Example: Planning a Journey from Waterloo to Victoria**

- **From**: Waterloo Station - NaPTAN ID: `940GZZLUWLO`
- **To**: Victoria Station - NaPTAN ID: `940GZZLUVIC`

API Endpoint: https://api.tfl.gov.uk/Journey/JourneyResults/{from}/to/{to}

Replace `{from}` and `{to}` with the NaPTAN IDs of the origin and destination stations:

- Journey from Waterloo to Victoria - https://api.tfl.gov.uk/Journey/JourneyResults/940GZZLUWLO/to/940GZZLUVIC

By clicking on the links above, you can see the real-time data provided by the TfL API for station arrivals and journey planning.

To access the TfL API, visit the [TfL API documentation](https://api.tfl.gov.uk/).

## Data Files

This repository includes the following data files containing NaPTAN IDs and related station information:

- **`Station_NaPTANs.csv`**: A CSV file listing all TfL stations along with their NaPTAN IDs and the lines they serve.
- **`Station_NaPTANs.json`**: A JSON file containing the same information as the CSV but in a structured format for developers.

These files can be used to reference and fetch NaPTAN IDs by comparing them to station names or codes. This approach allows you to use these datasets for a wide range of applications, from simple lookups to more complex data integrations.

## Python Scripts for NaPTAN Data Fetching

This repository also includes several **Python scripts** designed to fetch and process NaPTAN IDs for TfL stations and the lines they serve. These scripts provide additional functionality for developers who wish to dynamically retrieve or update station data from the TfL API.

### Purpose of the Python Scripts

The primary purpose of these Python scripts is to automate the fetching and processing of station data, including:

- **Retrieving NaPTAN IDs for TfL Stations**: The scripts can be used to query the TfL API and obtain the NaPTAN IDs for specific stations, which are essential for accessing real-time information such as arrivals, departures, and journey details.
- **Identifying Lines Served by Each Station**: The scripts also facilitate the retrieval of information about which lines are served by a particular station, enabling more comprehensive journey planning and data analysis.

### Usage

While the data files (`Station_NaPTANs.csv` and `Station_NaPTANs.json`) provided in the **`data`** folder already contain a comprehensive list of stations, NaPTAN IDs, and the lines they serve, these Python scripts offer a way to:

- **Update the Existing Data**: If there have been changes in the TfL network or if you require the most current data, the scripts can be executed to fetch the latest NaPTAN IDs and station details.
- **Fetch Customised Data**: Developers can modify the scripts to fetch data tailored to their specific needs, such as a subset of stations or additional details not covered in the pre-collected data files.

### Optional Use

These scripts are **optional** to use. All necessary data has already been collected and stored in the repository's data files, so you do not need to run the scripts unless you wish to obtain updated or customized information. 

### How to Execute the Scripts

To execute these scripts:

1. Ensure you have Python installed on your system.
2. Clone this repository and navigate to the directory containing the scripts.
3. Run the desired script from the command line or terminal e.g:

   ```sh
   python TfL_Stations_naptans_&_lines.py

## Contributing

Contributions are encouraged to improve the NaPTAN ID repository! If you have ideas on how to enhance the usage of NaPTAN IDs or add new features, please consider contributing. Here’s how you can help:

1. **Fork the Repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.

2. **Create a Branch**: In your forked repository, create a new branch for your changes. For example, you might use a branch name like `feature/add-new-script`.

3. **Make Changes**: Implement your changes or enhancements. Be sure to follow any coding standards or guidelines provided in this repository.

4. **Submit a Pull Request**: Once you’ve tested your changes, submit a pull request to the original repository. Describe the changes you made and why they are beneficial.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
