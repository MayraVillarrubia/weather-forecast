
![Weather Image](/images/NPIC-20221019112854-5-696x438.jpg)


## Project Description

This project has as purpose to allow you to send messages with the weather forecast to your cellphone daily. 
The technologies that we are going to use are:
* Twilio, for to send messages
* AWS EC2, for deployment
* python 

## Prerequisites
* A Twilio account with PHONE NUMBER, ACCOUNT SSID, and AUTH TOKEN. [See Twilio Web](https://www.twilio.com/en-us)
* A Weather Api account with API KEY. [See Weather Api](https://www.weatherapi.com)
* An AWS EC2 instance. [See Amazon AWS](https://aws.amazon.com/es/ec2/?did=ap_card&trk=ap_card)

## How to run the project

#### To run locally

1. Clone this repo
2. Rename _twilio_config_TEMPLATE.py_ file to **_twilio_config.py_** and complete with your data.

#### To run in AWS EC2
1. Enter EC2 Instance and run the following commands:
```bash
   $ sudo apt update && sudo apt upgrade
   $ sudo apt install -y python3-pip
   $ git clone your-repo
   $ pip3 install -r requirements.txt 
   ```
2. Rename _twilio_config_TEMPLATE.py_ file to **_twilio_config.py_** and complete with your data.

## How to use

#### Locally
* Run the script _send_message.py_

#### In AWS EC2
* You can create a _cronjob_ to automatically run the script daily.