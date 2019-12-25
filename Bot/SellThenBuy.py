from bitmex_websocket import BitMEXWebsocket 
from time import sleep
from RequestTest import place_order, cancel_order
import logging
##############################

def run():
    logger = setup_logger()
    api_key = 'i3Bzs7XfOBdgyDmuTHIsHeVZ'
    api_secret = 'SJejr2P4y8BNzAyIV8xq2ckd1kVMgUK2-NmI3C3uwL01ryVb'

    ws = BitMEXWebsocket(endpoint="https://www.bitmex.com/api/v1", symbol="XBTUSD",
                         api_key=api_key, api_secret=api_secret)

    
    ContractQty = -1
    PositionPrice = 7316.5
    CurrentBidPrice = 0
    CurrentAskPrice = 0
    currentState = ws.get_tickerXBTUSD()
    while(ws.ws.sock.connected):

        print('\n')
        logger.info("Ticker: %s" % ws.get_tickerXBTUSD())
        # logger.info("Positions: %s" % ws.positions())
        # currentState = ws.get_tickerXBTUSD()
        
        a = ws.open_orders()
        print(a) 
        # ##################### Ideal condition to SELL and BUY
        # # Place Selling Order if there is no position and no active order
        # if currentState['Bid Size']<1380000 and ws.positions()['Quantity']==0 and len(a)==0:
        #     PositionPrice = ws.get_tickerXBTUSD()['Ask Price']
        #     # ContractQty = -int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price'])    # A negative number
        #     place_order(Quantity=ContractQty, Price=PositionPrice, api_key=api_key, api_secret=api_secret)
        
        # # sleep(11)
        # # Place Buy Order if there is a position and no active order
        # # a = ws.open_orders()
        # # print(len(a)) 
        # logger.info("Positions: %s" % ws.positions())
        # print(ContractQty)
        # print(ws.positions()['Quantity'])
        # if ws.positions()['Quantity']==ContractQty and len(a)==0:
        #     print('Placing Buy Order\n')
        #     CurrentBidPrice = ws.get_tickerXBTUSD()['Bid Price']      # Get current Bid Price
        #     if (CurrentBidPrice>=PositionPrice-0.5 and CurrentBidPrice<PositionPrice+168):     # PositionPrice-0.5<=CurrentBidPrice<PositionPrice+168 
        #         place_order(Quantity=-ContractQty, Price=PositionPrice-0.5, api_key=api_key, api_secret=api_secret)
        #     else:   # the rest of the cases
        #         place_order(Quantity=-ContractQty, Price=PositionPrice, api_key=api_key, api_secret=api_secret)

        # ##################### Price decreased more than 11 units from ACTIVE sell order price
        # if (len(a)!=0):
        #     CurrentAskPrice = ws.get_tickerXBTUSD()['Ask Price']
        #     if a[0]['Side']=='Sell' and a[0]['Price']>=(CurrentAskPrice+11):
        #         print("Cancel All Orders\n")
        #         cancel_order(api_key=api_key, api_secret=api_secret)
        #         PositionPrice = ws.get_tickerXBTUSD()['Ask Price']
        #         # ContractQty = -int(ws.funds()['Wallet Balance']*ws.get_tickerXBTUSD()['Ask Price'])    # A negative number
        #         place_order(Quantity=ContractQty, Price=PositionPrice, api_key=api_key, api_secret=api_secret)

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