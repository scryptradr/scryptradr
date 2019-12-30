import threading

from Engine import Worker

TRAIN = True

if __name__ == "__main__":
    while True:
        # Mainloop
        if TRAIN:
            # program in train mode
            pass
            # todo get input and output values from db
            # todo calculate percentages from values
            # todo put output percentages in sigmoid function
            # todo train NN with percentages (input) and sigmoid numbers (output)

        else:
            # program is live

            # start queue thread
            t_queue = threading.Thread(target=Worker.order_worker_thread())
            t_queue.start()
