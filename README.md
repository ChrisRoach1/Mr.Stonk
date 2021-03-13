# Mr.Stonk

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)  [![Generic badge](https://img.shields.io/badge/version-1.0.0-neongreen.svg)](https://shields.io/)

## General info

Simple python script meant to be ran as a cron job. It will run during market hours and check the current price of GME, if the price is above a certain threshold it will send a message to a discord server using a webhook. The project requires your own configuration file for an API key and webhook url.

## Technologies

Project is created with:

* python version 3.9.2
* Discord webhooks
* API calls for market data from https://twelvedata.com/