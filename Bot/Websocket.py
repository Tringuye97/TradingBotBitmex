from bitmex_websocket import BitMEXWebsocket 
from time import sleep
from RequestTest import place_order
import logging
##############################

def run():
    logger = setup_logger()
    api_key = 'i3Bzs7XfOBdgyDmuTHIsHeVZ'
    api_secret = 'SJejr2P4y8BNzAyIV8xq2ckd1kVMgUK2-NmI3C3uwL01ryVb'
    # # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    # # ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
    # #                      api_key="OwLL1sNPTWOxelVnqAFcThEb", api_secret="krFBRj0Lm2gShd8gH5JM9iPCM5u3dj-zTl5L80tH2fkVI-v3")
    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key=api_key, api_secret=api_secret)
    # # logger.info("Instrument data: %s" % ws.get_instrument())

    
    # print("\n\n\n")
    # a = active_orders(api_key=api_key, api_secret=api_secret)
    # print(a)
    # Run forever
    while(ws.ws.sock.connected):
    # while(1):
        print('\n\n\n')
        logger.info("Ticker: %s" % ws.get_tickerXBTUSD())
        logger.info("Positions: %s" % ws.positions())
        a = ws.open_orders()
        print(a) 
        # if len(a)==0:
        #     place_order(Quantity=int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price']),
        #                 Price=ws.get_tickerXBTUSD()['Bid Price'], api_key=api_key, api_secret=api_secret)
        #     place_order(Quantity=-int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price']),
        #                 Price=ws.get_tickerXBTUSD()['Ask Price'], api_key=api_key, api_secret=api_secret)
        sleep(6)

    #         place_order(Quantity=-1, Price=8000, api_key=api_key, api_secret=api_secret)
    #         place_order(Quantity=1, Price=3000, api_key=api_key, api_secret=api_secret)
    #     sleep(3)

        # if ws.api_key:
        #     logger.info("Funds: %s" % ws.funds())
        # logger.info("Positions: %s" % ws.positions())
        #   logger.info("Market Depth: %s" % ws.market_depth())
        #   logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        
            


def setup_logger():
    # Prints logger info to terminal
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Change this to DEBUG if you want a lot more info
    ch = logging.StreamHandler()
    # create formatter
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # add formatter to ch
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger

# def reve_iter(L):
#     for index in reversed(xrange(len(L))):
#         yield L[index]

if __name__ == "__main__":
    run()