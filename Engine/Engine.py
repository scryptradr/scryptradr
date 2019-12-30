import time

import API_Calls.bitmex_api_calls as api
import sigmoid as sg
from Engine import Worker


class Engine_Object:
    # current position information
    api_caller = api.Bitmex_Caller()
    current_position = api_caller.get_current_position()

    def __init__(self, outputs, inputs, amount):
        Worker.output_values = outputs
        Worker.input_prices = inputs
        Worker.base_amount = amount



    def __del__(self):
        return

    def start(self):
        percentages = []
        for i in range(900):
            percentages.append(sg.sigmoid_reverse((Worker.output_values[i])) / 100 + 1)

        min_percentage = percentages.index(min(percentages))
        max_percentage = percentages.index(max(percentages))

        Worker.queue_timestamps.append(time.time() + min_percentage)
        Worker.queue_amounts.append(Worker.base_amount)

        Worker.queue_timestamps.append(time.time() + max_percentage)
        Worker.queue_amounts.append(Worker.base_amount)
