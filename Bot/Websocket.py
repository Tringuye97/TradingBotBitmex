from bitmex_websocket import BitMEXWebsocket 
from time import sleep
import logging
##############################

def run():
    logger = setup_logger()

    # Instantiating the WS will make it connect. Be sure to add your api_key/api_secret.
    ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key="OwLL1sNPTWOxelVnqAFcThEb", api_secret="krFBRj0Lm2gShd8gH5JM9iPCM5u3dj-zTl5L80tH2fkVI-v3")
    # ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD",
    #                      api_key=None, api_secret=None)
    # logger.info("Instrument data: %s" % ws.get_instrument())

    print("\n\n\n")

    # Run forever
    while(ws.ws.sock.connected):
        logger.info("Ticker: %s" % ws.get_tickerXBTUSD())
        if ws.api_key:
            logger.info("Funds: %s" % ws.funds())
        logger.info("Positions: %s" % ws.positions())
        logger.info("Orders: %s" % ws.open_orders())
        #   logger.info("Market Depth: %s" % ws.market_depth())
        #   logger.info("Recent Trades: %s\n\n" % ws.recent_trades())
        print("\n")
        sleep(5)

    # logger.info("Ticker: %s" % ws.get_tickerXBTUSD())
    # if ws.api_key:
    #     logger.info("Funds: %s" % ws.funds())
    # logger.info("Positions: %s" % ws.positions())
    # logger.info("Orders: %s" % ws.open_orders())

    print("\n\n\n\n")


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