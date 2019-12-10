class Engine:
    output_values = [0, 0, 0]

    def __init__(self, output_values):
        self.output_values = output_values

    def __del__(self):
        pass

    def find_largest_output(self):
        # Returns the index of the node with the largest value
        max_pos = -1
        largest = max(self.output_values)

        for i in range(3):
            if self.output_values[i] == largest:
                max_pos = i
                break

        return max_pos

    def start(self):
        biggest_val_index = self.find_largest_output()
        safety_cutoff = 0.5  # todo change this with realistic value

        if self.output_values[biggest_val_index] > safety_cutoff:
            # Neural Network output is sure enough to make a decision
            if biggest_val_index == 0:
                # Predominant Output long
                print("== going long ==")
                # todo go long with limits + check on trigger to avoid mirrored positions

            elif biggest_val_index == 1:
                # Predominant Output hodl
                print("== hodl-ing ==")
                # todo check position time-to-live is not reached, if yes close the position

            elif biggest_val_index == 2:
                # Predominant Output short
                print("== going short==")
                # todo go short with limits + check on trigger to avoid mirrored positions

        else:
            print("== inclonclusive output, trying again in 1 minute ==")
            del self
