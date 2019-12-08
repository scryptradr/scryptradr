import os

from NeuralNetwork.Evaluate import evaluate
from NeuralNetwork.Setup import setupNetwork
from NeuralNetwork.Train import trainNetwork
from NeuralNetwork.Load import loadNetwork


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# ----------------- Input ----------------- #
neurons_in_input_layer = 900
# ----------------- Hidden ---------------- #
# [0] starting_at || [1] operation (add, sub, mul) || [2] difference_per_layer || [3] max_number_of_layers
hidden_layer = [100, 'add', 10, 100]
# ---------------- Output ----------------- #
neurons_in_output_layer = 3
# ---------------- General ---------------- #
epochs_per_file = 100
overlap = 0
# ---------------- Options ---------------- #
class_names = ['Long', 'Hodl', 'Short']
# [x][0] activation function || [x][1] kernel initializer || [x][2] bias initializer
# [0][x] input layer         || [1][x] hidden layer       || [2][x] output layer
attributes = [['elu',                'random_normal',     'random_normal'],
              ['relu',               'random_normal',     'random_normal'],
              ['softmax',            'random_normal',     'random_normal']]
# [0] optimizer || [1] loss function
compiler = ['Adadelta', 'mean_absolute_error']

# -------------------------------------------------------------------------------------------------------------------- #

#model = loadNetwork('Checkpoints\\Save-98.h5')

model = setupNetwork(neurons_in_input_layer, hidden_layer, neurons_in_output_layer, attributes, compiler)
model = trainNetwork(model, neurons_in_input_layer, epochs_per_file, overlap)

evaluate(model, class_names)

