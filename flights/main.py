import pandas as pd

aircode_1 = pd.io.parsers.read_csv('data/L_AIRPORT.csv_')
aircode_2 = pd.io.parsers.read_csv('data/L_AIRPORT_ID.csv_')

aircode_1 = aircode_1.reset_index()
aircode_2 = aircode_2.reset_index()
aircodes = pd.merge(aircode_1, aircode_2, on='Description')
aircode_dict = dict(zip(aircodes['Code_y'].astype(str), aircodes['Code_x']))

# Load data
flights = pd.io.parsers.read_csv('data/flights.csv')

# Make sure all Origin and departing airports are strings
flights['ORIGIN_AIRPORT'] = flights['ORIGIN_AIRPORT'].values.astype(str)
flights['DESTINATION_AIRPORT'] = flights['DESTINATION_AIRPORT'].values.astype(str)

N_flights = len(flights)
for i in range(N_flights):
    if i % 100000 == 0:
        print(i)
    if len(flights['ORIGIN_AIRPORT'][i]) != 3:
        to_replace = flights['ORIGIN_AIRPORT'][i]
        value = aircode_dict[flights['ORIGIN_AIRPORT'][i]]
        flights = flights.replace(to_replace, value)
        print('replaced', to_replace, 'with', value)
    elif len(flights['DESTINATION_AIRPORT'][i]) != 3:
        to_replace = flights['DESTINATION_AIRPORT'][i]
        value = aircode_dict[flights['DESTINATION_AIRPORT'][i]]
        flights = flights.replace(to_replace, value)
        print('replaced', to_replace, 'with', value)