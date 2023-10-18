import pandas as pd
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, API_KEY_WAPI, PHONE_NUMBER_TO
from datetime import datetime
from tqdm import tqdm
import requests
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def get_date():
    return (datetime.now()).strftime("%Y-%m-%d") #'YYYY-MM-DD'

def request_wapi(api_key, place):
    url_weather = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+place+'&days=1&aqi=no&alerts=no'
    try:
        return requests.get(url_weather).json()
    except Exception as e:
        print(e)

def create_df(data):
    columns = ['Date', 'Hour', 'Condition', 'Temperature', 'Rain', 'Probability rain']
    df = pd.DataFrame(data, columns= columns)
    df = df.sort_values(by= 'Hour', ascending = True)

    df_rain =  df[(df['Rain']==1) & (df['Hour']>6) & (df['Hour']< 22)]
    df_rain = df_rain[['Hour','Condition']]
    df_rain.set_index('Hour', inplace = True)

    return df_rain if (not df_rain.empty) else 'There is no rain today! Enjoy your day!'


def get_forecast(place = 'La Plata'):
    data = []
    response = request_wapi(API_KEY_WAPI, place)

    for i in tqdm(range(len(response['forecast']['forecastday'][0]['hour'])), colour = 'green'):
        
        data.append(fill_data(response, i))
    return data

def fill_data(response, i):
    date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
    hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
    condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
    tempe = float(response['forecast']['forecastday'][0]['hour'][i]['temp_c'])
    rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
    prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']
    
    return date,hour,condition,tempe,rain,prob_rain


def send_message(df, place):

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body='\nHi! \n The forecast today '+ get_date() +' in '+ place +' is: \n\n ' + str(df), 
        from_=PHONE_NUMBER,
        to= PHONE_NUMBER_TO
    ) 
    return message.sid