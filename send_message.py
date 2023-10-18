'''
******************************************************
* Author: Mayra Villarrubia                          *
* Date: 17/09/2023                                   *  
* Description: Send Twilio messages using Python     *
******************************************************
'''

from utils import create_df, get_forecast, send_message


def main():

    place = 'La Plata' 
    data = get_forecast(place)

    data_rain = create_df(data)

    msg_id = send_message(data_rain, place)
    print('Message sent successfully: ' + msg_id)



if __name__ == "__main__":
    main()