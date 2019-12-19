import time

from bitmex import bitmex


class Bitmex_Caller:
    api_key = 'uYEyijptAwbC4Ojvyu-v47TS'
    api_secret = 'ww85Y4r8URbCEr0nmyHDPn0crtJ4kdmv3mFNgUc9rMkX6IUl'

    client = bitmex(test=True, api_key=api_key, api_secret=api_secret)

    def get_market_price(self):
        # Pulls the last market price
        # Params: none
        # Return: current Bitmex mark Price

        if int(round(self.get_current_position().get("currentPrice"))) == 0:
            print("No open position, please create one on bitmex")
            exit(1)
            return 0
        else:
            return int(round(self.get_current_position().get("currentPrice")))

    def place_order(self, amount):
        # Places an order at the current BitMEX mark price
        symbol = 'XBTUSD'
        price = self.get_market_price()

        # Cancel all Orders
        self.client.Order.Order_cancelAll().result()

        # Get size of old position
        old_amount = self.get_current_position().get("amount")

        # Place order
        self.client.Order.Order_new(symbol=symbol, orderQty=amount, price=price).result()

        # Get new position size
        new_amount = self.get_current_position().get("amount")

        # Wait for the API to update
        time.sleep(3)

        # If the new position size remains unchanged, retry the order with spread
        while old_amount == new_amount:

            # Cancel all open orders
            self.client.Order.Order_cancelAll().result()

            print("== order not filled, retrying with spread ==")

            price = self.get_market_price()
            if amount > 0:
                self.client.Order.Order_new(symbol=symbol, orderQty=amount, price=price + 20).result()
            else:
                self.client.Order.Order_new(symbol=symbol, orderQty=amount, price=price - 20).result()

            # Wait for the API to update
            time.sleep(3)

            # Update the new position size
            new_amount = self.get_current_position().get("amount")

        print("== Order filled, new position size: {} ==".format(new_amount))

    def get_current_position(self):
        global processed_position

        # Get positions
        positions = self.client.Position.Position_get().result()

        # Cycle through all current positions - there should only be one
        positions = positions[0]
        for positions in positions:
            processed_position = {"amount": positions["currentQty"], "breakEvenPrice": positions["breakEvenPrice"],
                                  "leverage": positions["leverage"], "isOpen": positions["isOpen"],
                                  "currentPrice": positions["lastPrice"]}

        # Return the dictionary containing the wanted data
        return processed_position

    def liquidate_position(self):
        # Liquidates the position at market
        current_position = self.get_current_position().get("amount")
        if current_position > 0:
            self.place_order(-(current_position - 1))
        else:
            self.place_order(-current_position + 1)
