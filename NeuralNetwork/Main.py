import os

from NeuralNetwork.Evaluate import evaluate
from NeuralNetwork.Setup import setupNetwork
from NeuralNetwork.Train import trainNetwork
from NeuralNetwork.Load import loadNetwork

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
neurons_in_input_layer = 900
difference_per_layer = 50
neurons_in_output_layer = 3
epochs_per_file = 100
overlap = 0
class_names = ['Long', 'Hodl', 'Short']
'''             Activation-function | kernel initializer | bias initializer '''
attributes = [['elu',                'random_normal',     'random_normal'],
              ['relu',               'random_normal',     'random_normal'],
              ['softmax',            'random_normal',     'random_normal']]
'''          Optimizer | loss function                                      '''
compiler = ['Adadelta', 'mean_absolute_error']

# -------------------------------------------------------------------------------------------------------------------- #

#model = loadNetwork('Checkpoints\\Save-22.h5')

model = setupNetwork(neurons_in_input_layer, difference_per_layer, neurons_in_output_layer, attributes, compiler)
model = trainNetwork(model, neurons_in_input_layer, epochs_per_file, overlap)

evaluate(model, class_names)

