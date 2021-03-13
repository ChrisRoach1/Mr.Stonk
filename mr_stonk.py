from twelvedata import TDClient
from discord import Webhook, RequestsWebhookAdapter
import datetime
import config_values as config

current_time = datetime.datetime.now().time()
value_threshold = 450

#run only between market hours
if (current_time > datetime.time(9)) and (current_time < datetime.time(15,59)):
    td = TDClient(apikey=config.static_values["api_key"])

    ts = td.time_series(
        symbol="GME",
        interval="1min",
        outputsize=1,
        timezone="America/New_York",
    ).as_json()


    stock_time = ts[0]["datetime"]
    stock_high = ts[0]["high"]

    format_string = "{time}  -  the high in the last two minutes for GME is ${high}".format(time = stock_time, high = stock_high)

    webhook = Webhook.from_url(config.static_values["webhook_url"], adapter=RequestsWebhookAdapter())

    if float(stock_high) > value_threshold:
        webhook.send(format_string)




print(r"""
    
  __  __      _____ _              _      _                     _              _            _ 
 |  \/  |    / ____| |            | |    | |                   | |            | |          | |
 | \  / |_ _| (___ | |_ ___  _ __ | | __ | |__   __ _ ___   ___| |_ ___  _ __ | | _____  __| |
 | |\/| | '__\___ \| __/ _ \| '_ \| |/ / | '_ \ / _` / __| / __| __/ _ \| '_ \| |/ / _ \/ _` |
 | |  | | |_ ____) | || (_) | | | |   <  | | | | (_| \__ \ \__ \ || (_) | | | |   <  __/ (_| |
 |_|  |_|_(_)_____/ \__\___/|_| |_|_|\_\ |_| |_|\__,_|___/ |___/\__\___/|_| |_|_|\_\___|\__,_|
                                                                                              
                                                                                              
    
    """)        