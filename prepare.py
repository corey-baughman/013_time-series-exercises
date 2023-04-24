# prepare.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convert_date(df, col1='sale_date'):
    df[col1] = pd.to_datetime(df[col1])
    
    return df


def set_date_index(df, col1='sale_date'):
    df = df.set_index(col1).sort_index()
    
    return df


def add_columns(df, col1='month', col2='day_of_week', 
                col3='sales_total'):
    '''
    function takes in a df and adds the specified columns.
    Defaults to those needed for superstore prepare
    exercise.'''
    df[col1] = df.index.strftime('%B')
    df[col2] = df.index.strftime('%A')
    df[col3] = df.sale_amount * df.item_price
    
    return df

def drop_columns_energy(df):
    '''
    '''
    df = df.drop(columns='Unnamed: 0')
    
    return df

def pythonic_names_energy(df):
    '''
    '''
    df = df.rename(columns={'Date':'date', 'Consumption':'consumption',
                       'Wind':'wind', 'Solar':'solar','Wind+Solar':'wind_and_solar'})
    
    return df


def convert_date_energy(df):
    '''
    '''
    df['date'] = pd.to_datetime(df['date'])
    
    return df

def set_date_index_energy(df):
    '''
    '''
    df = df.set_index('date', ).sort_index()

    return df


def fillna_energy(df):
    '''
    '''
    df = df.fillna(0)

    return df


def add_cols_energy(df):
    '''
    '''
    df['month'] = df.index.strftime('%B')
    df['year'] = df.index.strftime('%Y')
    
    return df

def plot_cols(df):
    '''
    '''
    for col in df.columns:
        plt.hist(df[col], ec='black')
        plt.title(f'Distribution of {col}')
        plt.show()