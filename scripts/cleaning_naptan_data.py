import pandas as pd

df = pd.read_json("naptans-for-tfl-stations/data/OLD_DATA/OLD_TfL-Station-NaPTANs.json")

patterns_to_remove = [
    'Underground Station', 'Rail Station', 'DLR Station', 'Tram Stop', 'Station', 
    r'\(Bakerloo Line\)', r'\(Circle Line\)', 'Stn / H&c and Circle Lines', 
    r'\(Dist&Picc Line\)', r'\(H&C Line\)', r'\(Central Line\) Underground Stn', 
    'Overground'
]

pattern = '|'.join(patterns_to_remove) + r'|\(\)'

df['Station Name'] = df['Station Name'].str.replace(pattern, '', regex=True).str.strip()

df = df.groupby('Station Name').agg({
    'NaPTAN ID': lambda x: list(x.unique()),
    'Hub NaPTAN': lambda x: list(x.unique()),
    'Lines': lambda x: sorted(set([item for sublist in x for item in sublist]))
}).reset_index()

df = df.sort_values(by='Station Name')

print(df.to_string())

df.to_json('naptans-for-tfl-stations/data/tfl-station-naptan-data.json', orient='records', lines=False, indent=4)
df.to_csv('naptans-for-tfl-stations/data/tfl-station-naptan-data.csv', index=False)
