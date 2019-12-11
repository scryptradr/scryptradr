import os

from Neural_Network.Evaluate import evaluate
from Neural_Network.Setup import setupNetwork
from Neural_Network.Train import trainNetwork
from Neural_Network.Load import loadNetwork


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# ----------------- Input ----------------- #
neurons_in_input_layer = 900
# ----------------- Hidden ---------------- #
# [0] starting_at || [1] operation (add, sub, mul) || [2] difference_per_layer || [3] max_number_of_layers
hidden_layer = [900, 'sub', 100, 10]
# ---------------- Output ----------------- #
neurons_in_output_layer = 3
# ---------------- General ---------------- #
epochs_per_file = 60
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

model = loadNetwork('Checkpoints\\Save-148.h5')

#model = setupNetwork(neurons_in_input_layer, hidden_layer, neurons_in_output_layer, attributes, compiler)
model = trainNetwork(model, neurons_in_input_layer, epochs_per_file, overlap)

evaluate(model, class_names)

