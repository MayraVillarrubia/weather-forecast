'''
******************************************************
* Author: Mayra Villarrubia                          *
* Date: 17/09/2023                                   *  
* Description: Send Twilio messages using Python     *
******************************************************
'''

from utils import create_df, get_forecast, send_message


def main():

    data = get_forecast()

    data_rain = create_df(data)

    msg_id = send_message(data_rain)
    print('Message sent successfully: ' + msg_id)



if __name__ == "__main__":
    main()