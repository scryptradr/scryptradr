TRAIN = True


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
        pass
        # todo shift current data by one and append pulled current price (converted to percent) from API
        # todo plug current data into nn
        # todo send resulting data from nn to the engine
