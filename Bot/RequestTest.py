import requests
import base64
import uuid
from util.api_key import generate_nonce, generate_signature
from BotAuth.APIKeyAuthWithExpires import APIKeyAuthWithExpires
# ######### Making Order ##############
# orderIDPrefix='mm_bitmex_'
# clOrdID = orderIDPrefix + base64.b64encode(uuid.uuid4().bytes).decode('utf8').rstrip('=\n')

# jsoncontent = { 'symbol': 'XBTUSD', 'orderQty': 368, 'price':6400, 'clOrdID':clOrdID}


# StopOrder = { 'symbol': 'XBTUSD','orderQty': 468, 'clOrdID': clOrdID,  
# 'stopPx': 7800, 'ordType': 'Stop', 'timeInForce': 'ImmediateOrCancel', 
# 'execInst': 'Close,LastPrice'}
# ###############LinkNguye API keys########
# # key = XLF0BPZb4AWiLFka2wF_hRqo
# # secret = LPJYu0LZ85uWt7_Fg8Jnvjp5olV6jLdI9VPqBTbEo5l0fOkW


# api_key = 'OwLL1sNPTWOxelVnqAFcThEb'
# api_secret = 'krFBRj0Lm2gShd8gH5JM9iPCM5u3dj-zTl5L80tH2fkVI-v3'
# url = 'https://testnet.bitmex.com/api/v1/order'


# auth = APIKeyAuthWithExpires(api_key, api_secret)

# response = requests.request('POST', url='https://testnet.bitmex.com/api/v1/order', json=jsoncontent, auth=auth)

# # response = requests.get(url, auth=auth)

# print(response.status_code)

########## Getting Data ###############

data = requests.get(url='https://testnet.bitmex.com/api/v1/XBTUSD')

print(data.status_code)
print("\n")
print(data.json())