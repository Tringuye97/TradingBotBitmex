from bitmex_websocket import BitMEXWebsocket 
from time import sleep
from RequestTest import place_order
import logging
##############################

def run():
    logger = setup_logger()

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    # ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
    #                      api_key="OwLL1sNPTWOxelVnqAFcThEb", api_secret="krFBRj0Lm2gShd8gH5JM9iPCM5u3dj-zTl5L80tH2fkVI-v3")
    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key='i3Bzs7XfOBdgyDmuTHIsHeVZ', api_secret='SJejr2P4y8BNzAyIV8xq2ckd1kVMgUK2-NmI3C3uwL01ryVb')
    # logger.info("Instrument data: %s" % ws.get_instrument())

    print("\n\n\n")
    i = 0
    # Run forever
    while(ws.ws.sock.connected):
        order_len =  len(ws.open_orders())   
        if order_len==0:
            print(len(ws.open_orders()))
            # place_order(Quantity=int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price']), Price=ws.get_tickerXBTUSD()['Bid Price'])
            # place_order(Quantity=-int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price']), Price=ws.get_tickerXBTUSD()['Ask Price'])
            place_order(Quantity=1, Price=ws.get_tickerXBTUSD()['Bid Price'])
            place_order(Quantity=-1, Price=ws.get_tickerXBTUSD()['Ask Price'])
            sleep(3)
            for order in ws.open_orders():
                logger.info("Orders: %s" % order)
            # place_order(Quantity=-368,Price=8400)
        # if ws.api_key:
        #     logger.info("Funds: %s" % ws.funds())
        # logger.info("Positions: %s" % ws.positions())
        #   logger.info("Market Depth: %s" % ws.market_depth())
        #   logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        i+=1
        if i==700000:
            # print(len(ws.open_orders()))

            logger.info("Ticker: %s" % ws.get_tickerXBTUSD())
            # for order in ws.open_orders():
            #     logger.info("Orders: %s" % order)
            print("\n\n\n")
            i=0
        
            


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


if __name__ == "__main__":
    run()