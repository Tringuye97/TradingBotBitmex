from bitmex_websocket import BitMEXWebsocket 
from time import sleep
from RequestTest import place_order, cancel_order
import logging
##############################

def run():
    logger = setup_logger()
    api_key = 'i3Bzs7XfOBdgyDmuTHIsHeVZ'
    api_secret = 'SJejr2P4y8BNzAyIV8xq2ckd1kVMgUK2-NmI3C3uwL01ryVb'

    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api", symbol="XBTUSD",
                         api_key=api_key, api_secret=api_secret)

    # i = 0
    # ContractQty = -1
    # PositionPrice = 0
    # CurrentBidPrice = 0
    # CurrentAskPrice = 0
    # currentState = ws.get_tickerXBTUSD()
    # positionState = ws.positions()
    while(ws.ws.sock.connected):
        print('\n\n')
        currentState = ws.get_tickerXBTUSD()
        positionState = ws.positions()
        a = ws.open_orders()
        logger.info("Ticker: %s" % currentState)
        logger.info("Positions: %s" % positionState)
        logger.info("Orders: %s" % a) 
        print('\n')
        # if i == 6:
        #     logger.info("Ticker: %s" % currentState)
        #     logger.info("Positions: %s" % positionState)
        #     print(a) 
        #     i=0
        #################### Ideal condition to SELL and BUY
        # Place Selling Order if there is no position and no active order
        # if currentState['Bid Size']<1380000 and positionState['Quantity']==0 and len(a)==0:
        # if positionState['Quantity']==0 and len(a)==0:
        #     PositionPrice = ws.get_tickerXBTUSD()['Ask Price']
        #     # ContractQty = -int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price'])    # A negative number
        #     if place_order(Quantity=ContractQty, Price=PositionPrice, api_key=api_key, api_secret=api_secret):
        #         print('Just place Sell Order\n')
        
        # # sleep(11)
        # # Place Buy Order if there is a position and no active order
        # # a = ws.open_orders()
        # # print(len(a)) 
        
        # if positionState['Quantity']==ContractQty and len(a)==0:
            
        #     CurrentBidPrice = ws.get_tickerXBTUSD()['Bid Price']      # Get current Bid Price
        #     if (CurrentBidPrice>=PositionPrice-0.5 and CurrentBidPrice<PositionPrice+168):     # PositionPrice-0.5<=CurrentBidPrice<PositionPrice+168 
        #         if place_order(Quantity=-ContractQty, Price=PositionPrice-0.5, api_key=api_key, api_secret=api_secret):
        #             print('Just Place Buy Order\n')
        #     else:   # the rest of the cases
        #         if place_order(Quantity=-ContractQty, Price=PositionPrice, api_key=api_key, api_secret=api_secret):
        #             print('Just Place Buy Order\n')

        # ##################### Price decreased more than 11 units from ACTIVE sell order price
        # if (len(a)!=0):
        #     CurrentAskPrice = ws.get_tickerXBTUSD()['Ask Price']
        #     if a[0]['Side']=='Sell' and a[0]['Price']>=(CurrentAskPrice+11):
        #         print("Cancel All Orders\n")
        #         cancel_order(api_key=api_key, api_secret=api_secret)
        #         PositionPrice = ws.get_tickerXBTUSD()['Ask Price']
        #         # ContractQty = -int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price'])    # A negative number
        #         place_order(Quantity=ContractQty, Price=PositionPrice, api_key=api_key, api_secret=api_secret)
        # i+=1
        sleep(13)
     
        
            


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