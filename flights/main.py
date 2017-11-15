import pandas as pd
import random

aircode_1 = pd.read_csv('data/L_AIRPORT.csv_')
aircode_2 = pd.read_csv('data/L_AIRPORT_ID.csv_')

aircode_1 = aircode_1.reset_index()
aircode_2 = aircode_2.reset_index()
aircodes = pd.merge(aircode_1, aircode_2, on='Description')

# Create a dictionary for quick lookup of airport code equivalents
aircode_dict = dict(zip(aircodes['Code_y'].astype(str), aircodes['Code_x']))

# Create a dictionary of all 3 letter airports
airports_3letter = dict(zip(aircode_1['Code'], aircode_1['Description']))

# Load data
n = 5819078
skip = random.sample(range(1,n),n-2000000)
flights = pd.read_csv('data/flights.csv',
                      skiprows=skip,
                      usecols = ['MONTH','DAY','DAY_OF_WEEK','AIRLINE',
                                 'ORIGIN_AIRPORT','DESTINATION_AIRPORT',
                                 'SCHEDULED_DEPARTURE','DEPARTURE_DELAY',
                                 'ARRIVAL_DELAY','CANCELLED'],
                      low_memory=False)
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

# Take in user input for the airport of choice
while True:
    airport = input('Enter a 3-letter airport code: ')
    if len(airport) != 3:
        print('Sorry, your airport code was not 3 letters')
        continue
    elif not airport in airports_3letter:
        print('Sorry, your airport was not found')
        continue
    else:
        # Need to ensure that all airport code are in the same format
        # Initially October airports were using the 5-digit scheme and all other months
        # were using a 3-digit scheme so we need to correct October
        airport = airport.upper()
        flights = flights[flights['ORIGIN_AIRPORT'] == airport]
    
        
                
        
 
        # Filter dataset to just contain the flights starting at the point of
        # interest
        break





#def airport_insights(airport_data):
    


#        airport_insights(airport_specific_flights)
        

        
    
       

