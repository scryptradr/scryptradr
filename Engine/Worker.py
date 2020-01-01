import time

import API_Calls.bitmex_api_calls as api


def order_worker_thread():
    trader = api.Bitmex_Caller()
    while 1:
        spread = 1
        # cycle through queue
        valid_timestamps = [
            time.time(),
            time.time() + spread,
            time.time() - spread
        ]
        for i in queue_timestamps:
            # check if it's time to place an order in the queue
            if time.time() in valid_timestamps:
                # Place order from queue
                trader.place_order(base_amount)
                # Delete order from queue
                queue_timestamps.pop(i)
                queue_amounts.pop(i)

        time.sleep(1)


# Base amount - standard first position size
base_amount = []

# Values of the 900 output nodes
output_values = []

# Predicted  future values
output_prices = []

# input prices that correspond to the 900 output nodes
input_prices = []

# Order queue timestamps
queue_timestamps = []

# Order queue amounts
queue_amounts = []
