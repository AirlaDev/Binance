from binance.client import Client
import config
from binance.websockets import BinanceSocketManager
from binance.enums import *
#import ccxt
from datetime import datetime
import plotly.graph_objects as go
import ssl
import time
import json
import urllib
import hmac, hashlib
import requests

apiKey = 'sua chave api'
apiSecurity = 'sua chave secreta'

client = Client(apiKey, apiSecurity)


order = client.create_order(
    symbol='BNBUSDT',
    side='BUY',
    type='LIMIT',
    timeInForce=TIME_IN_FORCE_GTC,
    quantity=0.037,
    price='415.8138',
    stopPrice= '418.7163')

