from tensorflow_core.python.keras.models import load_model


def loadNetwork(filename):
    return load_model(filename)

