# acquire.py
import requests
import numpy as np
import pandas as pd
import math
import os

def see_swapi_categories():
    '''
    queries the root url of the swapi website for the
    available categories, converts the json to a dictionary
    and returns a list of the keys which are category names.
    '''
    root_url = 'https://swapi.dev/api/'
    response = requests.get(root_url)
    response = response.json()
    
    return response.keys()

def get_swapi_category_data(category):
    '''
    takes in a category of data from the swapi.dev website
    and returns a DataFrame of all of the entries in that
    category as rows and all of the observations for each
    entry as features.
    Available categories can be found using the see_swapi_
    categories() function.
    '''
    #check to see if local file already exists
    if os.path.isfile(category + '.csv'):
        df = pd.read_csv((category + '.csv'), index_col=0)
        print('Local file found!')
        return df
    
    # if no local file, then query with API and
    # write local cache file.
    else:
        # get the root url of the category
        category_url = f'https://swapi.dev/api/{category}/'
        # request the category url and assign to response
        response = requests.get(category_url)
        # convert the response to a dictionary called 'data'
        data = response.json()
        # 'count' key in data stores the total number of entries
        number_of_entries = data['count']
        # 'next' key in data stores the url of the next page of results
        next_page = data['next']
        # 'previous' key in data stores url of previous page of results
        previous_page = data['previous']
        # 'results' key in data stores all of results on page
        number_of_results = len(data['results'])
        # use math.ceil() to find the next highest integer from dividing
        # number of entries by number of results for max page of results.
        max_page = math.ceil(number_of_entries / number_of_results)
        # make a DataFrame of the first page of results
        df = pd.DataFrame(data['results'])
        # write a for loop that gets each page of results and adds to df
        for i in range(1, max_page):
            response = requests.get(data['next'])
            data = response.json()
            number_of_entries = data['count']
            next_page = data['next']
            previous_page = data['previous']
            number_of_results = len(data['results'])
            max_page = math.ceil(number_of_entries / number_of_results)
            print(len(df), len(pd.DataFrame(data['results'])))
            df = pd.concat([df, pd.DataFrame(data['results'])], ignore_index=True)
        # Cache data
        df.to_csv(category + '.csv')
        return df

def new_energy_data():
    '''
    This function queries data from Open Power Systems Data for Germany
    and reads them into pandas DataFrames. 
    
    Arguments: None
    
    Returns: DataFrame of properties queried
    '''
    df = pd.read_csv(
        'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')    
    
    return df
        
def get_energy_data():
    '''
    This function checks to see if there is a local version of 'energy.csv'.
    If it finds one, it reads it into a DataFrame and returns that df.
    If it does not find one, it runs 'new_energy_data()' to pull the data
    from the host and convert to a df. Then it writes that df to a local
    file 'energy.csv' and returns the df. Function relies
    on other functions in the wrangle.py module.
    '''
    if os.path.isfile('energy.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('energy.csv')
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_energy_data()
        
        # Cache data
        df.to_csv('energy.csv')
        
    return df