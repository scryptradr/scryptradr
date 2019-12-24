import csv
import os
import tensorflow as tf
import math


def sig(val):
    return 1 / (1 + pow(math.e, -0.2 * val))


def trainNetwork(model, neurons_in_input_layer, epochs_per_file, overlap):
    column_values = 1
    delimiter = ';'

    fileCount = 0
    for _ in os.listdir(os.fsencode('Checkpoints')):
        fileCount += 1

    for file in os.listdir(os.fsencode('Data')):
        filename = "Data\\" + os.fsdecode(file)
        if filename.endswith('.CSV'):
            with open(filename) as csv_file:
                content = csv.reader(csv_file, delimiter=delimiter)
                data = []
                for row in content:
                    data.append(row[column_values])

                trainingSets = []
                desiredValues = []
                counter = 0
                while counter <= (len(data) - 1):
                    tmpTrainingSets = []
                    tmpDesiredValues = []
                    firstValue = data[counter]
                    for i in range(0, neurons_in_input_layer):
                        value = (data[i] - firstValue) * 100 / firstValue
                        tmpTrainingSets.append(value)
                        desiredValue = (data[i + (neurons_in_input_layer - overlap)] - firstValue) * 100 / firstValue
                        tmpDesiredValues.append(sig(desiredValue))

                    trainingSets.append(tmpTrainingSets)
                    desiredValues.append(tmpDesiredValues)
                    counter += neurons_in_input_layer - overlap

                (tf.keras.models.Sequential()(model)).fit(trainingSets, desiredValues, epochs=epochs_per_file)

                fileCount += 1
                model.save('Checkpoints\\Save-' + str(fileCount) + '.h5')

    return model