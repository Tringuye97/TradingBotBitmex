import requests
import base64
import uuid
# from util.api_key import generate_nonce, generate_signature
from BotAuth.APIKeyAuthWithExpires import APIKeyAuthWithExpires
######### Making Order ##############
def place_order(Quantity=None, Price=None):
    if Quantity==None:
        print('No order commanded.')
        return 
    orderIDPrefix='mm_bitmex_'
    clOrdID = orderIDPrefix + base64.b64encode(uuid.uuid4().bytes).decode('utf8').rstrip('=\n')

    jsoncontent = { 'symbol': 'XBTUSD', 'orderQty': Quantity, 'price':Price, 'clOrdID':clOrdID}#, { 'symbol': 'XBTUSD', 'orderQty': -Quantity, 'price':8400, 'clOrdID':clOrdID}]


    # StopOrder = { 'symbol': 'XBTUSD','orderQty': 468, 'clOrdID': clOrdID,  
    # 'stopPx': 7800, 'ordType': 'Stop', 'timeInForce': 'ImmediateOrCancel', 
    # 'execInst': 'Close,LastPrice'}
    ###############LinkNguye API keys########
    # key = XLF0BPZb4AWiLFka2wF_hRqo
    # secret = LPJYu0LZ85uWt7_Fg8Jnvjp5olV6jLdI9VPqBTbEo5l0fOkW
    ###############Vantringuyen97 API keys########
    # key = i3Bzs7XfOBdgyDmuTHIsHeVZ
    # secret = SJejr2P4y8BNzAyIV8xq2ckd1kVMgUK2-NmI3C3uwL01ryVb


    api_key = 'i3Bzs7XfOBdgyDmuTHIsHeVZ'
    api_secret = 'SJejr2P4y8BNzAyIV8xq2ckd1kVMgUK2-NmI3C3uwL01ryVb'
    url = 'https://www.bitmex.com/api/v1/order'


    auth = APIKeyAuthWithExpires(api_key, api_secret)

    response = requests.request('POST', url=url, json=jsoncontent, auth=auth)

    # response = requests.get(url, auth=auth)

    if response.status_code == 200:
        return True
    else:
        return False


# place_order(Quantity=368,Price=6400)
# place_order(Quantity=-368,Price=8400)