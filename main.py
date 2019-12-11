import Database_Management as dm
import Neural_Network
import Engine.Engine

TRAIN = True

while True:
    # Mainloop
    if TRAIN:
        # program in train mode
        pass
        # todo get values from db and calculate desired output
        # todo train nn with said data

    else:
        # program is live
        pass
        # todo shift current data by one and append pulled current price from API
        # todo plug current data into nn
        # todo send resulting data to the engine


