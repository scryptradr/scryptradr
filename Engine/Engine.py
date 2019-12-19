import API_Calls.bitmex_api_calls as api
import sigmoid as sg


class Engine:
    # Values of the 900 output nodes
    output_values = []
    # Predicted  future values
    output_prices = []

    # input prices that correspond to the 900 output nodes
    input_prices = []

    # current position information
    api_caller = api.Bitmex_Caller()
    current_position = api_caller.get_current_position()

    def __init__(self, output_values, input_prices):
        self.output_values = output_values
        self.input_prices = input_prices

    def __del__(self):
        return

    def find_largest_output(self):
        # Returns the index of the node with the largest value
        max_pos = -1
        largest = max(self.output_values)

        for i in range(900):
            if self.output_values[i] == largest:
                max_pos = i
                break

        return max_pos

    def find_smallest_output(self):
        min_pos = -1
        smallest = min(self.output_values)
        for i in range(900):
            if self.output_values[i] == smallest:
                min_pos = i
                break

        return min_pos

    def start(self):
        min_pos = self.find_smallest_output()
        max_pos = self.find_largest_output()

        current_price = self.current_position.get("currentPrice")

        percentages = []
        for i in range(900):
            percentages.append(sg.sigmoid_reverse((self.output_values[i])) / 100 + 1)

        for i in range(900):
            self.output_prices.append(round(percentages[i] * current_price, 1))
